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
    
    #********************************************************************* Set up UI ******************************************************************************
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
        
        #=============================================== Left label frame ===============================================#
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
        dep_combobox["values"] = ("Chọn","Cong nghe ky thuat may tinh")
        dep_combobox.current(0)
        dep_combobox.grid(row=0, column=1, padx=5, pady=30)

            # hệ đào tạo
        he_dao_tao_combobox = ttk.Combobox(current_course_label, textvariable=self.var_he_dao_tao,width=15, font=("verdana",15,"bold"),state="readonly", foreground="white")
        he_dao_tao_combobox["values"] = ("Chọn","IT1","IT2","IT-E10","IT-E15","IT-EP","IT-E6","IT-E7", "IT-LTU", "IT-VUW")
        he_dao_tao_combobox.current(0)
        he_dao_tao_combobox.grid(row= 0, column= 3, padx=5, pady=30)

            # Năm học
        year_combobox = ttk.Combobox(current_course_label, textvariable= self.var_year, width=23, font=("verdana",15,"bold"),state="readonly", foreground="white" )
        year_combobox["values"] = ("Chọn","2020-21", "2021-22", "2022-23")
        year_combobox.current(0)
        year_combobox.grid(row=1, column=1,  padx=5, pady=30 )

            # học kỳ
        semester_combobox = ttk.Combobox(current_course_label, textvariable= self.var_semester, width=15, font=("verdana",15,"bold"),state="readonly", foreground="white")
        semester_combobox["values"] = ("Chọn","Hoc ky I", "Hoc ky II", "Hoc ky he")
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
        gender_combobox["values"]= ("Chọn", "Nam", "Nu")
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
        #dob_entry.insert(0, "dd/mm/yyyy")

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
        button_frame.place(x=10, y=430, width=900, height=150)

        button_frame_1 = Frame(button_frame, bg="white", relief=RIDGE)
        button_frame_1.place(x=0, y=0, width=900, height=75)

        button_frame_2 = Frame(button_frame, bg="white", relief=RIDGE)
        button_frame_2.place(x=0, y=75, width=900, height=75)

        # Button - Lưu
        save_button = Button(button_frame_1, text="Lưu", width=27,height=3,font=("verdana",10,"bold"),fg="black",bg="blue", command=self.add_data)
        save_button.grid(row=0, column=0, pady=20,sticky=W)

        # Button sửa
        fix_button = Button(button_frame_1, text="Sửa", width=27,height=3,font=("verdana",10,"bold"),fg="black",bg="blue", command=self.update_data)
        fix_button.grid(row=0, column=1,  pady=20,sticky=W)

        # Button Xoá
        delete_button = Button(button_frame_1, text="Xoá", width=27,height=3,font=("verdana",10,"bold"),fg="black",bg="blue", command=self.delete_data)
        delete_button.grid(row=0, column=2,  pady=20,sticky=W)

        #Button - Làm mới
        reset_button = Button(button_frame_1, text="Làm mới", width=27,height=3,font=("verdana",10,"bold"),fg="black",bg="blue",command=self.reset_data)
        reset_button.grid(row=0, column=3,  pady=20,sticky=W)

        #Button - Lấy ảnh sinh viên
        take_photo_button = Button(button_frame_2, text="Lấy ảnh sinh viên", width=59,height=3,font=("verdana",10,"bold"),fg="black",bg="blue", command=self.generate_data)
        take_photo_button.grid(row=1, column=0, pady=10,sticky=W)

        # Button - Training Data
        training_data_button = Button(button_frame_2, text="Training Data", width=59,height=3,font=("verdana",10,"bold"),fg="black",bg="blue")
        training_data_button.grid(row=1, column=1,  pady=10,sticky=W)


        #=============================================== Right label frame ===============================================#
        #================================ Right label frame up ================================
        right_label_frame_up = LabelFrame(main_frame, bd=2, bg = "white", relief=RIDGE, text="Hệ Thống Tìm Kiếm",font=("verdana",20,"bold"),fg="navyblue")
        right_label_frame_up.place(x = main_frame.winfo_screenwidth()/ 2 +20, y=10, width=main_frame.winfo_screenwidth()/ 2 -30, height= 465)

        #Label search
        search_label = Label(right_label_frame_up,text="Tìm kiếm theo:",font=("verdana",20,"bold"),fg="red",bg="white" )
        search_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)
        self.var_search_TX = StringVar()
        # conbobox search
        search_combobox = ttk.Combobox(right_label_frame_up, textvariable=self.var_search_TX, width=12, font=("verdana",15,"bold"),state="readonly")
        search_combobox["values"] = ("Chọn", "Ma sinh vien", "Ten sinh vien", "Lop")
        search_combobox.current(0)
        search_combobox.grid(row=0, column=1, padx=5, pady=10, sticky=W)

        # entry search
        self.var_search = StringVar()
        search_entry = ttk.Entry(right_label_frame_up, textvariable= self.var_search, width=18, font=("verdana",15,"bold"))
        search_entry.grid(row=0, column=2,  padx=5, pady=10, sticky=W)

        # Button - tìm kiếm
        find_button = Button(right_label_frame_up, text="Tìm kiếm", width=15, height=2,font=("verdana",10,"bold"),fg="black",bg="blue", command=self.search_data)
        find_button.grid(row=0, column=3, padx=8, pady=10)

        # Button - Xem tất cả
        find_all_button = Button(right_label_frame_up, text="Xem tất cả", width=15, height=2,font=("verdana",10,"bold"),fg="black",bg="blue", command=self.search_all_data)
        find_all_button.grid(row=0, column=4, padx=5, pady=10)

          #================================ Table Frame ================================
        table_frame = Frame(right_label_frame_up, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=10, y=75, width=905, height=350)

        # Croll bar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        # Create table
        self.student_table = ttk.Treeview(table_frame, columns=("Major","He_dao_tao","Year","Semester",
                                                                "ID", "Name","Class", 
                                                                "Gender", "Email","CCCD","D.O.B",
                                                                "SĐT","Address","Photo" ),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("ID", text="ID Sinh viên")
        self.student_table.heading("Name", text="Tên sinh viên")
        self.student_table.heading("Major", text="Chuyên ngành")
        self.student_table.heading("Class", text="Lớp")
        self.student_table.heading("Year", text="Năm học")
        self.student_table.heading("Semester", text="Học kỳ")
        self.student_table.heading("He_dao_tao", text="Hệ đào tạo")
        self.student_table.heading("Gender", text="Giới tính")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("Address", text="Địa chỉ")
        self.student_table.heading("D.O.B", text="Ngày sinh")
        self.student_table.heading("SĐT", text="SĐT")
        self.student_table.heading("CCCD", text="CCCD")
        self.student_table.heading("Photo", text="Ảnh") 
        self.student_table["show"] = "headings"

        #set width colunms
        self.student_table.column("ID", width=120) 
        self.student_table.column("Name", width=120)
        self.student_table.column("Major", width=120)      
        self.student_table.column("Class", width=120)
        self.student_table.column("Year", width=120)
        self.student_table.column("Semester", width=120)
        self.student_table.column("He_dao_tao", width=120)
        self.student_table.column("Gender", width=120)
        self.student_table.column("Email", width=120)
        self.student_table.column("Address", width=120)
        self.student_table.column("D.O.B", width=120)
        self.student_table.column("SĐT", width=120)
        self.student_table.column("CCCD", width=120)
        self.student_table.column("Photo", width=120)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

#======================================== Function Decleration===================================================================
    def add_data(self):
        if self.var_he_dao_tao.get() == "Chọn" or self.var_major.get() == "Chọn" or self.var_year.get() == "Chọn" or self.var_semester.get() == "Chọn" or self.var_ID.get()=="" or self.var_class.get()=="" or self.var_name.get() =="" or self.var_CCCD.get() =="" or self.var_gender.get() =="Chọn" or self.var_dob.get() =="" or self.var_email.get() =="" or self.var_mobile.get() =="" or self.var_address.get() =="":
            messagebox.showerror("Error","Vui lòng điền vào tất cả các trường là bắt buộc!",parent=self.root)
        
        else:
            try:
                conn = mysql.connector.connect(user='root', password='19112002', host='localhost', database='face_recognition', port=3306)
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_major.get(),
                    self.var_he_dao_tao.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_ID.get(),
                    self.var_name.get(),
                    self.var_class.get(),
                    self.var_gender.get(),
                    self.var_email.get(),
                    self.var_CCCD.get(),
                    self.var_dob.get(),
                    self.var_mobile.get(),
                    self.var_address.get(),
                    self.var_radio.get()
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Tất cả các bản ghi đã được lưu!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

    
    #======================================== Fetch Data from table ===================================================================
    def fetch_data(self):
        conn = mysql.connector.connect(user='root', password='19112002', host='localhost', database='face_recognition', port=3306)
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) !=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        
        conn.close()

    #======================================== Get cursor function ===================================================================
    def get_cursor(self, even=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_major.set(data[0]),
        self.var_he_dao_tao.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_ID.set(data[4]),
        self.var_name.set(data[5]),
        self.var_class.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_email.set(data[8]),
        self.var_CCCD.set(data[9]),
        self.var_dob.set(data[10]),
        self.var_mobile.set(data[11]),
        self.var_address.set(data[12]),
        self.var_radio.set(data[13])
    #======================================== Update function ===================================================================
    def update_data(self):
        if self.var_he_dao_tao.get() == "Chọn" or self.var_major.get() == "Chọn" or self.var_year.get() == "Chọn" or self.var_semester.get() == "Chọn" or self.var_ID.get()=="" or self.var_class.get()=="" or self.var_name.get() =="" or self.var_CCCD.get() =="" or self.var_gender.get() =="Chọn" or self.var_dob.get() =="" or self.var_email.get() =="" or self.var_mobile.get() =="" or self.var_address.get() =="":
            messagebox.showerror("Error","Vui lòng điền vào tất cả các trường là bắt buộc!",parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Bạn có muốn sửa lại không!", parent= self.root)
                if Update >0:
                    conn = mysql.connector.connect(user='root', password='19112002', host='localhost', database='face_recognition', port=3306)
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set major=%s, he_dao_tao=%s,year=%s, semester=%s, name=%s, class=%s, gender=%s, email=%s, cccd=%s, dob=%s, phone=%s, address=%s, photo_sample=%s where student_id=%s", (
                        self.var_major.get(),
                        self.var_he_dao_tao.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_name.get(),
                        self.var_class.get(),
                        self.var_gender.get(),
                        self.var_email.get(),
                        self.var_CCCD.get(),
                        self.var_dob.get(),
                        self.var_mobile.get(),
                        self.var_address.get(),
                        self.var_radio.get(), 
                        self.var_ID.get()
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success", "Cập nhật thành công!", parent = self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
            
    #======================================== Delete function ===================================================================
    def delete_data(self):
        if self.var_ID.get() =="":
            messagebox.showerror("Error", "ID sinh viên phải bắt buộc!", parent= self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete", "Bạn có muốn xoá không?", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(user='root', password='19112002', host='localhost', database='face_recognition', port=3306)
                    my_cursor = conn.cursor()
                    query = "delete from student where student_id=%s"
                    val = (self.var_ID.get(),)
                    my_cursor.execute(query, val)
                else:
                    if not delete:
                        return
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Xóa Thành Công!",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

    #======================================== Reset function ===================================================================#
    def reset_data(self):
        self.var_major.set(""),
        self.var_he_dao_tao.set(""),
        self.var_year.set(""),
        self.var_semester.set(""),
        self.var_ID.set(""),
        self.var_name.set(""),
        self.var_class.set(""),
        self.var_gender.set(""),
        self.var_email.set(""),
        self.var_CCCD.set(""),
        self.var_dob.set(""),
        self.var_mobile.set(""),
        self.var_address.set(""),
        self.var_radio.set("")

    #======================================== search data function ===================================================================#
    def search_data(self):
        if self.var_search.get()=="" or self.var_search_TX.get() == "Chọn":
            messagebox.showerror("Error", "Chọn loại tìm kiếm và thông tin cần tìm kiếm!", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(user='root', password='19112002', host='localhost', database='face_recognition', port=3306)
                my_cursor = conn.cursor()

                if self.var_search_TX.get() == "Ma sinh vien":
                    #query = "SELECT major, he_dao_tao, year, semester, student_id, name, class, gender, email, cccd, dob, phone, address, photo_sample FROM student WHERE student_id='" + str(self.var_search.get() + "")
                    query = "SELECT major, he_dao_tao, year, semester, student_id, name, class, gender, email, cccd, dob, phone, address, photo_sample FROM student WHERE student_id='" + str(self.var_search.get()) + "'"
                elif self.var_search_TX.get() == "Ten sinh vien":
                    query = "SELECT major, he_dao_tao, year, semester, student_id, name, class, gender, email, cccd, dob, phone, address, photo_sample FROM student WHERE name LIKE '%" + str(self.var_search.get()) + "%'"
                elif self.var_search_TX.get() == "Lop":
                    query = "SELECT major, he_dao_tao, year, semester, student_id, name, class, gender, email, cccd, dob, phone, address, photo_sample FROM student WHERE class LIKE '%" + str(self.var_search.get()) + "%'"

                my_cursor.execute(query)

                rows = my_cursor.fetchall()
                if len(rows) != 0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("", END, values=i)
                    conn.commit()
                else:
                    messagebox.showerror("Error", "Không tìm thấy dữ liệu phù hợp", parent = self.root)
                    
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
    #======================================== search ALL data function ===================================================================#
    def search_all_data(self):
        try:
            conn = mysql.connector.connect(user='root', password='19112002', host='localhost', database='face_recognition', port=3306)
            my_cursor = conn.cursor()

            query = "SELECT major, he_dao_tao, year, semester, student_id, name, class, gender, email, cccd, dob, phone, address, photo_sample FROM student"
            my_cursor.execute(query)

            rows = my_cursor.fetchall()
            if len(rows) != 0:
                self.student_table.delete(*self.student_table.get_children())
                for i in rows:
                    self.student_table.insert("", END, values=i)
            else:
                messagebox.showinfo("Info", "Không có dữ liệu để hiển thị", parent=self.root)

            conn.close()
        except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
        
    #======================================== OpenCV Camera ===================================================================#
    #======================================== Tạo dataset ===================================================================#

    def generate_data(self):
        if self.var_he_dao_tao.get() == "Chọn" or self.var_major.get() == "Chọn" or self.var_year.get() == "Chọn" or self.var_semester.get() == "Chọn" or self.var_ID.get()=="" or self.var_class.get()=="" or self.var_name.get() =="" or self.var_CCCD.get() =="" or self.var_gender.get() =="Chọn" or self.var_dob.get() =="" or self.var_email.get() =="" or self.var_mobile.get() =="" or self.var_address.get() =="":
            messagebox.showerror("Error","Vui lòng điền vào tất cả các trường là bắt buộc!",parent=self.root)
        else:
            try:

                conn = mysql.connector.connect(user='root', password='19112002', host='localhost', database='face_recognition', port=3306)
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                my_result = my_cursor.fetchall()
                id=0
                for x in my_result:
                    id+=1

                my_cursor.execute("update student set major=%s, he_dao_tao=%s,year=%s, semester=%s, name=%s, class=%s, gender=%s, email=%s, cccd=%s, dob=%s, phone=%s, address=%s, photo_sample=%s where student_id=%s", (
                        self.var_major.get(),
                        self.var_he_dao_tao.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_name.get(),
                        self.var_class.get(),
                        self.var_gender.get(),
                        self.var_email.get(),
                        self.var_CCCD.get(),
                        self.var_dob.get(),
                        self.var_mobile.get(),
                        self.var_address.get(),
                        self.var_radio.get(), 
                        self.var_ID.get()== id +1
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #==================================================== Open CV ================================================================#
                
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_croped(img):
                    # chuyen sang anh xam
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

                    for (x, y, w, h) in faces:
                        face_croped = img[y:y+h, x:x+h]
                        return face_croped
                
                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_croped(my_frame) is not None:
                        img_id +=1

                        face = cv2.resize(face_croped(my_frame), (500, 500))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_path = "data_img/student." +str(id) + "." +str(img_id) +".jpg"
                        cv2.imwrite(file_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX,2, (0,255), 2)
                        cv2.imshow("Capture Images", face)

                    if cv2.waitKey(1) == 13 or int(img_id)== 100:
                        break
                
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Đã hoàn tất tạo tập dữ liệu!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root) 


        #================================ Right label frame down ================================
        #right_label_frame_down = LabelFrame(main_frame, bd=2, bg = "white", relief=RIDGE, text="Quản Lý lớp học",font=("verdana",20,"bold"),fg="red")
        #right_label_frame_down.place(x = main_frame.winfo_screenwidth()/ 2 +20, y= 480, width=main_frame.winfo_screenwidth()/ 2 -30, height= 460 )

if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()