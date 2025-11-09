import streamlit as st
import time

# Page configuration
st.set_page_config(
    page_title="School Management System",
    page_icon="🏫",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for animations and responsive design
st.markdown("""
<style>
    /* Main container styling */
    .main {
        padding: 2rem;
    }
    
    /* Animated gradient background */
    .stApp {
        background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
    }
    
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Card styling with hover effect */
    .card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2);
    }
    
    /* Title animation */
    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    h1, h2, h3 {
        animation: fadeInDown 0.6s ease-out;
        color: #1e3a8a;
    }
    
    /* Button styling */
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.5rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
    }
    
    /* Input field styling */
    .stTextInput>div>div>input, .stNumberInput>div>div>input {
        border-radius: 10px;
        border: 2px solid #e0e0e0;
        transition: border-color 0.3s ease;
    }
    
    .stTextInput>div>div>input:focus, .stNumberInput>div>div>input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 2px rgba(102, 126, 234, 0.2);
    }
    
    /* Sidebar styling */
    .css-1d391kg, [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
    
    .css-1d391kg .stRadio>label, [data-testid="stSidebar"] .stRadio>label {
        color: white;
        font-weight: 600;
    }
    
    /* Success/Error message animations */
    .stSuccess, .stError, .stWarning, .stInfo {
        animation: slideIn 0.5s ease-out;
    }
    
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateX(-20px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    /* Metric card styling */
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 15px;
        padding: 1.5rem;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease;
    }
    
    .metric-card:hover {
        transform: scale(1.05);
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .main {
            padding: 1rem;
        }
        .card {
            padding: 1rem;
        }
    }
    
    /* Loading animation */
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
</style>
""", unsafe_allow_html=True)

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

# Initialize session state
if "students" not in st.session_state:
    st.session_state.students = {}
if "teachers" not in st.session_state:
    st.session_state.teachers = {}

# Header with metrics
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f"""
    <div class="metric-card">
        <h2 style="color: white; margin: 0;">👨‍🎓 {len(st.session_state.students)}</h2>
        <p style="margin: 0;">Total Students</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <h2 style="color: white; margin: 0;">👩‍🏫 {len(st.session_state.teachers)}</h2>
        <p style="margin: 0;">Total Teachers</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    total_subjects = sum(len(s.subjects) for s in st.session_state.students.values())
    st.markdown(f"""
    <div class="metric-card">
        <h2 style="color: white; margin: 0;">📚 {total_subjects}</h2>
        <p style="margin: 0;">Total Enrollments</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.title("🏫 School Management System")
st.markdown("---")

# Sidebar menu
st.sidebar.title("📋 Navigation")
menu = st.sidebar.radio(
    "Choose Action",
    ["🏠 Dashboard", "➕ Add Student", "👩‍🏫 Add Teacher", "📚 Enroll Subject", "📝 Assign Grade", "👨‍🎓 View Students", "👩‍🏫 View Teachers"],
    label_visibility="collapsed"
)

# Dashboard
if menu == "🏠 Dashboard":
    st.header("📊 Dashboard Overview")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("📈 Quick Stats")
        st.metric("Students Enrolled", len(st.session_state.students), delta=None)
        st.metric("Teachers Registered", len(st.session_state.teachers), delta=None)
        st.metric("Active Subjects", total_subjects, delta=None)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("🎯 Quick Actions")
        if st.button("➕ Add New Student", use_container_width=True):
            st.session_state.menu = "➕ Add Student"
            st.rerun()
        if st.button("👩‍🏫 Add New Teacher", use_container_width=True):
            st.session_state.menu = "👩‍🏫 Add Teacher"
            st.rerun()
        if st.button("📚 Enroll in Subject", use_container_width=True):
            st.session_state.menu = "📚 Enroll Subject"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Recent activity
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🔔 Recent Activity")
    if st.session_state.students:
        st.write("✅ Latest students added:")
        for sid in list(st.session_state.students.keys())[-3:]:
            student = st.session_state.students[sid]
            st.write(f"- {student.name} (ID: {student.student_id})")
    else:
        st.info("No recent activity. Start by adding students and teachers!")
    st.markdown('</div>', unsafe_allow_html=True)

# Add Student
elif menu == "➕ Add Student":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("➕ Add New Student")
    
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("👤 Full Name", placeholder="Enter student name")
        age = st.number_input("🎂 Age", min_value=5, max_value=100, step=1, value=15)
        contact = st.text_input("📞 Contact Number", placeholder="+92 XXX XXXXXXX")
    
    with col2:
        student_id = st.text_input("🆔 Student ID", placeholder="S001")
        grade = st.text_input("📖 Class/Grade", placeholder="Grade 10")
        st.write("")  # Spacing

    if st.button("✅ Add Student", use_container_width=True):
        if not name.strip() or not student_id.strip():
            st.error("⚠️ Name and Student ID are required.")
        elif student_id in st.session_state.students:
            st.error("⚠️ Student ID already exists.")
        else:
            with st.spinner("Adding student..."):
                time.sleep(0.5)  # Animation effect
                st.session_state.students[student_id] = Student(name, age, contact, student_id, grade)
            st.success(f"🎉 Student {name} added successfully!")
            st.balloons()
    
    st.markdown('</div>', unsafe_allow_html=True)

# Add Teacher
elif menu == "👩‍🏫 Add Teacher":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("👩‍🏫 Add New Teacher")
    
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("👤 Full Name", placeholder="Enter teacher name")
        age = st.number_input("🎂 Age", min_value=18, max_value=100, step=1, value=30)
        contact = st.text_input("📞 Contact Number", placeholder="+92 XXX XXXXXXX")
    
    with col2:
        emp_id = st.text_input("🆔 Employee ID", placeholder="T001")
        specialization = st.text_input("🎓 Specialization", placeholder="Mathematics, Physics, etc.")
        st.write("")  # Spacing

    if st.button("✅ Add Teacher", use_container_width=True):
        if not name.strip() or not emp_id.strip():
            st.error("⚠️ Name and Employee ID are required.")
        elif emp_id in st.session_state.teachers:
            st.error("⚠️ Employee ID already exists.")
        else:
            with st.spinner("Adding teacher..."):
                time.sleep(0.5)  # Animation effect
                st.session_state.teachers[emp_id] = Teacher(name, age, contact, emp_id, specialization)
            st.success(f"🎉 Teacher {name} added successfully!")
            st.balloons()
    
    st.markdown('</div>', unsafe_allow_html=True)

# Enroll Subject
elif menu == "📚 Enroll Subject":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("📚 Enroll Student in Subject")
    
    if not st.session_state.students:
        st.warning("⚠️ No students available. Please add students first.")
    else:
        col1, col2 = st.columns([2, 1])
        with col1:
            student_options = {f"{s.name} ({sid})": sid for sid, s in st.session_state.students.items()}
            selected_student = st.selectbox("👨‍🎓 Select Student", list(student_options.keys()))
            student_id = student_options[selected_student]
        
        with col2:
            subject = st.text_input("📖 Subject Name", placeholder="e.g., Mathematics")

        # Show current enrollments
        current_student = st.session_state.students[student_id]
        if current_student.subjects:
            st.info(f"📋 Current subjects: {', '.join(current_student.subjects.keys())}")

        if st.button("✅ Enroll Student", use_container_width=True):
            if subject.strip():
                with st.spinner("Enrolling student..."):
                    time.sleep(0.3)
                    st.session_state.students[student_id].enroll_subject(subject)
                st.success(f"🎉 Student enrolled in {subject}!")
            else:
                st.error("⚠️ Please enter a valid subject name.")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Assign Grade
elif menu == "📝 Assign Grade":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("📝 Assign Grade to Student")
    
    if not st.session_state.teachers:
        st.warning("⚠️ No teachers available. Please add teachers first.")
    elif not st.session_state.students:
        st.warning("⚠️ No students available. Please add students first.")
    else:
        col1, col2 = st.columns(2)
        
        with col1:
            teacher_options = {f"{t.name} ({tid})": tid for tid, t in st.session_state.teachers.items()}
            selected_teacher = st.selectbox("👩‍🏫 Select Teacher", list(teacher_options.keys()))
            emp_id = teacher_options[selected_teacher]
            
            student_options = {f"{s.name} ({sid})": sid for sid, s in st.session_state.students.items()}
            selected_student = st.selectbox("👨‍🎓 Select Student", list(student_options.keys()))
            student_id = student_options[selected_student]
        
        with col2:
            subject = st.text_input("📖 Subject", placeholder="e.g., Mathematics")
            grade = st.text_input("🏆 Grade", placeholder="e.g., A+, 95%, etc.")

        # Show student's current subjects
        current_student = st.session_state.students[student_id]
        if current_student.subjects:
            st.info(f"📋 {current_student.name}'s subjects: {', '.join(current_student.subjects.keys())}")

        if st.button("✅ Assign Grade", use_container_width=True):
            if subject.strip() and grade.strip():
                with st.spinner("Assigning grade..."):
                    time.sleep(0.3)
                    teacher = st.session_state.teachers[emp_id]
                    student = st.session_state.students[student_id]
                    result = teacher.assign_grade(student, subject, grade)
                if "✅" in result:
                    st.success(result)
                else:
                    st.warning(result)
            else:
                st.error("⚠️ Please enter both subject and grade.")
    
    st.markdown('</div>', unsafe_allow_html=True)

# View Students
elif menu == "👨‍🎓 View Students":
    st.header("👨‍🎓 Students List")
    
    if not st.session_state.students:
        st.info("📭 No students added yet. Start by adding some students!")
    else:
        # Search functionality
        search = st.text_input("🔍 Search students", placeholder="Search by name or ID")
        
        # Filter students
        filtered_students = {
            sid: s for sid, s in st.session_state.students.items()
            if search.lower() in s.name.lower() or search.lower() in sid.lower()
        } if search else st.session_state.students
        
        # Display in grid
        cols = st.columns(2)
        for idx, (sid, student) in enumerate(filtered_students.items()):
            with cols[idx % 2]:
                st.markdown('<div class="card">', unsafe_allow_html=True)
                st.subheader(f"👤 {student.name}")
                st.write(f"**🆔 ID:** {student.student_id}")
                st.write(f"**🎂 Age:** {student.age}")
                st.write(f"**📞 Contact:** {student.contact_number}")
                st.write(f"**📖 Grade:** {student.grade}")
                
                if student.subjects:
                    st.write("**📚 Subjects & Grades:**")
                    for subj, grd in student.subjects.items():
                        grade_color = "🟢" if grd not in ["Not Assigned", "F"] else "🔴"
                        st.write(f"{grade_color} {subj}: **{grd}**")
                else:
                    st.write("📭 No subjects enrolled yet")
                
                st.markdown('</div>', unsafe_allow_html=True)

# View Teachers
elif menu == "👩‍🏫 View Teachers":
    st.header("👩‍🏫 Teachers List")
    
    if not st.session_state.teachers:
        st.info("📭 No teachers added yet. Start by adding some teachers!")
    else:
        # Search functionality
        search = st.text_input("🔍 Search teachers", placeholder="Search by name or ID")
        
        # Filter teachers
        filtered_teachers = {
            tid: t for tid, t in st.session_state.teachers.items()
            if search.lower() in t.name.lower() or search.lower() in tid.lower()
        } if search else st.session_state.teachers
        
        # Display in grid
        cols = st.columns(2)
        for idx, (tid, teacher) in enumerate(filtered_teachers.items()):
            with cols[idx % 2]:
                st.markdown('<div class="card">', unsafe_allow_html=True)
                st.subheader(f"👨‍🏫 {teacher.name}")
                st.write(f"**🆔 ID:** {teacher.employee_id}")
                st.write(f"**🎂 Age:** {teacher.age}")
                st.write(f"**📞 Contact:** {teacher.contact_number}")
                st.write(f"**🎓 Specialization:** {teacher.specialization}")
                
                if teacher.subjects_taught:
                    st.write("**📚 Subjects Taught:**")
                    for subj in teacher.subjects_taught:
                        st.write(f"📖 {subj}")
                else:
                    st.write("📭 No subjects assigned yet")
                
                st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: white; padding: 1rem;'>
    <p>🏫 School Management System | Built with Streamlit</p>
</div>
""", unsafe_allow_html=True)
