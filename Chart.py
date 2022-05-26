import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import tkinter as Tk
import threading

class Chart(Tk.Frame, threading.Thread):
    def __init__(self, master, evt):
        Tk.Frame.__init__(self, master)
        threading.Thread.__init__(self)
        
        self.evt = evt
        self.count = 0
        self.preco = 0

        self.fig, self.ax = plt.subplots()
        self.ax.set(xlim=(0, 50), ylim=(0, 50))
        self.line, = plt.plot(np.arange(0), np.arange(0), 'ro') 

        self.ax.set_title("counting pull-up",fontsize=25)

        self.ax.set_xlabel("time",fontsize=18)
        self.ax.set_ylabel("count",fontsize=18)

        canvas = FigureCanvasTkAgg(self.fig, master=master)
        canvas.get_tk_widget().pack()


    def update(self):
        # 한점으로 나타내기
        # self.line.set_xdata(np.arange(self.preco, self.count))
        # self.line.set_ydata(np.arange(self.preco, self.count))
        # 한점 이어서 나타내기
        self.line.set_xdata(np.arange(0, self.count))
        self.line.set_ydata(np.arange(0, self.count))
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
        self.preco = self.count

    def run(self):
        while(True):
            self.evt.wait()
            self.count = self.count + 1
            self.update()
            self.evt.clear()

