class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course
        self.exams = []

    def take_exam(self, exam):
        self.exams.append(exam)

    def get_exams(self):
        return self.exams

# Example usage
student1 = Student("Alice", "Computer Science")
exam1 = {"title": "Mathematics Exam", "questions": ["Question 1", "Question 2"]}

student1.take_exam(exam1)

print(student1.get_exams())