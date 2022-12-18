from django.contrib import admin
import workerStuff.models as models

# Register your models here.

admin.site.register(models.Workers)
admin.site.register(models.Duties)
admin.site.register(models.WorkHours)
admin.site.register(models.VacationsWeekends)
