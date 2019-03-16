"""
from django.urls import path
from . import views

urlpatterns = [

]
"""


from django.conf.urls import url

from . import views

urlpatterns = [url(r"^$", views.FibV.fibIndex, name="fibonacci")]
