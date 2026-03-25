from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

# -----------------------
# APP CONFIG
# -----------------------
app = Flask(__name__)
app.secret_key = "secret_key"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///university.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# -----------------------
# DATABASE MODEL
# -----------------------
class Student(db.Model):
    __tablename__ = 'student'

    id = db.Column(db.Integer, primary_key=True)

    first_name = db.Column(db.String(50), nullable=False)

    last_name = db.Column(db.String(50), nullable=False)

    email = db.Column(db.String(100), nullable=False)  # REQUIRED FIELD


# -----------------------
# HOME → redirect to view
# -----------------------
@app.route('/')
def home():
    return redirect(url_for('view_students'))


# -----------------------
# VIEW ALL STUDENTS
# -----------------------
@app.route('/student/view')
def view_students():
    students = Student.query.all()
    return render_template('view_students.html', students=students)


# -----------------------
# CREATE STUDENT
# -----------------------
@app.route('/student/create', methods=['GET', 'POST'])
def create_student():

    if request.method == 'POST':

        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')

        # Basic validation
        if not first_name or not last_name or not email:
            flash("All fields are required!", "danger")
            return redirect(url_for('create_student'))

        new_student = Student(
            first_name=first_name,
            last_name=last_name,
            email=email
        )

        db.session.add(new_student)
        db.session.commit()

        flash("Student added successfully!", "success")
        return redirect(url_for('view_students'))

    return render_template('create_student.html')


# -----------------------
# UPDATE STUDENT
# -----------------------
@app.route('/student/update/<int:id>', methods=['GET', 'POST'])
def update_student(id):

    student = Student.query.get_or_404(id)

    if request.method == 'POST':

        student.first_name = request.form.get('first_name')
        student.last_name = request.form.get('last_name')
        student.email = request.form.get('email')

        # Validation
        if not student.first_name or not student.last_name or not student.email:
            flash("All fields are required!", "danger")
            return redirect(url_for('update_student', id=id))

        db.session.commit()

        flash("Student updated successfully!", "success")
        return redirect(url_for('view_students'))

    return render_template('update_student.html', student=student)


# -----------------------
# DELETE STUDENT
# -----------------------
@app.route('/student/delete/<int:id>')
def delete_student(id):

    student = Student.query.get_or_404(id)

    db.session.delete(student)
    db.session.commit()

    flash("Student deleted successfully!", "success")

    return redirect(url_for('view_students'))


# -----------------------
# RUN APP
# -----------------------
if __name__ == '__main__':
    app.run(debug=True)