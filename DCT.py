
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
from tkinter import filedialog

def open_file():
    global filepath
    filepath = filedialog.askopenfilename(title="Select File")
    if filepath:
        process_dct(filepath)

def dct1d(x):
    N = len(x)
    y = np.zeros(N)

    for k in range(N):
        sum_val = 0.0
        for n in range(N):
            sum_val += np.sqrt(2/N) * x[n] * np.cos(np.pi / (4 * N) * (2 * n - 1) * (2 * k - 1))
        y[k] = sum_val

    return y

def process_dct(filepath):
    with open(filepath, 'r') as file:
        lines = file.read().splitlines()

    data = [line.split() for line in lines[3:]]
    data = np.array(data, dtype=float)

    time = np.arange(0, len(data))

    signal = data[:, 1]

    # Computing DCT for the given input
    dct_result = dct1d(signal)

    # Displaying DCT coefficients
    plt.subplot(2, 1, 1)
    plt.plot(time, signal, label='Original Signal')
    plt.title('Original Signal')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.stem(dct_result, label='DCT Coefficients')
    plt.title('DCT Coefficients')
    plt.xlabel('DCT Coefficient Index')
    plt.ylabel('Magnitude')
    plt.legend()

    plt.tight_layout()
    plt.show()

    # Print the DCT coefficients
    print("DCT Coefficients:")
    print(dct_result)

    # Save the DCT coefficients to a file
    save_dct_result(dct_result)

def save_dct_result(dct_result):
    save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if save_path:
        with open(save_path, 'w') as file:
            for coeff in dct_result:
                file.write(f'{coeff:.8f}\n')
        print(f"DCT coefficients saved to {save_path}")

myfram = tk.Tk()
myfram.geometry("300x300")
myfram.title("Choose File")
myfram.configure(bg="palegreen4")

mybutton = tk.Button(myfram, text="Open File", command=open_file, bg="black", fg="white")
mybutton.pack(padx=40, pady=50)

myfram.mainloop()
