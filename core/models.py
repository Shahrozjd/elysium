from django.db import models
from datetime import datetime,timedelta, date

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
    full_name = models.CharField(max_length=225, blank=True)
    father_name = models.CharField(max_length=225, blank=True)
    company_name = models.CharField(max_length=225, blank=True)
    phone = models.CharField(max_length=11, blank=True, unique=True)
    email = models.CharField(max_length=50, blank=True)
    street_address = models.TextField(max_length=500, blank=True)
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=225, blank=True)
    post_code = models.CharField(max_length=255, blank=True)
    password = models.CharField(max_length=25, blank=True)
    occupation = models.CharField(max_length=225, blank=True)
    Gender_CHOICES = (
        ('male', "Male"),
        ('female', "Female"),
    )
    gender = models.CharField(max_length=25,
                  choices=Gender_CHOICES,
                  default='male')    
    blood_group = models.CharField(max_length=25, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    religion = models.CharField(max_length=25, blank=True)
    nationality = models.CharField(max_length=25, blank=True)
    hobby = models.CharField(max_length=225, blank=True)
    PURPOSE_CHOICES = (
        ('fitness', "Fitness"),
        ('reduce_weight', "Reduce Weight"),
        ('increase_weight', "Increase Weight"),
        ('hyper_trophy', "Hyper Trophy"),
    )
    purpose = models.CharField(max_length=225,
                  choices=PURPOSE_CHOICES,
                  default='fitness')

    profile_approved = models.BooleanField(default=False)
    dues_paid = models.BooleanField(default=False)
    membership = models.ForeignKey(Membership, on_delete=models.SET_NULL, null=True)
    membership_updated_on = models.DateField(null=True, blank=True)
    membership_expires_on = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.full_name} ({self.id})'
    
    def save(self, *args, **kwargs):
        if self.pk:
            profile = Profile.objects.get(id=self.pk)
            if profile.membership_updated_on != self.membership_updated_on:
                Invoice.objects.create(member=profile, amount=profile.membership.price, transaction='credit')

        if self.membership_updated_on is not None:
            self.membership_expires_on = self.membership_updated_on + timedelta(days=30)
        if  self.membership_updated_on is not None and self.membership_expires_on is not None:
            if date.today() < self.membership_expires_on:
              self.dues_paid = True
            else:
              self.dues_paid = False

        super(Profile,self).save(*args, **kwargs)

class Attendance(models.Model):
    member = models.ForeignKey(Profile, on_delete=models.CASCADE)
    attendance_time = models.DateTimeField(default=datetime.now, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.member.full_name


class Invoice(models.Model):
    member = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True)
    amount = models.PositiveIntegerField(default=0, blank=True) 
    comments = models.TextField(max_length=500, blank=True)
    LEDGER_CHOICES = (
        ('debit', "debit"),
        ('credit', "credit"),
    )
    transaction = models.CharField(max_length=9,
                  choices=LEDGER_CHOICES,
                  default='credit')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.member.full_name