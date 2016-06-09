from django import forms
from tracks.models import Track, Genre

from django.utils.translation import ugettext_lazy as _

from tracks.models import Track 

class AddTrackForm(forms.ModelForm):
	class Meta:
		model = Track 
		fields = "__all__"
		error_message={
			'title' : {
				'max_length':_("Title of the track is too long.")
			},
		}
		
class AddGenreForm(forms.ModelForm):
	class Meta:
		model = Genre
		fields="__all__"