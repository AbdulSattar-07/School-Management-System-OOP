# 🏫 School Management System

A modern, interactive web application built with Streamlit for managing students, teachers, grades, and subject enrollments. Features a beautiful animated UI with responsive design.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## ✨ Features

- **👨‍🎓 Student Management**: Add, view, and search student records
- **👩‍🏫 Teacher Management**: Register and track teacher information
- **📚 Subject Enrollment**: Enroll students in various subjects
- **📝 Grade Assignment**: Teachers can assign grades to students
- **📊 Dashboard**: Real-time statistics and quick actions
- **🔍 Search Functionality**: Easily find students and teachers
- **🎨 Beautiful UI**: Animated gradient backgrounds and smooth transitions
- **📱 Responsive Design**: Works seamlessly on all screen sizes

## 🚀 Quick Start

### Option 1: Using Scripts (Easiest)

**Windows:**
```bash
run.bat
```

**Mac/Linux:**
```bash
chmod +x run.sh
./run.sh
```

### Option 2: Manual Installation

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application**
   ```bash
   streamlit run app.py
   ```

3. **Open your browser**
   - The app will automatically open at `http://localhost:8501`

## 📋 Usage Guide

### 1. Add a Teacher
- Navigate to "👩‍🏫 Add Teacher"
- Fill in name, age, contact, employee ID, and specialization
- Click "Add Teacher"

### 2. Add a Student
- Navigate to "➕ Add Student"
- Fill in name, age, contact, student ID, and grade
- Click "Add Student"

### 3. Enroll in Subject
- Navigate to "📚 Enroll Subject"
- Select a student and enter subject name
- Click "Enroll Student"

### 4. Assign Grade
- Navigate to "📝 Assign Grade"
- Select teacher, student, subject, and grade
- Click "Assign Grade"

### 5. View Records
- Use "👨‍🎓 View Students" or "👩‍🏫 View Teachers"
- Search by name or ID
- View all details and grades

## 📁 Project Structure

```
school-management-system/
├── app.py                          # Main application
├── School_management_System.ipynb  # OOP implementation notebook
├── requirements.txt                # Dependencies
├── README.md                       # Documentation
├── LICENSE                         # MIT License
├── CONTRIBUTING.md                 # Contribution guidelines
├── .gitignore                      # Git ignore rules
├── .streamlit/config.toml          # Streamlit config
├── run.sh                          # Linux/Mac launcher
└── run.bat                         # Windows launcher
```

## 🛠️ Technologies

- **[Streamlit](https://streamlit.io/)**: Web framework
- **Python 3.8+**: Programming language
- **OOP Design**: Clean, maintainable code structure

## 🌐 Deploy to Streamlit Cloud

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io/)
3. Sign in with GitHub
4. Click "New app" and select your repository
5. Set main file to `app.py`
6. Click "Deploy"

Your app will be live at: `https://yourusername-school-management.streamlit.app`

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Abdul Sattar**
- GitHub: [@yourusername](https://github.com/yourusername)

## 🔮 Future Enhancements

- [ ] Database integration (SQLite/PostgreSQL)
- [ ] User authentication and roles
- [ ] Export reports to PDF/Excel
- [ ] Attendance tracking
- [ ] Fee management
- [ ] Parent portal

## 📞 Support

If you have any questions or need help, please open an issue in the GitHub repository.

---

⭐ If you find this project useful, please consider giving it a star!
