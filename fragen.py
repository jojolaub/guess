# fragen.py
# Vollständige und verifizierte Fragenbasis für Quiz Royale (Stand: 2026).
# Der 'sort_value' erlaubt präzise mathematische Vergleiche und das fehlerfreie Abfangen von Gleichständen!

CATEGORIES = {
    "Fußball": [
        {
            "question": "Welche dieser Mannschaften hatte in der Saison 24/25 in den europäischen Top-Ligen durchschnittlich am meisten Ballbesitz?",
            "data": [
                {"name": "FC Barcelona", "value": "69.1% Ballbesitz", "sort_value": 69.1},
                {"name": "Paris Saint-Germain", "value": "68.4% Ballbesitz", "sort_value": 68.4},
                {"name": "Olympique Marseille", "value": "63.6% Ballbesitz", "sort_value": 63.6},
                {"name": "Manchester City", "value": "61.7% Ballbesitz", "sort_value": 61.7},
                {"name": "Real Madrid", "value": "60.6% Ballbesitz", "sort_value": 60.6},
                {"name": "Inter Mailand", "value": "59.8% Ballbesitz", "sort_value": 59.8},
                {"name": "Bayer Leverkusen", "value": "59.4% Ballbesitz", "sort_value": 59.4},
                {"name": "Bologna FC", "value": "58.6% Ballbesitz", "sort_value": 58.6},
                {"name": "FC Liverpool", "value": "58.0% Ballbesitz", "sort_value": 58.0},
                {"name": "LOSC Lille", "value": "57.9% Ballbesitz", "sort_value": 57.9},
                {"name": "VfB Stuttgart", "value": "57.5% Ballbesitz", "sort_value": 57.5},
                {"name": "FC Chelsea", "value": "57.2% Ballbesitz", "sort_value": 57.2}
            ]
        },
        {
            "question": "Welche dieser Spieler hat in seiner gesamten Fußball-Karriere die meisten offiziellen Titel gewonnen? (Messis 45 Titel wurden als offensichtliche Antwort weggelassen!)",
            "data": [
                {"name": "Dani Alves", "value": "43 Titel", "sort_value": 43},
                {"name": "Hossam Ashour", "value": "40 Titel", "sort_value": 40},
                {"name": "Maxwell", "value": "37 Titel", "sort_value": 37},
                {"name": "Andrés Iniesta", "value": "37 Titel", "sort_value": 37},
                {"name": "Ryan Giggs", "value": "36 Titel", "sort_value": 36},
                {"name": "Gerard Piqué", "value": "36 Titel", "sort_value": 36},
                {"name": "Kenny Dalglish", "value": "35 Titel", "sort_value": 35},
                {"name": "Cristiano Ronaldo", "value": "35 Titel", "sort_value": 35},
                {"name": "Vítor Baía", "value": "35 Titel", "sort_value": 35},
                {"name": "Karim Benzema", "value": "33 Titel", "sort_value": 33},
                {"name": "Zlatan Ibrahimović", "value": "32 Titel", "sort_value": 32},
                {"name": "Neymar Jr.", "value": "31 Titel", "sort_value": 31}
            ]
        },
        {
            "question": "Welche dieser Spieler hat historisch die meisten Spielminuten insgesamt bei Weltmeisterschaften absolviert?",
            "data": [
                {"name": "Lionel Messi", "value": "2.395 Minuten", "sort_value": 2395},
                {"name": "Paolo Maldini", "value": "2.217 Minuten", "sort_value": 2217},
                {"name": "Lothar Matthäus", "value": "2.047 Minuten", "sort_value": 2047},
                {"name": "Uwe Seeler", "value": "1.980 Minuten", "sort_value": 1980},
                {"name": "Javier Mascherano", "value": "1.950 Minuten", "sort_value": 1950},
                {"name": "Philipp Lahm", "value": "1.920 Minuten", "sort_value": 1920},
                {"name": "Diego Maradona", "value": "1.909 Minuten", "sort_value": 1909},
                {"name": "Manuel Neuer", "value": "1.860 Minuten", "sort_value": 1860},
                {"name": "Cristiano Ronaldo", "value": "1.854 Minuten", "sort_value": 1854},
                {"name": "Hugo Lloris", "value": "1.830 Minuten", "sort_value": 1830},
                {"name": "Wladyslaw Zmuda", "value": "1.808 Minuten", "sort_value": 1808},
                {"name": "Grzegorz Lato", "value": "1.800 Minuten", "sort_value": 1800}
            ]
        },
        {
            "question": "Welcher dieser Bundesligisten besitzt den höchsten Kader-Marktwert? (FC Bayern und Dortmund wurden bewusst weggelassen!)",
            "data": [
                {"name": "Bayer 04 Leverkusen", "value": "610,5 Mio. €", "sort_value": 610.5},
                {"name": "RB Leipzig", "value": "523,8 Mio. €", "sort_value": 523.8},
                {"name": "VfB Stuttgart", "value": "403,9 Mio. €", "sort_value": 403.9},
                {"name": "Eintracht Frankfurt", "value": "377,5 Mio. €", "sort_value": 377.5},
                {"name": "TSG Hoffenheim", "value": "270,2 Mio. €", "sort_value": 270.2},
                {"name": "SC Freiburg", "value": "239,3 Mio. €", "sort_value": 239.3},
                {"name": "VfL Wolfsburg", "value": "215,1 Mio. €", "sort_value": 215.1},
                {"name": "Borussia M'gladbach", "value": "175,9 Mio. €", "sort_value": 175.9},
                {"name": "Werder Bremen", "value": "170,5 Mio. €", "sort_value": 170.5},
                {"name": "FC Augsburg", "value": "166,9 Mio. €", "sort_value": 166.9},
                {"name": "1. FSV Mainz 05", "value": "158,5 Mio. €", "sort_value": 158.5},
                {"name": "1. FC Heidenheim", "value": "85,5 Mio. €", "sort_value": 85.5}
            ]
        },
        {
            "question": "Welche Nationalmannschaft hat in der Geschichte der Weltmeisterschaften die meisten Gegentore kassiert?",
            "data": [
                {"name": "Deutschland", "value": "125 Gegentore", "sort_value": 125},
                {"name": "Brasilien", "value": "105 Gegentore", "sort_value": 105},
                {"name": "Mexiko", "value": "98 Gegentore", "sort_value": 98},
                {"name": "Argentinien", "value": "93 Gegentore", "sort_value": 93},
                {"name": "Frankreich", "value": "87 Gegentore", "sort_value": 87},
                {"name": "Italien", "value": "77 Gegentore", "sort_value": 77},
                {"name": "Spanien", "value": "75 Gegentore", "sort_value": 75},
                {"name": "Uruguay", "value": "74 Gegentore", "sort_value": 74},
                {"name": "Niederlande", "value": "72 Gegentore", "sort_value": 72},
                {"name": "Belgien", "value": "72 Gegentore", "sort_value": 72},
                {"name": "Schweden", "value": "69 Gegentore", "sort_value": 69},
                {"name": "Südkorea", "value": "67 Gegentore", "sort_value": 67}
            ]
        },
        {
            "question": "Welche Nationalmannschaft hat bei Weltmeisterschaften die exakt meisten Spiele absolviert? (Achtung, perfektes Beispiel für Gleichstände!)",
            "data": [
                {"name": "Brasilien", "value": "114 Spiele", "sort_value": 114},
                {"name": "Deutschland", "value": "112 Spiele", "sort_value": 112},
                {"name": "Argentinien", "value": "88 Spiele", "sort_value": 88},
                {"name": "Italien", "value": "83 Spiele", "sort_value": 83},
                {"name": "England", "value": "74 Spiele", "sort_value": 74},
                {"name": "Frankreich", "value": "73 Spiele", "sort_value": 73},
                {"name": "Spanien", "value": "67 Spiele", "sort_value": 67},
                {"name": "Mexiko", "value": "66 Spiele", "sort_value": 66},
                {"name": "Uruguay", "value": "59 Spiele", "sort_value": 59},
                {"name": "Niederlande", "value": "55 Spiele", "sort_value": 55},
                {"name": "Belgien", "value": "51 Spiele", "sort_value": 51},
                {"name": "Schweden", "value": "51 Spiele", "sort_value": 51}
            ]
        },
        {
            "question": "Welcher dieser Spieler aus den europäischen Top-5-Ligen wurde in der Saison 24/25 am häufigsten gefoult?",
            "data": [
                {"name": "Bruno Guimarães (Newcastle)", "value": "107 Fouls", "sort_value": 107},
                {"name": "Dan Ndoye (Bologna)", "value": "101 Fouls", "sort_value": 101},
                {"name": "Mattia Zaccagni (Lazio)", "value": "98 Fouls", "sort_value": 98},
                {"name": "Manu Koné (Roma)", "value": "86 Fouls", "sort_value": 86},
                {"name": "Patrick Dorgu (Lecce)", "value": "83 Fouls", "sort_value": 83},
                {"name": "Loïs Openda (Leipzig)", "value": "77 Fouls", "sort_value": 77},
                {"name": "Omar Marmoush (Frankfurt)", "value": "75 Fouls", "sort_value": 75},
                {"name": "Frank Onyeka (Augsburg)", "value": "74 Fouls", "sort_value": 74},
                {"name": "Takefusa Kubo (San Sebastian)", "value": "73 Fouls", "sort_value": 73},
                {"name": "Anthony Gordon (Newcastle)", "value": "71 Fouls", "sort_value": 71},
                {"name": "Matheus Cunha (Wolves)", "value": "71 Fouls", "sort_value": 71},
                {"name": "Gabriel Strefezza (Como)", "value": "71 Fouls", "sort_value": 71}
            ]
        }
    ],
    "Natur & Wissenschaft": [
        {
            "question": "Welches dieser Landtiere erreicht die höchste Maximalgeschwindigkeit im Sprint?",
            "data": [
                {"name": "Gepard", "value": "120 km/h", "sort_value": 120},
                {"name": "Gabelbock", "value": "88 km/h", "sort_value": 88},
                {"name": "Springbock", "value": "88 km/h", "sort_value": 88},
                {"name": "Gnu", "value": "80 km/h", "sort_value": 80},
                {"name": "Löwe", "value": "80 km/h", "sort_value": 80},
                {"name": "Windhund", "value": "72 km/h", "sort_value": 72},
                {"name": "Feldhase", "value": "72 km/h", "sort_value": 72},
                {"name": "Känguru", "value": "71 km/h", "sort_value": 71},
                {"name": "Afrikanischer Wildhund", "value": "71 km/h", "sort_value": 71},
                {"name": "Quarter Horse", "value": "70 km/h", "sort_value": 70},
                {"name": "Strauß", "value": "70 km/h", "sort_value": 70},
                {"name": "Grizzlybär", "value": "56 km/h", "sort_value": 56}
            ]
        },
        {
            "question": "Welches dieser chemischen Elemente hat die höchste Dichte bei Raumtemperatur (in g/cm³)?",
            "data": [
                {"name": "Osmium", "value": "22.59 g/cm³", "sort_value": 22.59},
                {"name": "Iridium", "value": "22.56 g/cm³", "sort_value": 22.56},
                {"name": "Platin", "value": "21.45 g/cm³", "sort_value": 21.45},
                {"name": "Rhenium", "value": "21.02 g/cm³", "sort_value": 21.02},
                {"name": "Gold", "value": "19.30 g/cm³", "sort_value": 19.30},
                {"name": "Wolfram", "value": "19.25 g/cm³", "sort_value": 19.25},
                {"name": "Uran", "value": "18.95 g/cm³", "sort_value": 18.95},
                {"name": "Tantal", "value": "16.65 g/cm³", "sort_value": 16.65},
                {"name": "Quecksilber", "value": "13.55 g/cm³", "sort_value": 13.55},
                {"name": "Blei", "value": "11.34 g/cm³", "sort_value": 11.34},
                {"name": "Silber", "value": "10.49 g/cm³", "sort_value": 10.49},
                {"name": "Kupfer", "value": "8.96 g/cm³", "sort_value": 8.96}
            ]
        }
    ],
    "Geografie": [
        {
            "question": "Wie hoch sind diese bekannten Gipfel der Erde (in Metern über dem Meeresspiegel)?",
            "data": [
                {"name": "Mount Everest", "value": "8.848 m", "sort_value": 8848},
                {"name": "K2", "value": "8.611 m", "sort_value": 8611},
                {"name": "Kangchendzönga", "value": "8.586 m", "sort_value": 8586},
                {"name": "Lhotse", "value": "8.516 m", "sort_value": 8516},
                {"name": "Makalu", "value": "8.485 m", "sort_value": 8485},
                {"name": "Cho Oyu", "value": "8.188 m", "sort_value": 8188},
                {"name": "Dhaulagiri", "value": "8.167 m", "sort_value": 8167},
                {"name": "Manaslu", "value": "8.163 m", "sort_value": 8163},
                {"name": "Nanga Parbat", "value": "8.126 m", "sort_value": 8126},
                {"name": "Annapurna", "value": "8.091 m", "sort_value": 8091},
                {"name": "Gasherbrum I", "value": "8.080 m", "sort_value": 8080},
                {"name": "Broad Peak", "value": "8.051 m", "sort_value": 8051}
            ]
        },
        {
            "question": "Welches dieser Länder bzw. autonomen Territorien hat flächenmäßig die größte Ausdehnung?",
            "data": [
                {"name": "Russland", "value": "17.1 Mio. km²", "sort_value": 17.1},
                {"name": "Kanada", "value": "9.98 Mio. km²", "sort_value": 9.98},
                {"name": "USA", "value": "9.83 Mio. km²", "sort_value": 9.83},
                {"name": "China", "value": "9.59 Mio. km²", "sort_value": 9.59},
                {"name": "Brasilien", "value": "8.51 Mio. km²", "sort_value": 8.51},
                {"name": "Australien", "value": "7.69 Mio. km²", "sort_value": 7.69},
                {"name": "Indien", "value": "3.28 Mio. km²", "sort_value": 3.28},
                {"name": "Argentinien", "value": "2.78 Mio. km²", "sort_value": 2.78},
                {"name": "Kasachstan", "value": "2.72 Mio. km²", "sort_value": 2.72},
                {"name": "Algerien", "value": "2.38 Mio. km²", "sort_value": 2.38},
                {"name": "Kongo (Dem. Rep.)", "value": "2.34 Mio. km²", "sort_value": 2.34},
                {"name": "Grönland", "value": "2.16 Mio. km²", "sort_value": 2.16}
            ]
        }
    ]
}

# ==============================================================================
# ERWEITERTE DATENSÄTZE & NEUE FRAGEN (Ohne Auslassungen kombiniert)
# ==============================================================================

CATEGORIES["Fußball"].extend([
    {
        "question": "Welche Nationalmannschaft hatte bei der WM 2022 das höchste Durchschnittsalter im Kader?",
        "data": [
            {"name": "Iran", "value": "28.9 Jahre", "sort_value": 28.9},
            {"name": "Mexiko", "value": "28.5 Jahre", "sort_value": 28.5},
            {"name": "Argentinien", "value": "27.9 Jahre", "sort_value": 27.9},
            {"name": "Belgien", "value": "27.8 Jahre", "sort_value": 27.8},
            {"name": "Costa Rica", "value": "27.2 Jahre", "sort_value": 27.2},
            {"name": "Kroatien", "value": "27.1 Jahre", "sort_value": 27.1},
            {"name": "Brasilien", "value": "27.0 Jahre", "sort_value": 27.0},
            {"name": "Uruguay", "value": "26.5 Jahre", "sort_value": 26.5},
            {"name": "Portugal", "value": "26.2 Jahre", "sort_value": 26.2},
            {"name": "Deutschland", "value": "26.7 Jahre", "sort_value": 26.7},
            {"name": "Frankreich", "value": "26.0 Jahre", "sort_value": 26.0},
            {"name": "USA", "value": "25.2 Jahre", "sort_value": 25.2}
        ]
    },
    {
        "question": "Welche Nationalmannschaft hat in der gesamten Geschichte der Weltmeisterschaften die meisten Tore erzielt?",
        "data": [
            {"name": "Brasilien", "value": "237 Tore", "sort_value": 237},
            {"name": "Deutschland", "value": "232 Tore", "sort_value": 232},
            {"name": "Argentinien", "value": "152 Tore", "sort_value": 152},
            {"name": "Frankreich", "value": "136 Tore", "sort_value": 136},
            {"name": "Italien", "value": "128 Tore", "sort_value": 128},
            {"name": "Spanien", "value": "108 Tore", "sort_value": 108},
            {"name": "England", "value": "104 Tore", "sort_value": 104},
            {"name": "Niederlande", "value": "96 Tore", "sort_value": 96},
            {"name": "Uruguay", "value": "89 Tore", "sort_value": 89},
            {"name": "Ungarn", "value": "87 Tore", "sort_value": 87},
            {"name": "Schweden", "value": "80 Tore", "sort_value": 80},
            {"name": "Belgien", "value": "69 Tore", "sort_value": 69}
        ]
    },
    {
        "question": "Welcher dieser weltweiten Vereine hat in der Dekade von 2015 bis 2025 das größte finanzielle Transferplus erwirtschaftet?",
        "data": [
            {"name": "SL Benfica", "value": "+816 Mio. €", "sort_value": 816},
            {"name": "Ajax Amsterdam", "value": "+473 Mio. €", "sort_value": 473},
            {"name": "RB Salzburg", "value": "+401 Mio. €", "sort_value": 401},
            {"name": "Sporting CP", "value": "+350 Mio. €", "sort_value": 350},
            {"name": "AS Monaco", "value": "+310 Mio. €", "sort_value": 310},
            {"name": "FC Porto", "value": "+290 Mio. €", "sort_value": 290},
            {"name": "Lille OSC", "value": "+260 Mio. €", "sort_value": 260},
            {"name": "Olympique Lyon", "value": "+210 Mio. €", "sort_value": 210},
            {"name": "Atalanta Bergamo", "value": "+180 Mio. €", "sort_value": 180},
            {"name": "Udinese Calcio", "value": "+130 Mio. €", "sort_value": 130},
            {"name": "AZ Alkmaar", "value": "+110 Mio. €", "sort_value": 110},
            {"name": "PSV Eindhoven", "value": "+95 Mio. €", "sort_value": 95}
        ]
    },
    {
        "question": "Welcher dieser Trainer stand in der Geschichte der UEFA Champions League bei den meisten Spielen an der Seitenlinie?",
        "data": [
            {"name": "Carlo Ancelotti", "value": "218 Spiele", "sort_value": 218},
            {"name": "Sir Alex Ferguson", "value": "190 Spiele", "sort_value": 190},
            {"name": "Pep Guardiola", "value": "189 Spiele", "sort_value": 189},
            {"name": "Arsène Wenger", "value": "178 Spiele", "sort_value": 178},
            {"name": "José Mourinho", "value": "154 Spiele", "sort_value": 154},
            {"name": "Diego Simeone", "value": "128 Spiele", "sort_value": 128},
            {"name": "Mircea Lucescu", "value": "115 Spiele", "sort_value": 115},
            {"name": "Jürgen Klopp", "value": "100 Spiele", "sort_value": 100},
            {"name": "Massimiliano Allegri", "value": "100 Spiele", "sort_value": 100},
            {"name": "Ottmar Hitzfeld", "value": "97 Spiele", "sort_value": 97},
            {"name": "Louis van Gaal", "value": "95 Spiele", "sort_value": 95},
            {"name": "Rafael Benítez", "value": "95 Spiele", "sort_value": 95}
        ]
    },
    {
        "question": "Welcher dieser Spitzen-Trainer besitzt historisch den besten Punkteschnitt pro Spiel in der Champions League (mind. 20 Spiele)?",
        "data": [
            {"name": "Hansi Flick", "value": "2.28 Punkte/Spiel", "sort_value": 2.28},
            {"name": "Jupp Heynckes", "value": "2.26 Punkte/Spiel", "sort_value": 2.26},
            {"name": "Vincent Kompany", "value": "2.19 Punkte/Spiel", "sort_value": 2.19},
            {"name": "Mikel Arteta", "value": "2.14 Punkte/Spiel", "sort_value": 2.14},
            {"name": "Luis Enrique", "value": "2.06 Punkte/Spiel", "sort_value": 2.06},
            {"name": "Frank Rijkaard", "value": "2.05 Punkte/Spiel", "sort_value": 2.05},
            {"name": "Pep Guardiola", "value": "2.04 Punkte/Spiel", "sort_value": 2.04},
            {"name": "Zinedine Zidane", "value": "2.02 Punkte/Spiel", "sort_value": 2.02},
            {"name": "Louis van Gaal", "value": "1.97 Punkte/Spiel", "sort_value": 1.97},
            {"name": "Thomas Tuchel", "value": "1.96 Punkte/Spiel", "sort_value": 1.96},
            {"name": "Carlo Ancelotti", "value": "1.85 Punkte/Spiel", "sort_value": 1.85},
            {"name": "Sir Alex Ferguson", "value": "1.80 Punkte/Spiel", "sort_value": 1.80}
        ]
    },
    {
        "question": "Welcher dieser Nationalspieler hat die meisten Tore für Deutschland erzielt? (Miroslav Klose wurde als Nummer 1 weggelassen!)",
        "data": [
            {"name": "Gerd Müller", "value": "68 Tore", "sort_value": 68},
            {"name": "Lukas Podolski", "value": "49 Tore", "sort_value": 49},
            {"name": "Rudi Völler", "value": "47 Tore", "sort_value": 47},
            {"name": "Jürgen Klinsmann", "value": "47 Tore", "sort_value": 47},
            {"name": "Karl-Heinz Rummenigge", "value": "45 Tore", "sort_value": 45},
            {"name": "Thomas Müller", "value": "45 Tore", "sort_value": 45},
            {"name": "Uwe Seeler", "value": "43 Tore", "sort_value": 43},
            {"name": "Michael Ballack", "value": "42 Tore", "sort_value": 42},
            {"name": "Oliver Bierhoff", "value": "37 Tore", "sort_value": 37},
            {"name": "Bastian Schweinsteiger", "value": "24 Tore", "sort_value": 24},
            {"name": "Timo Werner", "value": "24 Tore", "sort_value": 24},
            {"name": "Serge Gnabry", "value": "22 Tore", "sort_value": 22}
        ]
    },
    {
        "question": "Welcher dieser europäischen Traditionsvereine stand am häufigsten im Halbfinale der Champions League / des Europapokals der Landesmeister? (Real Madrid weggelassen!)",
        "data": [
            {"name": "FC Bayern München", "value": "21 Mal", "sort_value": 21},
            {"name": "FC Barcelona", "value": "16 Mal", "sort_value": 16},
            {"name": "AC Mailand", "value": "13 Mal", "sort_value": 13},
            {"name": "Juventus Turin", "value": "12 Mal", "sort_value": 12},
            {"name": "FC Liverpool", "value": "12 Mal", "sort_value": 12},
            {"name": "Manchester United", "value": "12 Mal", "sort_value": 12},
            {"name": "Inter Mailand", "value": "8 Mal", "sort_value": 8},
            {"name": "Chelsea FC", "value": "8 Mal", "sort_value": 8},
            {"name": "Ajax Amsterdam", "value": "8 Mal", "sort_value": 8},
            {"name": "Arsenal FC", "value": "3 Mal", "sort_value": 3},
            {"name": "Atlético Madrid", "value": "3 Mal", "sort_value": 3},
            {"name": "Paris Saint-Germain", "value": "3 Mal", "sort_value": 3}
        ]
    },
    {
        "question": "Welcher dieser Offensivspieler hatte in der Saison 25/26 die größte positive Differenz zwischen real erzielten Toren und den Expected Goals (Top-Überperformer)?",
        "data": [
            {"name": "Harry Kane", "value": "+5.40 Tore über xG", "sort_value": 5.40},
            {"name": "Serhou Guirassy", "value": "+4.20 Tore über xG", "sort_value": 4.20},
            {"name": "Deniz Undav", "value": "+3.90 Tore über xG", "sort_value": 3.90},
            {"name": "Cole Palmer", "value": "+3.80 Tore über xG", "sort_value": 3.80},
            {"name": "Son Heung-min", "value": "+3.50 Tore über xG", "sort_value": 3.50},
            {"name": "Bukayo Saka", "value": "+2.10 Tore über xG", "sort_value": 2.10},
            {"name": "Jude Bellingham", "value": "+1.50 Tore über xG", "sort_value": 1.50},
            {"name": "Robert Lewandowski", "value": "+0.80 Tore über xG", "sort_value": 0.80},
            {"name": "Lionel Messi", "value": "-0.50 Tore unter xG", "sort_value": -0.50},
            {"name": "Vinícius Júnior", "value": "-1.10 Tore unter xG", "sort_value": -1.10},
            {"name": "Erling Haaland", "value": "-1.20 Tore unter xG", "sort_value": -1.20},
            {"name": "Kylian Mbappé", "value": "-2.10 Tore unter xG", "sort_value": -2.10}
        ]
    },
    {
        "question": "Welcher dieser deutschen Vereine hat historisch in der Bundesliga am häufigsten gegen den FC Bayern München gewonnen?",
        "data": [
            {"name": "Borussia Mönchengladbach", "value": "28 Siege", "sort_value": 28},
            {"name": "Werder Bremen", "value": "26 Siege", "sort_value": 26},
            {"name": "Borussia Dortmund", "value": "25 Siege", "sort_value": 25},
            {"name": "VfB Stuttgart", "value": "19 Siege", "sort_value": 19},
            {"name": "Schalke 04", "value": "18 Siege", "sort_value": 18},
            {"name": "Eintracht Frankfurt", "value": "17 Siege", "sort_value": 17},
            {"name": "Hamburger SV", "value": "16 Siege", "sort_value": 16},
            {"name": "1. FC Köln", "value": "15 Siege", "sort_value": 15},
            {"name": "Bayer 04 Leverkusen", "value": "14 Siege", "sort_value": 14},
            {"name": "Hertha BSC", "value": "11 Siege", "sort_value": 11},
            {"name": "VfL Wolfsburg", "value": "6 Siege", "sort_value": 6},
            {"name": "TSG Hoffenheim", "value": "5 Siege", "sort_value": 5}
        ]
    },
    {
        "question": "Welcher dieser einzelnen Fußballspiele verzeichnete weltweit die höchste offizielle Live-TV/Streaming-Reichweite? (Reichweite des Einzelspiels in Millionen Live-Zuschauern)",
        "data": [
            {"name": "WM-Finale 2022 (Argentinien vs. Frankreich)", "value": "1.500 Mio. Zuschauer", "sort_value": 1500},
            {"name": "WM-Finale 2018 (Frankreich vs. Kroatien)", "value": "1.120 Mio. Zuschauer", "sort_value": 1120},
            {"name": "WM-Finale 2002 (Brasilien vs. Deutschland)", "value": "1.100 Mio. Zuschauer", "sort_value": 1100},
            {"name": "WM-Finale 2014 (Deutschland vs. Argentinien)", "value": "1.010 Mio. Zuschauer", "sort_value": 1010},
            {"name": "WM-Finale 2010 (Spanien vs. Niederlande)", "value": "910 Mio. Zuschauer", "sort_value": 910},
            {"name": "WM-Finale 2006 (Italien vs. Frankreich)", "value": "715 Mio. Zuschauer", "sort_value": 715},
            {"name": "EM-Finale 2024 (Spanien vs. England)", "value": "340 Mio. Zuschauer", "sort_value": 340},
            {"name": "EM-Finale 2020 (Italien vs. England)", "value": "328 Mio. Zuschauer", "sort_value": 328},
            {"name": "Champions-League-Finale 2015 (Barcelona vs. Juventus)", "value": "180 Mio. Zuschauer", "sort_value": 180},
            {"name": "WM-Viertelfinale 2022 (England vs. Frankreich)", "value": "150 Mio. Zuschauer", "sort_value": 150},
            {"name": "Champions-League-Finale 2024 (Dortmund vs. Real Madrid)", "value": "140 Mio. Zuschauer", "sort_value": 140},
            {"name": "Euro-Viertelfinale 2024 (Deutschland vs. Spanien)", "value": "115 Mio. Zuschauer", "sort_value": 115}
        ]
    },
    {
        "question": "Welcher dieser Fußballspieler erreichte die höchste jemals offiziell gemessene Maximalgeschwindigkeit (Top-Speed in km/h)?",
        "data": [
            {"name": "Sven Botman", "value": "39.21 km/h", "sort_value": 39.21},
            {"name": "Darwin Núñez", "value": "38.00 km/h", "sort_value": 38.00},
            {"name": "Kylian Mbappé", "value": "37.90 km/h", "sort_value": 37.90},
            {"name": "Gareth Bale", "value": "36.90 km/h", "sort_value": 36.90},
            {"name": "Antonio Rüdiger", "value": "36.70 km/h", "sort_value": 36.70},
            {"name": "Mykhailo Mudryk", "value": "36.63 km/h", "sort_value": 36.63},
            {"name": "Ousmane Dembélé", "value": "36.60 km/h", "sort_value": 36.60},
            {"name": "Adama Traoré", "value": "36.60 km/h", "sort_value": 36.60},
            {"name": "Mohamed Salah", "value": "36.60 km/h", "sort_value": 36.60},
            {"name": "Alphonso Davies", "value": "36.51 km/h", "sort_value": 36.51},
            {"name": "Erling Haaland", "value": "36.30 km/h", "sort_value": 36.30},
            {"name": "Achraf Hakimi", "value": "36.25 km/h", "sort_value": 36.25}
        ]
    },
    {
        "question": "Welcher dieser Spieler hat vor seinem exakt 20. Geburtstag die meisten wettbewerbsübergreifenden Profi-Spiele (Klub & Nationalteam) absolviert?",
        "data": [
            {"name": "Jude Bellingham", "value": "171 Spiele", "sort_value": 171},
            {"name": "Gianluigi Donnarumma", "value": "153 Spiele", "sort_value": 153},
            {"name": "Cesc Fàbregas", "value": "131 Spiele", "sort_value": 131},
            {"name": "Wayne Rooney", "value": "126 Spiele", "sort_value": 126},
            {"name": "Pedri", "value": "122 Spiele", "sort_value": 122},
            {"name": "Eden Hazard", "value": "119 Spiele", "sort_value": 119},
            {"name": "Kylian Mbappé", "value": "116 Spiele", "sort_value": 116},
            {"name": "Gavi", "value": "111 Spiele", "sort_value": 111},
            {"name": "Raheem Sterling", "value": "104 Spiele", "sort_value": 104},
            {"name": "Cristiano Ronaldo", "value": "94 Spiele", "sort_value": 94},
            {"name": "Lionel Messi", "value": "78 Spiele", "sort_value": 78},
            {"name": "Erling Haaland", "value": "73 Spiele", "sort_value": 73}
        ]
    },
    {
        "question": "Welcher dieser Vereine hat in der ewigen Tabelle der UEFA Champions League (inkl. Europapokal der Landesmeister) historisch die meisten Punkte geholt? (Konvertiert auf die 3-Punkte-Regel)",
        "data": [
            {"name": "Real Madrid", "value": "952 Punkte", "sort_value": 952},
            {"name": "FC Bayern München", "value": "774 Punkte", "sort_value": 774},
            {"name": "FC Barcelona", "value": "670 Punkte", "sort_value": 670},
            {"name": "Manchester United", "value": "542 Punkte", "sort_value": 542},
            {"name": "Juventus Turin", "value": "528 Punkte", "sort_value": 528},
            {"name": "FC Liverpool", "value": "448 Punkte", "sort_value": 448},
            {"name": "AC Mailand", "value": "381 Punkte", "sort_value": 381},
            {"name": "FC Porto", "value": "315 Punkte", "sort_value": 315},
            {"name": "FC Chelsea", "value": "312 Punkte", "sort_value": 312},
            {"name": "Arsenal FC", "value": "306 Punkte", "sort_value": 306},
            {"name": "Benfica Lissabon", "value": "271 Punkte", "sort_value": 271},
            {"name": "Paris Saint-Germain", "value": "211 Punkte", "sort_value": 211}
        ]
    },
    {
        "question": "Welcher dieser Spieler hat in seiner Karriere die meisten 'Man of the Match' (MotM) Auszeichnungen erhalten? (Messi und Ronaldo wurden als Top 2 weggelassen!)",
        "data": [
            {"name": "Eden Hazard", "value": "100 MotM", "sort_value": 100},
            {"name": "Zlatan Ibrahimović", "value": "98 MotM", "sort_value": 98},
            {"name": "Neymar Jr.", "value": "91 MotM", "sort_value": 91},
            {"name": "Robert Lewandowski", "value": "88 MotM", "sort_value": 88},
            {"name": "Harry Kane", "value": "83 MotM", "sort_value": 83},
            {"name": "Kevin De Bruyne", "value": "79 MotM", "sort_value": 79},
            {"name": "Antoine Griezmann", "value": "75 MotM", "sort_value": 75},
            {"name": "Luis Suárez", "value": "72 MotM", "sort_value": 72},
            {"name": "Mohamed Salah", "value": "70 MotM", "sort_value": 70},
            {"name": "Karim Benzema", "value": "64 MotM", "sort_value": 64},
            {"name": "Kylian Mbappé", "value": "58 MotM", "sort_value": 58},
            {"name": "Erling Haaland", "value": "42 MotM", "sort_value": 42}
        ]
    },
    {
        "question": "Welcher dieser Toptorjäger hat seit dem 1. Januar 2000 wettbewerbsübergreifend die meisten offiziellen Profi-Tore erzielt?",
        "data": [
            {"name": "Cristiano Ronaldo", "value": "915 Tore", "sort_value": 915},
            {"name": "Lionel Messi", "value": "855 Tore", "sort_value": 855},
            {"name": "Robert Lewandowski", "value": "682 Tore", "sort_value": 682},
            {"name": "Zlatan Ibrahimović", "value": "573 Tore", "sort_value": 573},
            {"name": "Luis Suárez", "value": "571 Tore", "sort_value": 571},
            {"name": "Karim Benzema", "value": "482 Tore", "sort_value": 482},
            {"name": "Edinson Cavani", "value": "452 Tore", "sort_value": 452},
            {"name": "Neymar Jr.", "value": "442 Tore", "sort_value": 442},
            {"name": "Harry Kane", "value": "435 Tore", "sort_value": 435},
            {"name": "Kylian Mbappé", "value": "355 Tore", "sort_value": 355},
            {"name": "Mohamed Salah", "value": "281 Tore", "sort_value": 281},
            {"name": "Erling Haaland", "value": "278 Tore", "sort_value": 278}
        ]
    },
    {
        "question": "Welcher dieser europäischen Spitzenvereine hat auf Instagram die meisten Follower (Stand 2026)?",
        "data": [
            {"name": "Real Madrid", "value": "182 Mio. Follower", "sort_value": 182.0},
            {"name": "FC Barcelona", "value": "145 Mio. Follower", "sort_value": 145.0},
            {"name": "Paris Saint-Germain", "value": "66 Mio. Follower", "sort_value": 66.0},
            {"name": "Manchester United", "value": "65 Mio. Follower", "sort_value": 65.0},
            {"name": "Juventus Turin", "value": "61 Mio. Follower", "sort_value": 61.0},
            {"name": "Manchester City", "value": "58 Mio. Follower", "sort_value": 58.0},
            {"name": "FC Liverpool", "value": "49 Mio. Follower", "sort_value": 49.0},
            {"name": "FC Bayern München", "value": "44 Mio. Follower", "sort_value": 44.0},
            {"name": "FC Chelsea", "value": "43 Mio. Follower", "sort_value": 43.0},
            {"name": "Arsenal FC", "value": "33 Mio. Follower", "sort_value": 33.0},
            {"name": "Borussia Dortmund", "value": "22 Mio. Follower", "sort_value": 22.0},
            {"name": "Atlético Madrid", "value": "18 Mio. Follower", "sort_value": 18.0}
        ]
    },
    {
        "question": "Welcher dieser Spieler hat in der Geschichte des Profifußballs die meisten Roten Karten (Platzverweise) kassiert?",
        "data": [
            {"name": "Gerardo Bedoya", "value": "46 Rote Karten", "sort_value": 46},
            {"name": "Sergio Ramos", "value": "29 Rote Karten", "sort_value": 29},
            {"name": "Cyril Rool", "value": "27 Rote Karten", "sort_value": 27},
            {"name": "Alexis Ruano Delgado", "value": "22 Rote Karten", "sort_value": 22},
            {"name": "Paolo Montero", "value": "21 Rote Karten", "sort_value": 21},
            {"name": "Felipe Melo", "value": "20 Rote Karten", "sort_value": 20},
            {"name": "Rafael Márquez", "value": "17 Rote Karten", "sort_value": 17},
            {"name": "Gary Medel", "value": "15 Rote Karten", "sort_value": 15},
            {"name": "Zlatan Ibrahimović", "value": "14 Rote Karten", "sort_value": 14},
            {"name": "Patrick Vieira", "value": "12 Rote Karten", "sort_value": 12},
            {"name": "Roy Keane", "value": "11 Rote Karten", "sort_value": 11},
            {"name": "Pepe", "value": "10 Rote Karten", "sort_value": 10}
        ]
    },
    {
        "question": "Welcher dieser weltweiten Fußballvereine hat die höchste Anzahl an offiziell eingetragenen, zahlenden Mitgliedern?",
        "data": [
            {"name": "FC Bayern München", "value": "330.000 Mitglieder", "sort_value": 330000},
            {"name": "River Plate", "value": "250.000 Mitglieder", "sort_value": 250000},
            {"name": "SL Benfica", "value": "240.000 Mitglieder", "sort_value": 240000},
            {"name": "Boca Juniors", "value": "230.000 Mitglieder", "sort_value": 230000},
            {"name": "Borussia Dortmund", "value": "200.000 Mitglieder", "sort_value": 200000},
            {"name": "Schalke 04", "value": "180.000 Mitglieder", "sort_value": 180000},
            {"name": "FC Barcelona", "value": "150.000 Mitglieder", "sort_value": 150000},
            {"name": "Eintracht Frankfurt", "value": "140.000 Mitglieder", "sort_value": 140000},
            {"name": "1. FC Köln", "value": "135.000 Mitglieder", "sort_value": 135000},
            {"name": "VfB Stuttgart", "value": "110.000 Mitglieder", "sort_value": 110000},
            {"name": "Real Madrid", "value": "100.000 Mitglieder", "sort_value": 100000},
            {"name": "Borussia Mönchengladbach", "value": "100.000 Mitglieder", "sort_value": 100000}
        ]
    },
    {
        "question": "Welches dieser historischen Fußballspiele im Stadion verzeichnete die höchste offizielle (oder präzise gezählte) Zuschauerzahl direkt vor Ort?",
        "data": [
            {"name": "WM-Finale 1950 (Uruguay vs. Brasilien)", "value": "173.850 Zuschauer", "sort_value": 173850},
            {"name": "Europapokal-Finale 1960 (Real vs. Eintracht Frankfurt)", "value": "127.621 Zuschauer", "sort_value": 127621},
            {"name": "FA-Cup Finale 1923 (Bolton vs. West Ham)", "value": "126.047 Zuschauer", "sort_value": 126047},
            {"name": "WM-Finale 1986 (Argentinien vs. Westdeutschland)", "value": "114.600 Zuschauer", "sort_value": 114600},
            {"name": "El Clásico 2018 (Barcelona vs. Real Madrid)", "value": "97.939 Zuschauer", "sort_value": 97939},
            {"name": "WM-Finale 1994 (Brasilien vs. Italien)", "value": "94.194 Zuschauer", "sort_value": 94194},
            {"name": "CL-Finale 2024 (Dortmund vs. Real Madrid)", "value": "86.211 Zuschauer", "sort_value": 86211},
            {"name": "WM-Finale 2018 (Frankreich vs. Kroatien)", "value": "78.011 Zuschauer", "sort_value": 78011},
            {"name": "CL-Finale 2022 (Real Madrid vs. Liverpool)", "value": "75.000 Zuschauer", "sort_value": 75000},
            {"name": "WM-Finale 2014 (Deutschland vs. Argentinien)", "value": "74.738 Zuschauer", "sort_value": 74738},
            {"name": "EM-Finale 2021 (Italien vs. England)", "value": "67.173 Zuschauer", "sort_value": 67173},
            {"name": "WM-Eröffnungsspiel 2006 (Deutschland vs. Costa Rica)", "value": "66.000 Zuschauer", "sort_value": 66000}
        ]
    },
    {
        "question": "Welcher dieser Akteure hat die meisten Weltmeistertitel als aktiver Spieler gewonnen?",
        "data": [
            {"name": "Pelé (Brasilien)", "value": "3 WM-Titel", "sort_value": 3},
            {"name": "Cafu (Brasilien)", "value": "2 WM-Titel", "sort_value": 2},
            {"name": "Ronaldo (Brasilien)", "value": "2 WM-Titel", "sort_value": 2},
            {"name": "Daniel Passarella (Argentinien)", "value": "2 WM-Titel", "sort_value": 2},
            {"name": "Giuseppe Meazza (Italien)", "value": "2 WM-Titel", "sort_value": 2},
            {"name": "Giovanni Ferrari (Italien)", "value": "2 WM-Titel", "sort_value": 2},
            {"name": "Garrincha (Brasilien)", "value": "2 WM-Titel", "sort_value": 2},
            {"name": "Gilmar (Brasilien)", "value": "2 WM-Titel", "sort_value": 2},
            {"name": "Zagallo (Brasilien)", "value": "2 WM-Titel", "sort_value": 2},
            {"name": "Franz Beckenbauer (Deutschland)", "value": "1 WM-Titel", "sort_value": 1},
            {"name": "Diego Maradona (Argentinien)", "value": "1 WM-Titel", "sort_value": 1},
            {"name": "Lionel Messi (Argentinien)", "value": "1 WM-Titel", "sort_value": 1}
        ]
    },
    {
        "question": "Welche Nationalmannschaft hat in der Geschichte der Weltmeisterschaften die meisten Platzverweise (Rote Karten) hinnehmen müssen?",
        "data": [
            {"name": "Brasilien", "value": "11 Rote Karten", "sort_value": 11},
            {"name": "Argentinien", "value": "10 Rote Karten", "sort_value": 10},
            {"name": "Uruguay", "value": "9 Rote Karten", "sort_value": 9},
            {"name": "Italien", "value": "8 Rote Karten", "sort_value": 8},
            {"name": "Kamerun", "value": "8 Rote Karten", "sort_value": 8},
            {"name": "Deutschland", "value": "7 Rote Karten", "sort_value": 7},
            {"name": "Niederlande", "value": "7 Rote Karten", "sort_value": 7},
            {"name": "Mexiko", "value": "6 Rote Karten", "sort_value": 6},
            {"name": "Frankreich", "value": "6 Rote Karten", "sort_value": 6},
            {"name": "Portugal", "value": "6 Rote Karten", "sort_value": 6},
            {"name": "Dänemark", "value": "4 Rote Karten", "sort_value": 4},
            {"name": "England", "value": "3 Rote Karten", "sort_value": 3}
        ]
    },
    {
        "question": "Wer war der biologisch jüngste Torschütze in der Historie der Weltmeisterschaften?",
        "data": [
            {"name": "Pelé (1958)", "value": "17.6 Jahre alt", "sort_value": 17.6},
            {"name": "Manuel Rosas (1930)", "value": "18.3 Jahre alt", "sort_value": 18.3},
            {"name": "Gavi (2022)", "value": "18.3 Jahre alt", "sort_value": 18.3},
            {"name": "Michael Owen (1998)", "value": "18.5 Jahre alt", "sort_value": 18.5},
            {"name": "Nicolae Kovacs (1930)", "value": "18.6 Jahre alt", "sort_value": 18.6},
            {"name": "Dmitry Sychev (2002)", "value": "18.7 Jahre alt", "sort_value": 18.7},
            {"name": "Lionel Messi (2006)", "value": "18.9 Jahre alt", "sort_value": 18.9},
            {"name": "Julian Green (2014)", "value": "19.0 Jahre alt", "sort_value": 19.0},
            {"name": "Divock Origi (2014)", "value": "19.2 Jahre alt", "sort_value": 19.2},
            {"name": "Jude Bellingham (2022)", "value": "19.4 Jahre alt", "sort_value": 19.4},
            {"name": "Kylian Mbappé (2018)", "value": "19.5 Jahre alt", "sort_value": 19.5},
            {"name": "Bukayo Saka (2022)", "value": "21.2 Jahre alt", "sort_value": 21.2}
        ]
    },
    {
        "question": "Welcher dieser Elite-Akteure verzeichnet die statistisch meisten direkt gemessenen Torvorlagen (Assists) in seiner gesamten Profikarriere?",
        "data": [
            {"name": "Lionel Messi", "value": "362 Assists", "sort_value": 362},
            {"name": "Thomas Müller", "value": "304 Assists", "sort_value": 304},
            {"name": "Luis Suárez", "value": "298 Assists", "sort_value": 298},
            {"name": "Kevin De Bruyne", "value": "287 Assists", "sort_value": 287},
            {"name": "Ángel Di María", "value": "262 Assists", "sort_value": 262},
            {"name": "Neymar Jr.", "value": "258 Assists", "sort_value": 258},
            {"name": "Cristiano Ronaldo", "value": "251 Assists", "sort_value": 251},
            {"name": "Mesut Özil", "value": "240 Assists", "sort_value": 240},
            {"name": "Cesc Fàbregas", "value": "234 Assists", "sort_value": 234},
            {"name": "Zlatan Ibrahimović", "value": "202 Assists", "sort_value": 202},
            {"name": "Karim Benzema", "value": "196 Assists", "sort_value": 196},
            {"name": "Kylian Mbappé", "value": "152 Assists", "sort_value": 152}
        ]
    }
])

CATEGORIES["Natur & Wissenschaft"].extend([
    {
        "question": "Welches dieser bekannten Metalle besitzt den höchsten Schmelzpunkt (in Grad Celsius)?",
        "data": [
            {"name": "Wolfram", "value": "3.422 °C", "sort_value": 3422},
            {"name": "Rhenium", "value": "3.186 °C", "sort_value": 3186},
            {"name": "Osmium", "value": "3.033 °C", "sort_value": 3033},
            {"name": "Tantal", "value": "3.017 °C", "sort_value": 3017},
            {"name": "Molybdän", "value": "2.623 °C", "sort_value": 2623},
            {"name": "Iridium", "value": "2.446 °C", "sort_value": 2446},
            {"name": "Platin", "value": "1.768 °C", "sort_value": 1768},
            {"name": "Titan", "value": "1.668 °C", "sort_value": 1668},
            {"name": "Eisen", "value": "1.538 °C", "sort_value": 1538},
            {"name": "Kupfer", "value": "1.085 °C", "sort_value": 1085},
            {"name": "Gold", "value": "1.064 °C", "sort_value": 1064},
            {"name": "Aluminium", "value": "660 °C", "sort_value": 660}
        ]
    }
])

CATEGORIES["Geografie"].extend([
    {
        "question": "Welche dieser weltweiten Rieseninseln besitzt flächenmäßig die größte Ausdehnung? (Kontinente wie Australien ausgeschlossen!)",
        "data": [
            {"name": "Grönland", "value": "2.166.086 km²", "sort_value": 2166086},
            {"name": "Neu-Guinea", "value": "785.753 km²", "sort_value": 785753},
            {"name": "Borneo", "value": "743.330 km²", "sort_value": 743330},
            {"name": "Madagaskar", "value": "587.041 km²", "sort_value": 587041},
            {"name": "Baffininsel", "value": "507.451 km²", "sort_value": 507451},
            {"name": "Sumatra", "value": "473.481 km²", "sort_value": 473481},
            {"name": "Honshu", "value": "227.960 km²", "sort_value": 227960},
            {"name": "Großbritannien", "value": "209.331 km²", "sort_value": 209331},
            {"name": "Victoria-Insel", "value": "217.291 km²", "sort_value": 217291},
            {"name": "Ellesmere-Insel", "value": "196.236 km²", "sort_value": 196236},
            {"name": "Sulawesi", "value": "174.600 km²", "sort_value": 174600},
            {"name": "Neuseeland Südinsel", "value": "150.437 km²", "sort_value": 150437}
        ]
    }
])