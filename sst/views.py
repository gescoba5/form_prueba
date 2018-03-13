# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def post_list(request):
  post = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
  return render(request, 'sst/post_list.html', {'post': post})

def post_detail(request, pk):
  post = get_object_or_404(Post, pk = pk)
  return render(request, 'sst/post_detail.html', {'post': post})