from django.conf import settings
from django.urls import path
from .views import admin_home, add_product, edit_product, delete_product, category_list, add_category, edit_category, delete_category, sign_out
from django.conf.urls.static import static

urlpatterns = [
    path('', admin_home, name='admin_home'),
    path('addproduct/', add_product, name='add_product'),
    path('editproduct/<int:product_id>/', edit_product, name='edit_product'),
    path('deleteproduct/<int:product_id>/', delete_product, name='delete_product'),
    path('categorylist/', category_list, name='category_list'),
    path('addcategory/', add_category, name='add_category'),
    path('editcategory/<int:category_id>/', edit_category, name='edit_category'),
    path('deletecategory/<int:category_id>/', delete_category, name='delete_category'),
    path('logout/', sign_out, name = 'sign_out')
   
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
