from tkinter import messagebox

class Logout:
    def __init__(self, window):
        self.window = window

    def logout(self):
        # Close all windows in the application
        for window in self.window.winfo_children():
            window.destroy()

        # Show a message indicating successful logout
        messagebox.showinfo("Logout", "Logged out successfully.",parent=self.root)

        # Optionally, you can redirect to the login page here or perform any other actions needed after logout
