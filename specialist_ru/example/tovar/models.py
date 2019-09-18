from django.db import models

# Create your models here.

class Tovar(models.Model):
    title = models.CharField(max_length=120, unique=True, )
    article = models.CharField(max_length=16, null=True, blank=True, unique=True)
    description = models.TextField(max_length=126, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=0, blank=True)
    group = models.ForeignKey('tovar.Group', on_delete=models.PROTECT, null=True)
    tags = models.ManyToManyField('tovar.Tag')



    def __str__(self):
        if self.article is None:
            return f'(----) {self.title}'

        else:
            return f'({self.article}) {self.title}'

class Group(models.Model):
    title = models.CharField(max_length=120, unique=True)
    code = models.CharField(max_length=18, unique=True)
    skoro = models.NullBooleanField()

    @property
    def full_title(self):
        return f'{self.code} {self.title}'

    def __str__(self):
        return self.full_title


class Tag(models.Model):
    title = models.CharField(max_length=32, unique=True, primary_key=True)

    def __str__(self):
        return self.title