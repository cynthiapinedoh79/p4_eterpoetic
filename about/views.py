from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import About
from .forms import CollaborateForm


def about_me(request):
    """
    Renders the most recent information on the website author
    and allows user collaboration requests.

    Displays an individual instance of :model:`about.About`.

    **Context**
    ``about``
        The most recent instance of :model:`about.About`.
        ``collaborate_form``
            An instance of :form:`about.CollaborateForm`.
    
    **Template**
    :template:`about/about.html`
    """
    # 1. Always fetch the static content
    about = About.objects.all().order_by('-updated_on').first()

    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(
                request, 
                messages.SUCCESS,
                "Collaboration request received! I endeavour to respond within 2 working days."
            )
            
            # CRITICAL FIX: Manually save the session to ensure messages persist
            request.session.save() 
            
            return redirect(reverse('about'))
        
    # 2. Handle GET request or unsuccessful POST
    else: # This block handles the initial GET and the GET following the redirect
        collaborate_form = CollaborateForm()
    
    # 3. Final render path (only for GET or invalid POST)
    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "collaborate_form": collaborate_form
        },
    )

