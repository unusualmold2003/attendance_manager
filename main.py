import pickle
import cv2

ATTENDANCE_FILE = "attendance.pkl"

attendance = {}

min_attendance = int(input("Welcome to Attendance Manager\nEnter the minimum attendance to be maintained (%): "))

def classes_to_attend(class_attended, total_days, min_attendance):
    min_attendance /= 100
    x = 0
    while (class_attended + x) / (total_days + x) < min_attendance:
        x += 1
    return x

def input_details():
    subject = input("Enter the subject name: ")
    class_attended = int(input("Total number of classes attended: "))
    total_days = int(input("Enter the total number of classes held: "))
    
    percentage = round((class_attended / total_days) * 100, 2)
    additional_classes = classes_to_attend(class_attended, total_days, min_attendance)
    attendance[subject] = [class_attended, total_days, percentage, additional_classes]
    save_attendance()

def print_details():
    print("\nAttendance Summary:")
    print("-------------------")
    for subject, details in attendance.items():
        print(f"Subject: {subject}")
        print(f"Classes attended: {details[0]} / {details[1]}")
        print(f"Percentage: {details[2]:.2f}%")
        print(f"Additional classes needed to meet minimum attendance: {details[3]}")
        print("-" * 20)

def update_details():
    sub_name = input("Enter the subject you want to update: ")
    if sub_name in attendance:
        details = attendance[sub_name]
        if input("Did you attend today? (yes/no): ").lower() == "yes":
            details[0] += 1
        details[1] += 1
        save_attendance()
    else:
        print("Subject not found!")

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

def show_image(img_path="Screenshot_20240804-135917.png"):
    img = cv2.imread(img_path)
    if img is None:
        print(f"Error: Image '{img_path}' not found.")
        return
    img = cv2.resize(img, (300, 300))
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

load_attendance()

if not attendance:
    noSubjects = int(input("No existing data found. \nEnter the number of subjects: "))
    for _ in range(noSubjects):
        input_details()

while True:
    #show_image()
    print("\nSelect an option:")
    print("1. Update attendance")
    print("2. Display all details")
    print("3. Exit")
    option = input("Enter your choice (1/2/3): ")

    if option == '1':
        if input("Do you want to start afresh? (1/0): ") == '1':
            noSubjects = int(input("Enter the number of subjects: "))
            for _ in range(noSubjects):
                input_details()
        else:
            update_details()
    elif option == '2':
        print_details()
    elif option == '3':
        break
    else:
        print("Invalid option. Please try again.")