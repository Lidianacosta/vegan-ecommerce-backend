import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail

from apps.users.managers import UserManager

from apps.users.validators import (
    cpf_regex_validator,
    email_regex_validator,
    legal_age_validator,
    min_length_name_validator,
    name_regex_validator,
    phone_number_regex_validator,
    valid_cpf_validator
)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(
        _("id"),
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    email = models.EmailField(
        _('email address'),
        unique=True,
        validators=[email_regex_validator]
    )
    full_name = models.CharField(
        _("full name"),
        max_length=100,
        default='',
        validators=[name_regex_validator, min_length_name_validator]
    )
    cpf = models.CharField(
        _("CPF"),
        max_length=14,
        unique=True,
        null=True,
        validators=[valid_cpf_validator, cpf_regex_validator]
    )
    date_of_birth = models.DateField(
        _("date of birth"),
        null=True,
        validators=[legal_age_validator]
    )
    phone_number = models.CharField(
        _("phone number"),
        max_length=20,
        default='',
        validators=[phone_number_regex_validator]
    )
    is_admin = models.BooleanField(
        _("admin status"),
        default=False,
        help_text=_(
            "Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(_("active"), default=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    @property
    def is_staff(self):
        """ Returns whether the user is an administrator """
        return self.is_admin

    def __str__(self):
        """ Returns the representation of the object as a string """
        return str(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)
