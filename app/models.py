# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.db import models


# Create your models here.
class category(models.Model):
    category_id = models.BigAutoField(primary_key=True)
    category_name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_id


class dept_entre(models.Model):
    category_id = models.ForeignKey(category, default=1, verbose_name="Category", on_delete=models.PROTECT)
    department_id = models.BigAutoField(primary_key=True)
    department_name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "department"

    def __str__(self):
        return self.department_id


class prog_entre(models.Model):
    department_id = models.ForeignKey(dept_entre, default = 1, on_delete=models.PROTECT)
    program_id = models.IntegerField(primary_key=True)
    department_name = models.CharField(max_length=100, default='NULL', unique = True)
    program_name = models.CharField(max_length=100, unique = True)
    state = models.CharField(max_length=100, blank = True)
    financial_year = models.IntegerField()
    no_of_participants = models.IntegerField(null=True)

    class Meta:
        db_table: "prog_entre"
