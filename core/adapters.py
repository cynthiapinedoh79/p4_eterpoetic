from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

class AutoSignupWithEmailAdapter(DefaultSocialAccountAdapter):
    def is_auto_signup_allowed(self, request, sociallogin):
        # Allow auto-signup when the provider returns an email.
        user = sociallogin.user
        email = user.email or sociallogin.account.extra_data.get("email")
        if email:
            user.email = email
            return True
        return False  # fall back to the "Complete your signup" form
