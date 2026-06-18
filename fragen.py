# fragen.py
# Kategorien enthalten nun Listen von verschiedenen Fragen.
# Der 'sort_value' ist entscheidend für die mathematische Berechnung von Gleichständen!

CATEGORIES = {
    "Fußball": [
        {
            "question": "Welcher dieser Spieler hat die meisten Karrieretore (Stand 2024)?",
            "data": [
                {"name": "Cristiano Ronaldo", "value": "873 Tore", "sort_value": 873},
                {"name": "Lionel Messi", "value": "821 Tore", "sort_value": 821},
                {"name": "Pelé", "value": "762 Tore", "sort_value": 762},
                {"name": "Romário", "value": "755 Tore", "sort_value": 755},
                {"name": "Ferenc Puskás", "value": "724 Tore", "sort_value": 724},
                {"name": "Josef Bican", "value": "722 Tore", "sort_value": 722},
                {"name": "Jimmy Jones", "value": "648 Tore", "sort_value": 648},
                {"name": "Gerd Müller", "value": "634 Tore", "sort_value": 634},
                {"name": "Robert Lewandowski", "value": "621 Tore", "sort_value": 621},
                {"name": "Zlatan Ibrahimović", "value": "573 Tore", "sort_value": 573},
                {"name": "Luis Suárez", "value": "557 Tore", "sort_value": 557},
                {"name": "Eusébio", "value": "473 Tore", "sort_value": 473}
            ]
        },
        {
            "question": "Welcher dieser Fußballer wurde in der Saison 23/24 in der Liga am meisten gefoult?",
            "data": [
                {"name": "Vinícius Júnior", "value": "112 Fouls", "sort_value": 112},
                {"name": "Jude Bellingham", "value": "98 Fouls", "sort_value": 98},
                {"name": "Jack Grealish", "value": "95 Fouls", "sort_value": 95},
                {"name": "Bukayo Saka", "value": "87 Fouls", "sort_value": 87},
                {"name": "Bruno Guimarães", "value": "84 Fouls", "sort_value": 84},
                {"name": "Jordan Ayew", "value": "84 Fouls", "sort_value": 84},
                {"name": "James Maddison", "value": "78 Fouls", "sort_value": 78},
                {"name": "John McGinn", "value": "75 Fouls", "sort_value": 75},
                {"name": "Lucas Paquetá", "value": "72 Fouls", "sort_value": 72},
                {"name": "Leroy Sané", "value": "65 Fouls", "sort_value": 65},
                {"name": "Phil Foden", "value": "60 Fouls", "sort_value": 60},
                {"name": "Rodri", "value": "52 Fouls", "sort_value": 52}
            ]
        },
        {
            "question": "Welcher dieser Vereine hat die meisten Champions-League-Titel gewonnen?",
            "data": [
                {"name": "Real Madrid", "value": "15 Titel", "sort_value": 15},
                {"name": "AC Mailand", "value": "7 Titel", "sort_value": 7},
                {"name": "FC Bayern München", "value": "6 Titel", "sort_value": 6},
                {"name": "FC Liverpool", "value": "6 Titel", "sort_value": 6},
                {"name": "FC Barcelona", "value": "5 Titel", "sort_value": 5},
                {"name": "Ajax Amsterdam", "value": "4 Titel", "sort_value": 4},
                {"name": "Inter Mailand", "value": "3 Titel", "sort_value": 3},
                {"name": "Manchester United", "value": "3 Titel", "sort_value": 3},
                {"name": "Juventus Turin", "value": "2 Titel", "sort_value": 2},
                {"name": "FC Chelsea", "value": "2 Titel", "sort_value": 2},
                {"name": "Borussia Dortmund", "value": "1 Titel", "sort_value": 1},
                {"name": "Manchester City", "value": "1 Titel", "sort_value": 1}
            ]
        }
    ],
    "Natur & Wissenschaft": [
        {
            "question": "Welches dieser Tiere erreicht die höchste Maximalgeschwindigkeit an Land?",
            "data": [
                {"name": "Gepard", "value": "120 km/h", "sort_value": 120},
                {"name": "Gabelbock", "value": "88 km/h", "sort_value": 88},
                {"name": "Springbock", "value": "88 km/h", "sort_value": 88},
                {"name": "Gnu", "value": "80 km/h", "sort_value": 80},
                {"name": "Löwe", "value": "80 km/h", "sort_value": 80},
                {"name": "Windhund (Greyhound)", "value": "72 km/h", "sort_value": 72},
                {"name": "Feldhase", "value": "72 km/h", "sort_value": 72},
                {"name": "Känguru", "value": "71 km/h", "sort_value": 71},
                {"name": "Afrikanischer Wildhund", "value": "71 km/h", "sort_value": 71},
                {"name": "Pferd (Quarter Horse)", "value": "70 km/h", "sort_value": 70},
                {"name": "Strauß", "value": "70 km/h", "sort_value": 70},
                {"name": "Grizzlybär", "value": "56 km/h", "sort_value": 56}
            ]
        },
        {
            "question": "Wie viele bekannte Monde haben diese Himmelskörper im Sonnensystem?",
            "data": [
                {"name": "Saturn", "value": "146 Monde", "sort_value": 146},
                {"name": "Jupiter", "value": "95 Monde", "sort_value": 95},
                {"name": "Uranus", "value": "28 Monde", "sort_value": 28},
                {"name": "Neptun", "value": "16 Monde", "sort_value": 16},
                {"name": "Pluto (Zwergplanet)", "value": "5 Monde", "sort_value": 5},
                {"name": "Mars", "value": "2 Monde", "sort_value": 2},
                {"name": "Haumea (Zwergplanet)", "value": "2 Monde", "sort_value": 2},
                {"name": "Erde", "value": "1 Mond", "sort_value": 1},
                {"name": "Makemake (Zwergplanet)", "value": "1 Mond", "sort_value": 1},
                {"name": "Eris (Zwergplanet)", "value": "1 Mond", "sort_value": 1},
                {"name": "Venus", "value": "0 Monde", "sort_value": 0},
                {"name": "Merkur", "value": "0 Monde", "sort_value": 0}
            ]
        }
    ],
    "Geografie": [
        {
            "question": "Wie hoch sind diese bekannten Berge?",
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
            "question": "Welches dieser Länder hat die größte Fläche?",
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
                {"name": "Kongo (DR)", "value": "2,34 Mio. km²", "sort_value": 2.34},
                {"name": "Grönland", "value": "2,16 Mio. km²", "sort_value": 2.16}
            ]
        }
    ]
}