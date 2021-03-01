from decimal import Decimal
from typing import Dict, Optional
from django.core.paginator import Paginator
from django.shortcuts import render

from django.core.handlers.wsgi import WSGIRequest
from django.db.models import F, Sum, ExpressionWrapper, DecimalField, Count, Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views import generic
from .models import *


def index(request: WSGIRequest) -> HttpResponse:
    print('Giorgi')
    return render(request=request, template_name='shipping/index.html')