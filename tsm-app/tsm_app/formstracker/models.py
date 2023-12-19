from django.db import models

class Retreat(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    capacity = models.IntegerField()
    registration_deadline = models.DateTimeField()
    cost = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title

class Attendee(models.Model):
    retreat = models.ForeignKey(Retreat, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    has_signed_waiverfile = models.BooleanField(default=False)
    has_signed_timberline = models.BooleanField(default=False)
    has_signed_other = models.BooleanField(default=False)
    registration_date = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=50)
    def __str__(self):
        return self.name