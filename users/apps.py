# """User app configuration"""

# from django.apps import AppConfig


# class UsersConfig(AppConfig):
# 	"""User app confing"""
#     name = 'users'
#     verbose_name= 'Users'

"""User app configuration"""

from django.apps import AppConfig


class UsersConfig(AppConfig):
    """User app config"""
    name = 'users'
    verbose_name = 'Users'
from django.apps import AppConfig


class UsersConfig(AppConfig):
    """User app configuration"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    verbose_name = 'Users'