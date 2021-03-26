from django.urls import path
from .views import PhotoCreate, PhotoDelete, PhotoDetail, PhotoList, PhotoUpdate, PhotoLike, PhotoFavorite
from django.conf.urls.static import static
from django.conf import settings

app_name = "photo"

urlpatterns = [
    path("", PhotoList.as_view(), name='index'),  #as_view해줘야 제네릭뷰연결가능
    path("detail/<int:pk>/", PhotoDetail.as_view(), name='detail'),
    path("update/<int:pk>/", PhotoUpdate.as_view(), name='update'),
    path("delete/<int:pk>/", PhotoDelete.as_view(), name='delete'),
    path("create/", PhotoCreate.as_view(), name='create'),
    path('like/<int:photo_id>/', PhotoLike.as_view(), name= 'like'),
    path('favorite/<int:photo_id>/', PhotoFavorite.as_view(), name='favorite'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
