import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo, KeyboardButton, ReplyKeyboardMarkup

TOKEN = "7892759186:AAF1j-Gsi4hJY8LxrI9RgTWeumj1YeDQNfk"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    web_app = WebAppInfo(url="https://yourusername.github.io/miniapp/")
    button = KeyboardButton(text="Открыть Mini App", web_app=web_app)
    keyboard.add(button)
    await message.answer("Нажмите кнопку, чтобы открыть приложение:", reply_markup=keyboard)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
