from django.shortcuts import render, redirect
from .models import SavedItem
from django.conf import settings


def save_for_later(request, product_id):
    if request.user.is_authenticated:
        # Check if the item is already in the saved list
        if not SavedItem.objects.filter(user=request.user, product_id=product_id).exists():
            SavedItem.objects.create(user=request.user, product_id=product_id)
        # Redirect to the product page or wherever you want
        return redirect('product_detail', product_id=product_id)
    else:
        # Handle when the user is not logged in
        # Redirect to login or show a message
        return redirect('login')


def remove_from_saved(request, item_id):
    if request.user.is_authenticated:
        saved_item = SavedItem.objects.get(id=item_id, user=request.user)
        saved_item.delete()
        return redirect('saved_for_later')
    else:
        # Handle when the user is not logged in
        # Redirect to login or show a message
        return redirect('login')


def saved_for_later(request):
    if request.user.is_authenticated:
        saved_items = SavedItem.objects.filter(user=request.user)
        return render(request, 'saved/saved_for_later.html', {'saved_items': saved_items})
    else:
        # Handle when the user is not logged in
        # Redirect to login or show a message
        return redirect('login')
