import pytest
from task import Teacher

teacher = Teacher('Иван Петров',"БГПУ","4")
def test_1_teacher_init(data_teacher_init):
    assert len(teacher.teacher_dict) == 1

def test_2_get_name(data_teacher_init):
    assert teacher.get_name() == 'Иван Петров'

def test_3_get_education(data_teacher_init):
    assert teacher.get_education() == 'БГПУ'

def test_4_get_xp(data_teacher_init):
    assert teacher.get_xp() == '4'

def test_5_teacher_data(data_teacher_init):
        assert teacher.get_teacher_data() == "Иван Петров, образование БГПУ, опыт работы 4 года"

def test_6_add_mark(data_teacher_init):
        assert teacher.add_mark('student_name','student_mark') == 'Иван Петров поставил оценку student_mark студенту student_name'

def test_7_remove_mark(data_teacher_init):
        assert teacher.remove_mark('student_name','student_mark') == 'Иван Петров удалил оценку student_mark студенту student_name'

def test_8_give_a_consultation(data_teacher_init):
        assert teacher.give_a_consultation('student_class') == 'Иван Петров провел консультацию в классе student_class'

def test_7_teacher_fire(data_teacher_init):
        assert teacher.teacher_fire() == 'Учитель Иван Петров был уволен'
        assert teacher.teacher_fire() == 'Учителя Иван Петров уже уволили'
        assert teacher.teacher_dict == {}