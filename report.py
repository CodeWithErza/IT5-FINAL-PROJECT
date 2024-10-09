from tkinter import*
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
# import mysql.connector

class Report_feedback:
    def __init__(self, root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

#=======================TITLE=======================
        label_title = Label(self.root, text="TEXT REPORT", font=("times new roman",18), bg="#89b0a4", fg="#f7e7ce", bd=4, relief=RIDGE)
        label_title.place(x=0, y=0, width=1295, height=50)

#========================LOGO=======================
        try:
            img3 = Image.open("logo.jpeg")
            img3 = img3.resize((100, 40), Image.LANCZOS)
            self.photoimg3 = ImageTk.PhotoImage(img3)

            labelimg3= Label(self.root, image=self.photoimg3, bd=0, relief=RIDGE)
            labelimg3.place(x=5, y=5, width=100, height=40)

        except FileNotFoundError:
            print("Image not found")

#=====================LABEL_FRAME======================

        label_frame_left = LabelFrame(self.root, bd=2, relief=RIDGE, text="REPORT",font=("times new roman", 12, "bold"),bg="#89b0a4", fg="#f7e7ce")
        label_frame_left.place(x=2, y=50, width=1292, height=499)





if __name__ == "__main__":
    root = Tk()
    obj = Report_feedback(root)
    root.mainloop()