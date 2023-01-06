from django.contrib import admin
from .models import agent, measurement, user, task, agenttask, report, event, sensor, threshold, warning


class agentAdmin(admin.ModelAdmin):
    list_display = ("agent_name", "agent_type")
    list_filter = ("agent_type", )

class userAdmin(admin.ModelAdmin):
    list_display = ("username", "fullname")


class sensorAdmin(admin.ModelAdmin):
    list_display = ("id", "sensor_type", "manufacturer")
    list_filter = ("sensor_type", )

class measurementAdmin(admin.ModelAdmin):
    list_display = ("sensor", "value", "time", "agent")
    list_filter = ("sensor","agent", "time")

class thresholdAdmin(admin.ModelAdmin):
    list_display = ("id", "sensor", "min_value", "max_value")
    list_filter = ("sensor", )

class eventAdmin(admin.ModelAdmin):
    list_display = ("id", "description", "emergencylevel")
    list_filter = ("emergencylevel", )

class reportAdmin(admin.ModelAdmin):
    list_display = ("id", "event", "time", "agent")
    list_filter = ("event", "time", "agent",)

class taskAdmin(admin.ModelAdmin):
    list_display = ("id", "task_name", "priority")
    list_filter = ("priority",)

class agenttaskAdmin(admin.ModelAdmin):
    list_display = ("agent", "task", "timeassigned", "timeaccomplished", "comment",)
    list_filter = ("agent", "task",)


class warningAdmin(admin.ModelAdmin):
    list_display = ("id","sensor", "value", "status","time", "agent")
    list_filter = ("agent", "sensor", "status", "time")

    
# Register your models here.
admin.site.register(agent, agentAdmin)
admin.site.register(measurement, measurementAdmin)
admin.site.register(user, userAdmin)
admin.site.register(task, taskAdmin)
admin.site.register(agenttask, agenttaskAdmin)
admin.site.register(report, reportAdmin)
admin.site.register(event, eventAdmin)
admin.site.register(sensor, sensorAdmin)
admin.site.register(threshold, thresholdAdmin)
admin.site.register(warning, warningAdmin)