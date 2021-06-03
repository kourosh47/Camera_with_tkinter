from tkinter import *
from tkinter.messagebox import showerror
import cv2,webbrowser
from tkinter import filedialog
import PIL.ImageTk,PIL.Image
import time

class  mainapp:
        def __init__(self):
                self.root=Tk()
                self.root.title("Webcam")
                self.cam=Vid()
                self.can=Canvas(height=self.cam.height,width=self.cam.width)
                self.but_1=Button(text="Capture",command=self.snap,bg="light green",fg="blue")
                self.but_2=Button(self.root,text="More",command=self.call,fg="green",bg="light yellow")
                self.can.pack()
                self.but_2.place(x=70,y=484)
                self.but_1.pack(expand=True,anchor=NW)
                self.upg()
                self.root.mainloop()

        def  call(self):
                webbrowser.open_new_tab("https://github.com/kourosh47?tab=repositories")

        def  snap(self):
                frame=self.cam.frame_get()
                path=filedialog.askdirectory()+"/"
                if path != "/":
                    cv2.imwrite(path+time.strftime("%d-%m-%Y-%H-%M-%S")+".jpg",cv2.cvtColor(frame,cv2.COLOR_RGB2BGR))
                else:
                    showerror("Error","No path given!")
        def upg(self):
                frame=self.cam.frame_get()
                self.im=PIL.ImageTk.PhotoImage(image= PIL.Image.fromarray(frame))
                self.can.create_image(0, 0, image=self.im, anchor=NW)
                self.root.after(10,self.upg)

class Vid:
        def __init__(self):
            self.vid=cv2.VideoCapture(0)
            if  not self.vid.isOpened():
                    showerror("Error","No Camera exist!")
            self.height=self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
            self.width=self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)

        def  frame_get(self):
            ret,frame=self.vid.read()
            return (cv2.cvtColor(frame,cv2.COLOR_RGB2BGR))

        def  __del__(self):
            if self.vid.isOpened():
                self.vid.release()


mainapp()