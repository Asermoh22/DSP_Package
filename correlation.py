import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
import numpy as np

filepath1 = None
filepath2 = None

def open_file():
    global filepath1
    filepath1 = filedialog.askopenfilename(title="Select File 1")
    if filepath1:
        if filepath2:
            process_signals(filepath1, filepath2)
        else:
            print("Please select the second file.")

def open_file2():
    global filepath2
    filepath2 = filedialog.askopenfilename(title="Select File 2")
    if filepath2:
        if filepath1:
            process_signals(filepath1, filepath2)
        else:
            print("Please select the first file.")

def cross_correlation(x1, x2):
    N = len(x1)
    cross_corr_result = []

    for n in range(N):
        cross_corr_value = 1/N * sum(x1[j] * x2[(j + n) % N] for j in range(N))
        cross_corr_result.append(cross_corr_value)

    return cross_corr_result


def normalized_cross_correlation(x1, x2):
    N = len(x1)

    if N == 0:
        raise ValueError("Length of signals must be greater than zero.")

    # Calculate the cross-correlation function r12(n)
    cross_corr_result = cross_correlation(x1, x2)

    # Calculate the normalization factor
    norm_factor = (1 / N) * sum(x1[j] ** 2 for j in range(N)) * (1 / N) * sum(
        x2[j] ** 2 for j in range(N))

    # Check for division by zero
    if norm_factor == 0:
        raise ValueError(
            "Normalization factor is zero. Unable to divide by zero.")

    norm_factor = np.sqrt(norm_factor)

    # Normalize the cross-correlation function
    normalized_corr_result = [r12_n / norm_factor for r12_n in
                              cross_corr_result]

    return normalized_corr_result
def process_signals(filepath1, filepath2):
    if not filepath1 or not filepath2:
        print("Please select both files.")
        return

    with open(filepath1, 'r') as file1:
        lines1 = file1.read().splitlines()

    # Extract metadata and data
    metadata1 = [float(line) for line in lines1[:3]]
    data1 = [list(map(float, line.split())) for line in lines1[3:]]

    time1, number1 = zip(*data1)
    signal1 = np.array(number1)

    with open(filepath2, 'r') as file2:
        lines2 = file2.read().splitlines()

    # Extract metadata and data
    metadata2 = [float(line) for line in lines2[:3]]
    data2 = [list(map(float, line.split())) for line in lines2[3:]]

    time2, number2 = zip(*data2)
    signal2 = np.array(number2)

    normalized_correlation_result = normalized_cross_correlation(signal1, signal2)

    plt.subplot(3, 1, 1)
    plt.stem(time1, signal1, basefmt='b-')
    plt.title('Signal 1')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')

    plt.subplot(3, 1, 2)
    plt.stem(time2, signal2, basefmt='r-')
    plt.title('Signal 2')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')

    plt.subplot(3, 1, 3)
    plt.stem(normalized_correlation_result, basefmt='g-')
    plt.title('Normalizing Cross-Correlation')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')

    plt.tight_layout()
    plt.show()

    print("Normalized Cross-Correlation Result:")
    print(normalized_correlation_result)
    print("Number 1 (second column of file 1):")
    print(number1)
    print("Number 2 (second column of file 2):")
    print(number2)

myfram = tk.Tk()
myfram.geometry("400x300")
myfram.title("Choose Files and Compute Normalizing Cross-Correlation")
myfram.configure(bg="palegreen4")

correlation_label = tk.Label(myfram, text="Normalizing Cross-Correlation", width=25)
correlation_label.pack(pady=10)

mybutton = tk.Button(myfram, text="Open File 1", command=open_file, bg="black", fg="white")
mybutton.place(relx=0.3, rely=0.4, anchor=tk.CENTER)

mybutton2 = tk.Button(myfram, text="Open File 2", command=open_file2, bg="white", fg="black")
mybutton2.place(relx=0.7, rely=0.4, anchor=tk.CENTER)

myfram.mainloop()