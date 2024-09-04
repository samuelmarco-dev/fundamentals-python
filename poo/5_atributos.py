from datetime import date

class Student:
    # atributo de classe
    school = 'Unicamp'
    
    def __init__(self, name, age, ID_STUDENT=None):
        # atributos de instância
        self.name = name
        self.age = age
        self.__ID_STUDENT = ID_STUDENT

    def __str__(self):
        return f'{self.name}, {self.age} {f'- {self.registration()}' if self.registration() else ''}'

    def __show_ID(self):
        return self.__ID_STUDENT
    
    def registration(self):
        return self.__show_ID()
    
    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school
        
    @classmethod
    def fabric_student(cls, name, year_birth):
        idade = date.today().year - year_birth
        return cls(name, idade)
        
    @staticmethod
    def is_adult(age):
        return age >= 18

student = Student('Paulo', 22, 55886633)
print(student.__str__())

# modificando o atributo para todas instâncias da classe Student
Student.change_school('UTFPR') 

student_no_default = Student.fabric_student('Joaquim', 1999)
print(student_no_default.__str__())
print(student_no_default.school)
