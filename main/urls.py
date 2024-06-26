from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.views import serve
from django.views.decorators.cache import never_cache


from .views import index, other_page, profile, user_activate, by_rubric
from .views import BBLoginView, bblogoutview, BBPasswordChangeView
from .views import ChangeUserInfoView, DeleteUserView
from .views import RegisterDoneView, RegisterUserView, detail

app_name = 'main'

urlpatterns = [
    path('accounts/password/change/', BBPasswordChangeView.as_view(),
         name='password_change'),
    path('accounts/profile/delete/', DeleteUserView.as_view(),
         name='profile_delete'),
    path('accounts/register/activate/<str:sign>/', user_activate,
         name='register_activate'),
    path('accounts/register/done', RegisterDoneView.as_view(),
         name='register_done'),
    path('accounts/register', RegisterUserView.as_view(),
         name='register'),
    path('accounts/profile/change',
         ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/login/', BBLoginView.as_view(), name='login'),
    path('accounts/logout/', bblogoutview, name='logout'),
    path('<int:rubric_pk>/<int:pk>/', detail, name='detail'),
    path('<int:pk>/', by_rubric, name='by_rubric'),
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index'),
]

if settings.DEBUG:
     urlpatterns.append(path('static/<path:path>', never_cache(serve)))
     urlpatterns += static(settings.MEDIA_URL,
          document_root=settings.MEDIA_ROOT)