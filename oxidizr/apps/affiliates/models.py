from django.db import models
from django.conf import settings


class Affiliate(models.Model):
    """
    This model allows us to enable multiple tenants register on and use Oxidizr.
    Like in other hosted Software as a Service, we store almost all other data per tenant.
    """
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)