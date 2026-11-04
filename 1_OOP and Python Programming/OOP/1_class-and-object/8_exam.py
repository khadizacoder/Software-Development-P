# class Exam():

#     def __init__(self, mark):
#         self.mark = mark
#         self.min_mark = 0
#         self.max_mark = 100

#     def main_mark(self):
#         return self.mark
    
#     def add_mark(self, number):
#         if number > self.min_mark and number < self.max_mark:
#             self.mark += number

# samia = Exam(10)

# print(samia.main_mark())
# samia.add_mark(20)
# print(samia.main_mark())
    

class Exam():
    def __init__(self, marks):
        self.marks = marks
        self.min_marks = 0
        self.max_marks = 100

    def main_marks(self):
        return self.marks

    def add_marks(self, num):
        if num > self.min_marks and num < self.max_marks:
            self.marks += num
        else: 
            return f'Please add valid number maximun add {self.max_marks} and minimum {self.min_marks}'

naima = Exam(20)
print(naima.main_marks())
naima.add_marks(150)
print(naima.add_marks(200))
