"""refugio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
#from home import views 

urlpatterns = [

    url('admin/', admin.site.urls),
    #url('home/', home, kwargs={'template_name': 'Home/index.html'}, name='home'),
    url(r'^mascota/', include('apps.mascota.urls'),name="mascota"),
    url('adopcion/', include('apps.adopcion.urls'),name="adopcion"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

