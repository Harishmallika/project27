from django.db import models

# Create your models here.

class Dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=100)
    loc=models.CharField(max_length=100)
class Employe(models.Model):
    Empno=models.IntegerField(primary_key=True)
    Ename=models.CharField(max_length=100)
    Job=models.CharField(max_length=100)
    MGR=models.IntegerField()
    HireDate=models.DateField()
    Salary=models.IntegerField()
    Comm=models.IntegerField()
    Deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)

class Salgrade(models.Model):
    Grand=models.IntegerField(primary_key=True)
    LSal=models.IntegerField()
    HSal=models.IntegerField()

class Bonus(models.Model):
    Ename=models.CharField(max_length=100)
    Job=models.CharField(max_length=100)
    Sal=models.IntegerField()
    Comm=models.IntegerField()       
