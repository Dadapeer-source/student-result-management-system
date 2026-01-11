# Student Result Management System

A full-stack web application built using Flask and MySQL to manage student details, enter subject-wise marks, and generate result reports with total and percentage.

---

## Features

- Add Student Details (USN, Name, Class)
- Enter Marks for 6 Subjects
- Store Data in MySQL Database
- View Result with:
  - Subject-wise Marks
  - Total Marks
  - Percentage
- Professional UI using HTML & CSS

---

## Technologies Used

- Frontend: HTML, CSS
- Backend: Python (Flask)
- Database: MySQL
- Tools: VS Code, MySQL Workbench

---

## Project Structure

student_result_system/
│
├── app.py
├── db.py
├── README.md
│
├── templates/
│   ├── index.html
│   ├── add_student.html
│   ├── add_marks.html
│   └── view_result.html
│
└── static/
    └── style.css

---

## Database Structure

### students table
- id (INT, Primary Key)
- usn (VARCHAR)
- name (VARCHAR)
- class (VARCHAR)

### marks table
- id (INT, Primary Key)
- usn (VARCHAR)
- subject (VARCHAR)
- marks (INT)

---

## How to Run the Project

1. Install required packages:
pip install flask mysql-connector-python

2. Create MySQL database:
CREATE DATABASE student_result;

3. Create tables:
CREATE TABLE students (...);
CREATE TABLE marks (...);

4. Update MySQL password in db.py.

5. Run the application:
python app.py

6. Open in browser:
http://127.0.0.1:5000

---

## Learning Outcomes

- Understanding Flask routing and templates
- Connecting Python with MySQL
- Implementing CRUD operations
- Designing normalized database tables
- Creating a complete full-stack project

---

## Future Enhancements

- Login Authentication (Admin / Student)
- PDF Result Download
- Rank Calculation
- Deployment to Cloud (PythonAnywhere / Render)

---

## Author

Dadapeer  
Student Result Management System – Full Stack Web Application
## Screenshots

![Home Page](screenshots/home.png)
![Add Student](screenshots/add_student.png)
![Add Marks](screenshots/add_marks.png)
![View Result](screenshots/view_result.png)
