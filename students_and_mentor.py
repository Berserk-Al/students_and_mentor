class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.grades_of_lecturers = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in self.grades_of_lecturers:
                self.grades_of_lecturers[course] += [grade]
            else:
                self.grades_of_lecturers[course] = [grade]
        else:
            return 'Ошибка'

    def _get_avg_grade(self):
        total_grades = sum(sum(grades) for grades in self.grades.values()) if self.grades else 0 # Handle empty grades
        total_courses = len(self.grades) if self.grades else 0 # Handle empty grades

        return total_grades / total_courses if total_courses else 0


    def __str__(self):
        avg_grade = self._get_avg_grade()
        courses_in_progress_str = ", ".join(self.courses_in_progress)
        finished_courses_str = ", ".join(self.finished_courses)
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {avg_grade}\nКурсы в процессе изучения: {courses_in_progress_str}\nЗавершенные курсы: {finished_courses_str}"

    def __lt__(self, other):
        return self._get_avg_grade() < other._get_avg_grade()

    def __gt__(self, other):
        return self._get_avg_grade() > other._get_avg_grade()

    def __eq__(self, other):
        return self._get_avg_grade() == other._get_avg_grade()



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_of_lecturer = {}

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

        def _get_avg_grade(self):
            total_grades = sum(sum(grades) for grades in
                               self.grades_of_lecturer.values()) if self.grades_of_lecturer else 0  # Handle empty grades
            total_courses = len(self.grades_of_lecturer) if self.grades_of_lecturer else 0  # Handle empty grades
            return total_grades / total_courses if total_courses else 0

        def __str__(self):
            avg_grade = self._get_avg_grade()
            return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg_grade}"

        def __lt__(self, other):
            return self._get_avg_grade() < other._get_avg_grade()

        def __gt__(self, other):
            return self._get_avg_grade() > other._get_avg_grade()

        def __eq__(self, other):
            return self._get_avg_grade() == other._get_avg_grade()

        best_student = Student('Ruoy', 'Eman', 'your_gender')
        best_student.courses_in_progress += ['Python']

        cool_mentor = Mentor('Some', 'Buddy')
        cool_mentor.courses_attached += ['Python']

        cool_reviewer = Reviewer('Reviewer', 'Name')
        cool_reviewer.courses_attached += ['Python']

        cool_lecturer = Lecturer('Lecturer', 'Surname')
        cool_lecturer.courses_attached += ['Python']

        cool_reviewer.rate_hw(best_student, 'Python', 10)
        cool_reviewer.rate_hw(best_student, 'Python', 10)
        cool_reviewer.rate_hw(best_student, 'Python', 10)

        best_student.rate_lecturer(cool_lecturer, 'Python', 9)
        best_student.rate_lecturer(cool_lecturer, 'Python', 8)

        print(best_student.grades)
        print(cool_lecturer.grades_of_lecturer)
        print(best_student)
        print(cool_lecturer)
        print(cool_reviewer)