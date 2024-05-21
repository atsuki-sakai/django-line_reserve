from allauth.account.forms import SignupForm
from django import forms

class SignupUserForm(SignupForm): 
    name = forms.CharField(max_length=30, label="名前")

    def save(self, request):
        # ユーザー情報を保存
        user = super().save(request)
        # 名前を保存
        user.name = self.cleaned_data['name']
        user.save()
        return user

