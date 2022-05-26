import tkinter as Tk
import Chart as chart
import VideoCap as videocap

import threading

class SampleApp(Tk.Tk):
    def __init__(self):
        Tk.Tk.__init__(self)
        self.title("인공지능을 활용한 풀업 자세 교정")
        evt = threading.Event()

        frame1=videocap.VideoCap(self, evt)
        frame1.pack(side=Tk.LEFT, fill="both", expand=True)
        frame1.start()

        frame2=chart.Chart(self, evt)
        frame2.pack(side=Tk.RIGHT, fill="both", expand=True)
        frame2.start()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()