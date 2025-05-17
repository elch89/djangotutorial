from ..models import Course, Lesson

class CourseService:

    @staticmethod
    def get_all_courses():
        return Course.objects.prefetch_related('lessons').all()

    @staticmethod
    def get_course_by_id(course_id):
        try:
            return Course.objects.prefetch_related('lessons').get(course_id=course_id)
        except Course.DoesNotExist:
            return None

    @staticmethod
    def create_course(data):
        return Course.objects.create(**data)

    @staticmethod
    def update_course(course_id, data):
        course = CourseService.get_course_by_id(course_id)
        if course:
            for key, value in data.items():
                setattr(course, key, value)
            course.save()
            return course
        return None

    @staticmethod
    def delete_course(course_id):
        course = CourseService.get_course_by_id(course_id)
        if course:
            course.delete()
            return True
        return False


class LessonService:

    @staticmethod
    def get_all_lessons():
        return Lesson.objects.select_related('course').all()

    @staticmethod
    def get_lessons_by_course(course_id):
        return Lesson.objects.filter(course__course_id=course_id)

    @staticmethod
    def get_lesson_by_id(lesson_id):
        try:
            return Lesson.objects.get(id=lesson_id)
        except Lesson.DoesNotExist:
            return None

    @staticmethod
    def create_lesson(data):
        return Lesson.objects.create(**data)

    @staticmethod
    def update_lesson(lesson_id, data):
        lesson = LessonService.get_lesson_by_id(lesson_id)
        if lesson:
            for key, value in data.items():
                setattr(lesson, key, value)
            lesson.save()
            return lesson
        return None

    @staticmethod
    def delete_lesson(lesson_id):
        lesson = LessonService.get_lesson_by_id(lesson_id)
        if lesson:
            lesson.delete()
            return True
        return False
