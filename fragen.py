# fragen.py
# Hier liegen alle Fragen. Die Logik greift automatisch darauf zu.

CATEGORIES = {
    "Fußball: Torschützen": {
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
    "Geschichte: Monarchen": {
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
    "Geografie: Berge": {
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
    },
    "Kino: Einspielergebnisse": {
        "question": "Welcher dieser Filme hat weltweit am meisten Geld eingespielt (Stand 2024)?",
        "data": [
            {"name": "Avatar", "value": "2,92 Mrd. $"},
            {"name": "Avengers: Endgame", "value": "2,79 Mrd. $"},
            {"name": "Avatar: The Way of Water", "value": "2,32 Mrd. $"},
            {"name": "Titanic", "value": "2,25 Mrd. $"},
            {"name": "Star Wars: Das Erwachen der Macht", "value": "2,06 Mrd. $"},
            {"name": "Avengers: Infinity War", "value": "2,05 Mrd. $"},
            {"name": "Spider-Man: No Way Home", "value": "1,92 Mrd. $"},
            {"name": "Jurassic World", "value": "1,67 Mrd. $"},
            {"name": "Der König der Löwen (2019)", "value": "1,66 Mrd. $"},
            {"name": "The Avengers", "value": "1,51 Mrd. $"},
            {"name": "Fast & Furious 7", "value": "1,51 Mrd. $"},
            {"name": "Top Gun: Maverick", "value": "1,49 Mrd. $"}
        ]
    },
    "Geografie: Länderfläche": {
        "question": "Welches dieser Länder hat die größte Fläche?",
        "data": [
            {"name": "Russland", "value": "17,1 Mio. km²"},
            {"name": "Kanada", "value": "9,98 Mio. km²"},
            {"name": "USA", "value": "9,83 Mio. km²"},
            {"name": "China", "value": "9,59 Mio. km²"},
            {"name": "Brasilien", "value": "8,51 Mio. km²"},
            {"name": "Australien", "value": "7,69 Mio. km²"},
            {"name": "Indien", "value": "3,28 Mio. km²"},
            {"name": "Argentinien", "value": "2,78 Mio. km²"},
            {"name": "Kasachstan", "value": "2,72 Mio. km²"},
            {"name": "Algerien", "value": "2,38 Mio. km²"},
            {"name": "Kongo (DR)", "value": "2,34 Mio. km²"},
            {"name": "Grönland", "value": "2,16 Mio. km²"}
        ]
    },
    "Biologie: Tier-Geschwindigkeit": {
        "question": "Welches dieser Tiere erreicht die höchste Maximalgeschwindigkeit an Land?",
        "data": [
            {"name": "Gepard", "value": "120 km/h"},
            {"name": "Gabelbock", "value": "88 km/h"},
            {"name": "Springbock", "value": "88 km/h"},
            {"name": "Gnu", "value": "80 km/h"},
            {"name": "Löwe", "value": "80 km/h"},
            {"name": "Hirschziegenantilope", "value": "80 km/h"},
            {"name": "Hase", "value": "72 km/h"},
            {"name": "Windhund (Greyhound)", "value": "72 km/h"},
            {"name": "Afrikanischer Wildhund", "value": "71 km/h"},
            {"name": "Känguru", "value": "71 km/h"},
            {"name": "Pferd (Quarter Horse)", "value": "70 km/h"},
            {"name": "Strauß", "value": "70 km/h"}
        ]
    },
    "Astronomie: Monde": {
        "question": "Welcher Planet unseres Sonnensystems hat die meisten bekannten Monde?",
        "data": [
            {"name": "Saturn", "value": "146 Monde"},
            {"name": "Jupiter", "value": "95 Monde"},
            {"name": "Uranus", "value": "28 Monde"},
            {"name": "Neptun", "value": "16 Monde"},
            {"name": "Pluto (Zwergplanet)", "value": "5 Monde"},
            {"name": "Mars", "value": "2 Monde"},
            {"name": "Erde", "value": "1 Mond"},
            {"name": "Haumea (Zwergplanet)", "value": "2 Monde"},
            {"name": "Makemake (Zwergplanet)", "value": "1 Mond"},
            {"name": "Eris (Zwergplanet)", "value": "1 Mond"},
            {"name": "Venus", "value": "0 Monde"},
            {"name": "Merkur", "value": "0 Monde"}
        ]
    },
    "Wirtschaft: Unternehmen": {
        "question": "Welches dieser Unternehmen hat die höchste Marktkapitalisierung (Stand Anfang 2024)?",
        "data": [
            {"name": "Microsoft", "value": "3,0 Billionen $"},
            {"name": "Apple", "value": "2,8 Billionen $"},
            {"name": "Saudi Aramco", "value": "2,0 Billionen $"},
            {"name": "Alphabet (Google)", "value": "1,8 Billionen $"},
            {"name": "Amazon", "value": "1,7 Billionen $"},
            {"name": "NVIDIA", "value": "1,5 Billionen $"},
            {"name": "Meta (Facebook)", "value": "1,0 Billionen $"},
            {"name": "Berkshire Hathaway", "value": "850 Milliarden $"},
            {"name": "Tesla", "value": "600 Milliarden $"},
            {"name": "Eli Lilly", "value": "580 Milliarden $"},
            {"name": "Visa", "value": "550 Milliarden $"},
            {"name": "TSMC", "value": "530 Milliarden $"}
        ]
    },
    "Musik: Spotify Streams": {
        "question": "Welcher dieser Songs hat die meisten Streams auf Spotify (Stand Jan 2024)?",
        "data": [
            {"name": "Blinding Lights (The Weeknd)", "value": "4,0 Mrd."},
            {"name": "Shape of You (Ed Sheeran)", "value": "3,7 Mrd."},
            {"name": "Someone You Loved (Lewis Capaldi)", "value": "3,1 Mrd."},
            {"name": "Sunflower (Post Malone)", "value": "3,1 Mrd."},
            {"name": "Starboy (The Weeknd)", "value": "2,9 Mrd."},
            {"name": "As It Was (Harry Styles)", "value": "2,9 Mrd."},
            {"name": "Dance Monkey (Tones And I)", "value": "2,9 Mrd."},
            {"name": "One Dance (Drake)", "value": "2,9 Mrd."},
            {"name": "Stay (The Kid LAROI)", "value": "2,8 Mrd."},
            {"name": "Rockstar (Post Malone)", "value": "2,8 Mrd."},
            {"name": "Believer (Imagine Dragons)", "value": "2,7 Mrd."},
            {"name": "Heat Waves (Glass Animals)", "value": "2,7 Mrd."}
        ]
    },
    "Demografie: Städte": {
        "question": "Welche dieser Metropolregionen hat die meisten Einwohner?",
        "data": [
            {"name": "Tokio (Japan)", "value": "37,4 Mio."},
            {"name": "Delhi (Indien)", "value": "29,3 Mio."},
            {"name": "Schanghai (China)", "value": "26,3 Mio."},
            {"name": "São Paulo (Brasilien)", "value": "21,8 Mio."},
            {"name": "Mexiko-Stadt (Mexiko)", "value": "21,6 Mio."},
            {"name": "Kairo (Ägypten)", "value": "20,4 Mio."},
            {"name": "Dhaka (Bangladesch)", "value": "20,2 Mio."},
            {"name": "Mumbai (Indien)", "value": "20,1 Mio."},
            {"name": "Peking (China)", "value": "19,4 Mio."},
            {"name": "Osaka (Japan)", "value": "19,2 Mio."},
            {"name": "Karatschi (Pakistan)", "value": "15,4 Mio."},
            {"name": "Istanbul (Türkei)", "value": "15,0 Mio."}
        ]
    }
}