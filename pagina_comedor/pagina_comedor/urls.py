"""pagina_comedor URL Configuration

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
from django.contrib import admin
from django.urls import path
from pagina_comedor.views import saludo
from pagina_comedor.views import menu
from pagina_comedor.views import horarios
from pagina_comedor.views import login
from pagina_comedor.views import trabajador
from pagina_comedor.views import gestor
from pagina_comedor.views import gestor_menu
from pagina_comedor.views import gestor_horarios
from pagina_comedor.views import gestor_platillo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('comedor/', saludo, name="comedor"),
    path('menu/', menu, name="menu"),
    path("horarios/",horarios, name="horarios"),
    path('trabajador/',trabajador, name="trabajador"),
    path('login/',login, name="login"),
    path('gestor/',gestor,name="gestor"),
    path('gestor_menu/',gestor_menu, name="gestor_menu"),
    path('gestor_horario/',gestor_horarios,name="gestor_horario"),
    path('gestor_platillo/',gestor_platillo,name="gesttor_platillo"),
]
