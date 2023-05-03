# 3.9
from typing import Union, Optional


class User:
    pass


def get_user_by_id(user_id: Union[str, int]) -> Optional[User]:
    return User()


# 3.10
# вместо Union используем |
# Вместо Optional используем User | None
def get_user_by_id2(user_id: str | int) -> User | None:
    return User()
