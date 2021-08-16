from datetimewidget.widgets import DateTimeWidget
from django.forms import (DateTimeField, ModelForm, ModelMultipleChoiceField)

from .models import Email, SentEmail


class SentEmailForm(ModelForm):
    time_of_sending = DateTimeField(
        label='Время отправки',
        widget=DateTimeWidget(
            attrs={'id': 'id'},
            usel10n=True,
            bootstrap_version=3
        ),
        required=False
    )

    class Meta:
        model = SentEmail
        fields = (
            'template',
        )


class EmailForm(ModelForm):
    class Meta:
        model = Email
        fields = '__all__'
