from django.db import models

class Complaint(models.Model):

    CATEGORY_CHOICES = [
        ('Electrical', 'Electrical'),
        ('Water', 'Water'),
        ('Internet', 'Internet'),
        ('Cleaning', 'Cleaning'),
    ]

    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Resolved', 'Resolved'),
    ]

    student_name = models.CharField(max_length=100)
    room_number = models.CharField(max_length=20)

    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField()

    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='Medium'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    def __str__(self):
        return self.title