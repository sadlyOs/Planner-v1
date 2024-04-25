from aiogram.types import User as User_info
from sqlalchemy.ext.asyncio import AsyncSession
from .models import User, Task, RelUserTask

class Request:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    ''' User '''

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
        task = Task(id=str(ids), user_id=user.id, title=title, description=description, due_datetime=due_datetime)
        rel = RelUserTask(user_id=user.id, task_id=str(ids))
        self.session.add(task)
        self.session.add(rel)
        await self.session.commit()

    async def get_task(self, ids: str):
        return await self.session.get(Task, ids)

    async def edit_completed(self, ids: str):
        task = await self.session.get(Task, ids)
        task.completed = True
        await self.session.commit()

    async def edit_excpectation(self, ids: str, expectation: bool = False):
        task = await self.session.get(Task, ids)
        task.expectation = expectation
        await self.session.commit()

    
