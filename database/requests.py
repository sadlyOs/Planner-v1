from aiogram.types import User as User_info
from sqlalchemy.ext.asyncio import AsyncSession
from .models import User, Task

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


    ''' Task '''
    async def create_task(self, ids: str, user: User_info, title: str, description: str, due_datetime: str):
        task = Task(code_id=str(ids), user_id=user.id, title=title, description=description, due_datetime=due_datetime)
        self.session.add(task)
        await self.session.commit()
