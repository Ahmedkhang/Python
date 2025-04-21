class Student:
    def __init__(self,name,roll_no,physics,chemistry,maths,programming):
        self.name = name
        self.roll_no = roll_no
        self.physics = physics
        self.chemistry = chemistry
        self.maths = maths
        self.programming = programming
    def total_marks(self):
        return self.physics + self.chemistry + self.maths + self.programming    
    def calculate_avg(self):
        return (self.physics + self.chemistry + self.maths + self.programming) / 4
    def get_grade(self):
        avg_marks = self.calculate_avg()
        if avg_marks >= 90:
          return 'A'
        elif avg_marks >= 80:
            return 'B'
        elif avg_marks >= 70:
            return 'C'
        elif avg_marks  >= 60:
            return 'D'
        else:
            return 'F'

    def display_info(self):
        print('--------- Student Report ---------')
        print(f'Student Name : {self.name}')
        print(f'Roll Number : {self.roll_no}')
        print(f'Physics Marks : {self.physics}')
        print(f'Chemistry Marks : {self.chemistry}')
        print(f'Maths Marks : {self.maths}')
        print(f'Programming Marks : {self.programming}')
        print(f'Total Marks : {self.total_marks()}')
        print(f'Percentage : {self.calculate_avg():.2f}%')
        print(f'Grade : {self.get_grade()}')
student_list = []
try:
    
  for i in range(5):
    student_name = input('Enter a Student Name or Press Enter to Quit : ')
    if student_name == '':
        break
    roll_no = int(input('Enter a roll no : '))
    physics_marks = int(input('Enter Physics marks : '))
    chemistry_marks = int(input('Enter Chemistry marks : '))
    maths_marks = int(input('Enter Maths marks : '))
    programming_marks = int(input('Enter Programming marks : '))
        
    students = Student(student_name,roll_no,physics_marks,chemistry_marks,maths_marks,programming_marks)
    student_list.append(students) 
    students.display_info() 
except Exception as e:
    print(e)
    print('Sorry For Inconvenience')

# avg_marks = students.calculate_avg()
# grade = students.get_grade()
# print(grade)  
# print(avg_marks)

# print(display_info)
# print(student_list)