"""CodePlanetTeacher URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

from mains.views import Signup, Login, CheckEmail, CreateClass, TeacherClass, DetailClassRoom, CreatedClassRoom, \
    CreateStudent

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name="pages/main.html")),
    url(r'^class$', TemplateView.as_view(template_name="pages/class.html")),
    url(r'^content$', TemplateView.as_view(template_name="pages/content.html")),
    url(r'^FAQ$', TemplateView.as_view(template_name="pages/FAQ.html")),
    url(r'^after_login$', TemplateView.as_view(template_name="pages/teacher_after_login.html")),
    url(r'^teacher_class', TeacherClass),
    url(r'^create_class$', TemplateView.as_view(template_name="pages/teacher_create_class.html")),
    url(r'^created_class', CreatedClassRoom),
    url(r'^signup$', Signup),
    url(r'^login$', Login),
    url(r'^checkEmail', CheckEmail),
    url(r'^createClass', CreateClass),
    url(r'^createStudent', CreateStudent),
    url(r'^detail_class', DetailClassRoom)
]
