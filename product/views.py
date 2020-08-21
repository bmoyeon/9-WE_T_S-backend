import json

from django.views import View
from django.http import (
    HttpResponse,
    JsonResponse
)

from .models import (
    Product,
    Size,
    Color,
    Image,
    ProductColor
)

class ListView(View):
    def get(self, request):
        try:
            category = {}
            if 'category_id' in request.GET.keys():
                category['category'] = request.GET.get('category_id')

            products = Product.objects.filter(**category).prefetch_related(
                'productcolor_set__color',
                'productcolor_set__image_set'
            )

            product_list = [{
                "product_id"     : product.id,
                "product_name"   : product.name,
                "product_price"  : int(product.price),
                "product_colors" : [product_color.color.image for product_color in product.productcolor_set.all()],
                "product_images" : [image.image_url
                                    for product_color in product.productcolor_set.all()
                                    for image in product_color.image_set.filter(is_thumbnail = True)
                                   ]
                } for product in products]

            return JsonResponse({"product_list" : product_list}, status = 200)

        except KeyError:
            return JsonResponse({'message' : 'INVALID_KEY'}, status = 400)

class DetailView(View):
    def get(self, request, product_id):
        try:
            if not ProductColor.objects.filter(product = product_id).exists():
                return JsonResponse({'message' : 'DOES_NOT_EXIST'}, status = 404)

            if 'color_id' not in request.GET.keys():
                raise KeyError
            color_id = request.GET.get('color_id')

            if not ProductColor.objects.filter(product = product_id, color = color_id).exists():
                return JsonResponse({'message' : 'DOES_NOT_EXIST'}, status = 404)

            colors = ProductColor.objects.filter(product = product_id).select_related('color')
            item = ProductColor.objects.prefetch_related(
                'image_set',
                'product__productsize_set__size'
            ).get(product = product_id, color = color_id)

            product_info = {
                'product_id'     : item.product.id,
                'product_name'   : item.product.name,
                'product_price'  : int(item.product.price),
                'product_colors' : [{
                    'color_id'    : product_color.color.id,
                    'color_name'  : product_color.color.name,
                    'color_image' : product_color.color.image
                } for product_color in colors],
                'product_sizes'  : [product_size.size.name for product_size in item.product.productsize_set.all()],
                'product_images' : [image.image_url for image in item.image_set.all()],
                'product_guide'  : item.product.guide
            }

            return JsonResponse({"product_info" : product_info}, status = 200)

        except KeyError:
            return JsonResponse({'message' : 'INVALID_KEY'}, status = 400)
