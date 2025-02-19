import strawberry
import strawberry_django

from .models import CustomUser


@strawberry_django.type(CustomUser)
class CustomUserType:
    id: strawberry.auto
    username: strawberry.auto
    email: strawberry.auto
    is_active: strawberry.auto
    is_staff: strawberry.auto
    is_admin: strawberry.auto


@strawberry_django.type(CustomUser)
class CreateCustomUserInput:
    username: strawberry.auto
    email: strawberry.auto
