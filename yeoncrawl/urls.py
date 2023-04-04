"""yeoncrawl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

import yeoncrawl.insta
import yeoncrawl.views

# schema_view = get_schema_view(
    # openapi.Info(
#  title="Your Server Name or Swagger Docs name",
#  default_version="Your API version (Custom)",
#  description="Your Swagger Docs descriptons",
        # term_of_service = "https://www.google.com/policies/terms/",
        # contact =  openapi.Contact( name = "test", email= "test@test.com"),
        # license =openapi.Contact(name = "test", email = "test@test.com"),

    # ),
    # public=True,
    # permission_classes=(permissions.AllowAny,),

# cd)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('insta/', yeoncrawl.insta.insta_soup),
    path('bulk/', yeoncrawl.insta.bulk_direct_postimg)

    # url(r'^swagger(?P<format>\.json|\.yaml)$',schema_view_v1.without_ui(cache_timeout =0),name = 'shema-json'),
    #  url(r'^swagger/$', schema_view_v1.with_ui('swagger',cache_timeout=0), name = 'schema-swagger-ui'),
    # url(r'^redoc/$', schema_view_v1.with_ui('redoc',cache_timeout=0), name = 'schema-redoc'),

]


