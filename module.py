"""Module for Soccer Manager Engine"""

separator = "=" * 50
mini_separator = "-" * 30

all_teams = {
    # --- FIRST DIVISION TEAMS ---
    "Real España": {
        "league": "First Division",
        "group": None,
        "wiki": "https://es.wikipedia.org/wiki/Real_Club_Deportivo_España",
    },
    "Motagua": {
        "league": "First Division",
        "group": None,
        "wiki": "https://es.wikipedia.org/wiki/Fútbol_Club_Motagua",
    },
    "Olimpia": {
        "league": "First Division",
        "group": None,
        "wiki": "https://es.wikipedia.org/wiki/Club_Olimpia_Deportivo",
    },
    "Victoria": {
        "league": "First Division",
        "group": None,
        "wiki": "https://es.wikipedia.org/wiki/Club_Deportivo_Victoria",
    },
    "Olancho F.C.": {
        "league": "First Division",
        "group": None,
        "wiki": "https://es.wikipedia.org/wiki/Olancho_Fútbol_Club",
    },
    "Maratón": {
        "league": "First Division",
        "group": None,
        "wiki": "https://es.wikipedia.org/wiki/Club_Deportivo_Marathón",
    },
    "Platense": {
        "league": "First Division",
        "group": None,
        "wiki": "https://en.wikipedia.org/wiki/Platense_F.C.",
    },
    "Club Deportivo Choloma": {
        "league": "First Division",
        "group": None,
        "wiki": "https://es.wikipedia.org/wiki/Club_Deportivo_Choloma",
    },
    "Juticalpa": {
        "league": "First Division",
        "group": None,
        "wiki": "https://es.wikipedia.org/wiki/Juticalpa_Fútbol_Club",
    },
    "Lobos UPNFM": {
        "league": "First Division",
        "group": None,
        "wiki": "https://en.wikipedia.org/wiki/Lobos_UPNFM",
    },
    "Club Deportivo Génesis Policía Nacional": {
        "league": "First Division",
        "group": None,
        "wiki": "https://es.wikipedia.org/wiki/Club_Deportivo_Génesis",
    },
    # --- ASCENSO LEAGUE (SECOND DIVISION TEAMS) ---
    # --- Group A ---
    "Boca Juniors": {"league": "Ascenso", "group": "Group A", "wiki": ""},
    "Vida": {
        "league": "Ascenso",
        "group": "Group A",
        "wiki": "https://es.wikipedia.org/wiki/Club_Deportivo_y_Social_Vida",
    },
    "Real Sociedad": {
        "league": "Ascenso",
        "group": "Group A",
        "wiki": "https://es.wikipedia.org/wiki/Club_Deportivo_Real_Sociedad",
    },
    "Roma F.C.": {"league": "Ascenso", "group": "Group A", "wiki": ""},
    # --- Group B ---
    "Honduras Progreso": {
        "league": "Ascenso",
        "group": "Group B",
        "wiki": "https://es.wikipedia.org/wiki/Club_Deportivo_Honduras_Progreso",
    },
    "Atlético Junior": {"league": "Ascenso", "group": "Group B", "wiki": ""},
    "Tela F.C.": {"league": "Ascenso", "group": "Group B", "wiki": ""},
    "F.C. Santa Rosa": {"league": "Ascenso", "group": "Group B", "wiki": ""},
    "Oro Verde F.C.": {"league": "Ascenso", "group": "Group B", "wiki": ""},
    "Estrella F.C.": {"league": "Ascenso", "group": "Group B", "wiki": ""},
    # --- Group C ---
    "Parrillas One": {
        "league": "Ascenso",
        "group": "Group C",
        "wiki": "https://es.wikipedia.org/wiki/Club_Deportivo_Parrillas_One",
    },
    "CD Choloma": {"league": "Ascenso", "group": "Group C", "wiki": ""},
    "Leones HT6": {"league": "Ascenso", "group": "Group C", "wiki": ""},
    "C.D. Brasilia": {"league": "Ascenso", "group": "Group C", "wiki": ""},
    "Pumas F.C.": {"league": "Ascenso", "group": "Group C", "wiki": ""},
    "Lone F.C.": {"league": "Ascenso", "group": "Group C", "wiki": ""},
    # --- Group D ---
    "San Juan Huracán": {"league": "Ascenso", "group": "Group D", "wiki": ""},
    "Olimpia Occidental": {"league": "Ascenso", "group": "Group D", "wiki": ""},
    "Santo Domingo Savio": {"league": "Ascenso", "group": "Group D", "wiki": ""},
    "Cuervos": {"league": "Ascenso", "group": "Group D", "wiki": ""},
    "San Juan Gualjoco": {"league": "Ascenso", "group": "Group D", "wiki": ""},
    "Real Juventud": {"league": "Ascenso", "group": "Group D", "wiki": ""},
    # --- Group E ---
    "Atlético Independiente": {"league": "Ascenso", "group": "Group E", "wiki": ""},
    "Real Tegus": {"league": "Ascenso", "group": "Group E", "wiki": ""},
    "AFFI Academia": {"league": "Ascenso", "group": "Group E", "wiki": ""},
    "CD Pirata": {"league": "Ascenso", "group": "Group E", "wiki": ""},
    "FAS": {"league": "Ascenso", "group": "Group E", "wiki": ""},
    "Inter": {"league": "Ascenso", "group": "Group E", "wiki": ""},
    "Policía Nacional": {"league": "Ascenso", "group": "Group E", "wiki": ""},
    # --- Group F ---
    "Hondupino": {"league": "Ascenso", "group": "Group F", "wiki": ""},
    "Estrella Roja": {"league": "Ascenso", "group": "Group F", "wiki": ""},
    "Gimnástico": {"league": "Ascenso", "group": "Group F", "wiki": ""},
    "Arsenal SAO": {"league": "Ascenso", "group": "Group F", "wiki": ""},
    "San Rafael": {"league": "Ascenso", "group": "Group F", "wiki": ""},
    "Meluca F.C.": {"league": "Ascenso", "group": "Group F", "wiki": ""},
}


# Functions to get teams
def get_first_division():
    """Generates a list of first division teams."""
    return [
        name for name, info in all_teams.items() if info["league"] == "First Division"
    ]


def get_ascenso_by_groups():
    """Generates a dictionary grouped by group names for Ascenso league"""
    groups = {}
    for name, info in all_teams.items():
        if info["league"] == "Ascenso":
            group_name = info["group"]
            if group_name not in groups:
                groups[group_name] = []
            groups[group_name].append(name)
    return groups
