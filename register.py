from tkinter import*
from tkinter import Tk, Label, Frame, Button, Entry, RIDGE
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        # variables
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_conpass=StringVar()


        # Background Image
         #self.bg = ImageTk.PhotoImage(file=r"C:\Users\Dell\Desktop\hotel_management_system\images\slide 4.jpg")
         #bg_lbl = Label(self.root, image=self.bg)
        #bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # Leftside Image
        #self.bg = ImageTk.PhotoImage(file=r"C:\Users\Dell\Desktop\hotel_management_system\images\slide 4.jpg")
        #bg_lbl = Label(self.root, image=self.bg)
        #bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # Main Frame
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)

        # Labels and Entries
        # row 1
        # First Name
        fname = Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white")
        fname.place(x=50, y=80)

        fname_entry = ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman", 15))
        fname_entry.place(x=50, y=110, width=250)

        # Last Name
        l_name = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white")
        l_name.place(x=370, y=80)

        self.txt_lname = ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman", 15))
        self.txt_lname.place(x=370, y=110, width=250)

        # Contact No
        contact = Label(frame, text="Contact No", font=("times new roman", 15, "bold"), bg="white")
        contact.place(x=50, y=150)

        self.txt_contact = ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman", 15))
        self.txt_contact.place(x=50, y=180, width=250)

        # Email
        email = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white")
        email.place(x=370, y=150)

        self.txt_email = ttk.Entry(frame,textvariable=self.var_email,font=("times new roman", 15))
        self.txt_email.place(x=370, y=180, width=250)

        # Select Security Question
        security_Q = Label(frame, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white")
        security_Q.place(x=50, y=220)

        self.combo_security_Q = ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman", 15), state="readonly")
        self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your Favourite Food")
        self.combo_security_Q.current(0)  # Set default value to "Select"
        self.combo_security_Q.place(x=50, y=250, width=250)

        # Security Answer
        security_A = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white")
        security_A.place(x=370, y=220)

        self.txt_security = ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman", 15))
        self.txt_security.place(x=370, y=250, width=250)

        # Password
        pswd = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white")
        pswd.place(x=50, y=290)

        self.txt_pswd = ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman", 15))
        self.txt_pswd.place(x=50, y=320, width=250)

        # Confirm Password
        confirm_pswd = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white")
        confirm_pswd.place(x=370, y=290)

        self.txt_confirm_pswd = ttk.Entry(frame,textvariable=self.var_conpass,font=("times new roman", 15))
        self.txt_confirm_pswd.place(x=370, y=320, width=250)
       

        # Check Button
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree the Terms and Conditions",font=("times new roman", 15, "bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)

        # Buttons
        img = Image.open(r"C:\Users\Dell\Desktop\hotel_management_system\images\reg 1.webp")
        img = img.resize((200, 50), Image.LANCZOS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(frame, image=self.photoimage,command=self.register_data,borderwidth=0, cursor="hand2")
        b1.place(x=10, y=420, width=200)

        # Load and resize "Login" button image
        img_login = Image.open(r"C:\Users\Dell\Desktop\hotel_management_system\images\login 2.jpg")
        img_login = img_login.resize((200, 50), Image.LANCZOS)
        self.photoimage_login = ImageTk.PhotoImage(img_login)

        # Create "Login" button
        b_login = Button(frame, image=self.photoimage_login, command=self.return_login,borderwidth=0, cursor="hand2")
        b_login.place(x=380, y=420,width=200)

        # Function Declaration
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_conpass.get():
            messagebox.showerror("Error","Password and Confirm Password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and conditions")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Atharva@2001",database="management")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
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
                messagebox.showinfo("Success","Registration Successfully")

    
    def return_login(self):
        self.root.destroy()









if __name__ == "__main__":
    root = Tk()
    obj = Register(root)
    root.mainloop()