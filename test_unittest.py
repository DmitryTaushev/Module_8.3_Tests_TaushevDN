import unittest
from task import Teacher

class TestTeacher(unittest.TestCase):
    teacher = Teacher("Иван Петров","БГПУ","4")
    
    def test_1_init(self):
        self.assertEqual(len(Teacher.teacher_dict),1)

    def test_2_get_name(self):
        self.assertEqual(self.teacher.get_name(), 'Иван Петров')

    def test_3_get_education(self):
        self.assertEqual(self.teacher.get_education(), 'БГПУ')

    def test_4_set_xp(self):
        self.assertEqual(self.teacher.get_xp(), '4')

    def test_5_teacher_data(self):
        self.assertEqual(self.teacher.get_teacher_data(), "Иван Петров, образование БГПУ, опыт работы 4 года")

    def test_6_add_mark(self):
        self.assertEqual(self.teacher.add_mark('student_name','student_mark'), 'Иван Петров поставил оценку student_mark студенту student_name')

    def test_7_remove_mark(self):
        self.assertEqual(self.teacher.remove_mark('student_name','student_mark'),'Иван Петров удалил оценку student_mark студенту student_name')

    def test_8_give_a_consultation(self):
        self.assertEqual(self.teacher.give_a_consultation('student_class'),'Иван Петров провел консультацию в классе student_class')

    def test_7_teacher_fire(self):
        self.assertEqual(self.teacher.teacher_fire(), 'Учитель Иван Петров был уволен')
        self.assertEqual(self.teacher.teacher_fire(), 'Учителя Иван Петров уже уволили')
        self.assertEqual(Teacher.teacher_dict, {})