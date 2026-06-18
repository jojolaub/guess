import streamlit as st
import random
# Wir importieren die Datenbank aus der anderen Datei
from fragen import CATEGORIES

# --- 1. SEITEN-KONFIGURATION (Hier kannst du Name und Icon ändern) ---
APP_NAME = "Quiz Royale"
st.set_page_config(page_title=APP_NAME, page_icon="👑", layout="wide")

# --- 2. FANCY CSS STYLING ---
st.markdown("""
    <style>
    /* Styling für die aktiven Buttons */
    div.stButton > button {
        background: linear-gradient(135deg, #4b6cb7 0%, #182848 100%);
        color: white;
        border: none;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
        height: 110px;
        font-size: 16px;
        font-weight: bold;
        white-space: normal;
        word-wrap: break-word;
    }
    
    /* Hover-Effekt (Button hebt sich an) */
    div.stButton > button:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.3);
        border: 1px solid #4CAF50;
    }
    
    /* Styling für DEAKTIVIERTE (bereits geklickte) Buttons */
    div.stButton > button:disabled {
        background: #f0f2f6 !important;
        color: #555 !important;
        transform: none !important;
        box-shadow: inset 0 2px 5px rgba(0,0,0,0.1) !important;
        border: 1px solid #ddd !important;
    }

    /* Großer Neues-Spiel-Button */
    .restart-btn {
        text-align: center;
        margin-top: 30px;
        padding: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. STATE MANAGEMENT INITIALISIERUNG ---
if "phase" not in st.session_state:
    st.session_state.phase = "setup"
if "players" not in st.session_state:
    st.session_state.players = [] 
if "current_player_idx" not in st.session_state:
    st.session_state.current_player_idx = 0
if "board" not in st.session_state:
    st.session_state.board = []
if "available_options" not in st.session_state:
    st.session_state.available_options = []

# --- 4. SPIELLOGIK FUNKTIONEN ---
def next_turn():
    active_players = [p for p in st.session_state.players if p["active"]]
    
    # Spiel vorbei?
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
    
    current_pool = st.session_state.available_options
    dynamic_index = current_pool.index(clicked_item["name"])
    
    if dynamic_index == 0:
        points = 0
        current_player["active"] = False
        status_text = "💥 AUSGESCHIEDEN (Platz 1)"
    elif dynamic_index == len(current_pool) - 1:
        points = 3
        current_player["score"] += points
        status_text = "🏆 +3 PUNKTE (Letzter Platz)"
    else:
        points = 1
        current_player["score"] += points
        status_text = "✅ +1 PUNKT"

    clicked_item["clicked_by"] = current_player["name"]
    clicked_item["status_text"] = status_text
    
    st.session_state.available_options.remove(clicked_item["name"])
    next_turn()

# --- 5. UI: SETUP-PHASE ---
if st.session_state.phase == "setup":
    st.title(f"👑 {APP_NAME} - Setup")
    st.markdown("Wer findet die schwächste Antwort, ohne die stärkste zu berühren?")
    
    col1, col2 = st.columns(2)
    with col1:
        num_players = st.number_input("Anzahl der Spieler", min_value=1, max_value=8, value=2)
        player_names = []
        for i in range(num_players):
            name = st.text_input(f"Name Spieler {i+1}", value=f"Spieler {i+1}")
            player_names.append(name)
            
    with col2:
        # Hier werden die Kategorien aus fragen.py geladen
        category = st.selectbox("Kategorie wählen", list(CATEGORIES.keys()))
        
    st.write("---")
    if st.button("🚀 Spiel starten", use_container_width=True):
        st.session_state.players = [{"name": name, "score": 0, "active": True} for name in player_names]
        st.session_state.current_player_idx = 0
        
        raw_data = CATEGORIES[category]["data"]
        board_data = []
        available_names = []
        for i, item in enumerate(raw_data):
            board_data.append({
                "name": item["name"],
                "value": item["value"],
                "original_rank": i + 1,
                "clicked_by": None,
                "status_text": ""
            })
            available_names.append(item["name"])
            
        random.shuffle(board_data)
        st.session_state.board = board_data
        st.session_state.available_options = available_names
        st.session_state.current_question = CATEGORIES[category]["question"]
        st.session_state.phase = "playing"
        st.rerun()

# --- 6. UI: SPIEL- & END-PHASE ---
elif st.session_state.phase in ["playing", "game_over"]:
    st.title(st.session_state.current_question)
    
    main_col, sidebar_col = st.columns([3, 1])
    
    # SEITENLEISTE: Rangliste
    with sidebar_col:
        st.markdown("### 📊 Rangliste")
        # Sortiere Spieler nach Punkten für die Anzeige (optional, sieht aber besser aus)
        sorted_players = sorted(st.session_state.players, key=lambda x: x["score"], reverse=True)
        
        for player in sorted_players:
            # Finde den originalen Index, um zu wissen, wer am Zug ist
            original_idx = st.session_state.players.index(player)
            
            if not player["active"]:
                st.markdown(f"~~{player['name']}: {player['score']} Pkt~~ 💀")
            elif original_idx == st.session_state.current_player_idx and st.session_state.phase == "playing":
                st.markdown(f"👉 **{player['name']}: {player['score']} Pkt**")
            else:
                st.markdown(f"{player['name']}: {player['score']} Pkt")
                
    # HAUPTBEREICH: 4x3 Grid
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
                            key=f"btn_disabled_{idx}",
                            disabled=True,
                            use_container_width=True
                        )
                    else:
                        st.button(
                            item['name'],
                            key=f"btn_active_{idx}",
                            on_click=handle_click,
                            args=(idx,),
                            disabled=(st.session_state.phase == "game_over"),
                            use_container_width=True
                        )
        
        # SPIELENDE: Fetter Restart-Button unten in der Mitte
        if st.session_state.phase == "game_over":
            st.markdown("---")
            st.balloons() # Ein kleiner Konfetti-Effekt für den Sieger
            st.markdown("<h2 style='text-align: center; color: #4CAF50;'>🏁 Spiel beendet!</h2>", unsafe_allow_html=True)
            
            col_space1, col_btn, col_space2 = st.columns([1, 2, 1])
            with col_btn:
                if st.button("🔄 Nächste Runde / Neues Spiel", use_container_width=True):
                    st.session_state.phase = "setup"
                    st.rerun()