import tkinter as tk
import importlib.util

def open_and_execute_file(file_path):
    spec = importlib.util.spec_from_file_location("module_name", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

def open_file_and_execute_code(file_path):
    open_and_execute_file(file_path)

root = tk.Tk()
root.geometry("500x500")
root.configure(bg="khaki3")
root.title("DSP Projects")
label_dsp_tasks = tk.Label(root, text="DSP Tasks", font=("", 12), bg="white")
label_dsp_tasks.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
# For the DFT button
def open_DFTIDFT_file():
    open_file_and_execute_code("DFT&IDFT.py")

button1 = tk.Button(root, text="DFT&IDFT", command=open_DFTIDFT_file)
button1.configure(font=("", 9), bg="black", fg="white",width=17)
button1.place(relx=0.3, rely=0.2, anchor=tk.CENTER)

# For the IDFT button
def open_REMOVEDC_file():
    open_file_and_execute_code("REMOVEDC.py")

button2 = tk.Button(root, text="Remove DC component", command=open_REMOVEDC_file)
button2.configure(font=("", 9), bg="black", fg="white")
button2.place(relx=0.7, rely=0.2, anchor=tk.CENTER)

def open_DCT_file():
   open_file_and_execute_code("DCT.py")

button3 = tk.Button(root, text="DCT", command=open_DCT_file)
button3.configure(font=("", 9), bg="black", fg="white",width=17)
button3.place(relx=0.3, rely=0.3, anchor=tk.CENTER)

def open_Sharpening_file():
    open_file_and_execute_code("Sharpening.py")

button1 = tk.Button(root, text="Sharpening", command=open_Sharpening_file)
button1.configure(font=("", 9), bg="black", fg="white",width=17)
button1.place(relx=0.7, rely=0.3, anchor=tk.CENTER)

def open_ShiftFold_file():
    open_file_and_execute_code("Shift&Fold.py")

button1 = tk.Button(root, text="Shift&Fold", command=open_ShiftFold_file)
button1.configure(font=("", 9), bg="black", fg="white",width=17)
button1.place(relx=0.3, rely=0.4, anchor=tk.CENTER)

def open_Smooth_file():
    open_file_and_execute_code("Smooth.py")

button1 = tk.Button(root, text="Smooth", command=open_Smooth_file)
button1.configure(font=("", 9), bg="black", fg="white",width=17)
button1.place(relx=0.7, rely=0.4, anchor=tk.CENTER)

def open_DCComponent_file():
    open_file_and_execute_code("DC Component.py")

button1 = tk.Button(root, text="DC Component", command=open_DCComponent_file)
button1.configure(font=("", 9), bg="black", fg="white",width=17)
button1.place(relx=0.3, rely=0.5, anchor=tk.CENTER)

def open_Folding_file():
    open_file_and_execute_code("Floding.py")

button1 = tk.Button(root, text="Floding", command=open_Folding_file)
button1.configure(font=("", 9), bg="black", fg="white",width=17)
button1.place(relx=0.7, rely=0.5, anchor=tk.CENTER)

def open_convolve_file():
    open_file_and_execute_code("convolve.py")

button1 = tk.Button(root, text="Convolve", command=open_Folding_file)
button1.configure(font=("", 9), bg="black", fg="white",width=17)
button1.place(relx=0.3, rely=0.6, anchor=tk.CENTER)

def open_Delayoradvance_file():
    open_file_and_execute_code("Delaying or advancing.py")

button1 = tk.Button(root, text="Delaying or advancing", command=open_Delayoradvance_file)
button1.configure(font=("", 9), bg="black", fg="white",width=17)
button1.place(relx=0.7, rely=0.6, anchor=tk.CENTER)

def open_correlation_file():
    open_file_and_execute_code("correlation.py")

button1 = tk.Button(root, text="correlation", command=open_correlation_file)
button1.configure(font=("", 9), bg="black", fg="white",width=17)
button1.place(relx=0.3, rely=0.7, anchor=tk.CENTER)

def open_timedelay_file():
    open_file_and_execute_code("timedelay.py")

button1 = tk.Button(root, text="time delay", command=open_timedelay_file)
button1.configure(font=("", 9), bg="black", fg="white",width=17)
button1.place(relx=0.7, rely=0.7, anchor=tk.CENTER)

def open_templetematch_file():
    open_file_and_execute_code("templete match.py")

button1 = tk.Button(root, text="templete match", command=open_templetematch_file)
button1.configure(font=("", 9), bg="black", fg="white",width=17)
button1.place(relx=0.3, rely=0.8, anchor=tk.CENTER)

def open_fastconvolution_file():
    open_file_and_execute_code("fastconvolution.py")

button1 = tk.Button(root, text="fastconvolution", command=open_fastconvolution_file)
button1.configure(font=("", 9), bg="black", fg="white",width=17)
button1.place(relx=0.7, rely=0.8, anchor=tk.CENTER)

def open_fastCorrelation_file():
    open_file_and_execute_code("fastCorrelation.py")

button1 = tk.Button(root, text="fastCorrelation", command=open_fastCorrelation_file)
button1.configure(font=("", 9), bg="black", fg="white",width=17)
button1.place(relx=0.3, rely=0.9, anchor=tk.CENTER)

root.mainloop()
