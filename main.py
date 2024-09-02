class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    def rate(self, lector, course, grade):
        if (isinstance(lector, Lecturer) and course in self.courses_in_progress and course in lector.courses_attached
                and grade in range(0,10)) :
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            pass #print(f'студент {self.surname} - оценка - лектор {lector.surname}  {course} конфликт !!! ')

    def avg_grade(self):
        sum_val = 0
        i = 0
        for key,value in self.grades.items():
            for val in value:
                sum_val += val
                i += 1
        return sum_val/i if i>0 else 0
    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания {self.avg_grade()}\n'
                f'Курсы в процессе изучения {self.courses_in_progress} \nЗавершенные курсы {self.finished_courses}\n')

    def __eq__(self, other):
        return self.avg_grade() == other.avg_grade()

    def __le__(self, other):
        return self.avg_grade() <= other.avg_grade()

    def __lt__(self, other):
        return self.avg_grade() < other.avg_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}



class Lecturer(Mentor):  # К заданию №1 добавлен класс - наследник Лектор
    def avg_grade(self):
        sum_val = 0
        i = 0
        for key,value in self.grades.items():
            for val in value:
                sum_val += val
                i += 1
        return sum_val/i if i>0 else 0

    def __eq__(self, other):
        return self.avg_grade() == other.avg_grade()

    def __le__(self, other):
        return self.avg_grade() <= other.avg_grade()

    def __lt__(self, other):
        return self.avg_grade() < other.avg_grade()

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции {self.avg_grade()}\n'

class Reviewer(Mentor):   # К заданию №1 добавлен класс - наследник Проверяющий
    def rate(self, student, course, grade):
        if (isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress
                                        and grade in range(0,10)):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
             pass #print (f'эксперт {self.surname}  -оценка- студент {student.surname}  {course} конфликт !!! ')

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n'

# функция подсчета среднего балла оценки суммарно по списку студентов (преподавателей) 1 аргумент в разрезе курса 2 арг.
#  задании требовалось 2 функции по студентам и преподавателям, но тк механизм учета оценок одинаков , применима единая
# функция
def avg_summ(students,course):
    sum_bal = 0
    i =0
    for person in students:

        value = person.grades.get(course)
        if value != None:
            for bal in value:
                sum_bal += bal
                i +=1

    return sum_bal/i if i>0 else 0




Student1 = Student('Незнайка', 'Балбесов')
Student1.courses_in_progress += ['Python']
Student1.courses_in_progress += ['Java']


Student2 = Student('Цветик', 'Ренуар')
Student2.courses_in_progress += ['WEB-design']
Student2.courses_in_progress += ['C++']
Student2.courses_in_progress += ['Python']
Student2.finished_courses+=['Рыболовство']
Student2.finished_courses+=['Кройка']

Student3 = Student('Илья', 'Репин')
Student3.courses_in_progress += ['WEB-design']


Reviz1 = Reviewer('Иван', 'Хлестаков')  #создаем эксперта
Reviz1.courses_attached += ['Python']  # закрепляем за проверяющими экспертами области знаний (курсов)

Reviz2 = Reviewer('Василий', 'Ноздрев') # то-же для другого эксперта
Reviz2.courses_attached += ['Java']
Reviz2.courses_attached += ['WEB-design']
Reviz2.courses_attached += ['C++']

Lect1 = Lecturer('Иван',"Тургенев") # создаем лекторов
Lect1.courses_attached += ['Python']
Lect1.courses_attached += ['WEB-design']

Lect2 = Lecturer('Александр',"Пушкин")
Lect2.courses_attached += ['C++']
Lect2.courses_attached += ['WEB-design']


# начинаем ставить оценки

# Проверяющие оценивают знания в студента в соотв. курсе
Reviz1.rate(Student1, 'Python', 10)  #  Должно зайти
Reviz1.rate(Student1, 'Java', 8) # тест Э. яву не знает
Reviz1.rate(Student1, 'WEB-design', 3) # тест С. веб не изучает

Reviz1.rate(Student2, 'Python', 10)  # Должно зайти
Reviz1.rate(Student2, 'Java', 8) # Э. яву не знает
Reviz1.rate(Student2, 'C++', 5) # тест . попасть не должно тк студент С++ не изучает

Reviz2.rate(Student1, 'Python', 10)  # Проверяющие оценивают знания в студента в соотв. курсе
Reviz2.rate(Student1, 'Java', 8)
Reviz2.rate(Student1, 'Java', 88) # оценка слишком большая. не пройдет

Reviz2.rate(Student1, 'C++', 5)  # Тест Э. С++ не знает

Reviz2.rate(Student2, 'Python', 10)  # Студент Питон не учит  конфликтнет
Reviz2.rate(Student2, 'WEB-design', 8)  # должно зайти
Reviz2.rate(Student2, 'WEB-design', 9)  # должно зайти
Reviz2.rate(Student2, 'C++', 5) # должно зайти

Reviz2.rate(Student3, 'WEB-design', 8)  # должно зайти


# Студенты оценивают лекторов
Student1.rate(Lect1, 'Python',10)  # должно зайти
Student1.rate(Lect2, 'WEB-design',10) # студент не учит веб

Student2.rate(Lect2, 'WEB-design',10)
Student2.rate(Lect1, 'WEB-design',2)
Student2.rate(Lect2, 'Python',8)

Student3.rate(Lect1, 'WEB-design',1)
Student3.rate(Lect2, 'WEB-design',1)

Student1.rate(Lect1, 'Python',6)
Student2.rate(Lect2, 'C++',4)
Student2.rate(Lect2, 'C++',14) ## too big rate



print(Lect1)   # str для лекторов
print(Lect2)

print(Student1)   # str для студентов
print(Student2)
print(Student3)

print(Student1 == Student2)
print(Student1 > Student2)      # сравнения студентов (по среднему балу за ДЗ)
print(Student1 >= Student2)

print(Lect1 == Lect2)
print(Lect1 >= Lect2)           # Сравнение преподавателей по средней оцене их студентами
print(Lect1 > Lect2)

list_students = [Student1,Student2,Student3]
print(avg_summ(list_students,'WEB-design'))  # средние оценки по студентам курса
print(avg_summ(list_students,'Java'))
print(avg_summ(list_students,'C++'))
print(avg_summ(list_students,'Python'))

list_lectors = [Lect1,Lect2]
print(avg_summ(list_lectors,'WEB-design'))   # средние оценки по лекторам курса
print(avg_summ(list_lectors,'Java'))
print(avg_summ(list_lectors,'C++'))
print(avg_summ(list_lectors,'Python'))
