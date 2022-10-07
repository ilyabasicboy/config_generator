from django import forms
from config_generator.configurator.models import WhiteLabel, WhiteLabelConfig


class WhiteLabelForm(forms.ModelForm):
    class Meta:
        model = WhiteLabel
        exclude = ('config', 'user', 'api_key')

    title = forms.CharField(
        label='Название приложения',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )


class WhiteLabelConfigForm(forms.ModelForm):
    class Meta:
        model = WhiteLabelConfig
        fields = '__all__'

    allowed_hosts = forms.CharField(
        label='Доступные для регистрации и авторизации xmpp хосты',
        required=False,
        help_text='Если пустой - доступны любые хосты. Значения разделить запятой.',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'cols': 10,
            }
        )
    )

    avatar_masks = forms.CharField(
        label='Маски для аватаров',
        required=False,
        help_text='Значения разделить запятой.',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'cols': 10,
            }
        )
    )
