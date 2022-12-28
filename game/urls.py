from django.urls import path,re_path
from . import views 

app_name = "game"

urlpatterns = [
    re_path(r"(?P<category>\d+)/headlines/$",views.Headlines.as_view(),name="headlines"), #(?P<pk>\d+)
    re_path(r"categories/$",views.Categories.as_view(),name="categories"),
    re_path(r"rules/$",views.Rules.as_view(),name="rules")
]