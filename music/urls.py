from django.urls import include, path
import music.views as view
from .schema import schema
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', view.index, name='index'),
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True , schema=schema))),
]
