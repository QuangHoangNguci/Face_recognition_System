from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import os
from tkinter import messagebox

import PIL

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.state('zoomed')
        self.root.title("Hệ thống quản lý điểm danh sử dụng nhận dạng khuôn mặt")
    
    # Image labels setting start
        #image header
        #imgae 1
        img_1 = Image.open(r"Images_GUI/banner-BK.jpg")
        img_1 = img_1.resize((root.winfo_screenwidth(), 130), Image.LANCZOS)
        self.photoimg= ImageTk.PhotoImage(img_1)

        #set image lable
        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=root.winfo_screenwidth(), height=130)


        #bg image
        bg_1 = Image.open(r"/Users/QuangHoang/Documents/Face_recognition_system/Images_GUI/bg4.png")
        remaining_height = root.winfo_screenheight() - 130 
        bg_1 = bg_1.resize((root.winfo_screenwidth(), remaining_height), PIL.Image.LANCZOS)
        self.photobg1 = ImageTk.PhotoImage(bg_1)

        #set bg
        bg_img = Label(self.root, image= self.photobg1)
        bg_img.place(x=0, y=130, width=root.winfo_screenwidth(), height=remaining_height)

        # set title section
        title_lb1 = Label(bg_img, text="HUST - Hệ thống điểm danh nhận dạng khuôn mặt", font=("times new roman",35,"bold"),bg="navyblue",fg="white")
        title_lb1.place(x=0, y=0, width=root.winfo_screenwidth(), height=50)


    #***********************************************************************************************************************#
    # Tạo button ở hàng đầu
        #button 1 - student detail
        std_img_button = Image.open(r"/Users/QuangHoang/Documents/Face_recognition_system/Images_GUI/std1.jpg")
        std_img_button = std_img_button.resize((180, 180), Image.LANCZOS)
        self.std_img1 = ImageTk.PhotoImage(std_img_button)

        std_button_1 = Button(bg_img,command= self.student_pannels ,image= self.std_img1, cursor="hand2")
        std_button_1.place(x=250, y=170, width=180, height=180)

        std_button_1_1 =Button(bg_img,command= self.student_pannels , text="Sinh viên", cursor="hand2", font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_button_1_1.place(x=250, y=350, width=180, height=40)

        #button 2 - Nhận diện
        dec_img_button = Image.open(r"/Users/QuangHoang/Documents/Face_recognition_system/Images_GUI/det1.jpg")
        dec_img_button = dec_img_button.resize((180, 180), Image.LANCZOS)
        self.dec_img_1 = ImageTk.PhotoImage(dec_img_button)

        dec_button_1 = Button(bg_img,command=self.face_rec, image= self.dec_img_1, cursor="hand2")
        dec_button_1.place(x=650, y=170, width=180, height=180)

        dec_button_1_1 =Button(bg_img, text="Nhận Diện", cursor="hand2", font=("tahoma",15,"bold"),bg="white",fg="navyblue", height=40, width=180)
        dec_button_1_1.place(x=650, y=350, width=180, height=40)

        #button 3 - Điểm danh
        att_img_button = Image.open(r"/Users/QuangHoang/Documents/Face_recognition_system/Images_GUI/att.jpg")
        att_img_button = att_img_button.resize((180, 180), Image.LANCZOS)
        self.att_img_1 = ImageTk.PhotoImage(att_img_button)

        att_button_1 = Button(bg_img,command= self.attendance_pannels ,image=self.att_img_1, cursor="hand2")
        att_button_1.place(x=1050, y=170, width=180, height=180)

        att_button_1_1 = Button(bg_img,command= self.attendance_pannels , text="Điểm Danh",font=("tahoma",15,"bold"),bg="white",fg="navyblue", height=40, width=180, cursor="hand2")
        att_button_1_1.place(x=1050, y= 350, height=40, width=180)

        #button 4 - Hỗ trợ
        sup_img_button = Image.open(r"/Users/QuangHoang/Documents/Face_recognition_system/Images_GUI/hlp.jpg")
        sup_img_button = sup_img_button.resize((180, 180), Image.LANCZOS)
        self.sup_img_1 = ImageTk.PhotoImage(sup_img_button)

        sup_button_1 = Button(bg_img,command= self.help_support, image=self.sup_img_1, cursor="hand2")
        sup_button_1.place(x=1450, y=170, width=180, height=180)

        sup_button_1_1 = Button(bg_img,command= self.help_support, text="Hỗ trợ", cursor="hand2", font=("tahoma",15,"bold"),bg="white",fg="navyblue", height=40, width=180)
        sup_button_1_1.place(x=1450, y=350, width=180, height=40)
    # Tạo buttons ở hàng 2
        # Button 5 - tải data
        load_img_button = Image.open(r"/Users/QuangHoang/Documents/Face_recognition_system/Images_GUI/tra1.jpg")
        load_img_button = load_img_button.resize((180, 180), Image.LANCZOS)
        self.load_data_button = ImageTk.PhotoImage(load_img_button)

        load_img_button_1 = Button(bg_img, command=self.train_pannels, image=self.load_data_button, cursor="hand2")
        load_img_button_1.place(x=250, y=550, height=180, width=180)

        load_img_button_1_1 = Button(bg_img, command=self.train_pannels, text="Tải Data", font=("tahoma",15,"bold"),bg="white",fg="navyblue", height=40, width=180, cursor="hand2")
        load_img_button_1_1.place(x=250, y=730, width=180, height=40)

        # Button 6 - Dataset
        data_img_button = Image.open(r"/Users/QuangHoang/Documents/Face_recognition_system/Images_GUI/dataset.jpg")
        data_img_button = data_img_button.resize((180, 180), Image.LANCZOS)
        self.data_button = ImageTk.PhotoImage(data_img_button)

        data_img_button_1 = Button(bg_img, command= self.open_img, image= self.data_button, cursor="hand2")
        data_img_button_1.place(x=650, y=550, width=180, height=180)

        data_img_button_1_1 = Button(bg_img,command= self.open_img, text="Dataset",cursor="hand2", font=("tahoma",15,"bold"),bg="white",fg="navyblue", height=40, width=180)
        data_img_button_1_1.place(x=650 ,y=730, width=180, height=40)

        # Button 7 - Developers
        dev_img_button = Image.open(r"/Users/QuangHoang/Documents/Face_recognition_system/Images_GUI/dev.jpg")
        dev_img_button = dev_img_button.resize((180, 180), Image.LANCZOS)
        self.dev_button = ImageTk.PhotoImage(dev_img_button)

        dev_img_button_1 = Button(bg_img, command=self.develop_pannels, image=self.dev_button, cursor="hand2")
        dev_img_button_1.place(x= 1050, y= 550, width=180, height=180)

        dev_img_button_1_1 = Button(bg_img,command=self.develop_pannels, text="Developers", font=("tahoma",15,"bold"),bg="white",fg="navyblue", height=40, width=180, cursor="hand2")
        dev_img_button_1_1.place(x=1050, y=730, width=180, height=40)

        # Button 8 - Exit
        exit_img_button = Image.open(r"/Users/QuangHoang/Documents/Face_recognition_system/Images_GUI/exi.jpg")
        exit_img_button = exit_img_button.resize((180, 180), Image.LANCZOS)
        self.exit_button = ImageTk.PhotoImage(exit_img_button)

        exit_button_1 = Button(bg_img,command=self.Close, image=self.exit_button, cursor="hand2")
        exit_button_1.place(x=1450, y=550, width=180, height=180)

        exit_button_1_1 = Button(bg_img,command=self.Close, text="Exit", font=("tahoma",15,"bold"),bg="white",fg="navyblue", height=40, width=180, cursor="hand2")
        exit_button_1_1.place(x=1450, y=730, width=180, height=40)

    #***********************************************************************************************************************#
    #============================ Functions for Button==================================================#
    def student_pannels(self):
        self.new_window = Toplevel(self.root)
        pass

    def train_pannels(self):
        self.new_window = Toplevel(self.root)
        pass

    def face_rec(self):
        self.new_window = Toplevel(self.root)
        pass

    def attendance_pannels(self):
        self.new_window = Toplevel(self.root)
        pass

    def develop_pannels(self):
        self.new_window = Toplevel(self.root)
        pass

    def help_support(self):
        self.new_window = Toplevel(self.root)
        pass

    def open_img(self):
        os.startfile("data_img")

    def Close(self):
        result = messagebox.askquestion("Exit", "Bạn có muốn thoát chương trình?")
        if result == "yes":
            self.root.destroy()






if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()



