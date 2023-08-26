from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np
from tkcalendar import Calendar

class Student:
    def __init__(self, root):
        self.root = root
        self.root.state('zoomed')
        self.root.title("Hệ thống quản lý điểm danh sử dụng nhận dạng khuôn mặt")

        #********************** Các biến sử dụng ********************************
        self.var_major = StringVar()
        self.var_he_dao_tao = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_ID = StringVar()
        self.var_name = StringVar()
        self.var_class = StringVar()
        self.var_gender = StringVar()
        self.var_email = StringVar()
        self.var_address = StringVar()
        self.var_CCCD = StringVar()
        self.var_dob = StringVar()
        self.var_mobile = StringVar()
    
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
        left_frame.place(x=10, y=10, width=main_frame.winfo_screenwidth()/ 2, height= 930)
        # Current course Label
        current_course_label = LabelFrame(left_frame, bd=2, bg="white", text="Thông tin khoá học",font=("verdana",20,"bold"),fg="navyblue")
        current_course_label.place(x=13, y= 8, width= 920, height= 250)
        
        # Label in current course label
        dep_label = Label(current_course_label, text="Chuyên ngành", font=("verdana",20,"bold"),bg="white",fg="navyblue")
        dep_label.grid(row=0, column=0, padx=15, pady=30, sticky="w")

        year_label = Label(current_course_label, text="Năm học", font=("verdana",20,"bold"),bg="white",fg="navyblue")
        year_label.grid(row=1, column=0, padx=15, pady=30, sticky="w")

        he_dao_tao_label = Label(current_course_label, text = "Hệ đào tạo",font=("verdana",20,"bold"),bg="white",fg="navyblue" )
        he_dao_tao_label.grid(row=0, column=2, padx=20, pady=30, sticky="w")

        semester_label = Label(current_course_label, text = "Học kì",font=("verdana",20,"bold"),bg="white",fg="navyblue" )
        semester_label.grid(row=1, column=2, padx=20, pady=30, sticky="w")

        #combobox
            #chuyên ngành
        dep_combobox = ttk.Combobox(current_course_label, textvariable=self.var_major, width=23, font=("verdana",15,"bold"),state="readonly", foreground="white")
        dep_combobox["values"] = ("Công nghệ kỹ thuật máy tính","Công nghệ thông tin","Khoa học dữ liệu và AI","Thiết kế mĩ thuật số","Quản trị kinh doanh","Logistics và chuỗi cung ứng")
        dep_combobox.current(0)
        dep_combobox.grid(row=0, column=1, padx=5, pady=30)

            # hệ đào tạo
        he_dao_tao_combobox = ttk.Combobox(current_course_label, textvariable=self.var_he_dao_tao,width=15, font=("verdana",15,"bold"),state="readonly", foreground="white")
        he_dao_tao_combobox["values"] = ("IT1","IT2","IT-E10","IT-E15","IT-EP","IT-E6","IT-E7", "IT-LTU", "IT-VUW")
        he_dao_tao_combobox.current(0)
        he_dao_tao_combobox.grid(row= 0, column= 3, padx=5, pady=30)

            # Năm học
        year_combobox = ttk.Combobox(current_course_label, textvariable= self.var_year, width=23, font=("verdana",15,"bold"),state="readonly", foreground="white" )
        year_combobox["values"] = ("2020-21", "2021-22", "2022-23")
        year_combobox.current(0)
        year_combobox.grid(row=1, column=1,  padx=5, pady=30 )

            # học kỳ
        semester_combobox = ttk.Combobox(current_course_label, textvariable= self.var_semester, width=15, font=("verdana",15,"bold"),state="readonly", foreground="white")
        semester_combobox["values"] = ("Học kỳ I", "Học kỳ II", "Học kỳ hè")
        semester_combobox.current(0)
        semester_combobox.grid(row=1, column=3, padx=5, pady=30)


        #class info Label
        class_info_label = LabelFrame(left_frame, bd=2, bg = "white", relief=RIDGE, text="Thông tin lớp học",font=("verdana",20,"bold"),fg="navyblue")
        class_info_label.place(x=13, y= 260, width= 920, height= 620)
            # label in class info label
        id_label = Label(class_info_label, text="ID sinh viên", font=("verdana",20,"bold"),bg="white",fg="navyblue" )
        id_label.grid(row=0, column=0, padx=15, pady=20, sticky="w")
        id_entry = ttk.Entry(class_info_label, textvariable= self.var_ID, width =15, font=("verdana",20,"bold"))
        id_entry.grid(row=0, column=1, padx=15, pady=20, sticky="w")

        class_label = Label(class_info_label, text="Lớp học", font=("verdana",20,"bold"),bg="white",fg="navyblue" )
        class_label.grid(row=1, column=0, padx=15, pady=20, sticky="w")
        class_entry = ttk.Entry(class_info_label, textvariable= self.var_class, width =15, font=("verdana",20,"bold"))
        class_entry.grid(row=1, column=1, padx=15, pady=20, sticky="w")

        gender_label = Label(class_info_label, text="Giới tính", font=("verdana",20,"bold"),bg="white",fg="navyblue" )
        gender_label.grid(row=2, column=0, padx=15, pady=20, sticky="w")
        gender_combobox = ttk.Combobox(class_info_label, textvariable=self.var_gender, width =14, font=("verdana",20,"bold"))
        gender_combobox["values"]= ("Nam", "Nữ")
        gender_combobox.current(0)
        gender_combobox.grid(row=2, column=1, padx=15, pady=20, sticky="w")

        email_label = Label(class_info_label, text="Email", font=("verdana",20,"bold"),bg="white",fg="navyblue")
        email_label.grid(row=3, column=0, padx=15, pady=20, sticky="w")
        email_entry = ttk.Entry(class_info_label, textvariable= self.var_email, width =15, font=("verdana",20,"bold"))
        email_entry.grid(row=3, column=1, padx=15, pady=20, sticky="w")

        address_label = Label(class_info_label, text="Địa chỉ", font=("verdana",20,"bold"),bg="white",fg="navyblue")
        address_label.grid(row=4, column=0, padx=15, pady=20, sticky="w")
        address_entry = ttk.Entry(class_info_label, textvariable= self.var_address, width =15, font=("verdana",20,"bold"))
        address_entry.grid(row=4, column=1, padx=15, pady=20, sticky="w")

        name_label = Label(class_info_label, text="Tên sinh viên", font=("verdana",20,"bold"),bg="white",fg="navyblue")
        name_label.grid(row=0, column=2, padx=15, pady=20, sticky="w")
        name_entry = ttk.Entry(class_info_label, textvariable= self.var_name, width =15, font=("verdana",20,"bold"))
        name_entry.grid(row=0, column=3, padx=15, pady=20, sticky="w")

        cccd_label = Label(class_info_label, text="CCCD", font=("verdana",20,"bold"),bg="white",fg="navyblue")
        cccd_label.grid(row=1, column=2, padx=15, pady=20, sticky="w")
        cccd_entry = ttk.Entry(class_info_label, textvariable= self.var_CCCD, width =15, font=("verdana",20,"bold"))
        cccd_entry.grid(row=1, column=3, padx=15, pady=20, sticky="w")

        dob_label = Label(class_info_label, text="Ngày sinh", font=("verdana",20,"bold"),bg="white",fg="navyblue")
        dob_label.grid(row=2, column=2, padx=15, pady=20, sticky="w")
        dob_entry = ttk.Entry(class_info_label, textvariable= self.var_dob, width =15, font=("verdana",20,"bold"))
        dob_entry.grid(row=2, column=3, padx=15, pady=20, sticky="w")
        dob_entry.insert(0, "dd/mm/yyyy")

        phone_label = Label(class_info_label, text="SĐT", font=("verdana",20,"bold"),bg="white",fg="navyblue")
        phone_label.grid(row=3, column=2, padx=15, pady=20, sticky="w")
        phone_entry = ttk.Entry(class_info_label, textvariable= self.var_mobile, width =15, font=("verdana",20,"bold"))
        phone_entry.grid(row=3, column=3, padx=15, pady=20, sticky="w")

    # Radio buttons
        self.var_radio = StringVar()
        radio_bt1 = ttk.Radiobutton(class_info_label, text="Có ảnh", value="Yes", variable=self.var_radio)
        radio_bt1.grid(row= 5, column=0, padx= 15, pady=20, sticky=W)

        radio_bt2 = ttk.Radiobutton(class_info_label, text="Không ảnh", value="No", variable=self.var_radio)
        radio_bt2.grid(row= 5, column=1, padx= 5, pady=20, sticky=W)

    # Button Frame
        button_frame = Frame(class_info_label, bg="white", relief=RIDGE)
        button_frame.place(x=5, y=950, width=920, height=300)

        # Button - Lưu
        save_button = Button(button_frame, text="Lưu", width=20,font=("verdana",10,"bold"),fg="white",bg="navyblue")
        save_button.grid(row=0, column=0, padx=5, pady=20, sticky=W)

        


if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()