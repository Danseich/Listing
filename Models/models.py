from django.db import models


class FirstModel(models.Model):
    name = models.CharField('Название', max_length=50)
    value = models.IntegerField('Некое значение')

    def __str__(self):
        return self.name


class Mom(models.Model):
    firstname = models.CharField("Имя", max_length=30)
    surname = models.CharField("Фамилия", max_length=30)
    patronymic = models.CharField("Отчество", max_length=30)
    # Качества
    SEX = {
        "M": "Male",
        "F": "Female",
    }

    sex = models.CharField("Пол", choices=SEX)
    age = models.PositiveIntegerField("Возраст")
    eye_color = models.CharField("Цвет глаз", max_length=20)
    height = models.FloatField("Рост")
    weight = models.FloatField("Вес")
    IQ = models.IntegerField("Показатель интелекта")

    def get_full_name(self) -> str:
        return ' '.join(filter(bool, [self.surname, self.firstname, self.patronymic]))

    def __str__(self):
        return self.get_full_name()

    class Meta:
        verbose_name = "Мама"


class Dad(models.Model):
    firstname = models.CharField("Имя", max_length=30)
    surname = models.CharField("Фамилия", max_length=30)
    patronymic = models.CharField("Отчество", max_length=30)
    # Качества
    sex = models.CharField("Пол", choices=SEX)
    age = models.PositiveIntegerField("Возраст")
    eye_color = models.CharField("Цвет глаз", max_length=20)
    height = models.FloatField("Рост")
    weight = models.FloatField("Вес")
    bread = models.BooleanField("Bread")

    def get_full_name(self) -> str:
        return ' '.join(filter(bool, [self.surname, self.firstname, self.patronymic]))

    def __str__(self):
        return self.get_full_name()

    class Meta:
        verbose_name = "Папа"


class Child(Mom, Dad):
    class Meta:
        verbose_name = "Ребенок"


class Wife(models.Model):
    name = models.CharField("Имя", max_length=30)

    class Meta:
        verbose_name = "Жена"


class Husband(models.Model):
    name = models.CharField("Имя", max_length=30)
    wife = models.OneToOneField(Wife, related_name="Жена", verbose_name="Mуж")

    class Meta:
        verbose_name = "Муж"


class ClothingCompany(models.Model):
    name = models.CharField("Название", max_length=100)
    capital = models.BigIntegerField("Капитал")
    address = models.CharField("Адрес", max_length=100)

    class Meta:
        verbose_name = "Компания одежды"


class TShirt(models.Model):
    SIZES = {
        "XS": "Extra Small",
        "S": "Small",
        "M": "Medium",
        "L": "Large",
        "XL": "Extra Large",
    }
    name = models.CharField("Название", max_length=100)
    size = models.CharField("Размер", choices=SIZES)
    manufacturer = models.ForeignKey(
        ClothingCompany,
        related_name="Производитель",
        on_delete=models.CASCADE,
        verbose_name="Футболки"
    )

    class Meta:
        verbose_name = "Футболка"
        verbose_name_plural = "Футболки"

