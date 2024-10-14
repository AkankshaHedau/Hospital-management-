import tkinter as tk
from tkinter import messagebox, font
import pymysql

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = '1234567890'
DB_NAME = 'hospital_management'

def connect_db():
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

def id_exists(table, id):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM {table} WHERE id=%s", (id,))
    exists = cursor.fetchone() is not None
    cursor.close()
    db.close()
    return exists

def add_patient(patient_id, name, age, gender):
    if id_exists('patients', patient_id):
        messagebox.showerror("Error", "Patient ID already exists.")
        return
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO patients (id, name, age, gender) VALUES (%s, %s, %s, %s)", (patient_id, name, age, gender))
    db.commit()
    cursor.close()
    db.close()
    messagebox.showinfo("Success", "Patient added successfully!")

def update_patient(patient_id, name, age, gender):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("UPDATE patients SET name=%s, age=%s, gender=%s WHERE id=%s", (name, age, gender, patient_id))
    db.commit()
    cursor.close()
    db.close()
    messagebox.showinfo("Success", "Patient updated successfully!")

def delete_patient(patient_id):
    if not id_exists('patients', patient_id):
        messagebox.showerror("Error", "Patient ID does not exist.")
        return
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM patients WHERE id=%s", (patient_id,))
    db.commit()
    cursor.close()
    db.close()
    messagebox.showinfo("Success", "Patient deleted successfully!")

def add_doctor(doctor_id, name, speciality):
    if id_exists('doctors', doctor_id):
        messagebox.showerror("Error", "Doctor ID already exists.")
        return
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO doctors (id, name, speciality) VALUES (%s, %s, %s)", (doctor_id, name, speciality))
    db.commit()
    cursor.close()
    db.close()
    messagebox.showinfo("Success", "Doctor added successfully!")

def update_doctor(doctor_id, name, speciality):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("UPDATE doctors SET name=%s, speciality=%s WHERE id=%s", (name, speciality, doctor_id))
    db.commit()
    cursor.close()
    db.close()
    messagebox.showinfo("Success", "Doctor updated successfully!")

def delete_doctor(doctor_id):
    if not id_exists('doctors', doctor_id):
        messagebox.showerror("Error", "Doctor ID does not exist.")
        return
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM doctors WHERE id=%s", (doctor_id,))
    db.commit()
    cursor.close()
    db.close()
    messagebox.showinfo("Success", "Doctor deleted successfully!")

class HospitalManagementApp:
    def __init__(self, master):
        self.master = master
        master.title("Hospital Management System")

        self.title_font = font.Font(size=16, weight='bold')
        self.label_font = font.Font(size=12)
        self.entry_font = font.Font(size=12)

        self.patient_frame = tk.Frame(master, bg='lightblue', padx=20, pady=20)
        self.patient_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        tk.Label(self.patient_frame, text="Patients", font=self.title_font, bg='lightblue').grid(row=0, columnspan=2)
        
        tk.Label(self.patient_frame, text="Patient ID:", font=self.label_font, bg='lightblue').grid(row=1, column=0, pady=5)
        self.patient_id = tk.Entry(self.patient_frame, font=self.entry_font, width=30)
        self.patient_id.grid(row=1, column=1, pady=5)

        tk.Label(self.patient_frame, text="Patient Name:", font=self.label_font, bg='lightblue').grid(row=2, column=0, pady=5)
        self.patient_name = tk.Entry(self.patient_frame, font=self.entry_font, width=30)
        self.patient_name.grid(row=2, column=1, pady=5)

        tk.Label(self.patient_frame, text="Age:", font=self.label_font, bg='lightblue').grid(row=3, column=0, pady=5)
        self.patient_age = tk.Entry(self.patient_frame, font=self.entry_font, width=30)
        self.patient_age.grid(row=3, column=1, pady=5)

        tk.Label(self.patient_frame, text="Gender:", font=self.label_font, bg='lightblue').grid(row=4, column=0, pady=5)
        self.patient_gender = tk.StringVar(value='Male')
        tk.OptionMenu(self.patient_frame, self.patient_gender, 'Male', 'Female', 'Other').grid(row=4, column=1, pady=5)

        tk.Button(self.patient_frame, text="Add Patient", command=self.add_patient, bg='lightgreen', font=self.label_font).grid(row=5, columnspan=2, pady=10)
        tk.Button(self.patient_frame, text="Update Patient", command=self.update_patient, bg='lightyellow', font=self.label_font).grid(row=6, columnspan=2, pady=5)
        tk.Button(self.patient_frame, text="Delete Patient", command=self.delete_patient, bg='lightcoral', font=self.label_font).grid(row=7, columnspan=2, pady=5)

        self.doctor_frame = tk.Frame(master, bg='lightyellow', padx=20, pady=20)
        self.doctor_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        tk.Label(self.doctor_frame, text="Doctors", font=self.title_font, bg='lightyellow').grid(row=0, columnspan=2)
        
        tk.Label(self.doctor_frame, text="Doctor ID:", font=self.label_font, bg='lightyellow').grid(row=1, column=0, pady=5)
        self.doctor_id = tk.Entry(self.doctor_frame, font=self.entry_font, width=30)
        self.doctor_id.grid(row=1, column=1, pady=5)

        tk.Label(self.doctor_frame, text="Doctor Name:", font=self.label_font, bg='lightyellow').grid(row=2, column=0, pady=5)
        self.doctor_name = tk.Entry(self.doctor_frame, font=self.entry_font, width=30)
        self.doctor_name.grid(row=2, column=1, pady=5)

        tk.Label(self.doctor_frame, text="Speciality:", font=self.label_font, bg='lightyellow').grid(row=3, column=0, pady=5)
        self.doctor_speciality = tk.Entry(self.doctor_frame, font=self.entry_font, width=30)
        self.doctor_speciality.grid(row=3, column=1, pady=5)

        tk.Button(self.doctor_frame, text="Add Doctor", command=self.add_doctor, bg='lightgreen', font=self.label_font).grid(row=4, columnspan=2, pady=10)
        tk.Button(self.doctor_frame, text="Update Doctor", command=self.update_doctor, bg='lightyellow', font=self.label_font).grid(row=5, columnspan=2, pady=5)
        tk.Button(self.doctor_frame, text="Delete Doctor", command=self.delete_doctor, bg='lightcoral', font=self.label_font).grid(row=6, columnspan=2, pady=5)

    def add_patient(self):
        patient_id = self.patient_id.get()
        name = self.patient_name.get()
        age = self.patient_age.get()
        gender = self.patient_gender.get()
        if patient_id.isdigit() and name and age.isdigit() and gender:
            add_patient(int(patient_id), name, int(age), gender)
            self.patient_name.delete(0, tk.END)
            self.patient_age.delete(0, tk.END)
            self.patient_id.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter valid patient information.")

    def update_patient(self):
        patient_id = self.patient_id.get()
        name = self.patient_name.get()
        age = self.patient_age.get()
        gender = self.patient_gender.get()
        if patient_id.isdigit() and name and age.isdigit() and gender:
            if id_exists('patients', int(patient_id)):
                update_patient(int(patient_id), name, int(age), gender)
                self.patient_name.delete(0, tk.END)
                self.patient_age.delete(0, tk.END)
                self.patient_id.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Patient ID does not exist.")
        else:
            messagebox.showerror("Error", "Please enter valid patient information.")

    def delete_patient(self):
        patient_id = self.patient_id.get()
        if patient_id.isdigit():
            delete_patient(int(patient_id))
            self.patient_id.delete(0, tk.END)
            self.patient_name.delete(0, tk.END)
            self.patient_age.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter a valid Patient ID.")

    def add_doctor(self):
        doctor_id = self.doctor_id.get()
        name = self.doctor_name.get()
        speciality = self.doctor_speciality.get()
        if doctor_id.isdigit() and name and speciality:
            add_doctor(int(doctor_id), name, speciality)
            self.doctor_name.delete(0, tk.END)
            self.doctor_speciality.delete(0, tk.END)
            self.doctor_id.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter valid doctor information.")

    def update_doctor(self):
        doctor_id = self.doctor_id.get()
        name = self.doctor_name.get()
        speciality = self.doctor_speciality.get()
        if doctor_id.isdigit() and name and speciality:
            if id_exists('doctors', int(doctor_id)):
                update_doctor(int(doctor_id), name, speciality)
                self.doctor_name.delete(0, tk.END)
                self.doctor_speciality.delete(0, tk.END)
                self.doctor_id.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Doctor ID does not exist.")
        else:
            messagebox.showerror("Error", "Please enter valid doctor information.")

    def delete_doctor(self):
        doctor_id = self.doctor_id.get()
        if doctor_id.isdigit():
            delete_doctor(int(doctor_id))
            self.doctor_id.delete(0, tk.END)
            self.doctor_name.delete(0, tk.END)
            self.doctor_speciality.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter a valid Doctor ID.")

if __name__ == "__main__":
    root = tk.Tk()
    app = HospitalManagementApp(root)
    root.state("zoomed")  
    root.mainloop()

           
