from django.shortcuts import render

@sync_to_async
@login_required
def user_logout(request):
    logout(request)
    messages.success(request, "You have been successfully logged out!")
    return HttpResponsePermanentRedirect(reverse("home"))


@sync_to_async
def loginform(request):
    if request.method == "POST":
        form = LoginForm(request=request, data=request.POST)

        username = request.POST.get("username")
        if not User.objects.filter(username=username).exists():
            messages.warning(request, "Please create an new account !")
            return redirect(reverse("signin"))
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            try:
                next_url = ast.literal_eval(str(request.POST.get("next")))
            except:
                next_url = request.POST.get("next")

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                if bool(next_url):
                    return HttpResponsePermanentRedirect(next_url)
                return HttpResponsePermanentRedirect(reverse("home"))
            messages.error(request, "Invalid username or password.")
            return redirect(reverse("signin"))
        messages.error(request, "Details Invalid")
        return redirect(reverse("signin"))
    form = LoginForm()
    return render(
        request,
        "login.html",
        {
            "form": form,
            "next_url": request.GET.get("next")
        },
    )
