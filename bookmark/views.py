from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from bookmark.models import Bookmark


class BookmarkListView(ListView):  # bookmark_list.html
    model = Bookmark


class BookmarkCreateView(CreateView):  # bookmark_form.html
    model = Bookmark
    fields = ['site_name', 'url']   #form태그가 들어가는 항목에는 필드를 쓴다.
    template_name_suffix = '_create'  # bookmark_create.html
    success_url = reverse_lazy('bookmark:list')

class BookmarkDetailView(DetailView) :
    model = Bookmark