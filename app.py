import streamlit as st

# Import classes (paste the above OOP code here or import from file)
class Person:
    def __init__(self, name, age, contact_number):
        self.name = name
        self.age = age
        self.contact_number = contact_number
    
    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Contact: {self.contact_number}"

class Student(Person):
    def __init__(self, name, age, contact_number, student_id, grade):
        super().__init__(name, age, contact_number)
        self.student_id = student_id
        self.grade = grade
        self.subjects = {}
    
    def enroll_subject(self, subject):
        if subject not in self.subjects:
            self.subjects[subject] = "Not Assigned"
    
    def view_grades(self):
        return self.subjects

class Teacher(Person):
    def __init__(self, name, age, contact_number, employee_id, specialization):
        super().__init__(name, age, contact_number)
        self.employee_id = employee_id
        self.specialization = specialization
        self.subjects_taught = []

    def add_subject(self, subject):
        if subject not in self.subjects_taught:
            self.subjects_taught.append(subject)
    
    def assign_grade(self, student, subject, grade):
        if subject in student.subjects:
            student.subjects[subject] = grade
            return f"✅ Grade '{grade}' assigned to {student.name} for {subject}."
        else:
            return f"⚠️ {student.name} is not enrolled in {subject}."


# ------------------- STREAMLIT APP -------------------
st.title("🏫 School Management System")

# Initialize session state
if "students" not in st.session_state:
    st.session_state.students = {}
if "teachers" not in st.session_state:
    st.session_state.teachers = {}

menu = st.sidebar.radio("Choose Action", ["Add Student", "Add Teacher", "Enroll Subject", "Assign Grade", "View Students"])

# Add Student
if menu == "Add Student":
    st.header("➕ Add New Student")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=5, max_value=100, step=1)
    contact = st.text_input("Contact Number")
    student_id = st.text_input("Student ID")
    grade = st.text_input("Class/Grade")

    if st.button("Add Student"):
        if student_id not in st.session_state.students:
            st.session_state.students[student_id] = Student(name, age, contact, student_id, grade)
            st.success(f"Student {name} added successfully ✅")
        else:
            st.error("⚠️ Student ID already exists.")

# Add Teacher
elif menu == "Add Teacher":
    st.header("👩‍🏫 Add New Teacher")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=18, max_value=100, step=1)
    contact = st.text_input("Contact Number")
    emp_id = st.text_input("Employee ID")
    specialization = st.text_input("Specialization")

    if st.button("Add Teacher"):
        if emp_id not in st.session_state.teachers:
            st.session_state.teachers[emp_id] = Teacher(name, age, contact, emp_id, specialization)
            st.success(f"Teacher {name} added successfully ✅")
        else:
            st.error("⚠️ Employee ID already exists.")

# Enroll Subject
elif menu == "Enroll Subject":
    st.header("📚 Enroll Student in Subject")
    student_id = st.selectbox("Select Student", list(st.session_state.students.keys()))
    subject = st.text_input("Subject Name")

    if st.button("Enroll"):
        st.session_state.students[student_id].enroll_subject(subject)
        st.success(f"Student enrolled in {subject} ✅")

# Assign Grade
elif menu == "Assign Grade":
    st.header("📝 Assign Grade to Student")
    emp_id = st.selectbox("Select Teacher", list(st.session_state.teachers.keys()))
    student_id = st.selectbox("Select Student", list(st.session_state.students.keys()))
    subject = st.text_input("Subject")
    grade = st.text_input("Grade")

    if st.button("Assign Grade"):
        teacher = st.session_state.teachers[emp_id]
        student = st.session_state.students[student_id]
        result = teacher.assign_grade(student, subject, grade)
        st.info(result)

# View Students
elif menu == "View Students":
    st.header("👨‍🎓 Students List")
    for sid, student in st.session_state.students.items():
        st.subheader(f"{student.name} ({student.student_id})")
        st.write(student.get_details())
        st.write("📘 Subjects & Grades:", student.view_grades())
# streamlit run app.py
