import tkinter as tk
import os
from tkinter import filedialog
import numpy as np

def open_folder(title):
    folder_path = filedialog.askdirectory(title=f"Select {title} Folder")
    return folder_path

def open_test_file():
    global test_file_content
    test_file_content = process_file(filedialog.askopenfilename(title="Select Test Signal File"))
    print("Test File Content:", test_file_content)

def open_class1_folder():
    global class1_content
    class1_content = process_folder(open_folder("Class 1"))
    print("Class 1 Folder Content:", class1_content)

def open_class2_folder():
    global class2_content
    class2_content = process_folder(open_folder("Class 2"))
    print("Class 2 Folder Content:", class2_content)

def process_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        return np.array(content.split(), dtype=float)

def process_folder(folder_path):
    files_contents = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            content = process_file(file_path)
            files_contents.append(content)

    aggregated_samples = aggregate_samples(files_contents)
    return aggregated_samples

def aggregate_samples(files_contents):
    max_samples = max(len(content) for content in files_contents)
    aggregated_samples = np.zeros(max_samples)

    for content in files_contents:
        aggregated_samples[:len(content)] += content

    aggregated_samples /= len(files_contents)
    return aggregated_samples

def calculate_correlation(test_file_content, folder_content):
    test_mean = np.mean(test_file_content)
    folder_mean = np.mean(folder_content)

    v1 = np.sum((test_file_content - test_mean) * (folder_content - folder_mean))
    v2 = np.sqrt(np.sum((test_file_content - test_mean)**2) * np.sum((folder_content - folder_mean)**2))

    correlation = v1 / v2
    return correlation



def decide_correlation():
    correlation_class1 = calculate_correlation(test_file_content, class1_content)
    correlation_class2 = calculate_correlation(test_file_content, class2_content)

    print(f"Correlation with Class 1: {correlation_class1}")
    print(f"Correlation with Class 2: {correlation_class2}")

    if correlation_class1 > correlation_class2:
        result_label.config(text="The test file is highly correlated with Class 1.")
    else:
        result_label.config(text="The test file is highly correlated with Class 2.")

myfram = tk.Tk()
myfram.geometry("500x400")
myfram.title("Template Matching for Signal Classification")
myfram.configure(bg="palegreen4")

test_button = tk.Button(myfram, text="Open Test File", command=open_test_file, bg="black", fg="white")
test_button.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

class1_button = tk.Button(myfram, text="Open Class 1 Folder", command=open_class1_folder, bg="white", fg="black")
class1_button.place(relx=0.3, rely=0.4, anchor=tk.CENTER)

class2_button = tk.Button(myfram, text="Open Class 2 Folder", command=open_class2_folder, bg="gray", fg="black")
class2_button.place(relx=0.7, rely=0.4, anchor=tk.CENTER)

result_label = tk.Label(myfram, text="", bg="beige", font=("Helvetica", 12))
result_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

calculate_button = tk.Button(myfram, text="Calculate Correlation", command=decide_correlation, bg="green", fg="white")
calculate_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

myfram.mainloop()