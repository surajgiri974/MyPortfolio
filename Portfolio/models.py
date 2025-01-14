from django.db import models

class Project(models.Model):

    CATEGORY_CHOICES = [
        ('Web Development', 'Web Development'),
        ('Desktop Application', 'Desktop Application'),
        ('Data Science', 'Data Science'),
        ('Android Application', 'Mobile App'),
        ('IOS Application', 'IOS Mobile App'),
    ]

    STATUS_CHOICES = [
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('pending', 'Pending'),
    ]


    project_name = models.CharField(max_length=100,unique=True)
    intro = models.TextField()
    project_description = models.TextField()
    category_type = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    stack = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    images = models.ImageField(upload_to='projects/', null=True, blank=True)  

    def __str__(self):
        return self.project_name


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='project_images', on_delete=models.CASCADE) 
    image = models.ImageField(upload_to='project/images/', verbose_name='Image')

    def __str__(self):
        return f"Image for {self.project.project_name}"