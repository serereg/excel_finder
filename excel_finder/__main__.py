import PySimpleGUI as sg                        # Part 0 - The import
from pathlib import Path

from .convert import convert


if __name__ == "__main__":
    # Define the window's contents
    layout = [  [sg.Text("What's your name?")],     # Part 1 - The Layout
                [sg.Input()],
                [sg.Button('Ok')] ]

    # Create the window
    window = sg.Window('Window Title', layout)      # Part 2 - Window Defintion

    # Display and interact with the Window
    event, values = window.read()                   # Part 3 - Event loop or Window.read call

    # Do something with the information gathered
    path = Path(values[0])
    convert(path, path / "output", 9)  # 9 - номер колонки
    print('Working with path', path, " is finished")

    # Finish up by removing from the screen
    window.close()                                  # Part 4 - Close the Window
