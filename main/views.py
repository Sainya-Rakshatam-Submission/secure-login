from asgiref.sync import sync_to_async
from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.contrib.auth.decorators import login_required


@sync_to_async
@login_required
def main_view(request):
    return render(request, 'main.html')