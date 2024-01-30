from django.db import models

class TestExample(models.Model):
  nickname = models.CharField(max_length=255)
  country = models.CharField(max_length=255)
  poet = models.CharField(max_length=255, default='poet')
  person = models.CharField(max_length=255, default='Hero')

  def __str__(self):
    return f"{self.nickname} {self.country}"

