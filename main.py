# main.py
"""
Main entry point for the Project Chimera text adventure game.

Imports necessary modules and starts the main game sequence, typically
by displaying the main menu.
"""

# Import the main menu functionality from the main_menu module
import src.main_menu as mm

def main():
    """Runs the main game sequence."""
    # Display the main menu - this function contains the menu loop
    mm.display_main_menu()

    # This code runs after the menu loop has exited (player chose Quit)
    print("\nGame has exited. Program terminating.")

# Standard Python entry point check
if __name__ == "__main__":
    main()
