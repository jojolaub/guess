import flet as ft
import random
from fragen import CATEGORIES

def main(page: ft.Page):
    page.title = "Quiz Royale"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 15
    page.bgcolor = "#0f172a"
    page.scroll = ft.ScrollMode.AUTO

    state = {
        "players": [], "board": [], "available": [], 
        "q_idx": 0, "category": "", "phase": "setup", "current_p": 0
    }

    content = ft.Column(expand=True, horizontal_alignment="center")
    page.add(content)

    def show_points_snack(points):
        page.snack_bar = ft.SnackBar(ft.Text(f"+{points} Punkte!", size=20, weight="bold"))
        page.snack_bar.open = True
        page.update()

    def render_game():
        content.controls.clear()
        
        if state["phase"] == "setup":
            crew_names = ["TroX", "Connor", "Ritze", "Jojo"]
            crew_checkboxes = [ft.Checkbox(label=name, value=True, fill_color=ft.Colors.BLUE_500) for name in crew_names]
            cat_dropdown = ft.Dropdown(
                label="Kategorie", options=[ft.dropdown.Option(c) for c in CATEGORIES.keys()],
                width=280, color=ft.Colors.WHITE, bgcolor="#1e293b"
            )
            
            def start_game_logic(e):
                selected = [cb.label for cb in crew_checkboxes if cb.value]
                if not selected or not cat_dropdown.value: return
                cat = cat_dropdown.value
                state["category"] = cat
                state["players"] = [{"name": n, "score": 0, "active": True} for n in selected]
                state["q_idx"] = random.randint(0, len(CATEGORIES[cat])-1)
                
                raw_data = sorted(CATEGORIES[cat][state["q_idx"]]["data"], key=lambda x: x["sort_value"], reverse=True)
                board = []
                for i, item in enumerate(raw_data):
                    board.append({**item, "original_rank": i+1, "clicked": False, "status": None})
                random.shuffle(board)
                state["board"] = board
                state["available"] = [b["name"] for b in board]
                state["phase"] = "playing"
                state["current_p"] = 0
                render_game()

            content.controls.append(ft.Container(padding=30, content=ft.Column([
                ft.Text("👑 Quiz Royale", size=30, weight="bold", color=ft.Colors.WHITE),
                ft.Row(crew_checkboxes, wrap=True, alignment="center"),
                cat_dropdown,
                ft.FilledButton("🚀 Spiel starten", on_click=start_game_logic)
            ], horizontal_alignment="center")))

        elif state["phase"] in ["playing", "game_over"]:
            content.controls.append(ft.Container(content=ft.Text(CATEGORIES[state["category"]][state["q_idx"]]["question"], 
                                   text_align="center", color=ft.Colors.WHITE), padding=10, bgcolor="#334155", border_radius=10))

            score_row = ft.Row(alignment="center", wrap=True, spacing=10)
            for i, p in enumerate(state["players"]):
                score_row.controls.append(ft.Container(
                    content=ft.Column([ft.Text(p['name'], size=12), ft.Text(str(p['score']), weight="bold")], horizontal_alignment="center", spacing=0),
                    padding=10, bgcolor="#3b82f6" if i == state["current_p"] else "#1e293b", border_radius=10, width=80
                ))
            content.controls.append(score_row)
            
            # --- FIX: Grid mit fester Größe ---
            grid = ft.ResponsiveRow(expand=False, spacing=5, run_spacing=5)
            for i, b in enumerate(state["board"]):
                is_clicked = b["clicked"]
                color = "#64748b" if is_clicked else "#3b82f6"
                txt = f"{b['name']}\n{b['value']}" if not is_clicked else f"{b['name']}\n{b['value']}\nPlatz {b['original_rank']}"
                
                grid.controls.append(ft.Column(
                    col={"xs": 3},
                    controls=[
                        ft.Container(
                            content=ft.Text(txt, text_align="center", size=9, color=ft.Colors.WHITE, weight="bold", 
                                            max_lines=3, overflow=ft.TextOverflow.ELLIPSIS),
                            padding=5, bgcolor=color, border_radius=8, 
                            height=100, width=100, # Feste Größe erzwungen
                            on_click=handle_click if not is_clicked else None,
                            data=i
                        )
                    ]
                ))
            content.controls.append(grid)
            if state["phase"] == "game_over":
                content.controls.append(ft.FilledButton("🔄 Neue Runde", on_click=lambda e: render_setup()))
        
        page.update()

    def handle_click(e):
        idx = int(e.control.data)
        item = state["board"][idx]
        player = state["players"][state["current_p"]]
        
        item["clicked"] = True
        pool = [b for b in state["board"] if not b["clicked"]]
        vals = [b["sort_value"] for b in pool]
        
        if item["sort_value"] == max(vals) if vals else False:
            player["active"] = False
            item["status"] = "killer"
        elif item["sort_value"] == min(vals) if vals else False:
            player["score"] += 3
            item["status"] = "target"
            show_points_snack(3)
        else:
            player["score"] += 1
            item["status"] = "normal"
            show_points_snack(1)
            
        n = len(state["players"])
        next_p = (state["current_p"] + 1) % n
        while not state["players"][next_p]["active"]:
            next_p = (next_p + 1) % n
        state["current_p"] = next_p
        render_game()

    def render_setup():
        state["phase"] = "setup"
        render_game()

    render_game()

ft.run(main)