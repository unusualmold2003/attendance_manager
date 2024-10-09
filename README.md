# Attendance Manager

## Description
Attendance Manager is a Python-based application designed to help users track and manage their attendance for various subjects. It allows users to input class details, update attendance records, and calculate the additional classes required to meet minimum attendance requirements.

## Features
- Input and manage attendance records for multiple subjects.
- Calculate attendance percentage based on classes attended and total classes held.
- Display a summary of attendance details, including the percentage and additional classes needed.
- Update attendance records interactively.
- Persistent storage of attendance data using Python's `pickle` module.

## Technologies Used
- **Python**: Programming language for the application logic.
- **Tkinter**: Library for creating the graphical user interface (GUI).
- **OpenCV**: Library for image display (optional feature).
- **Pickle**: Module for serializing and deserializing attendance data.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/unusualmold2003/attendance-manager.git
   cd attendance-manager
2. Install the necessary packages:
   ```bash
   pip install --upgrade tk

   pip install --upgrade pickle

   pip install --upgrade cv2
3. Run the app
   ```bash
   python main.py
   python tkin.py

## Usage
When you start the application, it will prompt you to enter the minimum attendance percentage.
If there are no existing attendance records, you will be prompted to enter the number of subjects and their details.
You can update your attendance daily and view the summary of all subjects.
The application also displays an image of your choice (default is a placeholder).

## Contributing
Feel free to contribute by opening issues or submitting pull requests. Suggestions for improvements or additional features are welcome!
