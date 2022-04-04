import tkinter as tk
import tkinter.font as tkFont

from PIL import ImageTk, Image
import cv2

class GUI:
    def __init__(self, root):
        #setting title
        root.title("YOLOv5 Deer detection")
     

        #setting window size
        width=600
        height=500

        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()

        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)


        # Button configurations
        btnChangeImgSource=tk.Button(root)
        btnChangeImgSource["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Calibri',size=10)
        btnChangeImgSource["font"] = ft
        btnChangeImgSource["fg"] = "#000000"
        btnChangeImgSource["justify"] = "center"
        btnChangeImgSource["text"] = "Change image source"
        btnChangeImgSource.place(x=20,y=370,width=342,height=30)
        btnChangeImgSource["command"] = self.btnChangeImgSource_command

        btnChangeDataSource=tk.Button(root)
        btnChangeDataSource["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Calibri',size=10)
        btnChangeDataSource["font"] = ft
        btnChangeDataSource["fg"] = "#000000"
        btnChangeDataSource["justify"] = "center"
        btnChangeDataSource["text"] = "Change training model"
        btnChangeDataSource.place(x=20,y=410,width=342,height=30)
        btnChangeDataSource["command"] = self.btnChangeDataSource_command

        detectionIndicator=tk.Message(root)
        ft = tkFont.Font(family='Calibri',size=10)
        detectionIndicator["font"] = ft
        detectionIndicator["fg"] = "#333333"
        detectionIndicator["justify"] = "center"
        detectionIndicator["text"] = "Alarm indicator"
        detectionIndicator.place(x=410,y=370,width=171,height=116)

        btnManualOn=tk.Button(root)
        btnManualOn["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Calibri',size=10)
        btnManualOn["font"] = ft
        btnManualOn["fg"] = "#000000"
        btnManualOn["justify"] = "center"
        btnManualOn["text"] = "Manual: Alarm ON"
        btnManualOn.place(x=20,y=460,width=161,height=30)
        btnManualOn["command"] = self.btnManualOn_command

        btnManualOff=tk.Button(root)
        btnManualOff["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Calibri',size=10)
        btnManualOff["font"] = ft
        btnManualOff["fg"] = "#000000"
        btnManualOff["justify"] = "center"
        btnManualOff["text"] = "Manual: Alarm OFF"
        btnManualOff.place(x=200,y=460,width=160,height=30)
        btnManualOff["command"] = self.btnManualOff_command


        # Capture from camera
        cap = cv2.VideoCapture(0)

        # function for video streaming
        def video_stream():
            _, frame = cap.read()
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            img = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=img)
            lmain.imgtk = imgtk
            lmain.configure(image=imgtk)
            lmain.after(1, video_stream) 

        video_stream()
        root.mainloop()

    # Button commands
    def btnChangeImgSource_command(self):
        print("Prompt for choosing new image source")


    def btnChangeDataSource_command(self):
        print("Prompt for choosing new dataset")


    def btnManualOn_command(self):
        print("Alarm is now ON")


    def btnManualOff_command(self):
        print("Alarm is now OFF")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
