from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    bio_en = models.TextField(blank=True)
    bio_es = models.TextField(blank=True)
    photo = models.ImageField(upload_to="authors/", blank=True, null=True)

    def __str__(self):
        return self.name

class Collection(models.Model):
    name_en = models.CharField(max_length=120)
    name_es = models.CharField(max_length=120, blank=True)
    slug = models.SlugField(unique=True)
    description_en = models.TextField(blank=True)
    description_es = models.TextField(blank=True)

    def __str__(self):
        return self.name_en

class Poem(models.Model):
    title_en = models.CharField(max_length=200)
    title_es = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    collection = models.ForeignKey(Collection, on_delete=models.SET_NULL, null=True, blank=True)
    body_en = models.TextField()
    body_es = models.TextField(blank=True)
    is_featured = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title_en
