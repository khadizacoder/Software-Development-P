class Students:

    def __init__(self, name, cls, id):
        self.name = name
        self.id = id
        self.cls = cls

    def __repr__(self):
        return f'student with name: {self.name}, class: {self.cls} and student id: {self.id}'

    
alia = Students('Alia', 10, 4054)
print(alia)


class Teacher:
    def __init__(self, name, subject, id) -> None:
        self.name = name
        self.subject = subject
        self.id = id

    def __repr__(self) -> str:
        return f'Teacher name: {self.name}, Subject {self.subject} and teacher id: {self.id}'


alamin = Teacher("Alamin", "Economic", 9845936)
print(alamin)


class School:
    def __init__(self, name) -> None:
        self.name = name
        self.teachers = []
        self.students = []

    def add_teacher(self, name, subject, id):
        id = len(self.teachers) + 100
        teacher = Teacher(name, subject, id)
        self.teachers.append(teacher)

    def enroll(self, name, fee):
        if fee < 6500:
            print('Not anough fee')
        else:
            id = len(self.students) + 1
            student = Students(name, 'C', id)
            self.students.append(student)
            print(f'{name} is enrolled with id {id} extra money {fee - 6500}')

    def __repr__(self):
        print(f'Welcome to {self.name}')


phitron = School('Phitron')
phitron.enroll("alia", 7000)
phitron.enroll("manika", 4000)
phitron.enroll("minni", 6500)