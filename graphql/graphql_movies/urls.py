from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView
from graphql_movies.schema import schema
from django.views.decorators.csrf import csrf_exempt # New library

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
