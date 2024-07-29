from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from datetime import datetime, timedelta

class Report:
    def __init__(self, root):
        self.root = root
        self.root.title("Room Status Report")
        self.root.geometry("1295x550+230+220")

        # Database connection
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Atharva@2001",
            database="management"
        )
        self.cursor = self.conn.cursor()

        # ==================title========================
        lbl_title = Label(self.root, text="ROOM STATUS REPORT", font=("times new roman", 18, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # ==================logo=========================
        img2 = Image.open(r"C:\Users\Dell\Desktop\hotel_management_system\images\logohotel1.png")
        img2 = img2.resize((100, 40), Image.LANCZOS)  # Resize the image to the required dimensions
        self.photoimg2 = ImageTk.PhotoImage(img2)  # Convert the image to a Tkinter-compatible image
        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=2, width=100, height=40)

        # ==================Time Period Dropdown=========================
        lbl_time_period = Label(self.root, text="Select Time Period", font=("aerial", 13, "bold"), padx=2, pady=6)
        lbl_time_period.place(x=200, y=55)

        self.var_time_period = StringVar()
        combo_time_period = ttk.Combobox(self.root, textvariable=self.var_time_period, font=("aerial", 12, "bold"), width=27, state="readonly")
        combo_time_period["value"] = ("Weekly", "Monthly")
        combo_time_period.current(0)
        combo_time_period.place(x=400, y=55)

        btnShow = Button(self.root, text="Show Report", font=("aerial", 12, "bold"), bg="black", fg="gold", command=self.fetch_data)
        btnShow.place(x=700, y=55)

        # Table Frame
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Show Room Status", font=("aerial", 12, "bold"), padx=2, pady=6)
        Table_Frame.place(x=5, y=100, width=1285, height=440)

        scroll_x = ttk.Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_Frame, orient=VERTICAL)
        self.room_table = ttk.Treeview(Table_Frame, columns=("roomno", "status"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("roomno", text="Room No")
        self.room_table.heading("status", text="Room Status")

        self.room_table["show"] = "headings"

        self.room_table.column("roomno", width=100)
        self.room_table.column("status", width=100)

        self.room_table.pack(fill=BOTH, expand=1)

    def fetch_data(self):
        time_period = self.var_time_period.get()
        today = datetime.today()

        if time_period == "Weekly":
            start_date = today - timedelta(weeks=1)
        elif time_period == "Monthly":
            start_date = today - timedelta(days=30)
        else:
            start_date = today

        try:
            # Assuming the table has columns 'room_id', 'status', and 'date'
            query = "SELECT roomno, status FROM room_status WHERE date >= %s"
            self.cursor.execute(query, (start_date,))
            rows = self.cursor.fetchall()

            if len(rows) != 0:
                self.room_table.delete(*self.room_table.get_children())
                for row in rows:
                    self.room_table.insert("", END, values=row)
                self.conn.commit()
            else:
                messagebox.showinfo("Info", "No data found for the selected time period.")
        except Exception as e:
            messagebox.showerror("Error", f"Error due to: {str(e)}")

if __name__ == "__main__":
    root = Tk()
    obj = Report(root)
    root.mainloop()
