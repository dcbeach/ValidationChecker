import tkinter as tk
from tkinter import filedialog


# Asks the user to chose a file
def determine_folder_path():
    root = tk.Tk()
    root.withdraw()
    root.fileName = filedialog.askopenfilename()

    return root.fileName


def set_protocol():
    global protocol
    protocol = determine_folder_path()

    file_path_list = protocol.split('/')
    protocol_name = file_path_list[len(file_path_list)-1]

    protocol_label.config(text="Protocol: " + protocol_name)


def set_test():
    global test
    test = determine_folder_path()

    file_path_list = test.split('/')
    test_name = file_path_list[len(file_path_list) - 1]

    test_label.config(text="Test: " + test_name)


# create the GUI to be displayed
class CreateGUI():
    main = tk.Tk()
    main.title("Validation Checker")
    main.geometry("300x300+300+300")

    global protocol_label
    global test_label

    title_label = tk.Label(main, text='Validation Checker', fg='blue', font=('Times', 20, 'bold'))
    protocol_button = tk.Button(main, text="Select Protocol", command=set_protocol, width=20, bg='cyan', font=('Times', 12, 'bold'))
    test_button = tk.Button(main, text="Select Test", command=set_test, width=20, bg='cyan', font=('Times', 12, 'bold'))
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


CreateGUI()

