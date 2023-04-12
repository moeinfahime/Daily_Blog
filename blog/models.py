from django.db import models
from django.utils import timezone
from extensions.utils import jalali_converter


# My managers

class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='p')


class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)


# Create your models here.

class Category(models.Model):
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL,
                               related_name='children')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    status = models.BooleanField(default=True)
    position = models.IntegerField()
    thumbnail = models.ImageField(upload_to="images", default= "home-bg.jpg")

    # class Meta:
    #     verbose_name = "دسته بندی"
    #     verbose_name_plural = " دسته بندی ها"
    #     ordering = ['parent__id','position']

    def __str__(self):
        return self.title

    objects = CategoryManager()


class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'default'),
        ('p', 'published'),
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    category = models.ManyToManyField(Category, related_name="articles")
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="images")
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title

    # def publish(self):
    #     return jalali_converter(self.publish)

    def category_published(self):
        return self.category.filter(status=True)

    objects = ArticleManager()
