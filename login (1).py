from tkinter import Tk, Label, Frame, Button, Entry, RIDGE, StringVar, IntVar, Checkbutton,Toplevel
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from tkinter import *
from PIL import Image, ImageTk
from customer import Cust_Win
from room import Roombooking
from details import DetailsRoom


def main():
    win = Tk()
    app = Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        # Load background image
        img1 = Image.open(r"C:\Users\Dell\Desktop\hotel_management_system\images\slide.jpg")
        self.bg = ImageTk.PhotoImage(img1)
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        # Create a frame
        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=340, height=450)
      
        # Load and resize the login icon image
        img2 = Image.open(r"C:\Users\Dell\Desktop\hotel_management_system\images\login icon.jpg")
        img2 = img2.resize((100, 100), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img2)
        lblimg1 = Label(image=self.photoimage1, bg="black", borderwidth=0)
        lblimg1.place(x=730, y=175, width=100, height=100)

        # Add 'Get Started' label
        get_str = Label(frame, text="Get Started", font=("times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=95, y=100)

        # Username label and entry
        username = Label(frame, text="Username", font=("times new roman", 15, "bold"), fg="white", bg="black")
        username.place(x=40, y=155)

        self.txtuser = Entry(frame, font=("times new roman", 15), fg="black", bg="white")
        self.txtuser.place(x=40, y=180, width=270)

        # Password label and entry
        password = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=40, y=225)

        self.txtpass = Entry(frame, font=("times new roman", 15), fg="black", bg="white", show='*')
        self.txtpass.place(x=40, y=250, width=270)

        # Login button
        loginbtn = Button(frame, text="Login", command=self.login, font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        loginbtn.place(x=110, y=300, width=120, height=35)

        # Register button
        registerbtn = Button(frame, text="New User Register", command=self.register_window, font=("times new roman", 10, "bold"), borderwidth=0, relief=RIDGE, fg="white", bg="black", activeforeground="white", activebackground="black")
        registerbtn.place(x=15, y=350, width=160)

        # Forget Password button
        forgetbtn = Button(frame, text="Forget Password",command=self.forgot_password_window ,font=("times new roman", 10, "bold"), borderwidth=0, relief=RIDGE, fg="white", bg="black", activeforeground="white", activebackground="black")
        forgetbtn.place(x=10, y=370, width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
     
    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.txtuser.get() == "admin" and self.txtpass.get() == "admin":
            messagebox.showinfo("Success", "Welcome to Hotel Management System")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Atharva@2001",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                        self.txtuser.get(),
                                                                                        self.txtpass.get()
                                                                                    ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only registered user")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=HotelManagementSystem(self.root)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

    def login_window(self):
        self.root.destroy()



    # ===========================Reset password==========================================
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select the Security Question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Atharva@2001",database="management")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the correct Answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)
                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset,please login with the new password",parent=self.root2)
                self.root2.destroy()

    # ============================Forgot Password Window===================================
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the Email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Atharva@2001",database="management")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
           # print(row)

        if row == None:
          messagebox.showerror("Error", "Please enter a valid Username")
        else:
           conn.close()
           self.root2 = Toplevel()
           self.root2.title("Forgot Password")
           self.root2.geometry("340x450+610+170")

        l = Label(self.root2, text="Forgot Password", font=("times new roman", 20, "bold"), fg="red", bg="white")
        l.place(x=0, y=10, relwidth=1)

    # Select Security Question
        security_Q = Label(self.root2, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white")
        security_Q.place(x=50, y=60)

        self.combo_security_Q = ttk.Combobox(self.root2, font=("times new roman", 15), state="readonly")
        self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your Favorite Food")
        self.combo_security_Q.current(0)  # Set default value to "Select"
        self.combo_security_Q.place(x=50, y=90, width=250)

    # Security Answer
        security_A = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), bg="white")
        security_A.place(x=50, y=140)

        self.txt_security = ttk.Entry(self.root2, font=("times new roman", 15))
        self.txt_security.place(x=50, y=170, width=250)

    # New Password
        new_password = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), bg="white")
        new_password.place(x=50, y=220)

        self.txt_newpass = ttk.Entry(self.root2, font=("times new roman", 15))
        self.txt_newpass.place(x=50, y=250, width=250)

        btn = Button(self.root2, text="Reset", font=("times new roman", 15, "bold"), fg="white", bg="green")
        btn.place(x=100, y=290)

            

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        # variables
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_conpass = StringVar()

        # Main Frame
        frame = Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=800, height=550)

        register_lbl = Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="darkgreen", bg="white")
        register_lbl.place(x=20, y=20)

        # Labels and Entries
    
        # First Name
        fname = Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white")
        fname.place(x=50, y=80)

        fname_entry = ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15))
        fname_entry.place(x=50, y=110, width=250)

        # Last Name
        l_name = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white")
        l_name.place(x=370, y=80)

        self.txt_lname = ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 15))
        self.txt_lname.place(x=370, y=110, width=250)

        # Contact No
        contact = Label(frame, text="Contact No", font=("times new roman", 15, "bold"), bg="white")
        contact.place(x=50, y=150)

        self.txt_contact = ttk.Entry(frame, textvariable=self.var_contact, font=("times new roman", 15))
        self.txt_contact.place(x=50, y=180, width=250)

        # Email
        email = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white")
        email.place(x=370, y=150)

        self.txt_email = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15))
        self.txt_email.place(x=370, y=180, width=250)

        # Select Security Question
        security_Q = Label(frame, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white")
        security_Q.place(x=50, y=220)

        self.combo_security_Q = ttk.Combobox(frame, textvariable=self.var_securityQ, font=("times new roman", 15), state="readonly")
        self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your Favourite Food")
        self.combo_security_Q.current(0)  # Set default value to "Select"
        self.combo_security_Q.place(x=50, y=250, width=250)

        # Security Answer
        security_A = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white")
        security_A.place(x=370, y=220)

        self.txt_security = ttk.Entry(frame, textvariable=self.var_securityA, font=("times new roman", 15))
        self.txt_security.place(x=370, y=250, width=250)

        # Password
        pswd = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white")
        pswd.place(x=50, y=290)

        self.txt_pswd = ttk.Entry(frame, textvariable=self.var_pass, font=("times new roman", 15))
        self.txt_pswd.place(x=50, y=320, width=250)

        # Confirm Password
        confirm_pswd = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white")
        confirm_pswd.place(x=370, y=290)

        self.txt_confirm_pswd = ttk.Entry(frame, textvariable=self.var_conpass, font=("times new roman", 15))
        self.txt_confirm_pswd.place(x=370, y=320, width=250)

        # Check Button
        self.var_check = IntVar()
        checkbtn = Checkbutton(frame, variable=self.var_check, text="I Agree the Terms and Conditions", font=("times new roman", 15, "bold"), onvalue=1, offvalue=0)
        checkbtn.place(x=50, y=380)

        # Register Button
        img = Image.open(r"C:\Users\Dell\Desktop\hotel_management_system\images\reg 1.webp")
        img = img.resize((200, 50), Image.LANCZOS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(frame, image=self.photoimage, command=self.register_data, borderwidth=0, cursor="hand2")
        b1.place(x=10, y=420, width=200)

        # Load and resize "Login" button image
        img_login = Image.open(r"C:\Users\Dell\Desktop\hotel_management_system\images\login 2.jpg")
        img_login = img_login.resize((200, 50), Image.LANCZOS)
        self.photoimage_login = ImageTk.PhotoImage(img_login)
        b_login = Button(frame, image=self.photoimage_login,command=self.return_login, borderwidth=0, cursor="hand2")
        b_login.place(x=380, y=420, width=200)

   # Function Declaration
    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "All fields are required")
        elif self.var_pass.get() != self.var_conpass.get():
            messagebox.showerror("Error", "Password and Confirm Password must be same")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree to our terms and conditions")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="Atharva@2001", database="management")
                my_cursor = conn.cursor()
                query = "select * from register where email=%s"
                value = (self.var_email.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                if row != None:
                    messagebox.showerror("Error", "User already exists, please try another email")
                else:
                    my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)", (
                        self.var_fname.get(),
                        self.var_lname.get(),
                        self.var_contact.get(),
                        self.var_email.get(),
                        self.var_securityQ.get(),
                        self.var_securityA.get(),
                        self.var_pass.get()
                    ))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success", "Registration Successfully")
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}")

    


    def return_login(self):
        self.root.destroy()

    



class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

        # ==================1st image=======================
        img1 = Image.open(r"C:\Users\Dell\Desktop\hotel_management_system\images\hotel1.jpg")
        img1 = img1.resize((1550, 140), Image.LANCZOS)  # Resize the image to the required dimensions
        self.photoimg1 = ImageTk.PhotoImage(img1)  # Convert the image to a Tkinter-compatible image

        lblimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1550, height=140)

        # ====================logo==========================
        img2=Image.open(r"C:\Users\Dell\Desktop\hotel_management_system\images\logohotel1.png")
        img2=img2.resize((230, 140), Image.LANCZOS)  # Resize the image to the required dimensions
        self.photoimg2=ImageTk.PhotoImage(img2)  # Convert the image to a Tkinter-compatible image

        lblimg = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=230, height=140)

        # ====================title===========================
        lbl_title = Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman", 40, "bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)

        # =====================main frame=====================
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)

        # =====================menu===========================
        lbl_title = Label(self.root,text="MENU",font=("times new roman", 20, "bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=190,width=230)

        # =====================btn frame======================
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=190)

        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=22,font=("times new roman", 14, "bold"), bg="black", fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)

        
        room_btn=Button(btn_frame,text="ROOM",command=self.roombooking,width=22,font=("times new roman", 14, "bold"), bg="black", fg="gold",bd=0,cursor="hand1")
        room_btn.grid(row=1,column=0,pady=1)

        
        details_btn=Button(btn_frame,text="DETAILS",command=self.details_room,width=22,font=("times new roman", 14, "bold"), bg="black", fg="gold",bd=0,cursor="hand1")
        details_btn.grid(row=2,column=0,pady=1)

        
        report_btn=Button(btn_frame,text="REPORT",width=22,font=("times new roman", 14, "bold"), bg="black", fg="gold",bd=0,cursor="hand1")
        report_btn.grid(row=3,column=0,pady=1)

        
        logout_btn=Button(btn_frame,text="LOGOUT",width=22,font=("times new roman", 14, "bold"), bg="black", fg="gold",bd=0,cursor="hand1")
        logout_btn.grid(row=4,column=0,pady=1)


       # ========================right side image=================
        img3=Image.open(r"C:\Users\Dell\Desktop\hotel_management_system\images\slide1.jpg")
        img3=img3.resize((1310, 590), Image.LANCZOS)  # Resize the image to the required dimensions
        self.photoimg3=ImageTk.PhotoImage(img3)  # Convert the image to a Tkinter-compatible image

        lblimg1= Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg1.place(x=225, y=0, width=1310, height=590)

       # =======================down images=======================
        img4=Image.open(r"C:\Users\Dell\Desktop\hotel_management_system\images\slide2.jpg")
        img4=img4.resize((230, 210), Image.LANCZOS)  # Resize the image to the required dimensions
        self.photoimg4=ImageTk.PhotoImage(img4)  # Convert the image to a Tkinter-compatible image

        lblimg = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=225, width=230, height=210)


        img5=Image.open(r"C:\Users\Dell\Desktop\hotel_management_system\images\slide3.jpg")
        img5=img5.resize((230, 190), Image.LANCZOS)  # Resize the image to the required dimensions
        self.photoimg5=ImageTk.PhotoImage(img5)  # Convert the image to a Tkinter-compatible image

        lblimg = Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=420, width=230, height=190)


    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_Win(self.new_window)

    
    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=Roombooking(self.new_window)

    def details_room(self):
        self.new_window=Toplevel(self.root)
        self.app=DetailsRoom(self.new_window)


if __name__ == "__main__":
    main()
