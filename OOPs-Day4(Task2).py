
class Person:
    def __init__(self, name):
        self.name = name

    def display_person(self):
        print("Name:", self.name)

class Student(Person):
    def __init__(self, name, student_id):
        Person.__init__(self, name)
        self.student_id = student_id

    def display_student(self):
        print("Student ID:", self.student_id)


class SportsPlayer(Person):
    def __init__(self, name, sport_name):
        Person.__init__(self, name)
        self.sport_name = sport_name

    def display_sports_player(self):
        print("Sport Name:", self.sport_name)


class CollegeStudent(Student, SportsPlayer):
    def __init__(self, name, student_id, sport_name, college_name):

        Student.__init__(self, name, student_id)
        SportsPlayer.__init__(self, name, sport_name)

        self.college_name = college_name

    def display_college_student(self):
        print("College Name:", self.college_name)


cs = CollegeStudent("John", 101, "Football", "ABC College")

cs.display_person()
cs.display_student()
cs.display_sports_player()
cs.display_college_student()

