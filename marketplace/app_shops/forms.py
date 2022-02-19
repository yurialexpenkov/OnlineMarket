from django import forms
from app_shops.models import Shops


class ShopsForm(forms.ModelForm):

    class Meta:
        model = Shops
        exclude = ('user',)

class ToBusketForm(forms.Form):
    shop_id = forms.IntegerField()
    post_id = forms.IntegerField()

class ForRatingForm(forms.Form):
    calendar = forms.DateField()

# post_id = cache.get('post_id')
# if post_id is None:
#     post_id = form.cleaned_data['post_id']
# elif post_id == form.cleaned_data['post_id']:
#     return HttpResponseRedirect('/marketplace/products/<int:pk>/basket/')