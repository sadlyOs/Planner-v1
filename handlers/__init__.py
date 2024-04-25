from aiogram import Router

def setup_message_routers():
    from .user import other, settings, create, complete_ask, my_tasks
    router = Router()
    router.include_routers(
        create.create,
        settings.settings,
        other.other,
        complete_ask.complete,
        my_tasks.my_tasks
        )

    return router