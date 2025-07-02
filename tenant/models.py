from django.db import models

# Create your models here.

from django.db import models
from django_tenants.models import TenantMixin, DomainMixin

from multitenant_drf.behaviours import DateMixin


class Tenant(DateMixin, TenantMixin):
    name = models.CharField(max_length=100)

    auto_create_schema = True
    auto_drop_schema = True

    def __str__(self):
        return self.name


class Domain(DomainMixin):
    pass
