from aiogram.fsm.state import State, StatesGroup


class UserChannel(StatesGroup):
    chat = State()
    contract = State()
    photo = State()
    links = State()



class RemoveChannel(StatesGroup):
    wait_for_name_channel = State()