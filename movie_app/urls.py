from django.urls import path
from .views import GetMoviesView
# from rest_framework.routers import SimpleRouter
# from . import views
# from django.conf.urls import url


urlpatterns = [
    path('movies/', GetMoviesView.as_view(), name='Movies-all')
]


'''
simplerouter = SimpleRouter()
simplerouter.register('movies', GetMoviesView)

urlpatterns = SimpleRouter.urls

urlpatterns = [
    url(r'^movies', views.GetMoviesView)
]
'''

