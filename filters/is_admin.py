from typing import List

from aiogram.filters import BaseFilter
from aiogram.types import Message

from create_bot import admins


class IsAdmin(BaseFilter):
    def __init__(self, user_ids: List[int] = admins) -> None:
        self.user_ids = user_ids

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.user_ids
