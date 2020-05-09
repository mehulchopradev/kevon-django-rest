# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField(blank=True, null=True)
    pages = models.IntegerField()
    no_of_copies = models.IntegerField()
    published_date = models.DateField(blank=True, null=True)
    publication_house = models.ForeignKey('Publicationhouse', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'libapp_book'


class BookStudents(models.Model):
    book = models.ForeignKey(Book, models.DO_NOTHING)
    student = models.ForeignKey('Student', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'libapp_book_students'
        unique_together = (('book', 'student'),)


class Booksissued(models.Model):
    issue_date = models.DateField()
    return_date = models.DateField(blank=True, null=True)
    book_id = models.IntegerField()
    student_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'libapp_booksissued'


class Publicationhouse(models.Model):
    name = models.CharField(max_length=50)
    ratings = models.IntegerField()

    # book_set

    class Meta:
        managed = False
        db_table = 'libapp_publicationhouse'


class Review(models.Model):
    description = models.CharField(max_length=100)
    full_name = models.CharField(max_length=20)
    book = models.ForeignKey(Book, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'libapp_review'


class Student(models.Model):
    username = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=20)
    country = models.CharField(max_length=3, blank=True, null=True)
    gender = models.CharField(max_length=1)
    profilepicpath = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'libapp_student'
