from django.urls import path

app_name = 'bookmark'
urlpatterns = [
    path('', BookmarkList.as_view(), name='list'), #bookmark:list
]