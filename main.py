from aiogram import Bot, Dispatcher, executor, types
import re
import data
import model

API_TOKEN = '5833517642:AAHXEVIn-FB4b6WW6FoorHClykDrrDk9NBE'

x = ""
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Привет!\nЭтот бот предназначен для предсказания рисков заболеваний сердца по физиологическим параметрам\nДля того, чтобы узнать, как отправить свои данные на проверку, введите /instruction")


@dp.message_handler(commands=['help'])
async def first_reply(message: types.Message):
    await message.answer('/start - запуск бота\n/help - справка\n/instruction - инструкция по отправке физиологических данных')


@dp.message_handler(commands=['instruction'])
async def instruct(message: types.Message):
    await message.answer('Необходимо ввести 7 параметров через запятую с пробелом:\n\nболь в груди после физической нагрузки по шкале от 0 до 3\n\nпостоянная боль в груди по шкале от 0 до 3\n\nнаивысший показатель пульса\n\nдепрессия сегмента ST на кардиограмме после физической нагрузки относительно состояния покоя с десятичной точкой\n\nнаклон сегмента ST на кардиограмме, где 0 - горизонтальная, 1 - по часовой стрелке, 2 - против часовой стрелки\n\nколичество крупных сосудов, видимых при рентгеноскопии от 0 до 3\n\n2степень талассемии от 0 до 2')


@dp.message_handler()
async def data1(message: types.Message):
    global x
    x = message.text
    pattern = r'\d+, \d+, \d+, \d+.\d+, \d+, \d+, \d+'
    if re.fullmatch(pattern, x):
        raw = data.data_collect(x)
        pred = model.pred(data.data_assembly(raw))
        if pred[-1] < 0.3:
            answer = 'Наличие сердечно-сосудистых заболеваний маловероятно'
        elif (pred[-1] >= 0.3 and pred[-1] < 0.8):
            answer = 'Есть значительная вероятность наличия сердечно-сосудистых заболеваний'
        elif pred[-1] >= 0.8:
            answer = 'Вероятность наличия сердечно-сосудистых заболеваний крайне высока'
        await message.answer(answer)
    else:
        await message.answer('Неправильный формат значений')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

