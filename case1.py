from django.db import models


class ModelA(models.Model):

    id = models.AutoField()
    name = models.TextField()
    model_b = models.ForeignKey(ModelB)

    def __str__(self):
        return self.name


class ModelB(models.Model):

    id = models.AutoField()

    def __str__(self):
        return f'Model B: {self.id}'


for i in ModelB.objects.filter(modela__name__icontains='super model'):
    print(i.id)


'''
Дано:
    1 запись ModelB
    3 записи ModelA которые ссылаются на ModelB c name 'Super model A first', 'Super model A second' и 'Super model A third'

В консоль выводятся дубликаты идентификаторов ModelB, где ошибка?
'''
