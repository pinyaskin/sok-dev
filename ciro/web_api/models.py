from django.db import models


class Posts(models.Model):
    callerid = models.IntegerField(primary_key=True, blank=True, null=False)
    address = models.TextField(blank=True, null=True)  # This field type is a guess.
    post_number = models.IntegerField(blank=True, null=True)
    name_object = models.TextField(blank=True, null=True)  # This field type is a guess.
    status = models.TextField(blank=True, null=True)  # This field type is a guess.
    lastcall = models.TextField(blank=True, null=True)  # This field type is a guess.
    commentary = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'posts'


class Categories(models.Model):
    category = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'categories'
