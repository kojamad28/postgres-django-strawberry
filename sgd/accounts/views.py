from strawberry.django.views import AsyncGraphQLView

from .models import CustomUser


class CustomUserGraphQLView(AsyncGraphQLView):
    pass  # 将来的にGraphQLの共通部分をカスタマイズしたい場合に対応できるようにする。
