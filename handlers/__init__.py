from aiogram import Router

def setup_message_routers():
    from .user import other, settings, create
    router = Router()
    router.include_routers(
        create.create,
        settings.settings,
        other.other,
        )

    return router