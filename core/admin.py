from django.contrib import admin

from core import models


@admin.register(models.FirstModel)
class FirstModel(admin.ModelAdmin):
    list_display = ('id', 'name', 'something', 'value', 'link')
    list_display_links = ('id', 'link')


@admin.register(models.Child)
class Child(admin.ModelAdmin):
    ...


@admin.register(models.ClothingCompany)
class ClothingCompany(admin.ModelAdmin):
    list_display = ('id', 'name', 'capital', 'address')


@admin.register(models.TShirt)
class TShirt(admin.ModelAdmin):
    list_display = ('id', 'name', 'size', 'manufacturer')
    list_display_links = ('id', 'manufacturer')


@admin.register(models.Park)
class Park(admin.ModelAdmin):
    list_display = ('id', 'name', 'address')


@admin.register(models.Breed)
class Breed(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(models.Dog)
class Dog(admin.ModelAdmin):
    list_display = ('id', 'name', 'breed')
    list_display_links = ('id', 'breed')


@admin.register(models.Groupe)
class Groype(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(models.Student)
class Student(admin.ModelAdmin):
    list_display = ('id', 'name', 'birth', 'sex', 'avatar')


@admin.register(models.Teacher)
class Teacher(admin.ModelAdmin):
    list_display = ('id', 'name', 'birth', 'sex', 'grade', 'email')


@admin.register(models.MyPersonSlave)
class MyPersonSlave(admin.ModelAdmin):
    list_display = ('id', 'name', 'birth', 'sex')


@admin.register(models.Report)
class Report(admin.ModelAdmin):
    list_display = ('id', 'name', 'data')
