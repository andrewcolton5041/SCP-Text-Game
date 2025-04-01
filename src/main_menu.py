# src/main_menu.py
"""
Handles the display and interaction for the game's main menu.

Uses string constants defined in src.constants for display text.
Provides options for starting, loading, options, or quitting the game.
"""

import os  # For screen clearing functionality

# Import constants from the constants module within the same package
from constants import MainMenuStrings, EXIT_MESSAGE


def clear_screen():
    """Clears the terminal screen based on the operating system."""
    os.system('cls' if os.name == 'nt' else 'clear')


def display_main_menu():
    """
    Displays the game title, waits for user confirmation, then shows the
    main menu options. Loops until valid input is received, then acts on
    the input or quits the application.
    """
    clear_screen()
    print(MainMenuStrings.TITLE)
    print(MainMenuStrings.ENTER_TO_CONTINUE)
    input()  # Wait for user to press Enter

    # Main menu loop
    while True:
        clear_screen()
        # Display menu options
        print(MainMenuStrings.MAIN_MENU_TITLE)
        print(MainMenuStrings.NEW_GAME)
        print(MainMenuStrings.LOAD_GAME)
        print(MainMenuStrings.OPTIONS)
        print(MainMenuStrings.QUIT)
        print()  # Add a blank line for spacing

        # Input validation loop
        while True:
            selection = input(MainMenuStrings.INPUT_REQUEST)
            selection_lower = selection.lower()  # Convert to lowercase once

            # Check if the input is one of the allowed responses
            if selection_lower not in MainMenuStrings.PROPER_INPUT_RESPONSES:
                print(MainMenuStrings.INVALID_SELECTION)
                input("Press Enter to try again...") # Pause for user feedback
                # Re-draw the menu after invalid input message
                clear_screen()
                print(MainMenuStrings.MAIN_MENU_TITLE)
                print(MainMenuStrings.NEW_GAME)
                print(MainMenuStrings.LOAD_GAME)
                print(MainMenuStrings.OPTIONS)
                print(MainMenuStrings.QUIT)
                print()
            else:
                break  # Exit input validation loop when input is valid

        # Handle the valid selection
        if selection_lower == 'q':
            clear_screen()
            print(EXIT_MESSAGE)  # Use the imported constant
            break  # Exit the main menu loop

        elif selection_lower == 'n':
            clear_screen()
            print("\nStarting New Game... (Not implemented yet)")
            # TODO: Add call to the function that starts a new game
            input("Press Enter to return to menu...")  # Pause for user

        elif selection_lower == 'l':
            clear_screen()
            print("\nLoading Game... (Not implemented yet)")
            # TODO: Add call to the function that loads a saved game
            input("Press Enter to return to menu...")

        elif selection_lower == 'o':
            clear_screen()
            print("\nOpening Options... (Not implemented yet)")
            # TODO: Add call to the function that shows the options screen
            input("Press Enter to return to menu...")


# This block allows testing this module directly if needed
# Note: Running this directly might have issues with the relative import '.'
# unless run as a module (e.g., python -m src.main_menu)
if __name__ == "__main__":
    # Simple mock for testing if constants aren't easily available
    class MockMainMenuStrings:
        TITLE = "== MOCK TITLE =="
        ENTER_TO_CONTINUE = "Press Enter..."
        MAIN_MENU_TITLE = "-- Mock Menu --"
        NEW_GAME = "[N] New"
        LOAD_GAME = "[L] Load"
        OPTIONS = "[O] Options"
        QUIT = "[Q] Quit"
        INPUT_REQUEST = "> "
        PROPER_INPUT_RESPONSES = ['n', 'l', 'o', 'q']
        INVALID_SELECTION = "Invalid."

    EXIT_MESSAGE = "Exiting Mock."

    # Override imported constants with mocks for isolated testing
    MainMenuStrings = MockMainMenuStrings
    # EXIT_MESSAGE is already defined locally here

    print("Testing main_menu.py directly...")
    display_main_menu()
    print("Main menu test complete.")
