import re
from datetime import date
from django.core.validators import (
    ValidationError,
    RegexValidator,
    MinLengthValidator
)
from dateutil.relativedelta import relativedelta


min_length_name_validator = MinLengthValidator(
    limit_value=2,
    message='The name must contain more that two letters'
)


name_regex_validator = RegexValidator(
    regex=r'^[a-zá-ùA-ZÁ-Ù]+((?:[\s][a-zá-ùA-ZÁ-Ù]+)?)+$',
    message="The name must contain only letters"
)


phone_number_regex_validator = RegexValidator(
    regex=r'^[0-9]{11}$',
    message="The telephone number must contain only numbers and be in the format: 'DDD9XXXXXXXX'"
)


cpf_regex_validator = RegexValidator(
    regex=r'^[0-9]{11}$',
    message="The CPF must contain 11 numbers"
)


email_regex_validator = RegexValidator(
    regex=r"^[a-zA-Z0-9._]+@[a-z]+\.com$",
    message="Invalid email address"
)


def legal_age_validator(value):
    """ Checks if the user is over 18 years old"""
    idade = relativedelta(date.today(), value)
    if idade.years >= 18:
        return value
    raise ValidationError('You must be over 18 years old')


def valid_cpf_validator(value):
    """ Checks if the CPF is valid """

    cpf = str(value)
    cpf = re.sub(r'[^0-9]', '', cpf)

    if not cpf or len(cpf) != 11:
        raise ValidationError('Enter a valid CPF')

    new_cpf = cpf[:-2]
    reverse = 10
    total = 0

    for index in range(19):
        if index > 8:
            index -= 9

        total += int(new_cpf[index]) * reverse

        reverse -= 1
        if reverse < 2:
            reverse = 11
            digit = 11 - (total % 11)

            if digit > 9:
                digit = 0
            total = 0
            new_cpf += str(digit)

    sequence = new_cpf == str(new_cpf[0]) * len(cpf)

    if cpf == new_cpf and not sequence:
        return cpf

    raise ValidationError("Enter a valid CPF")
