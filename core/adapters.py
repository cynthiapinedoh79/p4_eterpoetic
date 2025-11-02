# core/adapters.py
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.utils import generate_unique_username

class AutoSignupWithEmailAdapter(DefaultSocialAccountAdapter):
    def is_auto_signup_allowed(self, request, sociallogin):
        """
        Allow auto-signup when the provider returns an email.
        Also auto-fill username if your site still requires one.
        """
        user = sociallogin.user
        data = sociallogin.account.extra_data

        email = user.email or data.get("email")
        if not email:
            return False  # fall back to allauth's "Complete your signup" form

        # ensure email is set
        user.email = email

        # if username is required, generate one from provider data
        if not getattr(user, "username", None):
            base = [
                data.get("name"),
                data.get("first_name"),
                data.get("last_name"),
                (email.split("@", 1)[0] if email else None),
                "user",
            ]
            user.username = generate_unique_username(base)

        return True
