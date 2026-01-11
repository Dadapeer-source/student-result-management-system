from flask import Flask, render_template, request, redirect
from db import get_connection

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add-student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        usn = request.form['usn']
        name = request.form['name']
        clas = request.form['class']

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO students (usn, name, class) VALUES (%s,%s,%s)",
                       (usn, name, clas))
        conn.commit()
        conn.close()
        return redirect('/')
    return render_template('add_student.html')

@app.route('/add-marks', methods=['GET', 'POST'])
def add_marks():
    if request.method == 'POST':
        usn = request.form['usn']
        marks = [request.form[f's{i}'] for i in range(1,7)]

        conn = get_connection()
        cursor = conn.cursor()
        for i, m in enumerate(marks, start=1):
            cursor.execute("INSERT INTO marks (usn, subject, marks) VALUES (%s,%s,%s)",
                           (usn, f"Subject{i}", m))
        conn.commit()
        conn.close()
        return redirect('/')
    return render_template('add_marks.html')

@app.route('/view-result', methods=['GET', 'POST'])
def view_result():
    student = None
    s = [0]*6
    total = percentage = 0

    if request.method == 'POST':
        usn = request.form['usn']
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM students WHERE usn=%s", (usn,))
        student = cursor.fetchone()

        cursor.execute("SELECT marks FROM marks WHERE usn=%s ORDER BY subject", (usn,))
        rows = cursor.fetchall()
        if len(rows) == 6:
            s = [r[0] for r in rows]
            total = sum(s)
            percentage = total / 6

        conn.close()

    return render_template('view_result.html',
                           student=student,
                           s1=s[0], s2=s[1], s3=s[2], s4=s[3], s5=s[4], s6=s[5],
                           total=total, percentage=percentage)

if __name__ == '__main__':
    app.run(debug=True)
