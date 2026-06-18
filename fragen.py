# fragen.py
# Umfangreiche Fragenbasis für Quiz Royale.
# Der 'sort_value' erlaubt präzise mathematische Vergleiche und das Abfangen von Gleichständen!

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
                {"name": "RB Leipzig", "value": "503,8 Mio. €", "sort_value": 503.8},
                {"name": "Bayer 04 Leverkusen", "value": "438,5 Mio. €", "sort_value": 438.5},
                {"name": "VfB Stuttgart", "value": "403,9 Mio. €", "sort_value": 403.9},
                {"name": "Eintracht Frankfurt", "value": "377,5 Mio. €", "sort_value": 377.5},
                {"name": "TSG Hoffenheim", "value": "270,2 Mio. €", "sort_value": 270.2},
                {"name": "SC Freiburg", "value": "239,3 Mio. €", "sort_value": 239.3},
                {"name": "VfL Wolfsburg", "value": "215,1 Mio. €", "sort_value": 215.1},
                {"name": "Hamburger SV", "value": "175,9 Mio. €", "sort_value": 175.9},
                {"name": "Werder Bremen", "value": "170,5 Mio. €", "sort_value": 170.5},
                {"name": "FC Augsburg", "value": "166,9 Mio. €", "sort_value": 166.9},
                {"name": "1. FSV Mainz 05", "value": "158,5 Mio. €", "sort_value": 158.5},
                {"name": "1. FC Köln", "value": "154,5 Mio. €", "sort_value": 154.5}
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
            "question": "Welches dieser chemischen Elemente hat die höchste Dichte bei Raumtemperatur?",
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
            "question": "Wie hoch sind diese bekannten Gipfel der Erde?",
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
            "question": "Welches dieser Länder hat flächenmäßig die größte Ausdehnung?",
            "data": [
                {"name": "Russland", "value": "17,1 Mio. km²", "sort_value": 17.1},
                {"name": "Kanada", "value": "9,98 Mio. km²", "sort_value": 9.98},
                {"name": "USA", "value": "9,83 Mio. km²", "sort_value": 9.83},
                {"name": "China", "value": "9,59 Mio. km²", "sort_value": 9.59},
                {"name": "Brasilien", "value": "8,51 Mio. km²", "sort_value": 8.51},
                {"name": "Australien", "value": "7,69 Mio. km²", "sort_value": 7.69},
                {"name": "Indien", "value": "3,28 Mio. km²", "sort_value": 3.28},
                {"name": "Argentinien", "value": "2,78 Mio. km²", "sort_value": 2.78},
                {"name": "Kasachstan", "value": "2,72 Mio. km²", "sort_value": 2.72},
                {"name": "Algerien", "value": "2,38 Mio. km²", "sort_value": 2.38},
                {"name": "Kongo (Dem. Rep.)", "value": "2,34 Mio. km²", "sort_value": 2.34},
                {"name": "Grönland", "value": "2,16 Mio. km²", "sort_value": 2.16}
            ]
        }
    ]
}