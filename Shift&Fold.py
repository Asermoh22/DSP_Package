import tkinter as tk
from tkinter import ttk, filedialog
import matplotlib.pyplot as plt

def delay_signal(x, signal, k):
    delayed_x = [value + k for value in x]
    delayed_signal = signal[:]
    return delayed_x, delayed_signal

def advance_signal(x, signal, k):
    advanced_x = [value - k for value in x]
    advanced_signal = signal[:]
    return advanced_x, advanced_signal

def fold_signal(x, y):
    folded_x = [-value for value in reversed(x)]
    folded_y = list(reversed(y))
    return folded_x, folded_y

def open_file():
    file_path = filedialog.askopenfilename(title="Select File")

    if file_path:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if len(lines) >= 3:
                array_size = int(lines[2].strip())
                x_values = []
                y_values = []

                for line in lines[3:]:
                    values = line.strip().split()
                    if len(values) >= 2:
                        x_value = float(values[0])
                        y_value = float(values[1])
                        x_values.append(x_value)
                        y_values.append(y_value)

                plt.figure(figsize=(10, 5 + len(x_values) * 0.1))
                plt.clf()

                plt.subplot(2, 1, 1)
                plt.scatter(x_values, y_values, label='Original Signal')
                plt.title('Original Signal')

                # Apply the selected operation
                if combo_box.get() == "Fold with Advance":
                    shift_val = int(shiftedValEntry.get())
                    folded_x, folded_y = fold_signal(x_values, y_values)
                    shifted_x, shifted_signal = delay_signal(folded_x, folded_y, shift_val)
                    print(f"Result: {shifted_signal}")
                elif combo_box.get() == "Fold with Delay":
                    shift_val = int(shiftedValEntry.get())
                    folded_x, folded_y = fold_signal(x_values, y_values)
                    shifted_x, shifted_signal = advance_signal(folded_x, folded_y, shift_val)
                    print(f"Result: {shifted_signal}")

                # Plot shifted signal
                plt.subplot(2, 1, 2)
                plt.scatter(shifted_x, shifted_signal)
                plt.title('Shifted Signal')

                plt.tight_layout()
                plt.show()

window = tk.Tk()
window.geometry("500x400")
window.configure(bg="aquamarine4")
window.title("Shifting Signal")

shiftedValLab = tk.Label(window, text="Shifted Value", bg="aquamarine4", fg="black")
shiftedValLab.place(relx=0.34, rely=0.37)

shiftedValEntry = tk.Entry(window)
shiftedValEntry.configure(font=("Arial", 12))
shiftedValEntry.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

choose_operation_label = tk.Label(window, text="Operation on Signals", bg="aquamarine4", fg="black")
choose_operation_label.place(relx=0.34, rely=0.2)

signals_operations = ["Fold with Advance", "Fold with Delay"]
style = ttk.Style()
style.configure("TCombobox", background="black", foreground="darkred")
combo_box = ttk.Combobox(window, values=signals_operations, style="TCombobox")
combo_box.place(relx=0.34, rely=0.3)

browse_and_process_button = tk.Button(window, text="Apply Operation", command=open_file)
browse_and_process_button.configure(font=("Arial", 12), bg="black", fg="white")
browse_and_process_button.place(relx=0.47, rely=0.55, anchor=tk.CENTER)

window.mainloop()
