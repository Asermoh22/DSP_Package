
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

def calculate_dft(signal):
    N = len(signal)
    X = np.zeros(N, dtype=complex)
    for k in range(N):
        X[k] = 0
        for n in range(N):
            X[k] += signal[n] * np.exp(-2j * np.pi * k * n / N)
    return X

def calculate_magnitude(X_k):
    magnitude = np.sqrt(X_k.real ** 2 + X_k.imag ** 2)
    return magnitude

def calculate_phase(X_k):
    phase = np.angle(X_k)  # Use np.angle to get the phase in radians
    return phase

def remove_dc_component(signal):
    mean_value = np.mean(signal)
    dc_removed_signal = signal - mean_value
    return dc_removed_signal

def plot_frequency_domain(signal, sampling_frequency):
    N = len(signal)
    frequencies = np.arange(N) * sampling_frequency / N
    X = calculate_dft(signal)

    amplitudes = [calculate_magnitude(X_k) for X_k in X]
    phases = [calculate_phase(X_k) for X_k in X]

    for k, X_k in enumerate(X):
        magnitude = calculate_magnitude(X_k)
        phase = calculate_phase(X_k)



    plt.figure(figsize=(12, 6))
    plt.subplot(2, 1, 1)
    plt.stem(frequencies, amplitudes)
    plt.title('Frequency vs. Amplitude')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')

    plt.subplot(2, 1, 2)
    plt.stem(frequencies, phases)
    plt.title('Frequency vs. Phase (Radians)')  # Update the title
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Phase (Radians)')  # Update the label

    plt.tight_layout()
    plt.show()

def browse_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)

def process_dft():
    file_path = file_entry.get()
    try:
        sampling_frequency = float(sampling_entry.get())

        with open(file_path, 'r') as file:
            lines = file.readlines()
            signal = [float(line.strip().split()[1]) for line in lines[3:] if len(line.strip().split()) == 2]

        if remove_dc_var.get():
            dc_removed_signal = remove_dc_component(signal)
            print("Signal after removing DC component:", dc_removed_signal)
            plot_frequency_domain(dc_removed_signal, sampling_frequency)
        else:
            plot_frequency_domain(signal, sampling_frequency)
    except Exception as e:
        print(f"Error: {e}")

window = tk.Tk()
window.title("Signal Analysis")
window.geometry("400x650")

file_label = tk.Label(window, text="Select a file:")
file_label.pack(pady=10)

file_entry = tk.Entry(window, width=30)
file_entry.pack()

browse_button = tk.Button(window, text="Browse", command=browse_file)
browse_button.pack()

sampling_label = tk.Label(window, text="Enter Sampling Frequency (Hz):")
sampling_label.pack(pady=10)

sampling_entry = tk.Entry(window, width=10)
sampling_entry.pack()

remove_dc_var = tk.IntVar()
remove_dc_button = tk.Checkbutton(window, text="Remove DC component", variable=remove_dc_var)
remove_dc_button.pack(pady=10)

dft_button = tk.Button(window, text="Process DFT", command=process_dft)
dft_button.pack(pady=10)

window.mainloop()


