from django.shortcuts import render

from shop.models import Product


def products_view(request):
    if request.GET.get('color'):
        product_list = Product.objects.filter(color=request.GET.get('color'))
    else:
        product_list = Product.objects.all()

    return render(request, "index.html", {"product_list": product_list})
