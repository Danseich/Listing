from django.db import models


# Первая модель показывает основные принципы создания моделей
class FirstModel(models.Model):
    name = models.CharField('Название', max_length=50)
    something = models.TextField("Текстовое поле", null=True)
    value = models.IntegerField('Некое значение', blank=True)
    link = models.ForeignKey(
        'self', related_name="%(app_label)s_%(class)s", on_delete=models.DO_NOTHING
                             )  # Название будет менятся в зависимости от класса и приложения
    manager = models.Manager()
    # nomber__of__something = models.IntegerField()  Неправильное поле
    # max = models.CharField()
    # yoo_ = models.OneToOneField()

    def __str__(self):  # Метод для отображения имени
        return self.name

    class Meta:  # Доп настройки
        db_table = 'default'
        # indexes = models.Index(fields=["name", "something"])


class Mom(models.Model):
    firstname = models.CharField("Имя", max_length=30)
    surname = models.CharField("Фамилия", max_length=30)
    patronymic = models.CharField("Отчество", max_length=30)
    # Качества
    SEX = {
        ("M", "Male"),
        ("F", "Female"),
        ("N", "Neither"),
    }
    # Словарь с чейсами
    sex = models.CharField("Пол", choices=SEX)  # Использование чейсов
    age = models.PositiveIntegerField("Возраст")
    eye_color = models.CharField("Цвет глаз", max_length=20)
    height = models.FloatField("Рост")
    weight = models.FloatField("Вес", help_text="В киллограммах")  # Пример вспомогательного текста
    IQ = models.IntegerField("Показатель интелекта")

    def get_full_name(self) -> str:  # Кастомный метод
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
    sex = models.CharField("Пол", choices={("M", "Male"), ("F", "Female"), ("N", "Neither")})
    # Альтернативный вариант использования чейсов
    age = models.PositiveIntegerField("Возраст")
    eye_color = models.CharField("Цвет глаз", max_length=20)
    height = models.FloatField("Рост")
    weight = models.FloatField("Вес", help_text="В киллограммах")
    bread = models.BooleanField("Bread")

    def get_full_name(self) -> str:
        return ' '.join(filter(bool, [self.surname, self.firstname, self.patronymic]))

    def __str__(self):
        return self.get_full_name()

    class Meta:
        verbose_name = "Папа"


class Child(Mom, Dad):  # Пример наследования
    mom = models.OneToOneField(Mom, related_name="Мама", verbose_name="Ребенок", on_delete=models.PROTECT)
    dad = models.OneToOneField(Dad, related_name="Папа", verbose_name="Ребенок", on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Ребенок"


class ClothingCompany(models.Model):
    name = models.CharField("Название", max_length=100, unique=True)
    capital = models.BigIntegerField("Капитал", db_comment="По последним данным")
    # Коментарий к базе данных
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
    # Связь с другой моделью

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
    name = models.CharField("Название", max_length=30, default="Дворняга", editable=True)

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
    ):  # Переопределение метода
        if self.hair_color == "Gi":
            return
        else:
            super().save()


class PersonInfo(models.Model):
    name = models.CharField("Имя", max_length=50)
    birth = models.DateField("Дата рождения", help_text="Укажите в формате ДД.ММ.ГГГГ")
    SEX = {
        ("M", "Male"),
        ("F", "Female"),
        ("N", "Neither"),
    }
    sex = models.CharField("Пол", choices=SEX)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True  # Абстрактная модель


class Groupe(models.Model):
    name = models.CharField("Название", max_length=50)
    groupe_id = models.AutoField(primary_key=True)

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"
        ordering = ["name"]  # Настройки Meta

    def __str__(self):
        return self.name


class Student(PersonInfo):
    group = models.ManyToManyField(Groupe, through=GroupeInfo, related_name="Группа")  # Плюс поля GropeInfo
    avatar = models.ImageField("Фото", upload_to="media/")  # Изображение (так же раюотает как FileField)

    class Meta:
        verbose_name = "Ученик"
        verbose_name_plural = "Ученики"


class GroupeInfo(models.Model):
    student = models.ForeignKey(Student, related_name="Студент", on_delete=models.PROTECT)
    groupe = models.ForeignKey(Groupe, related_name="Группа", on_delete=models.PROTECT)
    list_number = models.IntegerField("Номер по списку")


class Teacher(PersonInfo):
    grade = models.CharField("Степень", max_length=15)
    email = models.EmailField("Почта")

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


class Report(models.Model):
    name = models.CharField("Название", max_length=50)
    data = models.JSONField("Данные")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Отчет"
        verbose_name_plural = "Отчеты"
