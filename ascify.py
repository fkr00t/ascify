import pyfiglet
from pyfiglet import FigletFont
from prettytable import PrettyTable
import sys


def main():
    try:
        banner_ascii = r"""
         _______  _______  _______ _________ _______          
        (  ___  )(  ____ \(  ____ \\__   __/(  ____ \|\     /|
        | (   ) || (    \/| (    \/   ) (   | (    \/( \   / )
        | (___) || (_____ | |         | |   | (__     \ (_) / 
        |  ___  |(_____  )| |         | |   |  __)     \   /  
        | (   ) |      ) || |         | |   | (         ) (   
        | )   ( |/\____) || (____/\___) (___| )         | |   
        |/     \|\_______)(_______/\_______/|/          \_/   

         Advanced ASCII Banner Maker           
              Author: fkr00t                     
              GitHub: github.com/fkr00t              
              Version: 1.0.0  
        """
        print(banner_ascii)
        text = input("Enter your text: ")

        # Get all fonts
        fonts = FigletFont.getFonts()
        font_count = len(fonts)

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
        print("\nAvailable Fonts (select by number):")
        print(table)

        # Ask the user to select a font by number
        while True:
            font_choice = input("\nSelect a font (enter number): ")
            if font_choice.isdigit() and 1 <= int(font_choice) <= font_count:
                font = fonts[int(font_choice) - 1]  # Use the selected font number
                break
            else:
                print("Invalid input! Please enter a valid font number.")

        # Generate the ASCII banner
        banner = pyfiglet.figlet_format(text, font=font)
        print("\nGenerated ASCII Banner:")
        print(banner)

        # Ask if the user wants to save the result to a file
        save_choice = input("Do you want to save the result to a file? (Y/N): ").strip().lower()
        if save_choice in ["yes", "y", "YES", "Y"]:
            file_name = input("Enter the file name (e.g., output.txt): ").strip()
            try:
                with open(file_name, "w") as file:
                    file.write(banner)
                print(f"The result has been saved to: {file_name}")
            except Exception as e:
                print(f"An error occurred while saving the file: {e}")
        else:
            print("The result was not saved.")

    except KeyboardInterrupt:
        print("\n\nBye!!")  # Message when Ctrl+C is pressed
        sys.exit(0)  # Exit the program successfully


if __name__ == "__main__":
    main()
