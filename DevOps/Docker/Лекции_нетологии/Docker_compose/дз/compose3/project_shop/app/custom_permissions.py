from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import BasePermission, SAFE_METHODS


# =================================== permissions for class Product ===================================


class ProductCreatePermission(BasePermission):
    """
    This class defines permissions for model Product and <create> action.
    Внимание! Следуем строгому API:
        наследование от BasePermission,
        название функции - has_permission (оверрайдим)
    """

    def has_permission(self, request, view):
        # only admin can create products
        return request.user.is_superuser


# =================================== permissions for class Order ===================================


class OrderCreatePermission(BasePermission):
    """
    This class defines permissions for model Order and <create> action.
    """

    def has_permission(self, request, view):
        # only authenticated users can create orders
        return request.user.is_authenticated


class OrderRetrieveDestroyPermission(BasePermission):
    """
    This class defines permissions for model Order and <retrieve, destroy> actions.
    """
    def has_object_permission(self, request, view, obj):
        """
        In this case (and further, regarding GET, PUT, PATCH, DELETE), if necessary
        we will use has_object_permission, not has_permission, so here goes the detail.
        The main feature of this function is the <obj> parameter, due to which we do not have to
        additionally write queries to the database to get data about the object, its creator, etc.
        https://webdevblog.ru/razresheniya-v-django-rest-framework/
        https://stackoverflow.com/questions/43064417/whats-the-differences-between-has-object-permission-and-has-permission-in-drfp#answers
        """
        # only admin can see or delete any orders
        # regular user can see or delete only his own orders
        return request.user.is_superuser or request.user == obj.user


class OrderListPermission(BasePermission):
    """
    This class defines permissions for model Order and <list> action.
    """

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True


class OrderUpdatePartialUpdatePermission(BasePermission):
    """
    This class defines permissions for model Order and <update, partial_update> actions.
    """

    def has_object_permission(self, request, view, obj):
        # only admin can change any order
        if request.user.is_superuser:
            return True
        # regular user can change only his own orders
        order_initial_status = obj.status
        order_current_status = request.data['status']
        order_creator_id = obj.user_id
        current_request_sender_id = request.user.id
        if current_request_sender_id == order_creator_id:
            # but regular user can not change order status
            if order_current_status == order_initial_status:
                return True
            else:
                raise PermissionDenied('Only admins can change order status!')


# =================================== permissions for class ProductReview ===================================


class ProductReviewCreatePermission(BasePermission):
    """
    This class defines permissions for model ProductReview and <create> action.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated


class ProductReviewUpdatePartialUpdateDestroyPermission(BasePermission):
    """
    This class defines permissions for model ProductReview and
    <update, partial_update, destroy> actions.
    """

    def has_object_permission(self, request, view, obj):
        current_sender_id = request.user.id
        # only review creator can update, partial_update and destroy current review
        return current_sender_id == obj.creator.id


# =================================== permissions for class ProductCollections ===================================


class ProductCollectionsPermission(BasePermission):
    """
    This class defines permissions for model ProductCollections and
    <create, update, partial_update, destroy> actions.
    """
    def has_permission(self, request, view):
        # only admin can create collections
        return request.user.is_superuser
