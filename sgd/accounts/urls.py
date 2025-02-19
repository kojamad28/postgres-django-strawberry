from django.urls import path

from .schema import schema
from .views import CustomUserGraphQLView

app_name = "accouns"
urlpatterns = [
    path("graphql/", CustomUserGraphQLView.as_view(schema=schema)),
]
