from django.db import models
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import User
# Create your models here.

class Asset_types(models.TextChoices):
    LAPTOP= 'LAPTOP', _('LAPTOP')
    TRAVEL_BAG= 'TRAVEL_BAG', _('TRAVEL_BAG')
    PACKAGE = 'PACKAGE', _('PACKAGE')


class Sensitivities(models.TextChoices):
    HIGHLY_SENSITIVE = 'HIGHLY_SENSITIVE', _('HIGHLY_SENSITIVE')
    SENSITIVE = 'SENSITIVE', _('Sensitive')
    NORMAL = 'NORMAL', _('NORMAL')

class Travel_medium(models.TextChoices):
    CAR = 'CAR', _('CAR')
    BUS = 'BUS', _('BUS')
    TRAIN = 'TRAIN', _('TRAIN')

class Matched_Status(models.TextChoices):
    EXPIRED = 'EXPIRED', _('EXPIRED')
    PENDING = 'PENDING', _('PENDING')


class Applied_Status(models.TextChoices):
    APPLIED= 'APPLIED', _('APPLIED')
    NOT_APPLIED= 'NOT_APPLIED', _('NOT_APPLIED')

# class Requester(models.Model):
#     username=models.CharField(unique=True,max_length=20)
#     password=models.CharField(max_length=20)

#     def __str__(self):
#         return self.username

# class Rider(models.Model):
#     username=models.CharField(unique=True,max_length=20)
#     password=models.CharField(max_length=20)

#     def __str__(self):
#         return self.username

class Transport_Request(models.Model):
    requester=models.ForeignKey(User, on_delete=models.CASCADE,
        related_name="requester")
    rider=models.ForeignKey(User,null=True,on_delete=models.CASCADE,
        blank=True,related_name="rider")
    # applied_transport_request=models.ManyToManyField(Travel_info,
    #     blank=True,related_name="applied_rides_many")
    pickup=models.TextField()
    delivery_at=models.TextField()
    date_time=models.DateTimeField()
    flexible=models.BooleanField()
    whom_to_deliver=models.TextField()
    assets_quantity=models.IntegerField()

    asset_types = models.CharField(
        max_length=20,
        choices=Asset_types.choices,
        #default=Asset_types.NORMAL,
    )
    sensitivities = models.CharField(
        max_length=20,
        choices=Sensitivities.choices,
        #default=Sensitivities.NORMAL,
    )
    status=models.CharField(
        max_length=20,
        choices=Matched_Status.choices,
        default=Matched_Status.PENDING
    )


class Travel_info(models.Model):
    rider=models.ForeignKey(User,on_delete=models.CASCADE,related_name="travel_info_rider")
    applied_transport_request=models.ManyToManyField(Transport_Request,blank=True)
    pickup=models.TextField()
    delivery_at=models.TextField()
    date_time=models.DateTimeField()
    flexible=models.BooleanField(default=False)
    assets_quantity=models.IntegerField()
    travel_medium = models.CharField(
        max_length=20,
        choices=Travel_medium.choices,
    )

# class Applied_Rides(models.Model):
#     requester=models.ForeignKey(User,on_delete=models.CASCADE,related_name="applied_requester")
#     rider=models.ForeignKey(User,on_delete=models.CASCADE,related_name="applied_rider")
#     transport_request=models.ForeignKey(Transport_Request,
#         on_delete=models.CASCADE)


# class User_details(models.Model):
#     is_rider=models.BooleanField(default=False)
#     is_requester=models.BooleanField(default=False)
#     phonenumber=models.IntegerField(null=True,blank=True)
#     userlink=models.OneToOneField(User,on_delete=models.CASCADE)

    
    