# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.db import models

#
# # Create your models here.
# class category(models.Model):
#     category_name = models.CharField(max_length=100)
#     #
#     # class Meta:
#     #     verbose_name_plural = "Categories"
#     #
#     # def __str__(self):
#     #     return self.category_name
#
#
# class dept_entre(models.Model):
#     Category = models.ForeignKey(category, default=1, verbose_name="Category", on_delete=models.CASCADE)
#     department_name = models.CharField(max_length=100)
#
#     # class Meta:
#     #     verbose_name_plural = "department"
#     #
#     # def __str__(self):
#     #     return self.department_name
#
#
# class program_entre(models.Model):
#     # department_id = models.ForeignKey(dept_entre, default = 1, on_delete=models.CASCADE)
#     depart_name = models.ForeignKey(dept_entre, on_delete=models.CASCADE)
#     program_name = models.CharField(max_length=100, unique = True)
#     state = models.CharField(max_length=100, blank = True)
#     financial_year = models.IntegerField()
#     no_of_participants = models.IntegerField(null=True)
#     objects = models.Manager()
#
#     class Meta:
#         db_table: 'app_program_entre'
