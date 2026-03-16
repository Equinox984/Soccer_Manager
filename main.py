"""Soccer Manager Engine"""

import os
import random

from matches_module import first_div_list, second_div_list
from module import (
    all_teams,
    get_ascenso_by_groups,
    get_first_division,
    mini_separator,
    separator,
)
from trivia_module import soccer_trivia


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# --- MENU 1 (Soccer Information) ---
def honduran_leagues():
    clear_screen()
    while True:
        try:
            choice = int(
                input("""
--- Honduran Leagues ---
[1] Honduran National Professional Football League (First Division)
[2] Honduran Second Division (Ascenso League)
[3] Exit

-> """).strip()
            )

            if choice == 1:
                clear_screen()
                teams = get_first_division()
                print(
                    f"\n{separator}\n  Honduran National Professional Football League (First Division)\n{separator}"
                )
                for number, team in enumerate(teams, 1):
                    print(f"  {number}. {team}")
                print(separator)

            elif choice == 2:
                clear_screen()
                groups = get_ascenso_by_groups()
                print(
                    f"\n{separator}\n  Honduran Second Division (Ascenso League)\n{separator}"
                )
                for group_name, teams in groups.items():
                    print(f"\n   {group_name}\n {mini_separator}")
                    for number, team in enumerate(teams, 1):
                        print(f"    {number}. {team}")
                print(f"\n{separator}")

            elif choice == 3:
                clear_screen()
                break
            else:
                clear_screen()
                print(
                    "\nERROR: Invalid choice. Please select a valid option (1,2,3).\n"
                )
        except ValueError:
            clear_screen()
            print("\nERROR: Invalid input. Please enter a number.\n")


def finder():
    clear_screen()
    print("""
--- Finder ---
Search for a team to get its Wikipedia link.
(Type 'exit' to go back)
""")
    while True:
        query = input("Write the team name -> ").strip()
        if query.lower() == "exit":
            clear_screen()
            break
        if not query:
            print("\nERROR: Please enter a valid team name.\n")
            continue

        match = next(
            (name for name in all_teams if name.lower() == query.lower()), None
        )
        if match:
            clear_screen()
            team_data = all_teams[match]
            query = match
            url = team_data["wiki"]
            print(f"\n{separator}")
            print(f"\nTeam: {query}")
            print(f"League: {team_data['league']}")
            print(f"Group: {team_data['group']}")
            if url:
                print(f"Wikipedia: {url}")
            else:
                print("Wikipedia: Not available")
            print(f"\n{separator}\n")
        else:
            clear_screen()
            print(f"\nERROR: '{query}' not found.\n")


def soccer_information():
    clear_screen()
    while True:
        try:
            choice = int(
                input("""
=== Soccer General Info Menu ===

[1] Honduran Leagues & Teams
[2] Finder
[3] Exit

-> """).strip()
            )
            if choice == 1:
                honduran_leagues()
            elif choice == 2:
                finder()
            elif choice == 3:
                clear_screen()
                break
            else:
                print(
                    "\nERROR: Invalid choice. Please select a valid option (1,2,3).\n"
                )
                continue
        except ValueError:
            clear_screen()
            print("\nERROR: Invalid input. Please enter a number.\n")
            continue


# --- MENU 2 (Matches) ---
def display_matches(matches_list, title):
    clear_screen()
    while True:
        print(f"\n{separator}")
        print(f"\nUPCOMING MATCHES - {title}\n \n{separator}\n")

        for number, match in enumerate(matches_list, 1):
            print(mini_separator)
            print(f" {number}. {match['home']} vs {match['away']}")
            print(f"    Stadium: {match['stadium']} | Date: {match['date']}")
            print(mini_separator)

        user_input = input("\nType 'exit' to go back -> ").strip()
        if user_input.lower() == "exit":
            clear_screen()
            break
        else:
            clear_screen()
            print("\nERROR: Invalid input. Please type 'exit'.\n")
            continue


def matches_menu():
    clear_screen()
    while True:
        try:
            choice = int(
                input("""
=== Matches Menu ===

[1] First Division Matches
[2] Second Division Matches
[3] Exit

-> """).strip()
            )
            if choice == 1:
                display_matches(first_div_list, "First Division Upcoming Matches")
            elif choice == 2:
                display_matches(second_div_list, "Second Division Upcoming Matches")
            elif choice == 3:
                clear_screen()
                break
            else:
                print(
                    "\nERROR: Invalid choice. Please select a valid option (1,2,3).\n"
                )
                continue
        except ValueError:
            clear_screen()
            print("\nERROR: Invalid input. Please enter a number.\n")
            continue


# --- MENU 3 (Trivia Minigame) ---


def play_trivia(highest_score):
    clear_screen()
    print("--- Trivia Minigame ---\n")
    sample_size = min(5, len(soccer_trivia))
    questions = random.sample(soccer_trivia, sample_size)
    score = 0

    for question_number, question in enumerate(questions, 1):
        print(f"Q{question_number}: {question['question']}\n")
        for option_number, option in enumerate(question["options"], 1):
            print(f"  [{option_number}] {option}")
        try:
            answer = int(input("\nAnswer: ").strip())
            selected = question["options"][answer - 1]
            if selected == question["answer"]:
                print("Correct!\n")
                score += 1
            else:
                print(f"Incorrect. The answer was: {question['answer']}\n")
        except (ValueError, IndexError):
            print(f"Invalid input. The answer was: {question['answer']}\n")

    if highest_score is None or score > highest_score:
        highest_score = score

    print(f"{separator}")
    print(f"  Final score: {score}/{sample_size}")
    print(f"{separator}\n")
    input("Type Anything to Continue -> ")
    return highest_score


def show_highest_score(highest_score):
    clear_screen()
    if highest_score is None:
        print("\nNo games played yet.\n")
    else:
        print(f"\n{separator}")
        print(f"  Highest Score: {highest_score}/{min(5, len(soccer_trivia))}")
        print(f"{separator}\n")
    input("Type Anything to Continue -> ")
    clear_screen()


def trivia_minigame():
    clear_screen()
    highest_score = None
    while True:
        try:
            choice = int(
                input("""
=== Please Select an Option ===

[1] Start Trivia Minigame
[2] Last Highest Score
[3] Exit

-> """).strip()
            )
            if choice == 1:
                highest_score = play_trivia(highest_score)
            elif choice == 2:
                show_highest_score(highest_score)
            elif choice == 3:
                clear_screen()
                break
            else:
                print(
                    "\nERROR: Invalid choice. Please select a valid option (1,2,3).\n"
                )
                continue
        except ValueError:
            clear_screen()
            print("\nERROR: Invalid input. Please enter a number.\n")
            continue


# --- MAIN MENU ---
def main():
    clear_screen()
    while True:
        try:
            main_choice = int(
                input("""
===== Welcome to the Soccer Manager =====

[1] Soccer Information
[2] Matches
[3] Trivia Minigame
[4] Exit

-> """).strip()
            )
        except ValueError:
            clear_screen()
            print("\nERROR: Invalid input. Please enter a valid option.\n")
            continue

        if main_choice == 1:
            soccer_information()
        elif main_choice == 2:
            matches_menu()
        elif main_choice == 3:
            trivia_minigame()
        elif main_choice == 4:
            clear_screen()
            break
        else:
            clear_screen()
            print("\nERROR: Invalid option. Select 1, 2, 3, or 4!!!\n")
            continue


if __name__ == "__main__":
    main()
