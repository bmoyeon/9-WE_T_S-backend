from django.urls import path

from .views import (
	AccountSignUpView,
	AccountSignInView,
	GuestSignUpView,
)

urlpatterns = [
	path('/sign-up', AccountSignUpView.as_view()),
	path('/sign-in', AccountSignInView.as_view()),
	path('/guest/sign-up', GuestSignUpView.as_view()),
]
