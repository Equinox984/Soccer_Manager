"""Soccer Manager Engine

The purpose of this project is to create a tool that allows soccer enthusiasts to
have all the information from soccer teams, to soccer leagues from Honduras.
"""

from module import ascenso_league, first_division

############################################################################################
# Create a function that shows the Soccer Manager Menu
# - Submenu 1: If the user selects 1, we will have a Menu with all the Soccer Leagues
# and their teams.
# It will also have a Finder, where we will have information from every team. A mini
# Wikipedia basically.
# - Submenu 2: If the user selects 2, we will show with this function every match
# available with their dates and stadiums.
# - Submenu 3: If the user selects 3, we will have a Trivia Minigame, where you need
# to select the correct option from fun facts of every honduran team.
# Then we will show the results in the display.
############################################################################################


# === MENUS ===
# SOCCER TEAMS: MENU 1
def soccer_teams():
    while True:
        try:
            league_choice = int(
                input("""
--- Soccer Leagues Menu ---

[1] Honduran Leagues & Teams
[2] Finder
[3] Exit

-> """).strip()
            )
            if league_choice == 1:
                honduran_leagues()
            elif league_choice == 2:
                print("\n--- Finder ---")
            elif league_choice == 3:
                print("\nExiting...")
                break
            else:
                print(
                    "\nERROR: Invalid choice. Please select a valid option (1,2,3).\n"
                )
                continue
        except ValueError:
            print("\nERROR: Invalid input. Please enter a number.\n")
            continue


# Subfunction 1 (Belongs to Menu 1): Honduran Leagues
def honduran_leagues():
    while True:
        try:
            choice_leagues = int(
                input("""
--- Honduran Leagues ---
[1] Honduran National Professional Football League (First Division)
[2] Honduran Second Division (Ascenso League)
[3] Exit

-> """)
            )

            if choice_leagues == 1:
                print("\n" + "=" * 50)
                print("  Liga Nacional de Honduras (Primera División)")
                print("=" * 50)
                for league, teams in first_division.items():
                    for i, team in enumerate(teams, 1):
                        print(f"  {i}. {team}")
                print("=" * 50)

            elif choice_leagues == 2:
                print("\n" + "=" * 50)
                print("  Segunda División (Liga de Ascenso)")
                print("=" * 50)
                for group, teams in ascenso_league.items():
                    print(f"\n   {group}")
                    print("  " + "-" * 30)
                    for i, team in enumerate(teams, 1):
                        print(f"    {i}. {team}")
                print("\n" + "=" * 50)
            elif choice_leagues == 3:
                break
            else:
                print(
                    "\nERROR: Invalid choice. Please select a valid option (1,2,3).\n"
                )
        except ValueError:
            print("\nERROR: Invalid input. Please enter a number.\n")


# Subfunction 2 (Belongs to Menu 1): Finder
def finder():
    print("\n--- Finder ---")
    print("Search for a team to get its Wikipedia link.")
    print("(Type 'exit' to go back)\n")
    while True:
        query = input("Write the team name -> ").strip()
        if query.lower() == "exit":
            break
        if not query:
            continue
        
                

# MATCHES WITH DATES & STADIUM NAMES: MENU 2
# TRIVIA MINIGAME: MENU 3


# MAIN MENU: User selects one of the following options.
def main():
    while True:
        try:
            main_choice = int(
                input("""
===== Welcome to the Soccer Manager =====

[1] Soccer Leagues
[2] Matches
[3] Trivia Minigame
[4] Exit

-> """).strip()
            )
        except ValueError:
            print("\nERROR: Invalid input. Please enter a valid option.\n")
            continue

        if main_choice == 1:
            soccer_teams()
        elif main_choice == 2:
            print("\n--- Matches Menu ---")
        elif main_choice == 3:
            print("\n--- Trivia Minigame ---")
        elif main_choice == 4:
            break
        else:
            print("\nERROR: Invalid option. Select 1, 2, 3, or 4!!!\n")
            continue


if __name__ == "__main__":
    main()
