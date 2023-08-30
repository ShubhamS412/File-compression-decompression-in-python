import tkinter as tk
from compmodule import compress,decompress
from tkinter import filedialog

def open_file():
    filename = filedialog.askopenfilename(initialdir='/',title="Select a file to compress/decompress:")
    return filename


def compression(i,o):
    compress(i,o)
    
def decompression(i,o):
    decompress(i,o)
    

window = tk.Tk()
window.title("Compression/Decompression engine")
window.geometry("400x200")

input_entry = tk.Entry(window)
#output_entry = tk.Entry(window)

input_label = tk.Label(window,text="File to be compressed/decompressed:")
#output_label = tk.Label(window,text="Name of the compressed file:")

compress_button = tk.Button(window,text="Compress",command=lambda:compression(open_file(),"cp_output1.txt"))
decompress_button = tk.Button(window,text="Decompress",command=lambda:decompression(open_file(),"dcp_output1.txt"))


input_label.grid(row=0,column=0)
##input_entry.grid(row=0,column=1)
#output_label.grid(row=1,column=0)
#output_entry.grid(row=1,column=1)
compress_button.grid(row=1,column=0)
decompress_button.grid(row=2,column=0)


window.mainloop()