from django.urls import path
from . import views

urlpatterns = [
    # before login
    path('', views.indexclass.as_view(), name="Index"),
    path('thong-tin/<int:movie_id>', views.thongtinclass.as_view(), name="thongtin"),
    path('dang-nhap/', views.loginclass.as_view(), name="dangnhap"),
    path('dang-ki/', views.signupclass.as_view(), name="dangki"),
    path('xem-phim/<int:movie_id>', views.watchingclass.as_view(), name="xemphim"),
    path('xem-phim-theo-tap/<int:episode_id>', views.continueswatchingclass.as_view(), name="xemphimtheotap"),
    path('the-loai/anime', views.animeClass.as_view(), name="animeClass"),
    path('the-loai/cartoon', views.cartoonClass.as_view(), name="cartoonClass"),
    path('the-loai/drama', views.dramaClass.as_view(), name="dramaClass"),
    path('the-loai/sieu-nhan', views.superClass.as_view(), name="superClass"),



    # after login
    path('home/', views.userindexclass.as_view(), name="userIndex"),
    path('home/<int:user_id>', views.userindexclasss.as_view(), name="userIndexx"),
    path('user-thong-tin/<int:user_id>/<int:movie_id>', views.userthongtinclass.as_view(), name="userthongtin"),
    path('xem-phim/<int:user_id>/<int:movie_id>', views.userwatchingclass.as_view(), name="userxemphim"),
    path('xem-phim-theo-tap/<int:user_id>/<int:episode_id>', views.usercontinueswatchingclass.as_view(), name="userxemphimtheotap"),
    path('the-loai/anime/<int:user_id>', views.useranimeClass.as_view(), name="useranimeClass"),
    path('the-loai/cartoon/<int:user_id>', views.usercartoonClass.as_view(), name="usercartoonClass"),
    path('the-loai/drama/<int:user_id>', views.userdramaClass.as_view(), name="userdramaClass"),
    path('the-loai/sieu-nhan/<int:user_id>', views.usersuperClass.as_view(), name="usersuperClass"),




    # test
    path('test', views.test, name="test"),
]