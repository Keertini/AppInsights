import matplotlib
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
import numpy as np
import pandas as pd
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askyesno

df = pd.read_csv("MobileAppAnalysisData.csv")

def rating(f):
    plt.figure(figsize = (15,7))
    x = list(f['Rating'])
    x.sort(reverse=True)
    y = list(f['Category'])
    plt.title("MOBILE APPLICATION - RATING ANALYSIS")
    plt.xlabel("RATING")
    plt.ylabel("CATEGORY")
    plt.plot(x,y,'m--',color='grey',marker='D',markersize=4,markerfacecolor='black',label='Rating')
    plt.legend(loc='upper right',ncol=1)
    plt.show()
def installs(f):
    plt.figure(figsize = (15,7))
    x = list(f['Installs'])
    x.sort(reverse=True)
    y = list(f['Category'])
    plt.title("MOBILE APPLICATION - INSTALL ANALYSIS")
    plt.xlabel("INSTALLS")
    plt.ylabel("CATEGORY")
    plt.plot(x,y,'m--',color='grey',marker='D',markersize=4,markerfacecolor='black',label='Installs')
    plt.legend(loc='lower right',ncol=1)
    plt.show()
def size(f):
    plt.figure(figsize = (15,7))
    x = list(f['Size'])
    x.sort(reverse=True)
    y = list(f['Category'])
    plt.title("MOBILE APPLICATION - SIZE ANALYSIS")
    plt.xlabel("SIZE")
    plt.ylabel("CATEGORY")
    plt.plot(x,y,'m--',color='grey',marker='D',markersize=4,markerfacecolor='black',label='Size')
    plt.legend(loc='lower right',ncol=3)
    plt.show()
def reviews(f):
    plt.figure(figsize = (15,7))
    x = list(f['Reviews'])
    x.sort(reverse=True)
    y = list(f['Category'])
    plt.title("MOBILE APPLICATION - REVIEW ANALYSIS")
    plt.xlabel("REVIEWS")
    plt.ylabel("CATEGORY")
    plt.plot(x,y,'m--',color='grey',marker='D',markersize=4,markerfacecolor='black',label='Review')
    plt.legend(loc='upper right',ncol=1)
    plt.show()

def c1():
    rating(df)
def c2():
    installs(df)
def c3():
    size(df)
def c4():
    reviews(df)
def confirm():
    answer = askyesno(title='Confirmation',message='Are you sure that you want to quit?')
    if answer:
        root.destroy()
       
root = tk.Tk()
root.title('Python Package')
# root.configure(bg='Grey')
root.geometry('270x190')
frame = ttk.Frame(root)
frame.grid()

options = {'padx' : 10,'pady' : 10}
ttk.Label(frame, text="\n          MOBILE APPLICATION DATA ANALYSIS\n").grid(column=0, row=0)
button1 = ttk.Button(frame, text="Rating", command=c1).grid(column=0, row=1)
button2 = ttk.Button(frame, text="Install", command=c2).grid(column=0, row=2)
button3 = ttk.Button(frame, text="Size", command=c3).grid(column=0, row=3)
button4 = ttk.Button(frame, text="Review", command=c4).grid(column=0, row=4)
button5 = ttk.Button(frame, text="Quit", command=confirm).grid(column=0, row=6)
root.mainloop()