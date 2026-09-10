# PROJECT 25: PLACEMENT READINESS AND STUDENT PROGRESS
# MANAGEMENT SYSTEM
import os
from datetime import datetime
# CONSTANTS
DATA_FILE = "students.txt"

# BASE CLASS - PERSON

class Person:
    """
    Base class for storing common person information.
    """

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def display_person(self):
        print("Name       :", self.name)
        print("Email      :", self.email)
        print("Phone      :", self.phone)


# STUDENT CLASS

class Student(Person):
    """
    Student class inherits from Person.

    Concepts:
    - Inheritance
    - Encapsulation
    - Class variables
    - Static methods
    - Class methods
    - *args
    - **kwargs
    """

    # Class variable
    total_students = 0

    def __init__(
        self,
        student_id,
        name,
        email,
        phone,
        batch,
        attendance=0,
        python_score=0,
        sql_score=0,
        excel_score=0,
        powerbi_score=0,
        project_status="Not Completed",
        practice_sessions=0,
        mock_interview="Not Attempted"
    ):

        super().__init__(name, email, phone)

        # Encapsulation - private attribute
        self.__student_id = student_id

        self.batch = batch
        self.attendance = attendance

        self.python_score = python_score
        self.sql_score = sql_score
        self.excel_score = excel_score
        self.powerbi_score = powerbi_score

        self.project_status = project_status
        self.practice_sessions = practice_sessions
        self.mock_interview = mock_interview

        Student.total_students += 1


# PROPERTY - GET STUDENT ID

    def get_student_id(self):
        return self.__student_id

    # --------------------------------------------------------
    # UPDATE STUDENT INFORMATION
    # Uses **kwargs
    # --------------------------------------------------------

    def update_details(self, **kwargs):

        for key, value in kwargs.items():

            if key == "name":
                self.name = value

            elif key == "email":
                self.email = value

            elif key == "phone":
                self.phone = value

            elif key == "batch":
                self.batch = value

            elif key == "attendance":
                self.attendance = value

            elif key == "python_score":
                self.python_score = value

            elif key == "sql_score":
                self.sql_score = value

            elif key == "excel_score":
                self.excel_score = value

            elif key == "powerbi_score":
                self.powerbi_score = value

            elif key == "project_status":
                self.project_status = value

            elif key == "practice_sessions":
                self.practice_sessions = value

            elif key == "mock_interview":
                self.mock_interview = value

    # STATIC METHOD

    @staticmethod
    def validate_score(score):
        """
        Checks whether score is between 0 and 100.
        """

        return 0 <= score <= 100

    # --------------------------------------------------------
    # CLASS METHOD
    # --------------------------------------------------------

    @classmethod
    def get_total_students(cls):
        return cls.total_students

# AVERAGE TECHNICAL SCORE

    def technical_average(self):

        scores = (
            self.python_score,
            self.sql_score,
            self.excel_score,
            self.powerbi_score
        )

        return sum(scores) / len(scores)

# PERFORMANCE CATEGORY

    def performance_category(self):

        average = self.technical_average()

        if average >= 80:
            return "Excellent"

        elif average >= 60:
            return "Good"

        elif average >= 40:
            return "Average"

        else:
            return "Needs Improvement"


# PROJECT SCORE

    def project_score(self):

        if self.project_status.lower() == "completed":
            return 100
        else:
            return 0


# PRACTICE SCORE

    def practice_score(self):

        if self.practice_sessions >= 10:
            return 100

        elif self.practice_sessions >= 7:
            return 80

        elif self.practice_sessions >= 5:
            return 60

        elif self.practice_sessions >= 3:
            return 40

        else:
            return 20

    # MOCK INTERVIEW SCORE

    def mock_interview_score(self):

        status = self.mock_interview.lower()

        if status == "passed":
            return 100

        elif status == "average":
            return 60

        elif status == "failed":
            return 30

        else:
            return 0

 # OVERALL PROGRESS

    def overall_progress(self):

        technical = self.technical_average()

        attendance_score = min(self.attendance, 100)

        project = self.project_score()

        practice = self.practice_score()

        interview = self.mock_interview_score()

        overall = (
            technical
            + attendance_score
            + project
            + practice
            + interview
        ) / 5

        return round(overall, 2)
        
# PLACEMENT ELIGIBILITY

    def placement_eligibility(self):

        average = self.technical_average()

        if (
            self.attendance >= 75
            and average >= 60
            and self.project_status.lower() == "completed"
            and self.practice_sessions >= 5
            and self.mock_interview.lower() == "passed"
        ):
            return "Eligible"

        return "Not Eligible"

    # DETAILS METHOD

    def details(self):

        print("\n---------------------------------------------")
        print("           STUDENT DETAILS")
        print("---------------------------------------------")

        print("Student ID          :", self.__student_id)
        print("Name                :", self.name)
        print("Email               :", self.email)
        print("Phone               :", self.phone)
        print("Batch               :", self.batch)

        print("\nAttendance          :", self.attendance, "%")

        print("\nTechnical Scores")
        print("Python              :", self.python_score)
        print("SQL                 :", self.sql_score)
        print("Excel               :", self.excel_score)
        print("Power BI            :", self.powerbi_score)

        print("\nProject Status      :", self.project_status)
        print("Practice Sessions   :", self.practice_sessions)
        print("Mock Interview      :", self.mock_interview)

        print("\nTechnical Average   :", round(self.technical_average(), 2))
        print("Performance         :", self.performance_category())
        print("Overall Progress    :", self.overall_progress(), "%")
        print("Placement Status    :", self.placement_eligibility())

        print("---------------------------------------------")

# *args EXAMPLE


    def calculate_total(self, *scores):

        if len(scores) == 0:
            return 0

        return sum(scores)

# ADVANCED STUDENT CLASS

class AdvancedStudent(Student):
    """
    Child class of Student.

    Demonstrates inheritance and polymorphism.
    """

    def details(self):

        print("\n=============================================")
        print("        ADVANCED STUDENT DETAILS")
        print("=============================================")

        print("Student ID        :", self.get_student_id())
        print("Name              :", self.name)
        print("Batch             :", self.batch)
        print("Technical Average :", round(self.technical_average(), 2))
        print("Overall Progress  :", self.overall_progress(), "%")
        print("Placement Status  :", self.placement_eligibility())

        print("=============================================")



# BATCH CLASS

class Batch:

    def __init__(self, batch_name, trainer):
        self.batch_name = batch_name
        self.trainer = trainer
        self.students = []

    def add_student(self, student):

        self.students.append(student)

    def display_batch(self):

        print("\n---------------------------------------------")
        print("Batch Name :", self.batch_name)
        print("Trainer    :", self.trainer)
        print("Students   :", len(self.students))
        print("---------------------------------------------")

        for student in self.students:
            print(
                student.get_student_id(),
                "-",
                student.name
            )

# MANAGEMENT SYSTEM CLASS

class PlacementManagementSystem:

    def __init__(self):

        self.students = {}
        self.batches = {}

    # STUDENT REGISTRATION

    def register_student(self):

        print("\n========== STUDENT REGISTRATION ==========")

        student_id = input("Enter Student ID: ").strip()

        if student_id in self.students:
            print("Student ID already exists.")
            return

        name = input("Enter Student Name: ").strip()
        email = input("Enter Email: ").strip()
        phone = input("Enter Phone Number: ").strip()
        batch = input("Enter Batch Name: ").strip()

        student = Student(
            student_id,
            name,
            email,
            phone,
            batch
        )

        self.students[student_id] = student

        # Add batch if not already present
        if batch not in self.batches:
            trainer = input("Enter Trainer Name: ").strip()

            self.batches[batch] = Batch(
                batch,
                trainer
            )

        self.batches[batch].add_student(student)

        print("\nStudent registered successfully!")

 # BATCH MANAGEMENT

    def create_batch(self):

        print("\n========== CREATE BATCH ==========")

        batch_name = input("Enter Batch Name: ").strip()

        if batch_name in self.batches:
            print("Batch already exists.")
            return

        trainer = input("Enter Trainer Name: ").strip()

        self.batches[batch_name] = Batch(
            batch_name,
            trainer
        )

        print("Batch created successfully!")

    def show_batches(self):

        print("\n========== ALL BATCHES ==========")

        if not self.batches:
            print("No batches available.")
            return

        for batch in self.batches.values():
            batch.display_batch()

# SEARCH STUDENT
    
    def search_student(self):

        print("\n========== SEARCH STUDENT ==========")

        search = input(
            "Enter Student ID or Name: "
        ).strip().lower()

        found = False

        for student in self.students.values():

            if (
                search == student.get_student_id().lower()
                or search in student.name.lower()
            ):

                student.details()
                found = True

        if not found:
            print("Student not found.")

    # FIND STUDENT

    def get_student(self):

        student_id = input(
            "Enter Student ID: "
        ).strip()

        if student_id not in self.students:
            print("Student not found.")
            return None

        return self.students[student_id]

    # ATTENDANCE TRACKING
    def update_attendance(self):

        print("\n========== ATTENDANCE TRACKING ==========")

        student = self.get_student()

        if student is None:
            return

        try:

            attendance = float(
                input("Enter Attendance Percentage: ")
            )

            if 0 <= attendance <= 100:

                student.attendance = attendance

                print("Attendance updated successfully.")

            else:

                print("Attendance must be between 0 and 100.")

        except ValueError:

            print("Please enter a valid number.")

    # TECHNICAL ASSESSMENT SCORES

    def update_scores(self):

        print("\n========== TECHNICAL ASSESSMENT ==========")

        student = self.get_student()

        if student is None:
            return

        try:

            python_score = float(
                input("Enter Python Score: ")
            )

            sql_score = float(
                input("Enter SQL Score: ")
            )

            excel_score = float(
                input("Enter Excel Score: ")
            )

            powerbi_score = float(
                input("Enter Power BI Score: ")
            )

            scores = [
                python_score,
                sql_score,
                excel_score,
                powerbi_score
            ]

            for score in scores:

                if not Student.validate_score(score):

                    print(
                        "Scores must be between 0 and 100."
                    )

                    return

            student.update_details(
                python_score=python_score,
                sql_score=sql_score,
                excel_score=excel_score,
                powerbi_score=powerbi_score
            )

            print("Technical scores updated successfully.")

        except ValueError:

            print("Please enter valid numbers.")

    # PROJECT STATUS

    def update_project(self):

        print("\n========== PROJECT STATUS ==========")

        student = self.get_student()

        if student is None:
            return

        print("\n1. Completed")
        print("2. Not Completed")

        choice = input("Enter choice: ").strip()

        if choice == "1":

            student.project_status = "Completed"

        elif choice == "2":

            student.project_status = "Not Completed"

        else:

            print("Invalid choice.")
            return

        print("Project status updated.")

    # PRACTICE SESSION TRACKING

    def update_practice(self):

        print("\n========== PRACTICE SESSION ==========")

        student = self.get_student()

        if student is None:
            return

        try:

            sessions = int(
                input("Enter Number of Practice Sessions: ")
            )

            if sessions >= 0:

                student.practice_sessions = sessions

                print("Practice sessions updated.")

            else:

                print("Sessions cannot be negative.")

        except ValueError:

            print("Enter a valid number.")

    # MOCK INTERVIEW

    def update_mock_interview(self):

        print("\n========== MOCK INTERVIEW ==========")

        student = self.get_student()

        if student is None:
            return

        print("\n1. Passed")
        print("2. Average")
        print("3. Failed")
        print("4. Not Attempted")

        choice = input("Enter choice: ").strip()

        options = {
            "1": "Passed",
            "2": "Average",
            "3": "Failed",
            "4": "Not Attempted"
        }

        if choice in options:

            student.mock_interview = options[choice]

            print("Mock interview status updated.")

        else:

            print("Invalid choice.")

# DISPLAY ALL STUDENTS

    def display_all_students(self):

        print("\n========== ALL STUDENTS ==========")

        if not self.students:

            print("No students registered.")

            return

        for student in self.students.values():

            student.details()

# TOP PERFORMERS

    def top_performers(self):

        print("\n========== TOP PERFORMERS ==========")

        if not self.students:

            print("No students available.")

            return

        sorted_students = sorted(
            self.students.values(),
            key=lambda student: student.overall_progress(),
            reverse=True
        )

        top_students = sorted_students[:5]

        for position, student in enumerate(
            top_students,
            start=1
        ):

            print(
                position,
                ".",
                student.name,
                "-",
                student.overall_progress(),
                "%"
            )

# STUDENTS NEEDING IMPROVEMENT

    def students_needing_improvement(self):

        print(
            "\n========== STUDENTS NEEDING IMPROVEMENT =========="
        )

        found = False

        for student in self.students.values():

            if student.overall_progress() < 60:

                print(
                    student.get_student_id(),
                    "-",
                    student.name,
                    "-",
                    student.overall_progress(),
                    "%"
                )

                found = True

        if not found:

            print(
                "No students currently need improvement."
            )
            
# PLACEMENT ELIGIBILITY

    def placement_eligible_students(self):

        print(
            "\n========== PLACEMENT ELIGIBLE STUDENTS =========="
        )

        found = False

        for student in self.students.values():

            if student.placement_eligibility() == "Eligible":

                print(
                    student.get_student_id(),
                    "-",
                    student.name
                )

                found = True

        if not found:

            print("No eligible students found.")

# OVERALL PROGRESS REPORT

    def progress_report(self):

        print("\n========== PROGRESS REPORT ==========")

        if not self.students:

            print("No students available.")

            return

        for student in self.students.values():

            print(
                student.get_student_id(),
                "|",
                student.name,
                "| Progress:",
                student.overall_progress(),
                "%",
                "| Category:",
                student.performance_category()
            )

# TXT FILE STORAGE


    def save_to_file(self):

        try:

            with open(DATA_FILE, "w") as file:

                for student in self.students.values():

                    line = (
                        f"{student.get_student_id()}|"
                        f"{student.name}|"
                        f"{student.email}|"
                        f"{student.phone}|"
                        f"{student.batch}|"
                        f"{student.attendance}|"
                        f"{student.python_score}|"
                        f"{student.sql_score}|"
                        f"{student.excel_score}|"
                        f"{student.powerbi_score}|"
                        f"{student.project_status}|"
                        f"{student.practice_sessions}|"
                        f"{student.mock_interview}\n"
                    )

                    file.write(line)

            print("\nData saved successfully to", DATA_FILE)

        except Exception as error:

            print("Error while saving data:", error)

# LOAD FROM TXT FILE

    def load_from_file(self):

        if not os.path.exists(DATA_FILE):

            return

        try:

            with open(DATA_FILE, "r") as file:

                for line in file:

                    line = line.strip()

                    if not line:
                        continue

                    data = line.split("|")

                    if len(data) != 13:
                        continue

                    student = Student(
                        student_id=data[0],
                        name=data[1],
                        email=data[2],
                        phone=data[3],
                        batch=data[4],
                        attendance=float(data[5]),
                        python_score=float(data[6]),
                        sql_score=float(data[7]),
                        excel_score=float(data[8]),
                        powerbi_score=float(data[9]),
                        project_status=data[10],
                        practice_sessions=int(data[11]),
                        mock_interview=data[12]
                    )

                    self.students[data[0]] = student

                    batch_name = data[4]

                    if batch_name not in self.batches:

                        self.batches[batch_name] = Batch(
                            batch_name,
                            "Not Assigned"
                        )

                    self.batches[batch_name].add_student(
                        student
                    )

            print("Previous data loaded successfully.")

        except Exception as error:

            print("Error while loading data:", error)

# SAMPLE DATA

    def add_sample_data(self):

        if self.students:
            return

        student1 = Student(
            "ST101",
            "Bhavitesh",
            "bhavitesh@gmail.com",
            "9876543210",
            "DA-HYD-023",
            92,
            85,
            80,
            78,
            88,
            "Completed",
            12,
            "Passed"
        )

        student2 = Student(
            "ST102",
            "Rahul",
            "rahul@gmail.com",
            "9876543211",
            "DA-HYD-023",
            78,
            70,
            65,
            72,
            68,
            "Completed",
            8,
            "Passed"
        )

        student3 = Student(
            "ST103",
            "Priya",
            "priya@gmail.com",
            "9876543212",
            "DA-HYD-024",
            65,
            45,
            50,
            48,
            55,
            "Not Completed",
            3,
            "Average"
        )

        self.students["ST101"] = student1
        self.students["ST102"] = student2
        self.students["ST103"] = student3

        self.batches["DA-HYD-023"] = Batch(
            "DA-HYD-023",
            "Trainer 1"
        )

        self.batches["DA-HYD-024"] = Batch(
            "DA-HYD-024",
            "Trainer 2"
        )

        self.batches["DA-HYD-023"].add_student(student1)
        self.batches["DA-HYD-023"].add_student(student2)

        self.batches["DA-HYD-024"].add_student(student3)

    # MAIN MENU

    def menu(self):

        while True:

            print("\n")
            print("===================================================")
            print("       PLACEMENT READINESS MANAGEMENT SYSTEM")
            print("===================================================")

            print("1.  Register Student")
            print("2.  Create Batch")
            print("3.  Show Batches")
            print("4.  Update Attendance")
            print("5.  Enter Technical Scores")
            print("6.  Update Project Status")
            print("7.  Update Practice Sessions")
            print("8.  Update Mock Interview")
            print("9.  Search Student")
            print("10. Display All Students")
            print("11. Top Performers")
            print("12. Students Needing Improvement")
            print("13. Placement Eligibility")
            print("14. Overall Progress Report")
            print("15. Save Data to TXT")
            print("16. Show Total Students")
            print("17. Exit")

            print("===================================================")

            choice = input(
                "Enter your choice: "
            ).strip()

            # MENU OPTIONS

            if choice == "1":

                self.register_student()

            elif choice == "2":

                self.create_batch()

            elif choice == "3":

                self.show_batches()

            elif choice == "4":

                self.update_attendance()

            elif choice == "5":

                self.update_scores()

            elif choice == "6":

                self.update_project()

            elif choice == "7":

                self.update_practice()

            elif choice == "8":

                self.update_mock_interview()

            elif choice == "9":

                self.search_student()

            elif choice == "10":

                self.display_all_students()

            elif choice == "11":

                self.top_performers()

            elif choice == "12":

                self.students_needing_improvement()

            elif choice == "13":

                self.placement_eligible_students()

            elif choice == "14":

                self.progress_report()

            elif choice == "15":

                self.save_to_file()

            elif choice == "16":

                print(
                    "\nTotal Students:",
                    Student.get_total_students()
                )

            elif choice == "17":

                self.save_to_file()

                print(
                    "\nThank you for using the system!"
                )

                break

            else:

                print(
                    "\nInvalid choice. Please try again."
                )


# MAIN PROGRAM

def main():

    print("\n=============================================")
    print(" Welcome to Placement Management System")
    print("=============================================")

    system = PlacementManagementSystem()

    # Load previous saved data
    system.load_from_file()

    # If no saved data exists, add sample data
    if not system.students:

        system.add_sample_data()

    # Start menu
    system.menu()

# ============================================================

if __name__ == "__main__":
    main()
