import pprint

from database import create_cursor, connection, find_match_query


def list_syllabus():
    query = 'select * from syllabus'
    cursor = create_cursor()
    cursor.execute(query)
    return cursor.fetchall()


def search(id, major_id, course_name, credit_points,
           background_knowledge, textbook, reference, course_content, objectives, **kwargs):
    cursor = create_cursor()
    cursor.execute(
        'select * from syllabus where id=%s or major_id=%s or course_name like %s or credit_points_inECTs=%s or '
        'background_knowledge like %s or ref_literature like %s or textbook like %s or course_content like %s or '
        'objectives like %s',
        (id, major_id, course_name, credit_points, background_knowledge, textbook, reference, course_content,
         objectives))
    return cursor.fetchall()


def create_course(id, major_id, course_name, credit_points,
                  background_knowledge, textbook, reference, course_content, objectives,
                  lecture, tutor, practice, attendance, exercises, assignments, reports, midterm, final, **kwargs):
    cursor = create_cursor()
    cursor.execute('insert into syllabus values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s)', (
        id, major_id, course_name, credit_points, background_knowledge, textbook,
        reference, course_content, objectives, lecture, tutor, practice, attendance,
        exercises, assignments, reports, midterm, final))
    connection.commit()


def update_course(id, major_id, course_name, credit_points,
                  background_knowledge, textbook, reference, course_content, objectives,
                  lecture, tutor, practice, attendance, exercises, assignments, reports, midterm, final, **kwargs):
    cursor = create_cursor()
    cursor.execute(
        "update syllabus set major_id=%s, course_name=%s, credit_points_inECTs=%s, background_knowledge=%s, "
        "textbook=%s, ref_literature=%s, course_content=%s, objectives=%s, lecture=%s, tutorial=%s, practical=%s, "
        "attendance=%s, exercise=%s, assignment=%s, report=%s, midterm=%s, final=%s where id=%s",
        (major_id, course_name, credit_points, background_knowledge, textbook, reference, course_content,
         objectives, lecture, tutor, practice, attendance, exercises, assignments, reports,
         midterm, final, id))
    connection.commit()


def delete_course(id):
    cursor = create_cursor()
    cursor.execute('delete from syllabus where id = %s', id)
    connection.commit()


if __name__ == '__main__':
    pprint.pprint(list_syllabus())
