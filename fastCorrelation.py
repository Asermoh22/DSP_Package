import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt

plt.ion()

x_values1 = []
y_values1 = []
x_values2 = []
y_values2 = []

def apply_fourier_transform(x_values, y_values, sampling_frequency):
    N = len(x_values)

    if sampling_frequency == 0:
        print("Sampling frequency cannot be zero.")
        return []

    T = 1 / sampling_frequency
    xk = []

    frequencies = [(2 * np.pi * k) / (N * T) for k in range(N)]

    for k in range(N):
        sum_xk = 0
        for n in range(N):
            sum_xk += y_values[n] * np.exp(-2j * np.pi * k * n / N)
         xk.append(sum_xk)

    return xk, frequencies
def calculate_idft(X):
    N = len(X)
    signal = np.zeros(N, dtype=complex)
    for n in range(N):
        signal[n] = 0
        for k in range(N):
            angle = 2 * np.pi * n * k / N
            real_part = np.cos(angle)
            imaginary_part = np.sin(angle)
            signal[n] += (X[k].real * real_part) - (X[k].imag * imaginary_part)

        signal[n] /= N

    return signal

def complex_conjugate(numbers):
    return [complex(num.real, -num.imag) for num in numbers]

def open_file1():
    file_path = filedialog.askopenfilename()

    if file_path:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if len(lines) >= 3:
                array_size = int(lines[2].strip())

                for line in lines[3:]:
                    values = line.strip().split()
                    if len(values) >= 2:
                        x_value = float(values[0])
                        y_value = float(values[1])
                        x_values1.append(x_value)
                        y_values1.append(y_value)
    # xk, frequencies=apply_fourier_transform(x_values1,y_values1,sampling_frequency)
    # cong_xk1=complex_conjugate(xk)
    # return cong_xk1
def open_file2():
    file_path = filedialog.askopenfilename()

    if file_path:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if len(lines) >= 3:
                array_size = int(lines[2].strip())

                for line in lines[3:]:
                    values = line.strip().split()
                    if len(values) >= 2:
                        x_value = float(values[0])
                        y_value = float(values[1])
                        x_values2.append(x_value)
                        y_values2.append(y_value)
    # apply_fourier_transform(x_values2, y_values2, sampling_frequency)




def Fast_correlation():
    dft_array = []
    res=[]
    sampling_frequency = int(sampling_frequency_entry.get())
    xk1, frequencies = apply_fourier_transform(x_values1, y_values1, sampling_frequency)
    xk2, frequencies = apply_fourier_transform(x_values2, y_values2, sampling_frequency)
    cong_xk1 = complex_conjugate(xk1)

    for i in range(len(cong_xk1)):
        dft_array.append(cong_xk1[i] * xk2[i])
    print(xk1,"\n")
    print(cong_xk1,"\n")
    print(xk2,"\n")

    res.append(1/len(dft_array) * calculate_idft(dft_array))
    print(res)


myfram = tk.Tk()
myfram.geometry("400x300")
myfram.title("Choose Files and Convolve")
myfram.configure(bg="palegreen4")

# Label and Entry for sampling frequency
sampling_frequency_label = tk.Label(myfram, text="Enter the sampling frequency (Hz):")
sampling_frequency_label.configure(font=("Arial", 12), bg="palegreen4")
sampling_frequency_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

sampling_frequency_entry = tk.Entry(myfram)
sampling_frequency_entry.configure(font=("Arial", 12))
sampling_frequency_entry.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

# Buttons for uploading signals and performing Fast Correlation
mybutton = tk.Button(myfram, text="Open File 1", command=open_file1, bg="black", fg="white")
mybutton.place(relx=0.3, rely=0.5, anchor=tk.CENTER)

mybutton2 = tk.Button(myfram, text="Open File 2", command=open_file2, bg="white", fg="black")
mybutton2.place(relx=0.7, rely=0.5, anchor=tk.CENTER)

convolution_button = tk.Button(myfram, text="Fast Correlation", command=Fast_correlation, bg="black", fg="white")
convolution_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

# Run the GUI main loop
myfram.mainloop()