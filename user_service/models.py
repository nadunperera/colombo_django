from django.db import models


class Role(models.Model):
    ROLE_CHOICES = (
        (1, 'Administrator'),
        (2, 'Sales Agent'),
        (3, 'Business Partner'),
        (4, 'Introducer'),
        (5, 'BDM'),
        (6, 'Accountant'),
        (7, 'Acquisitions'),
        (8, 'Client'),
    )
    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.get_id_display()


class LeadSource(models.Model):
    source_name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.source_name


class User(models.Model):
    AGE_CHOICES = (
        (1, '15-25'),
        (2, '26-35'),
        (3, '36-50'),
        (4, '51+'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField(choices=AGE_CHOICES)
    email = models.EmailField(max_length=100, unique=True)
    role = models.ManyToManyField(Role, related_name='users')
    lead_source = models.ForeignKey(LeadSource, on_delete=models.PROTECT, null=True, blank=True, related_name='users')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
