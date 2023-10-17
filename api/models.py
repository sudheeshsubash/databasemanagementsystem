from django.db import models



class Student(models.Model):
    name = models.CharField(max_length=50)
    batch = models.IntegerField()
    school = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.name}|{self.batch}"



class Person(models.Model):
    name = models.CharField( max_length=50)
    age = models.IntegerField()
    place = models.CharField( max_length=50)

    def __str__(self) -> str:
        return f"{self.name}|{self.age}"