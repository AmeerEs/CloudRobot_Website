from django.db import models

# Create your models here.

class user(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    fullname = models.CharField(max_length=45)
    phone = models.IntegerField()
    datecreated = models.DateTimeField()

    def __str__(self):
       return f"{self.username}"



class agent(models.Model):
    agent_name = models.CharField(max_length=45)
    agent_type = models.CharField(max_length=45)
    manufacturer = models.CharField(max_length=45)
    firstoperationdate = models.DateTimeField()

    

    def __str__(self):
       return f"{self.agent_name}"  


class sensor(models.Model):
    sensor_type = models.CharField(max_length=45)
    cost = models.IntegerField()
    manufacturer = models.CharField(max_length=45)
    
    def __str__(self):
       return f"{self.sensor_type}"

class measurement(models.Model):
    sensor = models.ForeignKey(sensor, on_delete=models.CASCADE, related_name="measurement_sensor")
    value = models.FloatField()
    time = models.DateTimeField()
    agent = models.ForeignKey(agent, on_delete=models.CASCADE, related_name="measurement_agent")
    

    def __str__(self):
        return f"{self.sensor}: {self.value}  taken at  {self.time}"


class threshold(models.Model):
    sensor = models.ForeignKey(sensor, on_delete=models.CASCADE, related_name="threshold_sensor")
    min_value = models.FloatField()
    max_value = models.FloatField()
    
    def __str__(self):
       return f"{self.sensor}. {self.min_value} - {self.max_value}"

class event(models.Model):
    event_name = models.CharField(max_length=45, default='event_name')
    description = models.CharField(max_length=150)
    emergencylevel = models.IntegerField()    

    def __str__(self):
       return f"{self.event_name}"


class report(models.Model):
    event = models.ForeignKey(event, on_delete=models.CASCADE, related_name="report_event")
    time = models.DateTimeField()
    agent = models.ForeignKey(agent, on_delete=models.CASCADE, related_name="report_agent")
    describtion = models.CharField(null=True, blank=True, max_length=150)    

    def __str__(self):
       return f"{self.id}. {self.event}"

class task(models.Model):
    task_name = models.CharField(max_length=45)
    describtion = models.CharField(max_length=150)
    priority = models.IntegerField()

    def __str__(self):
       return f"{self.task_name}"

class agenttask(models.Model):
    agent = models.ForeignKey(agent, on_delete=models.CASCADE, related_name="agenttask_agent") 
    task = models.ForeignKey(task, on_delete=models.CASCADE, related_name="agenttask_task")   
    timeassigned = models.DateTimeField(auto_now_add=True, blank=True) 
    timeaccomplished = models.DateTimeField(null=True, blank=True)
    comment = models.CharField(null=True, blank=True, max_length=150)

    def __str__(self):
       return f"{self.id}"
       
class warning(models.Model):
    sensor = models.ForeignKey(sensor, on_delete=models.CASCADE, related_name="warning_sensor", null=True)
    agent = models.ForeignKey(agent, on_delete=models.CASCADE, related_name="warning_agent")
    value = models.FloatField()
    status = models.CharField(max_length=45)
    time = models.DateTimeField(null=True)

    def __str__(self):
       return f"{self.id}"

       

