import streamlit as st
import random

# --- SEITEN-KONFIGURATION ---
st.set_page_config(page_title="Dynamic Quiz", page_icon="🎯", layout="wide")

# CSS für das Grid und die "eingefrorenen" Buttons
st.markdown("""
    <style>
    div.stButton > button {
        height: 100px;
        white-space: normal;
        word-wrap: break-word;
        font-size: 16px;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# --- DATENSTRUKTUR (Kategorien & Fragen) ---
# Dictionaries sind extrem effizient in Python, um Key-Value-Paare abzubilden.
CATEGORIES = {
    "Fußball": {
        "question": "Welcher dieser Spieler hat die meisten Karrieretore (Stand 2024)?",
        "data": [
            {"name": "Cristiano Ronaldo", "value": "873 Tore"},
            {"name": "Lionel Messi", "value": "821 Tore"},
            {"name": "Pelé", "value": "762 Tore"},
            {"name": "Romário", "value": "755 Tore"},
            {"name": "Ferenc Puskás", "value": "724 Tore"},
            {"name": "Josef Bican", "value": "722 Tore"},
            {"name": "Jimmy Jones", "value": "648 Tore"},
            {"name": "Gerd Müller", "value": "634 Tore"},
            {"name": "Robert Lewandowski", "value": "621 Tore"},
            {"name": "Zlatan Ibrahimović", "value": "573 Tore"},
            {"name": "Luis Suárez", "value": "557 Tore"},
            {"name": "Eusébio", "value": "473 Tore"}
        ]
    },
    "Geschichte": {
        "question": "Wie lange regierten diese historischen Monarchen?",
        "data": [
            {"name": "Ludwig XIV. (Frankreich)", "value": "72 Jahre"},
            {"name": "Johann II. (Liechtenstein)", "value": "70 Jahre"},
            {"name": "Bhumibol Adulyadej (Thailand)", "value": "70 Jahre"},
            {"name": "Elisabeth II. (UK)", "value": "70 Jahre"},
            {"name": "Franz Joseph I. (Österreich)", "value": "67 Jahre"},
            {"name": "Victoria (UK)", "value": "63 Jahre"},
            {"name": "Hirohito (Japan)", "value": "62 Jahre"},
            {"name": "Kangxi (China)", "value": "61 Jahre"},
            {"name": "Qianlong (China)", "value": "60 Jahre"},
            {"name": "Christian IV. (Dänemark)", "value": "59 Jahre"},
            {"name": "Georg III. (UK)", "value": "59 Jahre"},
            {"name": "Pedro II. (Brasilien)", "value": "58 Jahre"}
        ]
    },
    "Geografie": {
        "question": "Wie hoch sind diese bekannten Berge?",
        "data": [
            {"name": "Mount Everest", "value": "8.848 m"},
            {"name": "K2", "value": "8.611 m"},
            {"name": "Kangchendzönga", "value": "8.586 m"},
            {"name": "Lhotse", "value": "8.516 m"},
            {"name": "Makalu", "value": "8.485 m"},
            {"name": "Cho Oyu", "value": "8.188 m"},
            {"name": "Dhaulagiri", "value": "8.167 m"},
            {"name": "Manaslu", "value": "8.163 m"},
            {"name": "Nanga Parbat", "value": "8.126 m"},
            {"name": "Annapurna", "value": "8.091 m"},
            {"name": "Gasherbrum I", "value": "8.080 m"},
            {"name": "Broad Peak", "value": "8.051 m"}
        ]
    }
}

# --- INITIALISIERUNG DES ZUSTANDSVEKTORS (State Management) ---
# Wenn das Skript läuft, prüfen wir, ob die Zustandsvariablen bereits existieren. 
# Falls nicht, initialisieren wir sie. Das ist unser endlicher Automat.
if "phase" not in st.session_state:
    st.session_state.phase = "setup" # Erlaubte Zustände: 'setup', 'playing', 'game_over'
if "players" not in st.session_state:
    # Liste aus Dictionaries für strukturierte Spielerdaten
    st.session_state.players = [] 
if "current_player_idx" not in st.session_state:
    st.session_state.current_player_idx = 0
if "board" not in st.session_state:
    st.session_state.board = []
if "available_options" not in st.session_state:
    st.session_state.available_options = []

# --- FUNKTIONEN ZUR ZUSTANDSÄNDERUNG (Transitions) ---
def next_turn():
    """Verschiebt den Index auf den nächsten aktiven Spieler (Modulorechnung)"""
    active_players = [p for p in st.session_state.players if p["active"]]
    
    # Abbruchbedingung: Spiel vorbei, wenn alle ausgeschieden sind oder keine Optionen mehr da sind
    if not active_players or len(st.session_state.available_options) == 0:
        st.session_state.phase = "game_over"
        return

    # Iteriere so lange, bis ein aktiver Spieler gefunden wird
    n = len(st.session_state.players)
    st.session_state.current_player_idx = (st.session_state.current_player_idx + 1) % n
    while not st.session_state.players[st.session_state.current_player_idx]["active"]:
        st.session_state.current_player_idx = (st.session_state.current_player_idx + 1) % n

def handle_click(board_index):
    """Callback-Funktion: Wird exakt in dem Moment ausgeführt, wenn ein Button geklickt wird, 
    BEVOR das Skript neu von oben durchläuft."""
    clicked_item = st.session_state.board[board_index]
    current_player = st.session_state.players[st.session_state.current_player_idx]
    
    # 1. Bestimme den DYNAMISCHEN Rang
    # Da available_options immer absteigend sortiert bleibt (Rang 1 bis N), 
    # suchen wir den Index des geklickten Elements in dieser verbleibenden Liste.
    current_pool = st.session_state.available_options
    dynamic_index = current_pool.index(clicked_item["name"])
    
    # 2. Punktevergabe basierend auf dynamischer Logik
    if dynamic_index == 0:
        # Dynamischer Platz 1 = Killer
        points = 0
        current_player["active"] = False
        status_text = "💥 AUSGESCHIEDEN (Platz 1)"
    elif dynamic_index == len(current_pool) - 1:
        # Dynamischer letzter Platz = Ziel
        points = 3
        current_player["score"] += points
        status_text = "🏆 +3 PUNKTE (Letzter Platz)"
    else:
        # Irgendwas dazwischen
        points = 1
        current_player["score"] += points
        status_text = "✅ +1 PUNKT"

    # 3. Status des Buttons auf dem Spielfeld einfrieren
    clicked_item["clicked_by"] = current_player["name"]
    clicked_item["status_text"] = status_text
    
    # 4. Element aus dem aktiven Pool entfernen (verkleinert die Menge für die nächste Runde)
    st.session_state.available_options.remove(clicked_item["name"])
    
    # 5. Zug weitergeben
    next_turn()


# --- UI: SETUP-PHASE ---
if st.session_state.phase == "setup":
    st.title("🎯 Dynamisches Ranking-Quiz")
    
    col1, col2 = st.columns(2)
    with col1:
        num_players = st.number_input("Anzahl der Spieler", min_value=1, max_value=8, value=2)
        player_names = []
        for i in range(num_players):
            name = st.text_input(f"Name Spieler {i+1}", value=f"Spieler {i+1}")
            player_names.append(name)
            
    with col2:
        category = st.selectbox("Kategorie wählen", list(CATEGORIES.keys()))
        
    if st.button("🚀 Spiel starten", use_container_width=True):
        # Zustand initialisieren für den Spielstart
        st.session_state.players = [{"name": name, "score": 0, "active": True} for name in player_names]
        st.session_state.current_player_idx = 0
        
        raw_data = CATEGORIES[category]["data"]
        # Wir speichern die Original-Ränge (1 bis 12) fest ab, da sich die Datenstruktur nicht mehr ändert.
        # Python iteriert hier über die Liste und nutzt 'enumerate', um den Index (i) mitzuführen.
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
            
        # Spielfeld mischen, damit Platz 1 nicht immer oben links ist
        random.shuffle(board_data)
        st.session_state.board = board_data
        
        # Diese Liste nutzen wir für die mathematische Dynamik. 
        # Sie behält die sortierte Reihenfolge bei, wird aber immer kürzer.
        st.session_state.available_options = available_names
        st.session_state.current_question = CATEGORIES[category]["question"]
        st.session_state.phase = "playing"
        st.rerun()


# --- UI: SPIEL-PHASE ---
elif st.session_state.phase in ["playing", "game_over"]:
    st.title(st.session_state.current_question)
    
    main_col, sidebar_col = st.columns([3, 1])
    
    # SEITENLEISTE: Spieler und Punkte
    with sidebar_col:
        st.subheader("📊 Rangliste")
        for i, player in enumerate(st.session_state.players):
            if not player["active"]:
                st.markdown(f"~~{player['name']}: {player['score']} Pkt~~ 💀")
            elif i == st.session_state.current_player_idx and st.session_state.phase == "playing":
                st.markdown(f"👉 **{player['name']}: {player['score']} Pkt**")
            else:
                st.markdown(f"{player['name']}: {player['score']} Pkt")
                
        if st.session_state.phase == "game_over":
            st.error("🏁 Spiel beendet!")
            if st.button("🔄 Neues Spiel"):
                st.session_state.phase = "setup"
                st.rerun()
                
    # HAUPTBEREICH: 4x3 Grid
    with main_col:
        # Mathematische Matrix-Darstellung: 3 Reihen á 4 Spalten
        for row in range(3):
            cols = st.columns(4)
            for col in range(4):
                # Eindimensionalen Index berechnen (0 bis 11)
                idx = row * 4 + col
                item = st.session_state.board[idx]
                
                with cols[col]:
                    if item["clicked_by"] is not None:
                        # Button ist eingefroren (deaktiviert), zeigt Metadaten an
                        st.button(
                            f"{item['name']}\n\n{item['value']} (Platz {item['original_rank']})\n\n👤 {item['clicked_by']}\n{item['status_text']}",
                            key=f"btn_disabled_{idx}",
                            disabled=True,
                            use_container_width=True
                        )
                    else:
                        # Aktiver Button
                        # Der Parameter 'on_click' triggert die Transition im Zustandsautomaten
                        st.button(
                            item['name'],
                            key=f"btn_active_{idx}",
                            on_click=handle_click,
                            args=(idx,),
                            disabled=(st.session_state.phase == "game_over"),
                            use_container_width=True
                        )