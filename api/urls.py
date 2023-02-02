from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import *

urlpatterns = [
    # authors books
    path('authors/', AuthorsView.as_view()),
    path('authors/<str:pk>/', AuthorView.as_view()),

    # books
    path('books/', BooksView.as_view()),
    path('books/<str:pk>/', BookView.as_view()),

    # metaphors
    path('metaphors/', MetaphorsView.as_view()),

    # customer
    path('customers/', CustomersView.as_view()),
    path('customers/<str:pk>/', CustomerView.as_view()),

    # cateogry
    path('categories/', CategoriesView.as_view()),
    path('categories/<str:pk>/', CategoryView.as_view()),

    # auth
    path('logout/', LogoutView.as_view(), name="logout"),
    path('login/', obtain_auth_token, name="obtain_auth_token"),

    #  employees
    path('users/', UsersView.as_view(), name="users"),
    path('users/<str:pk>/', UserView.as_view(), name="users"),

    # employee groups
    path('groups/', GroupsView.as_view()),
    path('groups/<str:pk>/', GroupView.as_view()),
]
