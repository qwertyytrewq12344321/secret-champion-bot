import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()

# ==================== СТАРТ ====================
@dp.message(Command("start"))
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="🏋️ Набор веса")],
            [types.KeyboardButton(text="🔥 Сушка")],
            [types.KeyboardButton(text="⚖️ Снижение веса")],
            [types.KeyboardButton(text="🛠 Восстановление")],
            [types.KeyboardButton(text="🏃 Выносливость")],
            [types.KeyboardButton(text="🛡️ Иммунитет")]
        ],
        resize_keyboard=True
    )
    
    await message.answer_photo(
        photo="https://i.imgur.com/0Z9vX8Z.jpg",
        caption="👑 <b>Секрет Чемпиона</b>\n\nПривет, спортсмен! 🔥\n\nВыбери направление:",
        parse_mode="HTML",
        reply_markup=keyboard
    )

# ==================== ОБЩАЯ ФУНКЦИЯ ====================
async def send_direction(message: types.Message, title: str, text: str, btn1: str, url1: str, btn2: str, url2: str):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=btn1, url=url1)],
        [InlineKeyboardButton(text=btn2, url=url2)]
    ])
    await message.answer(f"✅ <b>{title}</b>\n\n{text}", parse_mode="HTML", reply_markup=keyboard)

# ==================== НАПРАВЛЕНИЯ ====================

@dp.message(F.text == "🏋️ Набор веса")
async def mass_gain(message: types.Message):
    await send_direction(message, "Набор мышечной массы", "Хочешь качественно набирать мышцы без лишнего жира?\n\n• Профицит калорий\n• Силовые тренировки 5× в неделю\n• Контроль прогрессии", "📥 Скачать программу", "https://example.com/mass", "💰 Купить полный план", "https://example.com/mass-full")

@dp.message(F.text == "🔥 Сушка")
async def drying(message: types.Message):
    await send_direction(message, "Сушка", "Максимальное сжигание жира при сохранении мышц.\n\n• Правильный дефицит\n• Кардио + силовые\n• Контроль воды", "📥 Программа сушки", "https://example.com/dry", "💰 Полный курс сушки", "https://example.com/dry-full")

@dp.message(F.text == "⚖️ Снижение веса")
async def weight_loss(message: types.Message):
    await send_direction(message, "Снижение веса", "Комфортное похудение без потери мышц.\n\n• Плавный дефицит\n• Сохранение мышц\n• Без срывов", "📥 Программа снижения", "https://example.com/loss", "💰 Индивидуальный план", "https://example.com/loss-full")

@dp.message(F.text == "🛠 Восстановление")
async def recovery(message: types.Message):
    await send_direction(message, "Восстановление после соревнований", "Правильный выход из сушки и восстановление организма.", "📥 Протокол восстановления", "https://example.com/recovery", "💰 Полное сопровождение", "https://example.com/recovery-full")

@dp.message(F.text == "🏃 Выносливость")
async def endurance(message: types.Message):
    await send_direction(message, "Увеличение выносливости", "Для единоборств, кроссфита и бега.", "📥 Программа выносливости", "https://example.com/endurance", "💰 Полный цикл", "https://example.com/endurance-full")

@dp.message(F.text == "🛡️ Иммунитет")
async def immunity(message: types.Message):
    await send_direction(message, "Укрепление иммунитета", "Меньше болеть и лучше себя чувствовать.", "📥 Протокол иммунитета", "https://example.com/immunity", "💰 Расширенный план", "https://example.com/immunity-full")

# ==================== ЗАПУСК ====================
async def main():
    logging.basicConfig(level=logging.INFO)
    print("🤖 Бот 'Секрет Чемпиона' запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
