from django.db import models


class FirstModel(models.Model):
    name = models.CharField('Название', max_length=50)
    value = models.IntegerField('Некое значение')
    link = models.ForeignKey(self, related_name="%(app_label)s_%(class)s")
    manager = models.Manager()
    #nomber__of__something = models.IntegerField()  Неправильное поле
    #max = models.CharField()
    #yoo_ = models.OneToOneField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'default'


class Mom(models.Model):
    firstname = models.CharField("Имя", max_length=30)
    surname = models.CharField("Фамилия", max_length=30)
    patronymic = models.CharField("Отчество", max_length=30)
    # Качества
    SEX = {
        ("M", "Male"),
        ("F", "Female"),
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
    SEX = {
        ("M", "Male"),
        ("F", "Female"),
    }
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
    mom = models.OneToOneField(Mom, related_name="Мама", verbose_name="Ребенок")
    dad = models.OneToOneField(Dad, related_name="Папа", verbose_name="Ребенок")

    class Meta:
        verbose_name = "Ребенок"


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


class Park(models.Model):
    name = models.CharField("Название", max_length=30)
    address = models.CharField("Адрес", max_length=30)

    class Meta:
        verbose_name = "Парк"
        verbose_name_plural = "Парки"


class Breed(models.Model):
    name = models.CharField("Название", max_length=30)

    class Meta:
        verbose_name = "Порода"
        verbose_name_plural = "Породы"


class Dog(models.Model):
    name = models.CharField("Кличка", max_length=30)
    breed = models.ForeignKey(Breed, related_name="Порода", verbose_name="Собака", on_delete=models.CASCADE)
    park = models.ManyToManyField(Park, related_name="Парк", verbose_name="Собака")

    class Meta:
        verbose_name = "Собака"
        verbose_name_plural = "Собаки"


class Soul(models.Model):
    HAIR_COLOR = {
        ("Gi", "Рыжий"),
        ("Bl", "Черный"),
        ("Br", "Брюнет"),
        ("Bol", "Лысый"),

    }
    hair_color = models.CharField("Цвет волос", choices=HAIR_COLOR)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if self.hair_color == "Gi":
            return
        else:
            super().save()


class PersonInfo(models.Model):
    name = models.CharField("Имя", max_length=50)
    age = models.PositiveIntegerField("Возраст")
    SEX = {
        ("M", "Male"),
        ("F", "Female"),
    }
    sex = models.CharField("Пол", choices=SEX)

    def get_full_name(self) -> str:
        return ' '.join(filter(bool, [self.surname, self.firstname, self.patronymic]))

    def __str__(self):
        return self.get_full_name()

    class Meta:
        abstract = True


class Groupe(models.Model):
    name = models.CharField("Название", max_length=50)
    groupe_id = models.AutoField(primary_key=True)

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"

    def __str__(self):
        self.name


class Student(PersonInfo):
    group = models.ManyToManyField(Groupe, through=GroupeInfo, related_name="Группа")
    avatar = models.ImageField("Фото")

    class Meta:
        verbose_name = "Ученик"
        verbose_name_plural = "Ученики"


class GroupeInfo(models.Model):
    student = models.ForeignKey(Student, related_name="Студент")
    groupe = models.ForeignKey(Groupe, related_name="Группа")
    list_number = models.IntegerField("Номер по списку")


class Teacher(PersonInfo):
    grade = models.CharField("Степень", max_length=15)

    class Meta:
        verbose_name = "Учитель"
        verbose_name_plural = "Учителя"


class MyPersonSlave(PersonInfo):
    class Meta:
        proxy = True

    def do_work(self, task):
        self.task = task
        self.task_note = f"Сейчас я делаю {task}."
        self.tired = True



