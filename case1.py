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


for city in City.objects.filter(user__name__istartswith='ива'):
    print(city.name)


'''
Таблица city                 Таблица user
+----+--------------+        +----+-----------+---------+
| id | name         |        | id | name      | city_id |
+====+==============+        +====+===========+=========+
| 1  | Москва       |        | 1  | Иванов    | 1       |
+----+--------------+        +----+-----------+---------+
| 2  | Воронеж      |        | 2  | Петров    | 1       |
+----+--------------+        +----+-----------+---------+
| 3  | Новороссийск |        | 3  | Ивашкин   | 2       |
+----+--------------+        +----+-----------+---------+
                             | 4  | Иващенко  | 2       |
                             +----+-----------+---------+
                             | 5  | Сидоров   | 2       |
                             +----+-----------+---------+
                             | 6  | Баширов   | 3       |
                             +----+-----------+---------+
                             | 7  | Иванушкин | 1       |
                             +----+-----------+---------+

В консоль выводится: 
    Москва 
    Воронеж
    Воронеж
    Москва 

Почему выводятся дубликаты городов и как их убрать?
'''
