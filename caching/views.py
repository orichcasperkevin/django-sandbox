from django.http import HttpResponse
from django.views.decorators.cache import cache_page
from query_optimization.models import Product
# Create your views here.

# @cache_page(60 * 15) 
def test_view(request):
    products = Product.objects.all()

    return HttpResponse(products)
