from django.urls import path
from . import views
urlpatterns = [
    path("",views.home,name="home"),
    path("add_category/",views.add_category,name="add_category"),
    path("delete_category/<int:id>/",views.delete_category,name="delete_category"),
    path("edit_category/<int:id>/",views.edit_category,name="edit_category"),
    path("add_author/",views.add_author,name="add_author"),
    path("edit_author/<int:id>",views.edit_author,name="edit_author"),
    path("delete_author/<int:id>/",views.delete_author,name="delete_author"),
    path("add_post/",views.add_post,name="add_post"),
]
