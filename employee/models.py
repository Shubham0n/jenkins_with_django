from django.db import models
from django.utils.text import slugify

class EmployProfile(models.Model):
    ROLE_CHOICES = [
        ("developer", "Developer"),
        ("designer", "Designer"),
        ("manager", "Manager"),
    ]
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default="developer")

    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    objective = models.TextField()
    address = models.TextField()
    total_experience = models.FloatField(help_text="Total experience in years")
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:  # Generate slug only if it is not provided
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while EmployProfile.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
