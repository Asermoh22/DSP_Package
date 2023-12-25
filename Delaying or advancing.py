import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
import numpy as np

def open_file():
    filepath1 = filedialog.askopenfilename(title="Select File")
    if filepath1:
        process_signal(filepath1)

def process_signal(filepath1):
    with open(filepath1, 'r') as file1:
        lines1 = file1.read().splitlines()

    data1 = [line.split() for line in lines1[3:]]
    data1 = np.array(data1, dtype=float)

    time = np.arange(0, len(data1))

    number1 = data1[:, 1]

    k = int(entry_k.get())

    delayed_signal = delay_signal(number1, k)

    advanced_signal = advance_signal(number1, k)

    plt.subplot(3, 1, 1)
    plt.plot(time, number1)
    plt.title('Original Signal')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')

    plt.subplot(3, 1, 2)
    plt.stem(time, delayed_signal)
    plt.title(f'Delayed Signal (k={k})')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')

    plt.subplot(3, 1, 3)
    plt.stem(time, advanced_signal)
    plt.title(f'Advanced Signal (k={k})')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')

    plt.tight_layout()
    plt.show()

def delay_signal(signal, k):
    delayed_signal = np.zeros_like(signal)
    delayed_signal[k:] = signal[:-k]
    return delayed_signal

def advance_signal(signal, k):
    advanced_signal = np.zeros_like(signal)
    advanced_signal[:-k] = signal[k:]
    return advanced_signal

myfram = tk.Tk()
myfram.geometry("400x400")
myfram.title("Delay and Advance Signal")
myfram.configure(bg="aquamarine4")

squaring_label = tk.Label(myfram, text="Delay/Advance Signal", width=20)
squaring_label.pack(pady=10)

label_k = tk.Label(myfram, text="Enter k:", width=20)
label_k.pack(pady=5)

entry_k = tk.Entry(myfram, width=10)
entry_k.pack(pady=5)

mybutton = tk.Button(myfram, text="Open File", command=open_file, bg="white", fg="black", width=15)
mybutton.pack(padx=20, pady=20)



myfram.mainloop()
