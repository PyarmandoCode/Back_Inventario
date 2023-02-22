from django.urls import path
from .views import ProductosList,CategoriasList,CategoriasCreate,CategoriasDelete,CategoriasUpdate,ProductosCreate,RegistrarUsuarios


#Endpoint
urlpatterns = [
    path('api/productsall/', ProductosList.as_view()),
    path('api/categoriesall/', CategoriasList.as_view()),
    path('api/categoriescreate/', CategoriasCreate.as_view()),
    path('api/categoriesdelete/<pk>', CategoriasDelete.as_view()),
    path('api/categoriesupdate/<pk>', CategoriasUpdate.as_view()),
    path('api/productoscreate/', ProductosCreate.as_view()),
    path('api/registrarusuarios/', RegistrarUsuarios.as_view()),
]
