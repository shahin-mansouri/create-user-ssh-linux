from django .urls import path
# from .views import HomeView
from .views import HomeView
from django.contrib.auth.decorators import login_required
from . import views


urlpatterns = [
    # path('', HomeView.as_view(), name='home'),
    path('', login_required(HomeView.as_view()), name='home'),
    path('<int:pk>/', login_required(HomeView.as_view()), name="ssh_detail"),
    path('<int:pk>/save/', views.change, name='save'),
    path('create/', login_required(views.create), name='create'),
]


