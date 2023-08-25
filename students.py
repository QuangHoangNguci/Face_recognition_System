from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np 


class Student:
    def __init__(self, root):
        self.root = root
        self.root.state('zoomed')
        self.root.title("Hệ thống quản lý điểm danh sử dụng nhận dạng khuôn mặt")

        #********************** Các biến sử dụng ********************************
        self.var_major = StringVar()
        self.var_subject = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_ID = StringVar()
        self.var_name = StringVar()
        self.var_lesson = StringVar()
        self.var_gender = StringVar()
        self.var_email = StringVar()
        self.var_address = StringVar()
        self.var_roll_no = StringVar()
        self.var_dob = StringVar()
        self.var_mobile = StringVar()
        self.var_name_teacher = StringVar()
    
    #****************************** Set up UI ***************************************
        # header image
        img_header = Image.open(r"/Users/QuangHoang/Documents/Face_recognition_system/Images_GUI/banner1.jpg")
        img_header = img_header.resize((root.winfo_screenwidth(), 130), Image.LANCZOS)
        self.photoImg = ImageTk.PhotoImage(img_header)

        header_label = Label(self.root, image= self.photoImg)
        header_label.place(x=0, y=0, width=root.winfo_screenwidth(), height=130)

        # back ground Imgae
        img_bg = Image.open(r"/Users/QuangHoang/Documents/Face_recognition_system/Images_GUI/bg4.png")
        remaining_height = root.winfo_screenheight() - 130
        img_bg = img_bg.resize((root.winfo_screenwidth(), remaining_height),Image.LANCZOS)
        self.photo_bg = ImageTk.PhotoImage(img_bg)

        bg_label = Label(self.root, image=self.photo_bg)
        bg_label.place(x=0, y=130, width=root.winfo_screenwidth(), height=remaining_height)

        # set title
        title_lb = Label(bg_label, text="Quản lí thông tin sinh viên",font=("times new roman",35,"bold"),bg="navyblue",fg="white")
        title_lb.place(x=0, y=0, width=root.winfo_screenwidth(), height=50)

        # ************************************Creating Frames *******************************************
        # main frame
        main_frame = Frame(bg_label, bd=2,bg="white")
        main_frame.place(x=0, y=50, width=bg_label.winfo_screenwidth(), height=bg_label.winfo_screenheight())
        
        # Leaf label frame
        left_frame = LabelFrame(main_frame, bd=2, bg = "white", relief=RIDGE, text="Thông tin sinh viên",font=("verdana",20,"bold"),fg="navyblue")
        left_frame.place(x=10, y=10, width=main_frame.winfo_screenwidth()/ 2, height= main_frame.winfo_screenheight())

        # Current course Label
        current_course_label = LabelFrame(left_frame, bd=2, bg="white", text="Thông tin khoá học",font=("verdana",20,"bold"),fg="navyblue")
        current_course_label.place(x=13, y= 8, width= 920, height= 350)
        
        # In Current course Label
        dep_label = Label(current_course_label, text="Chuyên Ngành", font=("verdana",20,"bold"),bg="white",fg="navyblue")
        dep_label.grid(row=0, column=0, padx=15, pady=20)

        subject_label = Label(current_course_label, text = "Môn",font=("verdana",20,"bold"),bg="white",fg="navyblue" )
        subject_label.grid(row=0, column=2, padx=20, pady=20)



        #combobox
        dep_combobox = ttk.Combobox(current_course_label, textvariable=self.var_major, width=23, font=("verdana",15,"bold"),state="readonly", foreground="white")
        dep_combobox["values"] = ("Công nghệ kỹ thuật máy tính","Công nghệ thông tin","Khoa học dữ liệu và AI","Thiết kế mĩ thuật số","Quản trị kinh doanh","Logistics và chuỗi cung ứng")
        dep_combobox.current(0)
        dep_combobox.grid(row=0, column=1, padx=5, pady=20)

        subject_combobox = ttk.Combobox(current_course_label, textvariable=self.var_subject,width=23, font=("verdana",15,"bold"),state="readonly", foreground="white")
        subject_combobox["values"] = ("Công nghệ kỹ thuật máy tính","Công nghệ thông tin","Khoa học dữ liệu và AI","Thiết kế mĩ thuật số","Quản trị kinh doanh","Logistics và chuỗi cung ứng")
        subject_combobox.current(0)
        subject_combobox.grid(row= 0, column= 3, padx=5, pady=20)




        


if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()