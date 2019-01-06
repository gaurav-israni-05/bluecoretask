from django.db import models


class ModelBase(models.Model):
    """
    This is a abstract model class to add is_deleted, created_at and modified_at fields to any model
    """
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Email(ModelBase):
    """
    Email Model that will store all the emails along with their details
    """
    from_email = models.EmailField()
    to_email = models.EmailField()
    subject = models.CharField(max_length=256, null=True)
    body = models.TextField()
