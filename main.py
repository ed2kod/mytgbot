import requests

from aiogram import Bot, Dispatcher, executor, types

token = "1465623796:AAHIOYiysY-ATsqTfxXNgJ81-Jg0C-6LmKg"


bot = Bot(token="1465623796:AAHIOYiysY-ATsqTfxXNgJ81-Jg0C-6LmKg")
dp = Dispatcher(bot=bot)


async def get_weather():
    api_token = "e4e466cff0d40122b636aad08be6fa85"

    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=Армавир,ru&appid={api_token}&units=metric')
    data = response.json()
    return data


@dp.message_handler(commands=["weather"])
async def start_handler(message: types.Message):
    weather_data = await get_weather()

    await message.reply(
        f"Текущая погода в Армавире:\n\n"
        f"Температура: {weather_data['main']['temp']}°C\n"
        f"Влажность: {weather_data['main']['humidity']}%\n"
        f"Ветер: {weather_data['wind']['speed']} м/с\n"
    )


@dp.message_handler(commands=["help"])
async def echo(msg: types.Message) -> None:
    await msg.answer("idi nahoy")


@dp.message_handler(commands=["start"])
async def echo(msg: types.Message) -> None:
    await msg.answer(msg.text)


if __name__ == "__main__":
    executor.start_polling(dp)
