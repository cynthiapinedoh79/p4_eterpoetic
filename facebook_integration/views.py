import json, base64, hmac, hashlib
from django.conf import settings
from django.http import JsonResponse, HttpResponseBadRequest

def _parse_signed_request(signed_request, app_secret):
    sig, payload = signed_request.split('.', 1)
    sig = base64.urlsafe_b64decode(sig + '==')
    data = json.loads(base64.urlsafe_b64decode(payload + '=='))
    expected = hmac.new(app_secret.encode(), msg=payload.encode(), digestmod=hashlib.sha256).digest()
    if not hmac.compare_digest(sig, expected):
        raise ValueError("Bad signature")
    return data

def fb_data_deletion(request):
    if request.method != "POST":
        return HttpResponseBadRequest("POST required")
    signed_request = request.POST.get("signed_request")
    try:
        data = _parse_signed_request(
            signed_request,
            settings.SOCIALACCOUNT_PROVIDERS["facebook"]["APP"]["secret"]
        )
    except Exception:
        return HttpResponseBadRequest("Invalid signed_request")

    # Here you'd remove user data based on data["user_id"]
    status_url = "https://your-domain.com/facebook/datadeletion/status/"
    return JsonResponse({
        "url": status_url,
        "confirmation_code": str(data.get("user_id"))
    })

def fb_deauthorize(request):
    if request.method != "POST":
        return HttpResponseBadRequest("POST required")
    signed_request = request.POST.get("signed_request")
    try:
        data = _parse_signed_request(
            signed_request,
            settings.SOCIALACCOUNT_PROVIDERS["facebook"]["APP"]["secret"]
        )
    except Exception:
        return HttpResponseBadRequest("Invalid signed_request")

    # Optional: unlink or delete user data here
    return JsonResponse({"success": True})

