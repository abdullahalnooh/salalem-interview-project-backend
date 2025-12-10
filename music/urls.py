from django.urls import include, path
import music.views as view
from .schema import schema
from graphene_django.views import GraphQLView

urlpatterns = [
    path('', view.index, name='index'),
    path('graphql/', GraphQLView.as_view(graphiql=True , schema=schema), name='graphql'),
]