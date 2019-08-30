from tkinter import *
import cv2
from PIL import Image
from PIL import ImageTk
import os

class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill =BOTH, expand = 1)
        self.vid = cv2.VideoCapture(0)
        self.vid.set(cv2.CAP_PROP_FRAME_WIDTH, 640);
        self.vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 360);
        self.im =Image.open("allBlack.jpeg")
        self.photoBlack = ImageTk.PhotoImage(self.im)
        allblack = Label(self, image=self.photoBlack)
        allblack.config(width=640, height=354)
        allblack.image = self.photoBlack
        allblack.place(x=750,y=37)



        canvasFrame = Frame(width = 200, height =200)
        canvasFrame.place(in_=self, anchor="se", relx=.5, rely=.5)
        self.canvas = Canvas(canvasFrame, width = 640, height =360)
        self.canvas.place(anchor=CENTER)
        self.canvas.pack(side=LEFT)

        self.delay = 15
        self.update()


        #Retake Button
        self.retakeButton = Button(self, text="Retake Picture", command=self.clickRetakeButton)
        self.retakeButton.place(x=100, y=600)

        #Capture the Photo
        self.captureButton = Button(self, text="Capture Photo", command=self.capturePhoto)
        self.captureButton.place(x=670, y=600)

        #Name Entry
        self.namelabel = Label(self, text="Please Enter Your Name")
        self.namelabel.place(x=1210, y=575)
        self.nameEntry = Entry(self, text="Enter Name")
        self.nameEntry.place(x=1200, y=600)
        self.takeName = Button(self, text="Enter", command=self.getName)
        self.takeName.place(x=1210, y=635)

    def clickRetakeButton(self):
        allblack = Label(self, image=self.photoBlack)
        allblack.config(width=640, height=354)
        allblack.image = self.photoBlack
        allblack.place(x=750,y=37)


    def capturePhoto(self):

        self.name = self.getName()
        if(self.name != ''):
            ret ,frame = self.vid.read()
            cv2.imwrite(filename= self.name + ".jpg", img=frame)
            self.img_ = cv2.imread(self.name + '.jpg')
            self.gray = cv2.cvtColor(self.img_, cv2.COLOR_BGR2GRAY)
            self.blurred = cv2.GaussianBlur(self.gray, (3,3) , 0)
            self.wide = cv2.Canny(self.blurred, 15, 60)
            cv2.imwrite(filename=self.name+'cannyEdge.jpg', img=self.wide)
            os.remove(self.name+'.jpg')
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(self.wide))
            cannyimage = Label(self, image=self.photo)
            cannyimage.config(width=640, height=354)
            cannyimage.image = self.photo
            cannyimage.place(x=750,y=37)
        else:
            self.takeName.config(highlightbackground='red')
            self.nameEntry.config(highlightbackground='red')

    def getName(self):
        name = self.nameEntry.get()
        if(name ==''):
            self.nameEntry.config(highlightbackground='red')
        else:
            self.nameEntry.config(highlightbackground='white')
            self.takeName.config(highlightbackground='white')
        return name

    def update(self):
        ret, frame = self.get_frame()

        if ret:
            self.photo = ImageTk.PhotoImage(image = Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = NW)
        self.after(self.delay, self.update)

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
