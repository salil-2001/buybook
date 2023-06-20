from django.contrib import admin
from django.urls import path,include
from book.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name='index'),
    path('book', include("book.urls")),
    path('registration/',registration,name='registration'),
    # path('sing-in/',sign_in,name='sign-in'),
    path('Author_Input/',Author_input,name='Author_Input'),
    path('addbook/',addbook,name='addbook'),
    path('form_page/',Form_page,name='Form'),
    path('adminlist/',admin_list,name='adminlist'),
    path('stafflist/',staff_list,name='stafflist'),
    path('authorlist/',author_list,name='authorlist'),
    path("booklist/",book_list, name="booklist"),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)