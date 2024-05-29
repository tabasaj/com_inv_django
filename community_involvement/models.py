from django.db import models


class Program(models.Model):
    title = models.CharField(max_length=255)
    caption = models.CharField(max_length=1000)
    date_time = models.DateTimeField(auto_now_add=True)
    archive = models.BooleanField(default=False)
    image_upload = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=255)
    caption = models.CharField(max_length=1000)
    date_time = models.DateTimeField(auto_now_add=True)
    archive = models.BooleanField(default=False)
    image_upload = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title


class MOD(models.Model):
    donated = models.CharField(max_length=255)
    name = models.CharField(max_length=150)

    donation_type = models.CharField(max_length=10)
    gcash_number = models.CharField(max_length=11)
    paymaya_number = models.CharField(max_length=11)

    amount = models.IntegerField()
    date_time = models.DateTimeField(auto_now_add=True)

    address_volunteer = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=11)
    date_sched = models.CharField(max_length=20)

    def __str__(self):
        return self.name
