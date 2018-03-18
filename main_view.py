import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


# create the GUI to be displayed
def create_gui():
    main = tk.Tk()
    main.title("Validation Checker")
    main.geometry("300x300+300+300")

    title_label = tk.Label(main, text='Validation Checker', fg='blue', font=('Times', 20, 'bold'))
    protocol_button = tk.Button(main, text="Select Protocol", width=20, bg='cyan', font=('Times', 12, 'bold'))
    test_button = tk.Button(main, text="Select Test", width=20, bg='cyan', font=('Times', 12, 'bold'))
    protocol_label = tk.Label(main, text="Protocol: ")
    test_label = tk.Label(main, text="Test: ")
    parameter_match_label = tk.Label(main, text="Parameters: ")
    negative_match_label = tk.Label(main, text="Negative Count: ")
    positive_match_label = tk.Label(main, text="Positive Count: ")
    gross_match_label = tk.Label(main, text="Gross Count: ")
    acceptance_criteria_label = tk.Label(main, text="Acceptance Criteria: ")

    title_label.pack()
    protocol_button.pack()
    test_button.pack()
    protocol_label.pack()
    test_label.pack()
    parameter_match_label.pack()
    negative_match_label.pack()
    positive_match_label.pack()
    gross_match_label.pack()
    acceptance_criteria_label.pack()

    main.mainloop()

create_gui()

