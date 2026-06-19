import streamlit as st
import random
from fragen import CATEGORIES  



# --- SEITEN-KONFIGURATION ---
APP_NAME = "Quiz Royale"
st.set_page_config(page_title=APP_NAME, page_icon="👑", layout="wide")

st.markdown("""
    <style>
    div.stButton > button {
        background: linear-gradient(135deg, #4b6cb7 0%, #182848 100%);
        color: white; border: none; border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2); transition: all 0.3s ease;
        height: 110px; font-size: 16px; font-weight: bold;
        white-space: normal; word-wrap: break-word;
    }
    div.stButton > button:hover {
        transform: translateY(-4px); box-shadow: 0 8px 20px rgba(0,0,0,0.3); border: 1px solid #4CAF50;
    }
    div.stButton > button:disabled {
        background: #f0f2f6 !important; color: #555 !important;
        transform: none !important; box-shadow: inset 0 2px 5px rgba(0,0,0,0.1) !important;
        border: 1px solid #ddd !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- STATE MANAGEMENT ---
if "phase" not in st.session_state: st.session_state.phase = "setup"
if "players" not in st.session_state: st.session_state.players = [] 
if "current_player_idx" not in st.session_state: st.session_state.current_player_idx = 0
if "board" not in st.session_state: st.session_state.board = []
if "available_options" not in st.session_state: st.session_state.available_options = []
if "q_idx" not in st.session_state: st.session_state.q_idx = 0
if "last_category" not in st.session_state: st.session_state.last_category = ""

# --- SPIELLOGIK ---
def next_turn():
    active_players = [p for p in st.session_state.players if p["active"]]
    if not active_players or len(st.session_state.available_options) == 0:
        st.session_state.phase = "game_over"
        return

    n = len(st.session_state.players)
    st.session_state.current_player_idx = (st.session_state.current_player_idx + 1) % n
    while not st.session_state.players[st.session_state.current_player_idx]["active"]:
        st.session_state.current_player_idx = (st.session_state.current_player_idx + 1) % n

def handle_click(board_index):
    clicked_item = st.session_state.board[board_index]
    current_player = st.session_state.players[st.session_state.current_player_idx]
    
    current_pool_items = [item for item in st.session_state.board if item["name"] in st.session_state.available_options]
    pool_sort_values = [item["sort_value"] for item in current_pool_items]
    
    killer_val = max(pool_sort_values)
    ziel_val = min(pool_sort_values)
    clicked_val = clicked_item["sort_value"]
    
    if clicked_val == killer_val:
        current_player["active"] = False
        status_text = "💥 AUSGESCHIEDEN (Killer-Platz)"
    elif clicked_val == ziel_val:
        current_player["score"] += 3
        status_text = "🏆 +3 PUNKTE (Sicheres Ziel)"
    else:
        current_player["score"] += 1
        status_text = "✅ +1 PUNKT"

    clicked_item["clicked_by"] = current_player["name"]
    clicked_item["status_text"] = status_text
    
    st.session_state.available_options.remove(clicked_item["name"])
    next_turn()

# --- UI: SETUP-PHASE ---
if st.session_state.phase == "setup":
    st.title(f"👑 {APP_NAME} - Setup")
    
    col_p, col_q = st.columns(2)
    
    with col_p:
        st.subheader("👥 Spieler auswählen")
        crew_options = ["TroX", "Connor", "Ritze", "Jojo"]
        # Dropdown für die Stammcrew
        selected_crew = st.multiselect("Wähle Spieler aus der Crew:", options=crew_options, default=[])
        
        # Textfeld für optionale Zusatzspieler
        custom_players_str = st.text_input("Zusätzliche Spieler hinzufügen (mit Komma trennen):", "")
        custom_players = [name.strip() for name in custom_players_str.split(",") if name.strip()]
        
        player_names = selected_crew + custom_players
        
        if player_names:
            st.success(f"Bereit zu spielen: {', '.join(player_names)}")
            
    with col_q:
        st.subheader("📚 Kategorie")
        category = st.selectbox("Wähle eine Kategorie:", list(CATEGORIES.keys()))
        q_list = CATEGORIES[category]
        
        if st.session_state.last_category != category:
            st.session_state.q_idx = random.randint(0, len(q_list) - 1)
            st.session_state.last_category = category

        st.info(f"🎲 Aktuelle Zufallsfrage: **\"{q_list[st.session_state.q_idx]['question']}\"**")
        
        manual_change = st.checkbox("🔍 Frage manuell aus Katalog wählen")
        if manual_change:
            q_titles = [q["question"] for q in q_list]
            selected_q_text = st.selectbox("Frage bestimmen:", q_titles, index=st.session_state.q_idx)
            st.session_state.q_idx = q_titles.index(selected_q_text)
            
    st.write("---")
    
    # Start-Button ist nur aktiv, wenn mindestens ein Spieler ausgewählt wurde
    if st.button("🚀 Spiel starten", use_container_width=True, disabled=(len(player_names) == 0)):
        st.session_state.players = [{"name": n, "score": 0, "active": True} for n in player_names]
        st.session_state.current_player_idx = 0
        
        raw_data = sorted(CATEGORIES[category][st.session_state.q_idx]["data"], key=lambda x: x["sort_value"], reverse=True)
        
        board_data = []
        available_names = []
        current_rank = 1
        for i, item in enumerate(raw_data):
            if i > 0 and item["sort_value"] == raw_data[i-1]["sort_value"]:
                rank_to_assign = board_data[-1]["original_rank"]
            else:
                rank_to_assign = current_rank
            
            board_data.append({
                "name": item["name"],
                "value": item["value"],
                "sort_value": item["sort_value"],
                "original_rank": rank_to_assign,
                "clicked_by": None,
                "status_text": ""
            })
            available_names.append(item["name"])
            current_rank += 1
            
        random.shuffle(board_data)
        st.session_state.board = board_data
        st.session_state.available_options = available_names
        st.session_state.current_question = CATEGORIES[category][st.session_state.q_idx]["question"]
        st.session_state.phase = "playing"
        st.rerun()

# --- UI: SPIEL- & END-PHASE ---
elif st.session_state.phase in ["playing", "game_over"]:
    st.title(st.session_state.current_question)
    
    main_col, sidebar_col = st.columns([3, 1])
    
    with sidebar_col:
        st.markdown("### 📊 Rangliste")
        sorted_players = sorted(st.session_state.players, key=lambda x: x["score"], reverse=True)
        
        for player in sorted_players:
            original_idx = st.session_state.players.index(player)
            if not player["active"]:
                st.markdown(f"~~{player['name']}: {player['score']} Pkt~~ 💀")
            elif original_idx == st.session_state.current_player_idx and st.session_state.phase == "playing":
                st.markdown(f"👉 **{player['name']}: {player['score']} Pkt**")
            else:
                st.markdown(f"{player['name']}: {player['score']} Pkt")
                
    with main_col:
        for row in range(3):
            cols = st.columns(4)
            for col in range(4):
                idx = row * 4 + col
                item = st.session_state.board[idx]
                
                with cols[col]:
                    if item["clicked_by"] is not None:
                        st.button(
                            f"{item['name']}\n\n{item['value']} (Platz {item['original_rank']})\n\n👤 {item['clicked_by']}\n{item['status_text']}",
                            key=f"btn_disabled_{idx}", disabled=True, use_container_width=True
                        )
                    else:
                        st.button(
                            item['name'], key=f"btn_active_{idx}", on_click=handle_click, args=(idx,),
                            disabled=(st.session_state.phase == "game_over"), use_container_width=True
                        )
        
        if st.session_state.phase == "game_over":
            st.markdown("---")
            st.balloons()
            st.markdown("<h2 style='text-align: center; color: #4CAF50;'>🏁 Spiel beendet!</h2>", unsafe_allow_html=True)
            col_btn = st.columns([1, 2, 1])[1]
            with col_btn:
                if st.button("🔄 Neues Spiel / Kategorie wechseln", use_container_width=True):
                    st.session_state.last_category = ""
                    st.session_state.phase = "setup"
                    st.rerun()