import PIL.Image, PIL.ImageTk
import cv2

import tkinter as Tk
import threading

class VideoCap(Tk.Frame, threading.Thread):
    def __init__(self, master, evt):
        Tk.Frame.__init__(self, master)
        threading.Thread.__init__(self)

        self.evt = evt
        self.label = Tk.Label(self)
        self.label.pack()

        self.cap = cv2.VideoCapture(cv2.CAP_DSHOW)

    def run(self):
        while True:
            
            ret, frame = self.cap.read()

            # 행동인식 파트
            # 너무 길게 쓰지말것 프레임 떨어짐

            # 행동인식->행동분류 후에 밑에 함수를 반드시 실행시키셈
            # self.evt.set()

            imgtk = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
            self.label.configure(image=imgtk)
            self.label.image = imgtk
            
    def  __del__(self):
        cv2.destroyAllWindows()
