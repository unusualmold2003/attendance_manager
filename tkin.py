import pickle
import cv2
import tkinter as tk
from tkinter import messagebox, simpledialog

ATTENDANCE_FILE = "attendance.pkl"

attendance = {}
min_attendance = 75

def classes_to_attend(class_attended, total_days, min_attendance):
    min_attendance /= 100
    x = 0
    while (class_attended + x) / (total_days + x) < min_attendance:
        x += 1
    return x

def save_attendance():
    with open(ATTENDANCE_FILE, "wb") as f:
        pickle.dump(attendance, f)

def load_attendance():
    global attendance
    try:
        with open(ATTENDANCE_FILE, "rb") as f:
            attendance = pickle.load(f)
    except FileNotFoundError:
        attendance = {}

def update_attendance(subject, attended, total):
    if subject in attendance:
        details = attendance[subject]
        details[0] += attended
        details[1] += total
        details[2] = round((details[0] / details[1]) * 100, 2)
        details[3] = classes_to_attend(details[0], details[1], min_attendance)
        save_attendance()

def show_details():
    detail_str = "Attendance Summary:\n\n"
    for subject, details in attendance.items():
        detail_str += f"Subject: {subject}\n"
        detail_str += f"Classes attended: {details[0]} / {details[1]}\n"
        detail_str += f"Percentage: {details[2]}%\n"
        detail_str += f"Additional classes needed: {details[3]}\n\n"
    messagebox.showinfo("Attendance Details", detail_str)

def input_details():
    subject = simpledialog.askstring("Input", "Enter the subject name:")
    if subject:
        class_attended = simpledialog.askinteger("Input", "Total number of classes attended:")
        total_days = simpledialog.askinteger("Input", "Enter the total number of classes held:")
        if class_attended is not None and total_days is not None:
            percentage = round((class_attended / total_days) * 100, 2)
            additional_classes = classes_to_attend(class_attended, total_days, min_attendance)
            attendance[subject] = [class_attended, total_days, percentage, additional_classes]
            save_attendance()
            messagebox.showinfo("Success", f"Details for {subject} added successfully.")

def start():
    load_attendance()
    if not attendance:
        input_details()

def create_gui():
    root = tk.Tk()
    root.title("Attendance Manager")
    root.geometry("400x300")

    tk.Label(root, text="Welcome to Attendance Manager", font=("Arial", 16)).pack(pady=10)

    tk.Button(root, text="Input Attendance", command=input_details, width=20).pack(pady=5)
    tk.Button(root, text="Show Attendance Details", command=show_details, width=20).pack(pady=5)
    tk.Button(root, text="Exit", command=root.quit, width=20).pack(pady=5)

    start()
    root.mainloop()

if __name__ == "__main__":
    create_gui()