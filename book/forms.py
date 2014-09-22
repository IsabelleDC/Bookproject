from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from book.models import Genre, Livre, Visitor


class EmailUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Visitor
        fields = ("username", "email", "password1", "password2")

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            Visitor.objects.get(username=username)
        except Visitor.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )

class LivreForm(ModelForm):
    class Meta:
        model = Livre

class GenreForm(forms.Form):
    name = forms.CharField(label="Genre")
