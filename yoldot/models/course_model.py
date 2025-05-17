from django.db import models
import uuid

class Course(models.Model):
    course_id = models.CharField(max_length=100, primary_key=True)
    banner = models.CharField(max_length=255, verbose_name="Banner")
    title = models.CharField(max_length=255, verbose_name="Title")
    course_description = models.TextField(verbose_name="Course Description")
    tags = models.JSONField(verbose_name="Tags")
    access_token = models.CharField(max_length=255, verbose_name="Access Token")
    is_free = models.BooleanField(default=False, verbose_name="Is Free")

    class Meta:
        db_table = 'course'
        managed = False

    def __str__(self):
        return self.title


class Lesson(models.Model):
    id = models.CharField(max_length=100, primary_key=True, default=uuid.uuid4)
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE, db_column='course_id')
    snapshot = models.CharField(max_length=255, verbose_name="Snapshot")
    title = models.CharField(max_length=255, verbose_name="Title")
    uri = models.CharField(max_length=255, verbose_name="URI")
    description = models.TextField(verbose_name="Description")
    duration = models.CharField(max_length=20, verbose_name="Duration")

    class Meta:
        db_table = 'lessons'
        managed = False

    def __str__(self):
        return f"{self.title} ({self.duration})"
