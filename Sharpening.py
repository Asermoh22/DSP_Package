import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
from tkinter import filedialog

def open_file():
    filepath1 = filedialog.askopenfilename(title="Select File")
    if filepath1:
        process_signal(filepath1)

def first_derivative(signal):
    return [signal[i] - signal[i-1] for i in range(1, len(signal)-1)]

def second_derivative(signal):
    return [signal[i+1] - 2*signal[i] + signal[i-1] for i in range(1, len(signal)-1)]

def process_signal(filepath1):
    with open(filepath1, 'r') as file1:
        lines1 = file1.read().splitlines()


    data1 = []
    for line in lines1[3:]:
        try:
            data1.append(float(line))
        except ValueError:
            pass

    data1 = np.array(data1)
    time = np.arange(0, len(data1) - 2)

    choice = var.get()
    if choice == 1:
        deriv = first_derivative(data1)
        deriv_label = 'First Derivative'
    else:
        deriv = second_derivative(data1)
        deriv_label = 'Second Derivative'

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))

    ax1.plot(time, data1[:-2], label='Original Signal')
    ax1.set_title('Original Signal')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Amplitude')
    ax1.legend()

    ax2.plot(time, deriv, label=deriv_label, color='orange')
    ax2.set_title(deriv_label)
    ax2.set_xlabel('Time')
    ax2.set_ylabel('Amplitude')
    ax2.legend()

    plt.tight_layout()
    plt.show()

    print(f'{deriv_label}:\n{deriv}')

myfram = tk.Tk()
myfram.geometry("400x300")
myfram.title("Sharpening Signal")
myfram.configure(bg="aquamarine4")

sharpening_label = tk.Label(myfram, text="Sharpening", width=20)
sharpening_label.pack(pady=10)

mybutton = tk.Button(myfram, text="Open File", command=open_file, bg="white",fg="black", width=15)
mybutton.pack(padx=20, pady=10)

var = tk.IntVar()
first_deriv_button = tk.Radiobutton(myfram, text="First Derivative", variable=var, value=1, bg="aquamarine4" )
second_deriv_button = tk.Radiobutton(myfram, text="Second Derivative", variable=var, value=2, bg="aquamarine4")
second_deriv_button.place(relx=0.7,anchor=tk.CENTER)
first_deriv_button.pack()
second_deriv_button.pack()

myfram.mainloop()
