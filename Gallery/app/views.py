from django.shortcuts import render
from .models import Category
from django.db.models import Count

# Create your views here.


def Home(request):
    categories_with_last_images = []

    # Get all categories with image count
    categories_with_count = Category.objects.annotate(image_count=Count('images'))

    for category in categories_with_count:
        last_image = category.images.last()  # Use the related name 'images'
        categories_with_last_images.append({'category': category, 'last_image': last_image})

    return render(request, 'home.html', {'categories_with_last_images': categories_with_last_images})

def Category_details(request,cid):
    category = Category.objects.get(pk=cid)
    images = category.images.all()

    return render(request, 'category_details.html', {'category': category, 'images': images})