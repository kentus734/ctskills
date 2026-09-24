class AssignmentSubmission:
    def __init__(self, student_name, student_id, assignment_title, due_date):
        self.student_name = student_name
        self.student_id = student_id
        self.assignment_title = assignment_title
        self.due_date = due_date

    def __validate_grade(self, score):

        if self.__check_submission_status() == "Not Submitted":
            return 0  <= score <= 100

    def __check_submission_status(self):
        if hasattr(self, 'files') and self.files:
            return "Submitted"
        else:
            return "Missing"

    def __is_duplicate(self, filename=str):
        if filename in self.files:
            return "[Warning] '{filename}' already attatched!"
        else:
            pass

    def add_file(self, filename=str):
        if not hasattr(self, 'files'):
            self.files = []
        if self.__is_duplicate(filename):
            print(f"[Warning] '{filename}' already attatched!")
        else:
            self.files.append(filename)
            print(f"[Success] {self.student_name} attatched '{filename}'. Total Files: {len(self.files)}")

    def remove_file(self, filename=str):
        if hasattr(self, 'grade'):
            print("[Warning] Maria Santos cannot remove files. Assignment already graded.")
        elif hasattr(self, 'files') and filename in self.files:
            self.files.remove(filename)
            print(f"[Success] {self.student_name} removed '{filename}'.")
        else:
            print(f"[Error] '{filename}' not found in {self.student_name}'s submission.")

    def assign_grade(self, score=float):
        if self.__check_submission_status() == "Submitted":
            self.grade = score
            print(f"[Success] Grade {score} officially assigned to {self.student_name}.")
        else:
            print(f"[Error] Cannot grade. No files submitted by {self.student_name}.")

    def get_grade(self):
        if hasattr(self, 'grade'):
            return self.grade
        else:
            return None

    def view_files(self):
        if hasattr(self, 'files'):
            return self.files
        else:
            return []

    def get_status_report(self):
        submission_status = self.__check_submission_status()
        grade = self.get_grade()
        files = self.view_files()
        report = f"ID: {self.student_id} | Name: {self.student_name} | Status: {submission_status} {'(' + str(len(files)) + ' files' ')' if (files) else ''} | Grade: {grade if grade is not None else 'Not Graded'}"

        return report
        
    

print("--- INITIALIZING DROPBOX FOR STUDENTS ---")
student1 = AssignmentSubmission(student_name="Alex Gonzaga", student_id="pshs-1090-x", assignment_title="CS-101", due_date="2026-10-01")
student2 = AssignmentSubmission(student_name="Adelle", student_id="pshs-1920-x", assignment_title="CS-103", due_date="2026-10-01")
student3 = AssignmentSubmission(student_name="Juan dela Cruz", student_id="pshs-1033-x", assignment_title="CS-101", due_date="2026-10-01")
student4 = AssignmentSubmission(student_name="Maria Santos", student_id="pshs-1044-x", assignment_title="CS-101", due_date="2026-10-01")
student5 = AssignmentSubmission(student_name="Jose Reyes", student_id="pshs-1055-x", assignment_title="CS-101", due_date="2026-10-01")
print()

print("--- TEST SCENARIO 1: Multiple Files via List ---")
student1.add_file("main.py")
student1.add_file("report.pdf")
student1.assign_grade(95)
print(f"Alex's Files: {student1.view_files()}\n")

print("--- TEST SCENARIO 2: Removing Files from List ---")
student2.add_file("wrong_homework.docx")
student2.remove_file("wrong_homework.docx")
student2.add_file("correct_project.py")
student2.assign_grade(88)
print(f"Adelle's Files: {student2.view_files()}\n")

print("--- TEST SCENARIO 3: Preventing Duplicate Files ---")
student3.add_file("script.py")
student3.add_file("script.py") # Should trigger private duplicate check
print(f"Juan's Files: {student3.view_files()}\n")

print("--- TEST SCENARIO 4: Removing file after being graded ---")
student4.add_file("exam_answers.pdf")
student4.assign_grade(75)
student4.remove_file("exam_answers.pdf") # Blocked by grading status
print()

print("--- TEST SCENARIO 5: Empty List Handling ---")
student5.add_file("draft.txt")
student5.remove_file("draft.txt") 
student5.assign_grade(100) # Should fail because list is empty
print()

print("--- FINAL  SYSTEM REPORT ---")
print(student1.get_status_report())
print(student2.get_status_report())
print(student3.get_status_report())
print(student4.get_status_report())
print(student5.get_status_report())

