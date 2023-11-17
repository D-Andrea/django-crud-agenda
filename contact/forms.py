from django import forms
from django.core.exceptions import ValidationError

from . import models


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'class-a class-b',
                'placeholder': 'Write Here',
            },
        ),
        label='First Name',
        help_text='Text to help the user'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Just updating the current widget
        # self.fields['first_name'].widget.attrs.update({
        #     'class': 'class-a class-b',
        #     'placeholder': 'Write Here',
        # })

    class Meta:
        model = models.Contact
        fields = (
            'first_name',
            'last_name',
            'phone',
            'email',
            'description',
            'category',
        )
        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'class': 'class-a class-b',
        #             'placeholder': 'Write Here'
        #         }
        #     )
        # }

    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            msg = ValidationError(
                    "The first name can't be the same as the last",
                    code='invalid '
                )
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)

        return super().clean()

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(
                    'Come from add Error',
                    code='invalid'
                )
            )

        return first_name
