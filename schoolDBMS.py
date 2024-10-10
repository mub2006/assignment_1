import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('school.db')
c = conn.cursor()

# Create tables
def create_tables():
    # Drop tables if they exist to start fresh
    c.execute('DROP TABLE IF EXISTS students')
    c.execute('DROP TABLE IF EXISTS teachers')
    c.execute('DROP TABLE IF EXISTS principals')
    c.execute('DROP TABLE IF EXISTS admin')

    # Create Students table
    c.execute('''CREATE TABLE students (
                    studentsno INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER,
                    sex TEXT,
                    class TEXT,
                    fees REAL,
                    rank INTEGER,
                    english_mark INTEGER,
                    python_mark INTEGER,
                    math_mark INTEGER)''')

    # Create Teachers table
    c.execute('''CREATE TABLE teachers (
                    sno INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER,
                    sex TEXT,
                    salary REAL,
                    class_teacher_class TEXT)''')

    # Create Principals table
    c.execute('''CREATE TABLE principals (
                    sno INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER,
                    sex TEXT,
                    salary REAL)''')

    # Create Admin table
    c.execute('''CREATE TABLE admin (
                    sno INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL)''')

    # Insert default admin if the table is empty
    c.execute('INSERT OR IGNORE INTO admin (username, password) VALUES (?, ?)', ('admin', 'adminpass'))
    conn.commit()

# Function to authenticate admin
def authenticate(username, password):
    c.execute('SELECT * FROM admin WHERE username = ? AND password = ?', (username, password))
    return c.fetchone() is not None

# CRUD operations for students
def add_student(name, age, sex, class_name, fees, rank, english_mark, python_mark, math_mark):
    c.execute('INSERT INTO students (name, age, sex, class, fees, rank, english_mark, python_mark, math_mark) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', 
              (name, age, sex, class_name, fees, rank, english_mark, python_mark, math_mark))
    conn.commit()

def view_students():
    c.execute('SELECT * FROM students')
    return c.fetchall()

def update_student(studentsno, name, age, sex, class_name, fees, rank, english_mark, python_mark, math_mark):
    c.execute('UPDATE students SET name = ?, age = ?, sex = ?, class = ?, fees = ?, rank = ?, english_mark = ?, python_mark = ?, math_mark = ? WHERE studentsno = ?',
              (name, age, sex, class_name, fees, rank, english_mark, python_mark, math_mark, studentsno))
    conn.commit()

def delete_student(studentsno):
    c.execute('DELETE FROM students WHERE studentsno = ?', (studentsno,))
    conn.commit()

# CRUD operations for teachers
def add_teacher(name, age, sex, salary, class_teacher_class):
    c.execute('INSERT INTO teachers (name, age, sex, salary, class_teacher_class) VALUES (?, ?, ?, ?, ?)', 
              (name, age, sex, salary, class_teacher_class))
    conn.commit()

def view_teachers():
    c.execute('SELECT * FROM teachers')
    return c.fetchall()

def update_teacher(sno, name, age, sex, salary, class_teacher_class):
    c.execute('UPDATE teachers SET name = ?, age = ?, sex = ?, salary = ?, class_teacher_class = ? WHERE sno = ?',
              (name, age, sex, salary, class_teacher_class, sno))
    conn.commit()

def delete_teacher(sno):
    c.execute('DELETE FROM teachers WHERE sno = ?', (sno,))
    conn.commit()

# CRUD operations for principals
def add_principal(name, age, sex, salary):
    c.execute('INSERT INTO principals (name, age, sex, salary) VALUES (?, ?, ?, ?)', 
              (name, age, sex, salary))
    conn.commit()

def view_principals():
    c.execute('SELECT * FROM principals')
    return c.fetchall()

def update_principal(sno, name, age, sex, salary):
    c.execute('UPDATE principals SET name = ?, age = ?, sex = ?, salary = ? WHERE sno = ?',
              (name, age, sex, salary, sno))
    conn.commit()

def delete_principal(sno):
    c.execute('DELETE FROM principals WHERE sno = ?', (sno,))
    conn.commit()

# Main execution
if __name__ == "__main__":
    create_tables()

    # Admin login
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")

    if not authenticate(username, password):
        print("Authentication failed!")
    else:
        while True:
            print("\n1. Manage Students")
            print("2. Manage Teachers")
            print("3. Manage Principals")
            print("4. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                while True:
                    print("\n1. Add Student")
                    print("2. View Students")
                    print("3. Update Student")
                    print("4. Delete Student")
                    print("5. Back")
                    student_choice = input("Choose an option: ")

                    if student_choice == '1':
                        name = input("Enter name: ")
                        age = int(input("Enter age: "))
                        sex = input("Enter sex: ")
                        class_name = input("Enter class: ")
                        fees = float(input("Enter fees: "))
                        rank = int(input("Enter rank: "))
                        english_mark = int(input("Enter English mark: "))
                        python_mark = int(input("Enter Python mark: "))
                        math_mark = int(input("Enter Math mark: "))
                        add_student(name, age, sex, class_name, fees, rank, english_mark, python_mark, math_mark)
                        print("Student added successfully!")

                    elif student_choice == '2':
                        students = view_students()
                        print("Students:")
                        for student in students:
                            print(student)

                    elif student_choice == '3':
                        studentsno = int(input("Enter student number to update: "))
                        name = input("Enter new name: ")
                        age = int(input("Enter new age: "))
                        sex = input("Enter new sex: ")
                        class_name = input("Enter new class: ")
                        fees = float(input("Enter new fees: "))
                        rank = int(input("Enter new rank: "))
                        english_mark = int(input("Enter new English mark: "))
                        python_mark = int(input("Enter new Python mark: "))
                        math_mark = int(input("Enter new Math mark: "))
                        update_student(studentsno, name, age, sex, class_name, fees, rank, english_mark, python_mark, math_mark)
                        print("Student updated successfully!")

                    elif student_choice == '4':
                        studentsno = int(input("Enter student number to delete: "))
                        delete_student(studentsno)
                        print("Student deleted successfully!")

                    elif student_choice == '5':
                        break

            elif choice == '2':
                while True:
                    print("\n1. Add Teacher")
                    print("2. View Teachers")
                    print("3. Update Teacher")
                    print("4. Delete Teacher")
                    print("5. Back")
                    teacher_choice = input("Choose an option: ")

                    if teacher_choice == '1':
                        name = input("Enter name: ")
                        age = int(input("Enter age: "))
                        sex = input("Enter sex: ")
                        salary = float(input("Enter salary: "))
                        class_teacher_class = input("Enter class: ")
                        add_teacher(name, age, sex, salary, class_teacher_class)
                        print("Teacher added successfully!")

                    elif teacher_choice == '2':
                        teachers = view_teachers()
                        print("Teachers:")
                        for teacher in teachers:
                            print(teacher)

                    elif teacher_choice == '3':
                        sno = int(input("Enter teacher number to update: "))
                        name = input("Enter new name: ")
                        age = int(input("Enter new age: "))
                        sex = input("Enter new sex: ")
                        salary = float(input("Enter new salary: "))
                        class_teacher_class = input("Enter new class: ")
                        update_teacher(sno, name, age, sex, salary, class_teacher_class)
                        print("Teacher updated successfully!")

                    elif teacher_choice == '4':
                        sno = int(input("Enter teacher number to delete: "))
                        delete_teacher(sno)
                        print("Teacher deleted successfully!")

                    elif teacher_choice == '5':
                        break

            elif choice == '3':
                while True:
                    print("\n1. Add Principal")
                    print("2. View Principals")
                    print("3. Update Principal")
                    print("4. Delete Principal")
                    print("5. Back")
                    principal_choice = input("Choose an option: ")

                    if principal_choice == '1':
                        name = input("Enter name: ")
                        age = int(input("Enter age: "))
                        sex = input("Enter sex: ")
                        salary = float(input("Enter salary: "))
                        add_principal(name, age, sex, salary)
                        print("Principal added successfully!")

                    elif principal_choice == '2':
                        principals = view_principals()
                        print("Principals:")
                        for principal in principals:
                            print(principal)

                    elif principal_choice == '3':
                        sno = int(input("Enter principal number to update: "))
                        name = input("Enter new name: ")
