from django.urls import  path  
from portfolio.views import  index, download_document,contact_view


urlpatterns = [
    path('', index, name='index'),
    path('download/<int:doc_id>/', download_document, name='download_document'),
    path( 'contact/', contact_view, name='contact'),
]
