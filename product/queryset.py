# from django.contrib.auth import get_user_model
from product.models import Product
from constant import ORDER_BY


def get_order(user):
    order = []
    if user.is_authenticated:
        # pref = get_user_model().objects.get_or_create(
        #     user=user,
        #     defaults={
        #         "user": user,
        #         "order_by_1": ORDER_BY[0][1],
        #         "order_by_2": ORDER_BY[1][1],
        #         "order_by_3": ORDER_BY[2][1],
        #         "order_by_4": ORDER_BY[3][1],
        #     }
        # )
        order.append(user.order_by_1)
        order.append(user.order_by_2)
        order.append(user.order_by_3)
        order.append(user.order_by_4)
    else:
        order = [i[1] for i in ORDER_BY]
    return order


def get_substitute(id_, user):

    order = get_order(user)

    categories = Product.objects.get(id=id_).categories.all()

    queryset = Product.objects.filter(categories__in=categories) \
        .order_by(*order)

    return queryset
