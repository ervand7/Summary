import pytest
from model_bakery import baker


@pytest.fixture()
def product_factory():
    """
    Creates product.
    """

    def factory(**kwargs):
        return baker.make("Product", **kwargs)

    return factory


@pytest.fixture()
def product_review_factory():
    """
    Creates product-review.
    """

    def factory(**kwargs):
        return baker.make("ProductReview", **kwargs)

    return factory


@pytest.fixture()
def product_collections_factory():
    """
    Creates product-collection.
    """

    def factory(**kwargs):
        return baker.make("ProductCollections", **kwargs)

    return factory


@pytest.fixture()
def order_factory():
    """
    Creates order.
    """

    def factory(**kwargs):
        return baker.make("Order", **kwargs)

    return factory
