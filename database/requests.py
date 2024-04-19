from sqlalchemy.ext.asyncio import AsyncSession
from .models import User

class Request:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create_user(self, user_id: int) -> None:
        user = User(id=user_id)
        self.session.add(user)
        await self.session.commit()

    async def get_user(self, user_id: int) -> User:
        return await self.session.get(User, user_id)

    async def change_user_lang(self, user_id: int, lang: str) -> None:
        user = await self.session.get(User, user_id)
        if user.lang != lang:
            user.lang = lang
            await self.session.commit()