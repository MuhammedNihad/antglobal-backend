from __future__ import annotations

from typing import TypeVar

from django.db.models import Model, QuerySet

T_co = TypeVar("T_co", bound=Model, covariant=True)


class ProductItemQueryset(QuerySet[T_co]):
    """
    Custom queryset for the ProductItem model, providing specialized methods for querying product items.

    Methods:
        unpublished(self): Retrieve a queryset containing unpublished products.
        in_stock(self): Retrieve a queryset containing published products with stock greater than 0.
        new_arrivals(self): Retrieve a queryset containing published products marked as new arrivals.
        published(self): Retrieve a queryset containing published products.
    """

    def unpublished(self) -> QuerySet[T_co]:
        """
        Returns a queryset containing unpublished products.
        """
        return self.filter(is_published=False)

    def published(self) -> QuerySet[T_co]:
        """
        Returns a queryset containing published products.
        """
        return self.filter(is_published=True)

    def in_stock(self) -> QuerySet[T_co]:
        """
        Returns a queryset containing published products with stock greater than 0.
        """
        return self.published().filter(stock__gt=0)

    def new_arrivals(self) -> QuerySet[T_co]:
        """
        Returns a queryset containing published products marked as new arrivals.
        """
        return self.published().filter(is_new_arrival=True)
