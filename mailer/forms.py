from django.forms import ModelForm, DateTimeField, TextInput, DateTimeInput, Form
from datetimewidget.widgets import DateTimeWidget
from .models import SentEmail


class SentEmailForm(ModelForm):
    time_of_sending = DateTimeField(
        label='Время отправки',
        widget=DateTimeWidget(
            attrs={'id':'id'},
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
