class Teacher:
    teacher_dict = {}
    
    def __init__(self,name,education,xp):
        self.__name = name
        self.__education = education
        self.__xp = xp
        Teacher.teacher_dict[self.__name] = [self.__education]

    def get_name(self):
        return self.__name

    def get_education(self):
        return self.__education

    def set_xp(self,value):
        self.__xp = value

    def get_teacher_data(self):
        return print(f"{self.__name}, образование {self.__education}, опыт работы {self.__xp} года")

    def add_mark(self,student_name,student_mark):
        return print(f'{self.__name} поставил оценку {student_mark} студенту {student_name}')

    def remove_mark(self,student_name,student_mark):
        return print(f'{self.__name} удалил оценку {student_mark} студенту {student_name}')

    def give_a_consultation(self,student_class):
        return print(f'{self.__name} провел консультацию в классе {student_class}')
    
    def teacher_fire(self):
        if self.__name in Teacher.teacher_dict.keys():
            Teacher.teacher_dict.pop(self.__name)
            return f'Учитель {self.__name} был уволен'
        else:
            return f'Учителя {self.__name} уже уволили'
        

teacher = Teacher("Иван Петров","БГПУ","4")

teacher.get_teacher_data()
teacher.add_mark('Петр Борисов',"5")
teacher.remove_mark('Даниил Васильев',"3")
teacher.give_a_consultation("9Б")
print(teacher.teacher_dict)
print(teacher.teacher_fire())
print(teacher.teacher_dict)
print()

class DisciplineTeacher(Teacher):
    def __init__(self,name,education,xp,discipline,job_title):
        super().__init__(name,education,xp)
        self.__discipline = discipline
        self.__job_title = job_title

    def get_name(self):
        return self.__name

    def get_education(self):
        return self.__education

    def set_xp(self,value):
        self.__xp = value

    def get_discipline(self):
        return self.__discipline

    def set_job_title(self,value):
        self.__job_title = value

    def get_teacher_data(self):
        super().get_teacher_data()
        print(f"Предмет {self.__discipline}, должность {self.__job_title}")


    def add_mark(self,student_name,student_mark):
        super().add_mark(student_name,student_mark)
        print(f"Предмет: {self.__discipline}")


    def remove_mark(self,student_name,student_mark):
        super().remove_mark(student_name,student_mark)
        print(f"Предмет: {self.__discipline}")

    def give_a_consultation(self,student_class):
        super().give_a_consultation(student_class)
        print(f"По предмету {self.__discipline} как {self.__job_title}")

discipline = DisciplineTeacher("Иван Петров","БГПУ","4","Химия","Директор")

discipline.get_teacher_data()
discipline.add_mark('Петр Борисов',"5")
discipline.remove_mark('Даниил Петров',"3")
discipline.give_a_consultation('9Б')