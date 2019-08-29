from tkinter import *
import cv2
import PIL.Image, PIL.ImageTk

class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill =BOTH, expand = 1)
        self.vid = VideoCapture(0)

        canvasFrame = Frame(width = 200, height =200)
        canvasFrame.place(in_=self, anchor="se", relx=.5, rely=.5)
        self.canvas = Canvas(canvasFrame, width = 640, height =360)
        self.canvas.place(anchor=CENTER)
        self.canvas.pack(side=LEFT)
        self.delay = 15
        self.update()

        #Retake Button
        retakeButton = Button(self, text="Retake Picture", command=self.clickRetakeButton)
        retakeButton.place(x=100, y=600)

        #Capture the Photo
        captureButton = Button(self, text="Capture Photo", command=self.capturePhoto)
        captureButton.place(x=670, y=600)

        #Name Entry
        namelabel = Label(self, text="Please Enter Your Name")
        namelabel.place(x=1210, y=575)
        self.nameEntry = Entry(self, text="Enter Name")
        self.nameEntry.place(x=1200, y=600)
        takeName = Button(self, text="Enter", command=self.getName)
        takeName.place(x=1210, y=635)

    def clickRetakeButton(self):
        exit()
    def capturePhoto(self):
        return
    def getName(self):
        name = self.nameEntry.get()
        return name
    def update(self):
        ret, frame = self.vid.get_frame()

        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = NW)
        self.after(self.delay, self.update)


class VideoCapture:
    def __init__(self, vid_source):
        self.vid = cv2.VideoCapture(vid_source)
        self.vid.set(cv2.CAP_PROP_FRAME_WIDTH, 640);
        self.vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 360);
    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            frame = cv2.flip(frame,1)
            if ret:
                return (ret,cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (ret, None)

root = Tk()
app = App(root)
root.wm_title("Demo Gui")
root.geometry("1440x900")
root.mainloop()
