from rest_framework.permissions import BasePermission

from .models import Advertisement


class IsCreator(BasePermission):
    """
    Создадим кастомный permission.

    Тут мы обработаем ситуацию, где пользователь пытается обновить или удалить
    чужое объявление. Такой пользователь у нас получит ответ 403 (Forbidden):
    "detail": "You do not have permission to perform this action."
    Вгимание! Следуем строгому API:
        наследование от BasePermission,
        название функции - has_permission (оверрайдим)
    """

    def has_permission(self, request, view):
        advertisement_id: int = request.parser_context['kwargs']['pk']
        current_sender_id: int = request.user.id
        creator_id: int = \
            Advertisement.objects.filter(id=advertisement_id).values_list('creator', flat=True)[0]
        # и только если текущий отправитель запроса на update/partial_update/destroy объявления
        # действительно является создателем этого объявления, то
        if current_sender_id == creator_id:
            return bool(request.user.is_authenticated)


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_superuser)
