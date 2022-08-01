class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecture, course, grade):
        if isinstance(lecture, Lecturer) and course in self.courses_in_progress and course in lecture.courses_attached:
            if course in Lecturer.grades:
                Lecturer.grades[course] += [grade]
            else:
                Lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        summ = 0
        counter = 0
        for items in self.grades.values():
            for value in items:
                summ += value
                counter += 1
        summ = summ/counter
        return (summ)

    def __str__(self):
        res = f'Имя: {self.name} ' \
              f'\nФамилия:{self.surname}' \
              f'\nСредняя оценка за домашние задания:{self.average_grade()} ' \
              f'\nКурсы в процессе изучения: {" ".join(self.courses_in_progress)}' \
              f'\nЗавершенные курсы: {" ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer (Mentor):
    grades = {}

    def average_grade(self):
        summ = 0
        counter = 0
        for items in self.grades.values():
            for value in items:
                summ += value
                counter += 1
        summ = summ/counter
        return (summ)

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия:{self.surname} \nСредняя оценка за лекции:{self.average_grade()}'
        return res

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()


class Reviewer (Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия:{self.surname}'
        return res

def average_student (list, course):
    summ = 0
    counter = 0
    for name in list:
        for key, value in name.grades.items():
            if key == course:
                for element in value:
                    summ+=element
                    counter+=1
    return (summ/counter)

def average_lecture (list, course):
    summ = 0
    counter = 0
    for name in list:
        for key, value in name.grades.items():
            if key == course:
                for element in value:
                    summ+=element
                    counter+=1
    return (summ/counter)

student_1 = Student('Ruoy', 'Eman', 'man')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']
student_1.finished_courses += ['Вводный курс по программированию']

student_2 = Student('Helen', 'Park', 'woman')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Git']
student_2.finished_courses += ['Вводный курс по дизайну']


reviewer_1 = Reviewer('Geoffrey', 'Cameron')
reviewer_1.courses_attached += ['Python']

reviewer_2 = Reviewer('Charles', 'Pitts')
reviewer_2.courses_attached += ['Git']

reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Python', 7)
reviewer_1.rate_hw(student_1, 'Python', 8)

reviewer_1.rate_hw(student_2, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Python', 9)
reviewer_1.rate_hw(student_2, 'Python', 6)

reviewer_2.rate_hw(student_1, 'Git', 10)
reviewer_2.rate_hw(student_1, 'Git', 8)
reviewer_2.rate_hw(student_1, 'Git', 9)

reviewer_2.rate_hw(student_2, 'Git', 8)
reviewer_2.rate_hw(student_2, 'Git', 9)
reviewer_2.rate_hw(student_2, 'Git', 8)

lecturer_1 = Lecturer('Maks', 'Korz')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['Git']

lecturer_2 = Lecturer('Agnes', 'Stokes')
lecturer_2.courses_attached += ['Python']
lecturer_2.courses_attached += ['Git']

student_1.rate_hw(lecturer_1, 'Python', 10)
student_1.rate_hw(lecturer_1, 'Python', 9)
student_1.rate_hw(lecturer_1, 'Python', 10)

student_1.rate_hw(lecturer_1, 'Git', 9)
student_1.rate_hw(lecturer_1, 'Git', 5)
student_1.rate_hw(lecturer_1, 'Git', 9)

student_2.rate_hw(lecturer_2, 'Python', 9)
student_2.rate_hw(lecturer_2, 'Python', 8)
student_2.rate_hw(lecturer_2, 'Python', 10)

student_2.rate_hw(lecturer_2, 'Git', 9)
student_2.rate_hw(lecturer_2, 'Git', 6)
student_2.rate_hw(lecturer_2, 'Git', 9)

students = [student_1, student_2]
lecturers = [lecturer_1, lecturer_2]

print(student_1)
print()
print(student_2)
print()
print(student_2>student_1)
print()
print(lecturer_1)
print()
print(lecturer_2)
print()
print(lecturer_2>lecturer_1)
print()
print(reviewer_1)
print()


print(f"Средняя оценка по всем студентам в курсе Python: {average_student(students, 'Python')}")
print(f"Средняя оценка по всем преподавателям в курсе Git: {average_lecture(lecturers, 'Git')}")

