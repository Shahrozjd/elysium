from django.db import models
from datetime import datetime


class Membership(models.Model):
    name = models.CharField(max_length=225, blank=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.PositiveIntegerField(default=0, blank=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    first_name = models.CharField(max_length=225, blank=True)
    last_name = models.CharField(max_length=225, blank=True)
    company_name = models.CharField(max_length=225, blank=True)
    Country = models.CharField(max_length=225, blank=True)
    street_address = models.TextField(max_length=500, blank=True)
    password = models.CharField(max_length=25, blank=True)
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    Post_code = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=11, blank=True, unique=True)
    email = models.CharField(max_length=50, blank=True)
    occupation = models.CharField(max_length=225, blank=True)
    Gender_CHOICES = (
        ('male', "Male"),
        ('female', "Female"),
    )
    gender = models.CharField(max_length=25,
                  choices=Gender_CHOICES,
                  default='male')    
    father_name = models.CharField(max_length=225, blank=True)
    blood_group = models.CharField(max_length=25, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    religion = models.CharField(max_length=25, blank=True)
    nationality = models.CharField(max_length=25, blank=True)
    hobby = models.CharField(max_length=225, blank=True)
    SOURCE_CHOICES = (
        ('advertisement', "Advertisement"),
        ('social_media', "Social Media"),
        ('other', "Other"),
    )
    source = models.CharField(max_length=225,
                  choices=SOURCE_CHOICES,
                  default='advertisement')
    PURPOSE_CHOICES = (
        ('fitness', "Fitness"),
        ('reduce_weight', "Reduce Weight"),
        ('increase_weight', "Increase Weight"),
        ('hyper_trophy', "Hyper Trophy"),
    )
    source = models.CharField(max_length=225,
                  choices=PURPOSE_CHOICES,
                  default='fitness')

    approved = models.BooleanField(default=False)
    dues_paid = models.BooleanField(default=False)
    membership_updated_on = models.DateField(null=True, blank=True)
    Membership = models.ForeignKey(Membership, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Attendance(models.Model):
    member = models.ForeignKey(Profile, on_delete=models.CASCADE)
    attendance_time = models.DateTimeField(default=datetime.now, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.member.first_name

    # def save(self, *args, **kwargs):
    #     self.attendance_time = 
    #     super(Tracking,self).save(*args, **kwargs)





# class Invoice(models.Model):
#     salesman = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     total = models.PositiveIntegerField(default=0, blank=True)
#     comments = models.TextField(max_length=500, blank=True)
#     STATUS_CHOICES = (
#         ('placed', "placed"),
#         ('shipped', "shipped"),
#         ('blocked', "blocked"),
#         ('cancelled', "cancelled"),
#         ('delivered', "delivered"),
#     )
#     status = models.CharField(max_length=10,
#                   choices=STATUS_CHOICES,
#                   default='placed')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"{self.id}"


# class Ledger(models.Model):
#     member = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True)
#     amount = models.PositiveIntegerField(default=0, blank=True) 
#     comments = models.TextField(max_length=500, blank=True)
#     LEDGER_CHOICES = (
#         ('debit', "debit"),
#         ('credit', "credit"),
#     )
#     transaction = models.CharField(max_length=9,
#                   choices=LEDGER_CHOICES,
#                   default='debit')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.member