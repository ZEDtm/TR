from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from calldata.calldata import CartItemData
from keyboards.for_menu_handlers import cart_keyboard


router = Router()


@router.message(Command("start"))
async def command_start(message: Message, user: dict) -> None:
    text = 'Your ShoppingCart:\n'
    items_id = []
    for item_id, item in enumerate(user['cart']):
        text += f"Item: {item['label']} In cart: {item['count']}"
        items_id.append(item_id)
    await message.answer(f"DataBase ID: {user['_id']}\nYour ID: {user['user_id']}\n"+text,
                         reply_markup=cart_keyboard(items_id))


@router.callback_query(CartItemData.filter())
async def command_start(call: CallbackQuery, callback_data: CartItemData, user: dict) -> None:
    item_id = callback_data.item_id
    item = user['cart'][item_id]
    await call.message.answer(f"You pick {item['label']}")
