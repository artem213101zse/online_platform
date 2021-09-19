from django import forms


class GeoForm(forms.Form):
    latitude = forms.FloatField(
        label='Широта',
        required=True,
        max_value=1000,
        min_value=0,
        widget=forms.HiddenInput(
            attrs={
                'id': 'latitude',
            }
        )
    )
    longitude = forms.FloatField(
        label='Долгота',
        required=True,
        max_value=1000,
        min_value=0,
        widget=forms.HiddenInput(
            attrs={
                'id': 'longitude',
            }
        )
    )
    altitude = forms.FloatField(
        label='Высота',
        required=True,
        widget=forms.HiddenInput(
            attrs={
                'id': 'altitude',
            }
        )
    )
