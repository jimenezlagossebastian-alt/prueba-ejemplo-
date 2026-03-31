# ==============================
# STUDENT LOGIC
# ==============================

students_list = []

def add_student(student_id, name, age, course):
    new_student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course,
        "status": "Active"
    }
    students_list.append(new_student)
    return True


def get_all():
    return students_list


def find_by_id(student_id):
    for student in students_list:
        if student["id"] == student_id:
            return student
    return None


def remove_student(student_id):
    for student in students_list:
        if student["id"] == student_id:
            students_list.remove(student)
            return True
    return False


def update_info(student_id, new_name, new_age, new_course):
    student = find_by_id(student_id)
    if student:
        student["name"] = new_name
        student["age"] = new_age
        student["course"] = new_course
        return True
    return False
