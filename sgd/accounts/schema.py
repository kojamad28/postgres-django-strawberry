import strawberry
import strawberry_django

from .models import CustomUser
from .types import CustomUserType, CreateCustomUserInput


@strawberry.type
class Query:
    @strawberry_django.field
    def me(self, info):
        user = info.context.request.user
        if user.is_authenticated:
            return user.objects.get(id=user.id)
        else:
            return None


@strawberry.type
class Mutation:
    @strawberry_django.field
    def create_user(self, info, input):
        return CustomUser.objects.acreate(
            username=input.username, email=input.email,
            is_active=True, is_staff=False, is_admin=False
        )


schema = strawberry.Schema(query=Query, mutation=Mutation)
