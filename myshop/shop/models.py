# Create your models here.
#coding:utf-8
from django.db import models
from django.core.urlresolvers import reverse

class Category(models.Model):
    slug = models.SlugField(max_length=200,unique=True)
    name = models.CharField(max_length=200)
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                        args=[self.slug])
    def __str__(self):
        return self.name
#药物类别的表
class Product(models.Model):
    slug = models.SlugField(max_length=200)
    category = models.ForeignKey(Category,
                                 related_name='products')
    name = models.CharField(max_length=200)
    herbname = models.CharField(max_length=200)
    image = models.TextField(blank=True)
    description = models.TextField(blank=True)
    xiangsidu = models.FloatField(null=True)
    cass = models.CharField(max_length=200)
    pubchem = models.CharField(max_length=200)
    inchikey = models.CharField(max_length=200)
    druglikeness = models.CharField(max_length=200)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('shop:product_detail',
            args=[self.id, self.slug])
#药物的表