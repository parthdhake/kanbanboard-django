from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('board/<int:pk>', views.board_details, name='board'),
    path('board/card/<int:pk>', views.update_details, name='update'),
    path('board/card/delete/<int:pk>', views.delete_card, name='delete'),
]
