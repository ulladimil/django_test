from django.db import models


class User(models.Model):

    id = models.AutoField()
    name = models.TextField()
    city = models.ForeignKey(city)

    def __str__(self):
        return f'User: {self.name}'


class City(models.Model):

    id = models.AutoField()
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'City: {self.name}'


for user in User.objects.filter(city__name__icontains='ново'):
    print(user.name)


'''
Дано:
    3 записи City c полями name 'Новороссийск', 'Новоотрадное' и 'Новоселово'
    1 запись User c name 'Иванов' и city которое ссылается на запись 'Новороссийск'

В консоль выводится: 
    Иванов 
    Иванов 
    Иванов 

Почему так если пользователь один? 
Что сделать чтобы пользователь выводился один раз?
'''
