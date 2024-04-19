from aiogram import Router

def setup_message_routers():
    from .user import other
    router = Router()
    router.include_router(other.other)

    return router