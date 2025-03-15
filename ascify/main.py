import pyfiglet
from pyfiglet import FigletFont
from prettytable import PrettyTable
import argparse
import sys
import tkinter as tk  # Menggunakan tkinter untuk clipboard

# Application version
APP_VERSION = "1.1.0"


def copy_to_clipboard_tkinter(text):
    """
    Copy text to clipboard using tkinter.
    """
    try:
        root = tk.Tk()
        root.withdraw()  # Sembunyikan jendela utama
        root.clipboard_clear()
        root.clipboard_append(text)
        root.update()  # Pastikan teks disalin
        root.destroy()  # Tutup jendela
        print("The result has been copied to clipboard!")
    except Exception as e:
        print(f"An error occurred while copying to clipboard: {e}")


def main():
    try:
        banner_ascii = r"""   
    ___              _ ____     
   /   |  __________(_) __/_  __
  / /| | / ___/ ___/ / /_/ / / /
 / ___ |(__  ) /__/ / __/ /_/ / 
/_/  |_/____/\___/_/_/  \__, /  
                       /____/   

Advance ASCII Banner Generator
---------------------------------------
Version: v1.1.0  |  Developed by: fkr00t          
        """
        print(banner_ascii)
        text = input("Enter your text: ")

        # Get all fonts
        fonts = FigletFont.getFonts()
        font_count = len(fonts)
        print(f"\nTotal fonts available: {font_count}")  # Print total number of fonts

        # Set the number of columns in the table (e.g., 8)
        columns = 8
        rows = (font_count + columns - 1) // columns  # Calculate required rows

        # Arrange fonts in vertical order
        arranged_fonts = [[""] * columns for _ in range(rows)]
        for idx, font in enumerate(fonts):
            row = idx % rows
            col = idx // rows
            arranged_fonts[row][col] = f"{idx + 1}. {font}"

        # Create the table
        table = PrettyTable()
        table.header = False  # Remove table header
        table.align = "l"  # Left align text
        column_width = 25  # Fixed column width

        # Add all rows to the table
        for row in arranged_fonts:
            table.add_row([entry.ljust(column_width) for entry in row])

        # Display the table
        print("\nAvailable Fonts (select by number or name):")
        print(table)

        # Loop for font selection and preview
        while True:
            font_choice = input("\nSelect a font (enter number or name): ").strip()
            selected_font = None

            # Check if input is a number
            if font_choice.isdigit():
                font_number = int(font_choice)
                if 1 <= font_number <= font_count:
                    selected_font = fonts[font_number - 1]  # Use the selected font number
                else:
                    print("Invalid number! Please enter a valid font number.")
                    continue
            else:
                # Check if input is a valid font name
                if font_choice in fonts:
                    selected_font = font_choice
                else:
                    print("Invalid font name! Please enter a valid font name.")
                    continue

            # Generate preview with the selected font
            banner = pyfiglet.figlet_format(text, font=selected_font)
            print("\nPreview of the selected font:")
            print(banner)

            # Ask if the user wants to continue with this font or choose another
            while True:
                continue_choice = input("Do you want to continue with this font? (Y/N): ").strip().lower()
                if continue_choice in ["y", "n"]:
                    break
                else:
                    print("Invalid input! Please enter 'Y' or 'N'.")

            if continue_choice == "y":
                break  # Exit the font selection loop and proceed to saving
            else:
                continue  # Go back to font selection

        # Ask if the user wants to save the result to a file
        while True:
            save_choice = input("Do you want to save the result to a file? (Y/N): ").strip().lower()
            if save_choice in ["y", "n"]:  # Accept only 'y' or 'n'
                break
            else:
                print("Invalid input! Please enter 'Y' or 'N'.")

        if save_choice == "y":
            file_name = input("Enter the file name (e.g., output.txt, press Enter for default): ").strip()
            if not file_name:  # If the user presses Enter without input
                file_name = "output.txt"  # Default file name
            try:
                with open(file_name, "w") as file:
                    file.write(banner)  # Save only the plain text banner
                print(f"The result has been saved to: {file_name}")
            except Exception as e:
                print(f"An error occurred while saving the file: {e}")

        # Ask if the user wants to copy the result to clipboard
        while True:
            copy_choice = input("Do you want to copy the result to clipboard? (Y/N): ").strip().lower()
            if copy_choice in ["y", "n"]:  # Accept only 'y' or 'n'
                break
            else:
                print("Invalid input! Please enter 'Y' or 'N'.")

        if copy_choice == "y":
            copy_to_clipboard_tkinter(banner)  # Gunakan tkinter untuk menyalin ke clipboard
        else:
            print("The result was not copied to clipboard.")

    except KeyboardInterrupt:
        print("\n\nBye!!")  # Message when Ctrl+C is pressed
        sys.exit(0)  # Exit the program successfully


if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Advanced ASCII Banner Maker")
    parser.add_argument("-v", "--version", action="store_true", help="Show program's version and exit")

    args = parser.parse_args()

    # Handle version argument
    if args.version:
        print(f"Advanced ASCII Banner Maker {APP_VERSION}")
        sys.exit(0)

    # Run the main program only if no arguments are provided
    main()