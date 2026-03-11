"""Module for Soccer Manager Engine"""

first_division = {
    "Honduran National Professional Football League (First Division)": [
        "Real España",
        "Motagua",
        "Olimpia",
        "Victoria",
        "Olancho F.C.",
        "Maratón",
        "Platense",
        "Club Deportivo Choloma",
        "Juticalpa",
        "Lobos UPNFM",
        "Club Deportivo Génesis Policía Nacional",
    ]
}

finder_first_division = {
    "Real España": "https://es.wikipedia.org/wiki/Real_Club_Deportivo_España",
    "Motagua": "https://es.wikipedia.org/wiki/Fútbol_Club_Motagua",
    "Olimpia": "https://es.wikipedia.org/wiki/Club_Olimpia_Deportivo",
    "Victoria": "https://es.wikipedia.org/wiki/Club_Deportivo_Victoria",
    "Olancho F.C.": "https://es.wikipedia.org/wiki/Olancho_Fútbol_Club",
    "Maratón": "https://es.wikipedia.org/wiki/Club_Deportivo_Marathón",
    "Platense": "https://en.wikipedia.org/wiki/Platense_F.C.",
    "Club Deportivo Choloma": "https://es.wikipedia.org/wiki/Club_Deportivo_Choloma",
    "Juticalpa": "https://es.wikipedia.org/wiki/Juticalpa_Fútbol_Club",
    "Lobos UPNFM": "https://en.wikipedia.org/wiki/Lobos_UPNFM",
    "Club Deportivo Génesis Policía Nacional": "https://es.wikipedia.org/wiki/Club_Deportivo_Génesis",
}

ascenso_league = {
    "Group A": [
        "Boca Juniors",
        "Vida",
        "Juventus",
        "Social Sol",
        "Sampdoria",
        "Real Sociedad",
        "Roma F.C.",
    ],
    "Group B": [
        "Honduras Progreso",
        "Atlético Junior",
        "Tela F.C.",
        "F.C. Santa Rosa",
        "Oro Verde F.C.",
        "Estrella F.C.",
    ],
    "Group C": [
        "CD Choloma",
        "Parrillas One",
        "Leones HT6",
        "C.D. Brasilia",
        "Pumas F.C.",
        "Lone F.C.",
    ],
    "Group D": [
        "San Juan Huracán",
        "Olimpia Occidental",
        "Santo Domingo Savio",
        "Cuervos",
        "San Juan Gualjoco",
        "Real Juventud",
    ],
    "Group E": [
        "Atlético Independiente",
        "Real Tegus",
        "AFFI Academia",
        "CD Pirata",
        "FAS",
        "Inter",
        "Policía Nacional",
    ],
    "Group F": [
        "Hondupino",
        "Estrella Roja",
        "Gimnástico",
        "Arsenal SAO",
        "San Rafael",
        "Meluca F.C.",
    ],
}

finder_ascenso = {
    # Grupo A
    "Boca Juniors": "",
    "Vida": "https://es.wikipedia.org/wiki/Club_Deportivo_y_Social_Vida",
    "Juventus": "",
    "Social Sol": "",
    "Sampdoria": "",
    "Real Sociedad": "https://es.wikipedia.org/wiki/Club_Deportivo_Real_Sociedad",
    "Roma F.C.": "",
    # Grupo B
    "Honduras Progreso": "https://es.wikipedia.org/wiki/Club_Deportivo_Honduras_Progreso",
    "Atlético Junior": "",
    "Tela F.C.": "",
    "F.C. Santa Rosa": "",
    "Oro Verde F.C.": "",
    "Estrella F.C.": "",
    # Grupo C
    "CD Choloma": "",
    "Parrillas One": "https://es.wikipedia.org/wiki/Club_Deportivo_Parrillas_One",
    "Leones HT6": "",
    "C.D. Brasilia": "",
    "Pumas F.C.": "",
    "Lone F.C.": "",
    # Grupo D
    "San Juan Huracán": "",
    "Olimpia Occidental": "",
    "Santo Domingo Savio": "",
    "Cuervos": "",
    "San Juan Gualjoco": "",
    "Real Juventud": "",
    # Grupo E
    "Atlético Independiente": "",
    "Real Tegus": "",
    "AFFI Academia": "",
    "CD Pirata": "",
    "FAS": "",
    "Inter": "",
    "Policía Nacional": "",
    # Grupo F
    "Hondupino": "",
    "Estrella Roja": "",
    "Gimnástico": "",
    "Arsenal SAO": "",
    "San Rafael": "",
    "Meluca F.C.": "",
}


all_teams = {**finder_first_division, **finder_ascenso}
