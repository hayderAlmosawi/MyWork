from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Student(models.Model):
    StudentName = models.CharField(max_length=50)
    SurName = models.CharField(max_length=50)
    UniversityStage = models.CharField(max_length=45)
    Gender = models.CharField(max_length=45)
    Address = models.CharField(max_length=50)
    BirthDate = models.DateField()
    Phone = models.CharField(max_length=20)
    Subject_ID = models.ForeignKey('Subject', on_delete=models.CASCADE)
    Department_ID = models.ForeignKey('Department',on_delete=models.CASCADE)

    def __str__(self):
        return self.StudentName




class Marks(models.Model):
    Student_ID = models.ForeignKey(Student,on_delete=models.CASCADE)
    SubjectName = models.CharField(max_length=50)
    FirstCourse=models.IntegerField()
    SecondCourse=models.IntegerField()
    Average=models.IntegerField()
    FinalExam=models.IntegerField()
    Result=models.CharField(max_length=20)

    def __str__(self):
        return self.SubjectName




class Subject(models.Model):

    SubjectName = models.CharField(max_length=50)
    SubjectDate = models.TimeField()
    ClassRoomNumber = models.IntegerField()

    def __str__(self):
        return self.SubjectName




class Department(models.Model):

    DepartmentName = models.CharField(max_length=50)

    def __str__(self):
        return self.DepartmentName





class Specilization(models.Model):
    Specilization_ID = models.primary_key=True
    Specilization = models.CharField(max_length=50)

    def __str__(self):
        return self.Specilization




class ScientificResearch(models.Model):
    Research_ID = models.primary_key=True
    ResearchTitle = models.CharField(max_length=100)

    def __str__(self):
        return self.ResearchTitle





class Teacher(models.Model):
    Teacher_ID = models.primary_key=True
    TeacherName = models.CharField(max_length=50)
    SurName = models.CharField(max_length=50)
    Address = models.CharField(max_length=50)
    Phone = models.CharField(max_length=20)
    Specilization = models.ForeignKey(Specilization,on_delete=models.CASCADE)
    Research = models.ForeignKey(ScientificResearch,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.Teacher_ID





class Teacher_Subject(models.Model):
    ID = models.primary_key=True
    Subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    Teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)









