from django.shortcuts import render
from django.views.generic import ListView, CreateView

from bookmark.models import Bookmark


class BookmarkListView(ListView):
    model = Bookmark
