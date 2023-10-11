from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, FileExtensionValidator

class Skill(models.Model):
    name = models.CharField(max_length=30)
    mastery = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    logo = models.FileField(upload_to="portfolio/skills", validators=[FileExtensionValidator(['svg', 'jpeg', 'jpg', 'png'])], blank=True)
    
    def __str__(self) -> str:
        return self.name
    

class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to="portfolio/images", blank=True)
    url = models.URLField(blank=True)
    skills = models.ManyToManyField(Skill)
    
    def __str__(self) -> str:
        return f"{self.id} - {self.title}"
    

class SoftSkill(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=250)
    image = models.FileField(upload_to="portfolio/softskills", validators=[FileExtensionValidator(['svg', 'jpeg', 'jpg', 'png'])], blank=True)
    
    def __str__(self) -> str:
        return self.name
    

