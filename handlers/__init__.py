from aiogram import Router

def setup_message_routers():
    from .user import other, settings
    router = Router()
    router.include_routers(other.other, settings.settings)

    return router