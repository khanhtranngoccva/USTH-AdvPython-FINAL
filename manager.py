import pprint

from database import create_cursor, connection, find_match_query


def list_syllabus():
    query = 'select * from syllabus'
    cursor = create_cursor()
    cursor.execute(query)
    return cursor.fetchall()


def list_majors():
    query = 'select major_id from syllabus'
    cursor = create_cursor()
    cursor.execute(query)
    return list(set(map(lambda item: item[0].strip(" "), cursor)))


def search(id, major_id, course_name, credit_points,
           background_knowledge, textbook, reference, course_content, objectives, **kwargs):
    cursor = create_cursor()
    args = (id, major_id, course_name, credit_points, background_knowledge,
            textbook, reference, course_content,
            objectives)
    cursor.execute(
        'select * from syllabus where compareFuzzy(id, %s) and compareFuzzy(major_id, %s) and compareFuzzy(course_name, %s) and '
        'compareFuzzy(credit_points_inECTs, %s) and compareFuzzy(background_knowledge, %s) and compareFuzzy(ref_literature, %s) and '
        'compareFuzzy(textbook, %s) and compareFuzzy(course_content, %s) and compareFuzzy(objectives, %s)',
        args)
    result = cursor.fetchall()
    pprint.pprint(result)
    return result


def create_course(major_id, course_name, credit_points,
                  background_knowledge, textbook, reference, course_content, objectives,
                  lecture, tutor, practice, attendance, exercises, assignments, reports, midterm, final, **kwargs):
    cursor = create_cursor()
    cursor.execute('insert into syllabus values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s)', (
        None, major_id, course_name, credit_points, background_knowledge, textbook,
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
