import pytest


class Test01Account:

    @pytest.mark.django_db(transaction=True)
    def test_01_user_created(self, django_user_model):
        user = django_user_model.objects.create_user(  # noqa: S106
            username='test', email='test@test.org', password='test',
        )
        assert user.is_active, 'User not activated'

    @pytest.mark.django_db(transaction=True)
    def test_02_email_required(self, django_user_model):
        with pytest.raises(ValueError):
            assert django_user_model.objects.create_user(  # noqa: S106
                username='test', password='test',
            ), 'Email is not required'
