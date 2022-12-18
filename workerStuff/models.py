from django.db import models


# Create your models here.
class Workers(models.Model):
    id = models.IntegerField(primary_key=True)
    fio = models.CharField(max_length=100, blank=False, verbose_name="Worker", null=False, help_text="Сотрудник")
    position = models.CharField(max_length=100, blank=False, verbose_name="Position", null=False, help_text="Должность")
    salary = models.IntegerField(blank=False, verbose_name="Salary", null=False, help_text="Зарплата")
    full_time = models.BooleanField(default=True, verbose_name="Full time", help_text="Полная занятость")

    class Meta:
        db_table = "Workers"
        verbose_name = "Worker"

    def __str__(self):
        return self.fio


class Duties(models.Model):
    YES = 'YES'
    NO = 'NO'
    HALF = 'HALF'
    ALMOST = 'ALMOST'
    CHOISES_DONE = {
        (YES, "YES"),
        (NO, "NO"),
        (HALF, "HALF"),
        (ALMOST, "ALMOST"),
    }

    position = models.ForeignKey(Workers, on_delete=models.CASCADE, null=True,
                                 verbose_name="Position")
    task = models.CharField(max_length=100, blank=False, verbose_name="Task", null=False,
                            help_text="Задача", unique=True)
    is_done = models.CharField(choices=CHOISES_DONE, max_length=6, verbose_name="Is done", help_text="Завершено",
                               default=NO)
    deadline = models.DateField(verbose_name="Deadlines", auto_now=False, auto_now_add=False, help_text="Сроки сдачи")

    class Meta:
        db_table = "Duties"
        verbose_name = "Duty"

    def __str__(self):
        return self.is_done


class WorkHours(models.Model):
    full_time = models.ForeignKey(Workers, on_delete=models.CASCADE, verbose_name="Full time worker",
                                  help_text="Работник", null=True)
    am_hours_week = models.IntegerField(blank=False, verbose_name="Amount of hours a day", null=False,
                                        help_text="Кол-во рабочих часов в день")
    am_days_week = models.IntegerField(blank=False, verbose_name="Amount of days a week", null=False,
                                       help_text="Кол-во рабочих дней в неделю")
    am_weekends_week = models.IntegerField(blank=False, verbose_name="Amount of weekends a week",
                                           help_text="Кол-во выходных в неделю")

    class Meta:
        db_table = "WorkHours"
        verbose_name = "WorkHours"


class VacationsWeekends(models.Model):
    am_weekends_week = models.ForeignKey(WorkHours, on_delete=models.CASCADE, null=True,
                                         verbose_name="Amount of weekends a week",
                                         help_text="Кол-во выходных в неделю")
    am_vacations_year = models.IntegerField(blank=False, verbose_name="Amount of vacations a year",
                                            null=False,
                                            help_text="Кол-во отпусков в году")
    am_days_vacation = models.IntegerField(blank=False, verbose_name="Amount of days in a vacation",
                                           null=False,
                                           help_text="Кол-во дней в 1 отпуске")

    class Meta:
        db_table = "VacationsWeekends"
        verbose_name = "Vacations and Weekends"


class Requests(models.Model):
    username = models.CharField(max_length=50, blank=False, null=False, verbose_name="name",
                                help_text="имя пользователя")
    email = models.CharField(max_length=50, blank=False, null=False, verbose_name="email",
                             help_text="почта пользователя")
    theme = models.CharField(max_length=50, blank=False, null=False, verbose_name="Tема обращения")
    description_of_problem = models.CharField(max_length=300, blank=False, null=False, verbose_name="Oбращение",
                                              help_text="Опишите свою проблему")
    worker = models.ForeignKey(Workers, on_delete=models.CASCADE, blank=False, verbose_name="Worker", null=True, help_text="Сотрудник")

    class Meta:
        db_table = "Requests"
        verbose_name = "Requests"
