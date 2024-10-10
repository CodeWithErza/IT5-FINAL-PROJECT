from tkinter import *
from PIL import Image, ImageTk  
from tkinter import ttk
import random
import msql.connector
from tkinter import messagebox
import os

class Roombooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Reservation System")
        self.root.geometry("1135x550+220+220")
        
        #==============Variable==============
        self.var_conatct=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal =StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()
        
        #==============Titles================
        # Title Label
        title = Label(self.root, text="ROOM BOOKING DETAILS", font=("times new roman", 18, "bold"), bg="#89b0a4", fg="#f7e7ce")
        title.place(x=0, y=0, width=1295, height=50)
        
         
        #================Logo================
        # Try to load image
        
        try:
            img2 = Image.open("logo.jpeg")
            img2 = img2.resize((100, 40), Image.LANCZOS)
            self.photoimg2 = ImageTk.PhotoImage(img2)

            lblimg2 = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
            lblimg2.place(x=5, y=2, width=105, height=50)
        except FileNotFoundError:
            print("Image file not found. Please check the path for the logo image.")
            lblimg2 = Label(self.root, text="Logo", font=("times new roman", 18, "bold"), bg="#89b0a4", fg="#f7e7ce")
            lblimg2.place(x=5, y=2, width=105, height=50)
            
                       
        # ======================= Frames ====================================
        # Label Frame for Room Booking Details
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Roombooking Details", font=("arial", 12, "bold"),  padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=490, )
    
        # Label Frame for Room Booking Details
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Room Booking Details", font=("arial", 12, "bold"), bg="#89b0a4", fg="#f7e7ce", padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=490)
        
        # ======================= Labels and  Entry =========================
        # Customer contact
        lbl_cust_contact = Label(labelframeleft, text="Customer Contact:", font=("arial", 12, "bold"), bg="#89b0a4", fg="white", padx=2, pady=6)
        lbl_cust_contact.grid(row=0, column=0, sticky=W)

        enty_contact = ttk.Entry(labelframeleft, textvariable = self.var_conatct, font=("arial", 13, "bold"), width=20)
        enty_contact.grid(row=0, column=1, sticky=W)
        
        # =========== Fetch Data button ===========
        
        btnFetchData = Button(labelframeleft, command=self.Fetch_contact, text="Fetch Data", font=("arial", 8, "bold"), bg="#0F3325", fg="white", width=8)
        btnFetchData.place(x=347, y=4)

        # Check-in Date
        check_in_date = Label(labelframeleft, font=("arial", 12, "bold"), bg="#89b0a4", fg="white", text="Check-in Date:", padx=2, pady=6)
        check_in_date.grid(row=1, column=0, sticky=W)

        txtcheck_in_date = ttk.Entry(labelframeleft, textvariable = self.var_checkin, font=("arial", 13, "bold"), width=29)
        txtcheck_in_date.grid(row=1, column=1)

        # Check-out Date
        lbl_Check_out = Label(labelframeleft, font=("arial", 12, "bold"), bg="#89b0a4", fg="white", text="Check-out Date:", padx=2, pady=6)
        lbl_Check_out.grid(row=2, column=0, sticky=W)

        txt_Check_out = ttk.Entry(labelframeleft, textvariable = self.var_checkout, font=("arial", 13, "bold"), width=29)
        txt_Check_out.grid(row=2, column=1)
        
        # Room Type
        label_RoomType = Label(labelframeleft, font=("arial", 12, "bold"), bg="#89b0a4", fg="white", text="Room Type:", padx=2, pady=6)
        label_RoomType.grid(row=3, column=0, sticky=W)

        combo_RoomType = ttk.Combobox(labelframeleft, textvariable = self.var_roomtype, font=("arial", 12, "bold"), width=27, state="readonly")
        combo_RoomType["value"] = ("Single", "Double", "Luxury")
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3, column=1)

        # Available Room
        lblRoomAvailable = Label(labelframeleft, font=("arial", 12, "bold"), bg="#89b0a4", fg="white", text="Available Room:", padx=2, pady=6)
        lblRoomAvailable.grid(row=4, column=0, sticky=W)

        txtRoomAvailable = ttk.Entry(labelframeleft, textvariable = self.var_roomavailable, font=("arial", 13, "bold"), width=29)
        txtRoomAvailable.grid(row=4, column=1)

        # Meal
        lblMeal = Label(labelframeleft, font=("arial", 12, "bold"), bg="#89b0a4", fg="white", text="Meal:", padx=2, pady=6)
        lblMeal.grid(row=5, column=0, sticky=W)

        txtMeal = ttk.Entry(labelframeleft, textvariable = self.var_meal, font=("arial", 13, "bold"), width=29)
        txtMeal.grid(row=5, column=1)

        # No Of Days
        lblNoOfDays = Label(labelframeleft, font=("arial", 12, "bold"), bg="#89b0a4", fg="white", text="No Of Days:", padx=2, pady=6)
        lblNoOfDays.grid(row=6, column=0, sticky=W)

        txtNoOfDays = ttk.Entry(labelframeleft, textvariable = self.var_noofdays, font=("arial", 13, "bold"), width=29)
        txtNoOfDays.grid(row=6, column=1)
        
        # Paid Tax
        lblPaidTax = Label(labelframeleft, font=("arial", 12, "bold"), bg="#89b0a4", fg="white", text="Paid Tax:", padx=2, pady=6)
        lblPaidTax.grid(row=7, column=0, sticky=W)

        txtPaidTax = ttk.Entry(labelframeleft, textvariable = self.var_paidtax, font=("arial", 13, "bold"), width=29)
        txtPaidTax.grid(row=7, column=1)

        # Sub Total
        lblSubTotal = Label(labelframeleft, font=("arial", 12, "bold"), bg="#89b0a4", fg="white", text="Sub Total:", padx=2, pady=6)
        lblSubTotal.grid(row=8, column=0, sticky=W)

        txtSubTotal = ttk.Entry(labelframeleft, textvariable = self.var_actualtotal, font=("arial", 13, "bold"), width=29)
        txtSubTotal.grid(row=8, column=1)

        # Total Cost
        lblTotalCost = Label(labelframeleft, font=("arial", 12, "bold"), bg="#89b0a4", fg="white", text="Total Cost:", padx=2, pady=6)
        lblTotalCost.grid(row=9, column=0, sticky=W)

        txtTotalCost = ttk.Entry(labelframeleft, font=("arial", 13, "bold"), width=29)
        txtTotalCost.grid(row=9, column=1)
        
        # ======================= Button Frame ===============================
        btnBill = Button(labelframeleft, text="Bill", font=("arial", 11, "bold"), bg="#0F3325", fg="white", width=10)
        btnBill.grid(row=10, column=0, padx=1, sticky=W)
        
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btnAdd = Button(btn_frame, text="Add", font=("arial", 11, "bold"), bg="#0F3325", fg="white", width=10)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text="Update", font=("arial", 11, "bold"), bg="#0F3325", fg="white", width=10)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete", font=("arial", 11, "bold"), bg="#0F3325", fg="white", width=10)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset", font=("arial", 11, "bold"), bg="#0F3325", fg="white", width=10)
        btnReset.grid(row=0, column=3, padx=1)
        
        
        # ========================= Background image =========================
        try:
            img3 = Image.open(r"C:\\Users\\HUAWEI\\OneDrive\Documents\\GitHub\\IT5-FINAL-PROJECT\\hotel_bedroom.jpg")
            img3 = img3.resize((430, 300), Image.LANCZOS)
            self.photoimg3 = ImageTk.PhotoImage(img3)

            lblimg = Label(self.root, image=self.photoimg3, bd=0, relief=RIDGE)
            lblimg.place(x=700, y=60)  # Example position. Adjust x and y as needed.
        except Exception as e:
            print(f"Error loading image: {e}")
           
            lblimg = Label(self.root, text="Image not available", font=("arial", 12, "bold"), bg="lightgrey")
            lblimg.place(x=300, y=50)  
        
        # ========================= Table Frame Search System =========================
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And Search System", font=("arial", 12, "bold"))
        Table_Frame.place(x=435, y=280, width=860, height=260)

        lblSearchBy = Label(Table_Frame, font=("arial", 12, "bold"), text="Search By:",  bg="#89b0a4", fg="white")
        lblSearchBy.grid(row=0, column=0, sticky=W, padx=2)

        self.search_var = StringVar()
        combo_Search = ttk.Combobox(Table_Frame, textvariable=self.search_var, font=("arial", 12, "bold"), width=15, state="readonly")
        combo_Search["values"] = ("Contact", "Room")
        combo_Search.current(0)
        combo_Search.grid(row=0, column=1, padx=2)

        self.txt_search = StringVar()
        txtSearch = ttk.Entry(Table_Frame, textvariable=self.txt_search, font=("arial", 13, "bold"), width=23)
        txtSearch.grid(row=0, column=2, padx=2)

        btnSearch = Button(Table_Frame, text="Search", font=("arial", 11, "bold"), bg="#0F3325", fg="white", width=10)
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(Table_Frame, text="Show All", font=("arial", 11, "bold"), bg="#0F3325", fg="white", width=10)
        btnShowAll.grid(row=0, column=4, padx=1)
        
        # ===================== Show Data Table =====================
        details_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=680, height=180)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        # Corrected column names to match
        self.room_table = ttk.Treeview(details_table, columns=("contact", "checkin", "checkout", "roomtype", "roomavailable", "meal", "noofdays"),  
                                xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set, )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=LEFT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        # Table headings
        self.room_table.heading("contact", text="Contact")  
        self.room_table.heading("checkin", text="Check-in")
        self.room_table.heading("checkout", text="Check-out")
        self.room_table.heading("roomtype", text="Room Type")
        self.room_table.heading("roomavailable", text="Room No")
        self.room_table.heading("meal", text="Meal")
        self.room_table.heading("noofdays", text="No of Days")

        self.room_table["show"] = "headings"

        # Change "mobile" to "contact"
        self.room_table.column("contact", width=160)  # Corrected here
        self.room_table.column("checkin", width=80)
        self.room_table.column("checkout", width=80)
        self.room_table.column("roomtype", width=160)
        self.room_table.column("roomavailable", width=100)
        self.room_table.column("meal", width=100)
        self.room_table.column("noofdays", width=60)

        # Pack the Treeview widget into the details_table frame
        self.room_table.pack(fill=BOTH, expand=True)
        
    # ==================== All Data Fetch =======================
    def Fetch_contact(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please enter Contact Number", parent=self.root)
        else:
            conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="Test@123",
            database="management"
        )
        my_cursor = conn.cursor()
        query = "SELECT Name FROM customer WHERE Mobile=%s"
        value = (self.var_contact.get(),)
        my_cursor.execute(query, value)
        row = my_cursor.fetchone()
        
        if row is None:
            messagebox.showerror("Error", "This number Not Found", parent=self.root)
        else:
            conn.commit()
            conn.close()
            
            showDataframe = Frame(self.root, bd=4, relief=RIDGE, padx=2)
            showDataframe.place(x=455, y=55, width=300, height=180)
            # =================== Name =====================
            lblName = Label(showDataframe, text="Name:", font=("arial", 12, "bold"))
            lblName.place(x=0, y=0)
            lbl = Label(showDataframe, text=row[0], font=("arial", 12, "bold"))
            lbl.place(x=90,y=0)


             # ================== Gender ===================
            conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="Test@123",
            database="management")

            my_cursor = conn.cursor()
            query = "SELECT Gender FROM customer WHERE Mobile=%s"
            value = (self.var_contact.get(),)  # Corrected from self.var_conatct.get to self.var_contact.get()
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            lblGender = Label(showDataframe, text="Gender:", font=("arial", 12, "bold"))
            lblGender.place(x=0, y=30)

            lblGenderValue = Label(showDataframe, text=row[0] if row else "N/A", font=("arial", 12, "bold"))  # Added check for row
            lblGenderValue.place(x=90, y=30)

            # ===================== Email ===================
            conn = mysql.connector.connect(
             host="localhost",
            user="root",
            password="Test@123",
            database="management" )

            my_cursor = conn.cursor()
            query = "SELECT Email FROM customer WHERE Mobile=%s"
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            lblEmail = Label(showDataframe, text="Email:", font=("arial", 12, "bold"))
            lblEmail.place(x=0, y=60)

            lblEmailValue = Label(showDataframe, text=row[0] if row else "N/A", font=("arial", 12, "bold"))  # Added check for row
            lblEmailValue.place(x=90, y=60)

            # ========== Nationality ==========
            conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Test@123",
            database="management")
            my_cursor = conn.cursor()
            query = "SELECT Nationality FROM customer WHERE Mobile=%s"
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            lblNationality = Label(showDataframe, text="Nationality:", font=("arial", 12, "bold"))
            lblNationality.place(x=0, y=90)

            lblNationalityValue = Label(showDataframe, text=row[0] if row else "N/A", font=("arial", 12, "bold"))
            lblNationalityValue.place(x=90, y=90)

            # ========== Address ==========
            conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Test@123",
            database="management")

            my_cursor = conn.cursor()
            query = "SELECT Address FROM customer WHERE Mobile=%s"
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            lblAddress = Label(showDataframe, text="Address:", font=("arial", 12, "bold"))
            lblAddress.place(x=0, y=120)

            lblAddressValue = Label(showDataframe, text=row[0] if row else "N/A", font=("arial", 12, "bold"))
            lblAddressValue.place(x=90, y=120)

            conn.close() 
        
if __name__ == "__main__":
    root = Tk()
    obj = Roombooking(root)
    root.mainloop()