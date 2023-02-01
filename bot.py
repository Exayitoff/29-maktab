
import logging
import time
from aiogram import Bot, Dispatcher, executor, types
from tugma import *
from cfg import *
API_TOKEN = '1921988028:AAFo0TOaaw2uDUTJjvf6uq3Ij83Dqbt_OXg'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    try:
        msg =  await bot.send_message(message.from_user.id,"Assalomu alaykum "+str(message.from_user.first_name)+" hush kelibsiz 👋🏻 \nUshbu bot orqali 29-sonli maktabning dars jadvalini ko\'rishingiz mumkin 📚 \n Iltimos o\'z sinfingizni tanlang", reply_markup=mainMenu )            
    except Exception as e:
        print(e)

@dp.message_handler()
async def echo(message: types.Message):
    try:
        match message.text:
            case "1-sinf":
                await bot.send_message(chat_id=message.from_user.id, text="O'z sinfingizni tanlang ⌛️", reply_markup=sinfnomi1)      
            case "2-sinf":
                await bot.send_message(chat_id=message.from_user.id, text="2-sinf bosildi", reply_markup=sinfnomi2)      
            case "3-sinf":
                await bot.send_message(chat_id=message.from_user.id, text="3-sinf bosildi", reply_markup=sinfnomi3)      
            case "4-sinf":
                await bot.send_message(chat_id=message.from_user.id, text="4-sinf bosildi", reply_markup=sinfnomi4)     
            case "5-sinf":
                await bot.send_message(chat_id=message.from_user.id, text="5-sinf bosildi", reply_markup=sinfnomi5)      
            case "6-sinf":
                await bot.send_message(chat_id=message.from_user.id, text="6-sinf bosildi", reply_markup=sinfnomi6)      
            case "7-sinf":
                await bot.send_message(chat_id=message.from_user.id, text="7-sinf bosildi", reply_markup=sinfnomi7)      
            case "8-sinf":
                await bot.send_message(chat_id=message.from_user.id, text="8-sinf bosildi", reply_markup=sinfnomi8)      
            case "9-sinf":
                await bot.send_message(chat_id=message.from_user.id, text="9-sinf bosildi", reply_markup=sinfnomi9)      
            case "10-sinf":
                await bot.send_message(chat_id=message.from_user.id, text="10-sinf bosildi", reply_markup=sinfnomi10)      
            case "11-sinf":
                await bot.send_message(chat_id=message.from_user.id, text="11-sinf bosildi", reply_markup=sinfnomi11)   
            case "1-A sinf":
                await bot.send_message(chat_id=message.from_user.id , text="Siz 1-A sinfni tanladingiz \nSizga qaysi kunning dars jadvali kerak 📑", reply_markup=haftaNomi1a)
            case "1-B sinf":
                await bot.send_message(chat_id=message.from_user.id , text="Siz 1-B sinfni tanladingiz \nSizga qaysi kunning dars jadvali kerak 📑", reply_markup=haftaNomi1b)
            case "1-V sinf":
                await bot.send_message(chat_id=message.from_user.id , text="Siz 1-V sinfni tanladingiz \nSizga qaysi kunning dars jadvali kerak 📑", reply_markup=haftaNomi1v)
            case "1-G sinf":
                await bot.send_message(chat_id=message.from_user.id , text="Siz 1-G sinfni tanladingiz \nSizga qaysi kunning dars jadvali kerak 📑", reply_markup=haftaNomi1g)
            case "2-A sinf":
                await bot.send_message(chat_id=message.from_user.id , text="Siz 2-A sinfni tanladingiz \nSizga qaysi kunning dars jadvali kerak 📑", reply_markup=haftaNomi2a)
            case "2-B sinf":
                await bot.send_message(chat_id=message.from_user.id , text="Siz 2-B sinfni tanladingiz \nSizga qaysi kunning dars jadvali kerak 📑", reply_markup=haftaNomi2b)
            case "2-V sinf":
                await bot.send_message(chat_id=message.from_user.id , text="Siz 2-V sinfni tanladingiz \nSizga qaysi kunning dars jadvali kerak 📑", reply_markup=haftaNomi2v)
            case "3-A sinf":
                await bot.send_message(chat_id=message.from_user.id , text="Siz 3-A sinfni tanladingiz \nSizga qaysi kunning dars jadvali kerak 📑", reply_markup=haftaNomi3a)
            case "3-B sinf":
                await bot.send_message(chat_id=message.from_user.id , text="Siz 3-B sinfni tanladingiz \nSizga qaysi kunning dars jadvali kerak 📑", reply_markup=haftaNomi3b)
            case "3-V sinf":
                await bot.send_message(chat_id=message.from_user.id , text="Siz 3-V sinfni tanladingiz \nSizga qaysi kunning dars jadvali kerak 📑", reply_markup=haftaNomi3v)
            case "4-A sinf":
                await bot.send_message(chat_id=message.from_user.id , text="Siz 4-A sinfni tanladingiz \nSizga qaysi kunning dars jadvali kerak 📑", reply_markup=haftaNomi4a)
            case "4-B sinf":
                await bot.send_message(chat_id=message.from_user.id , text="Siz 4-B sinfni tanladingiz \nSizga qaysi kunning dars jadvali kerak 📑", reply_markup=haftaNomi4b)
            case "4-V sinf":
                await bot.send_message(chat_id=message.from_user.id , text="Siz 4-V sinfni tanladingiz \nSizga qaysi kunning dars jadvali kerak 📑", reply_markup=haftaNomi4v)
            case "5-A sinf":
                await bot.send_message(chat_id=message.from_user.id , text="Siz 5-A sinfni tanladingiz \nSizga qaysi kunning dars jadvali kerak 📑", reply_markup=haftaNomi5a)
            case "5-B sinf":
                await bot.send_message(chat_id=message.from_user.id , text="Siz 5-B sinfni tanladingiz \nSizga qaysi kunning dars jadvali kerak 📑", reply_markup=haftaNomi5b)
            case "5-V sinf":
                await bot.send_message(chat_id=message.from_user.id , text="Siz 5-V sinfni tanladingiz \nSizga qaysi kunning dars jadvali kerak 📑", reply_markup=haftaNomi5v)
            case "Orqaga 🔙":
                 await bot.send_message(message.from_user.id,"Assalomu alaykum "+str(message.from_user.first_name)+" hush kelibsiz 👋🏻 \nUshbu bot orqali 29-sonli maktabning dars jadvalini ko\'rishingiz mumkin 📚 \n Iltimos o\'z sinfingizni tanlang", reply_markup=mainMenu )            
            case "Dushanba 📕":
                await bot.send_message(chat_id=message.from_user.id , text=birad, reply_markup=haftaNomi1a , parse_mode="HTML")
            case "Seshanba 📕":
                await bot.send_message(chat_id=message.from_user.id , text=biras, reply_markup=haftaNomi1a , parse_mode="HTML")
            case "Chorshanba 📕":
                await bot.send_message(chat_id=message.from_user.id , text=birac, reply_markup=haftaNomi1a , parse_mode="HTML")
            case "Payshanba 📕":
                await bot.send_message(chat_id=message.from_user.id , text=birap, reply_markup=haftaNomi1a , parse_mode="HTML")
            case "Juma 📕":
                await bot.send_message(chat_id=message.from_user.id , text=biraj, reply_markup=haftaNomi1a , parse_mode="HTML")
            case "Shanba 📕":
                await bot.send_message(chat_id=message.from_user.id , text=birash, reply_markup=haftaNomi1a , parse_mode="HTML")
            case "Dushanba 📖":
                await bot.send_message(chat_id=message.from_user.id , text=birbd, reply_markup=haftaNomi1b , parse_mode="HTML")
            case "Seshanba 📖":
                await bot.send_message(chat_id=message.from_user.id , text=birbs, reply_markup=haftaNomi1b , parse_mode="HTML")
            case "Chorshanba 📖":
                await bot.send_message(chat_id=message.from_user.id , text=birbc, reply_markup=haftaNomi1b , parse_mode="HTML")
            case "Payshanba 📖":
                await bot.send_message(chat_id=message.from_user.id , text=birbp, reply_markup=haftaNomi1b , parse_mode="HTML")
            case "Juma 📖":
                await bot.send_message(chat_id=message.from_user.id , text=birbj, reply_markup=haftaNomi1b , parse_mode="HTML")
            case "Shanba 📖":
                await bot.send_message(chat_id=message.from_user.id , text=birbsh, reply_markup=haftaNomi1b , parse_mode="HTML")
            case "Dushanba 📓":
                await bot.send_message(chat_id=message.from_user.id , text=birvd, reply_markup=haftaNomi1v , parse_mode="HTML")
            case "Seshanba 📓":
                await bot.send_message(chat_id=message.from_user.id , text=birvs, reply_markup=haftaNomi1v , parse_mode="HTML")
            case "Chorshanba 📓":
                await bot.send_message(chat_id=message.from_user.id , text=birvc, reply_markup=haftaNomi1v , parse_mode="HTML")
            case "Payshanba 📓":
                await bot.send_message(chat_id=message.from_user.id , text=birvp, reply_markup=haftaNomi1v , parse_mode="HTML")
            case "Juma 📓":
                await bot.send_message(chat_id=message.from_user.id , text=birvj, reply_markup=haftaNomi1v , parse_mode="HTML")
            case "Shanba 📓":
                await bot.send_message(chat_id=message.from_user.id , text=birvsh, reply_markup=haftaNomi1v , parse_mode="HTML")
            case "Dushanba 📔":
                await bot.send_message(chat_id=message.from_user.id , text=birgd, reply_markup=haftaNomi1g , parse_mode="HTML")
            case "Seshanba 📔":
                await bot.send_message(chat_id=message.from_user.id , text=birgs, reply_markup=haftaNomi1g , parse_mode="HTML")
            case "Chorshanba 📔":
                await bot.send_message(chat_id=message.from_user.id , text=birgc, reply_markup=haftaNomi1g , parse_mode="HTML")
            case "Payshanba 📔":
                await bot.send_message(chat_id=message.from_user.id , text=birgp, reply_markup=haftaNomi1g , parse_mode="HTML")
            case "Juma 📔":
                await bot.send_message(chat_id=message.from_user.id , text=birgj, reply_markup=haftaNomi1g , parse_mode="HTML")
            case "Shanba 📔":
                await bot.send_message(chat_id=message.from_user.id , text=birgsh, reply_markup=haftaNomi1g , parse_mode="HTML")
            case "Dushanba 📘":
                await bot.send_message(chat_id=message.from_user.id , text=ikiad, reply_markup=haftaNomi2a , parse_mode="HTML")
            case "Seshanba 📘":
                await bot.send_message(chat_id=message.from_user.id , text=ikias, reply_markup=haftaNomi2a , parse_mode="HTML")
            case "Chorshanba 📘":
                await bot.send_message(chat_id=message.from_user.id , text=ikiac, reply_markup=haftaNomi2a , parse_mode="HTML")
            case "Payshanba 📘":
                await bot.send_message(chat_id=message.from_user.id , text=ikiap, reply_markup=haftaNomi2a , parse_mode="HTML")
            case "Juma 📘":
                await bot.send_message(chat_id=message.from_user.id , text=ikiaj, reply_markup=haftaNomi2a , parse_mode="HTML")
            case "Shanba 📘":
                await bot.send_message(chat_id=message.from_user.id , text=ikiash, reply_markup=haftaNomi2a , parse_mode="HTML")
            case  "Dushanba 📚":
                await bot.send_message(chat_id=message.from_user.id , text=ikibd, reply_markup=haftaNomi2b , parse_mode="HTML")
            case  "Seshanba 📚":
                await bot.send_message(chat_id=message.from_user.id , text=ikibs, reply_markup=haftaNomi2b , parse_mode="HTML")
            case"Chorshanba 📚":
                await bot.send_message(chat_id=message.from_user.id , text=ikibc, reply_markup=haftaNomi2b , parse_mode="HTML")
            case "Payshanba 📚":
                await bot.send_message(chat_id=message.from_user.id , text=ikibp, reply_markup=haftaNomi2b , parse_mode="HTML")
            case      "Juma 📚":
                await bot.send_message(chat_id=message.from_user.id , text=ikibj, reply_markup=haftaNomi2b , parse_mode="HTML")
            case    "Shanba 📚":
                await bot.send_message(chat_id=message.from_user.id , text=ikibsh, reply_markup=haftaNomi2b , parse_mode="HTML")
            case "Dushanba 📙":
                await bot.send_message(chat_id=message.from_user.id , text=ikivd, reply_markup=haftaNomi2v , parse_mode="HTML")
            case "Seshanba 📙":
                await bot.send_message(chat_id=message.from_user.id , text=ikivs, reply_markup=haftaNomi2v , parse_mode="HTML")
            case "Chorshanba 📙":
                await bot.send_message(chat_id=message.from_user.id , text=ikivc, reply_markup=haftaNomi2v , parse_mode="HTML")
            case "Payshanba 📙":
                await bot.send_message(chat_id=message.from_user.id , text=ikivp, reply_markup=haftaNomi2v , parse_mode="HTML")
            case "Juma 📙":
                await bot.send_message(chat_id=message.from_user.id , text=ikivj, reply_markup=haftaNomi2v , parse_mode="HTML")
            case "Shanba 📙":
                await bot.send_message(chat_id=message.from_user.id , text=ikivsh, reply_markup=haftaNomi2v , parse_mode="HTML")
            case "Dushanba 📗":
                await bot.send_message(chat_id=message.from_user.id , text=uchlarad, reply_markup=haftaNomi3a , parse_mode="HTML")
            case "Seshanba 📗":
                await bot.send_message(chat_id=message.from_user.id , text=uchlaras, reply_markup=haftaNomi3a , parse_mode="HTML")
            case "Chorshanba 📗":
                await bot.send_message(chat_id=message.from_user.id , text=uchlarac, reply_markup=haftaNomi3a , parse_mode="HTML")
            case "Payshanba 📗":
                await bot.send_message(chat_id=message.from_user.id , text=uchlarap, reply_markup=haftaNomi3a , parse_mode="HTML")
            case "Juma 📗":
                await bot.send_message(chat_id=message.from_user.id , text=uchlaraj, reply_markup=haftaNomi3a , parse_mode="HTML")
            case "Shanba 📗":
                await bot.send_message(chat_id=message.from_user.id , text=uchlarash,reply_markup=haftaNomi3a , parse_mode="HTML")
            case "Dushanba 📒":
                await bot.send_message(chat_id=message.from_user.id , text=uchlarbd, reply_markup=haftaNomi3b , parse_mode="HTML")
            case "Seshanba 📒":
                await bot.send_message(chat_id=message.from_user.id , text=uchlarbs, reply_markup=haftaNomi3b , parse_mode="HTML")
            case "Chorshanba 📒":
                await bot.send_message(chat_id=message.from_user.id , text=uchlarbc, reply_markup=haftaNomi3b , parse_mode="HTML")
            case "Payshanba 📒":
                await bot.send_message(chat_id=message.from_user.id , text=uchlarbp, reply_markup=haftaNomi3b , parse_mode="HTML")
            case "Juma 📒":
                await bot.send_message(chat_id=message.from_user.id , text=uchlarbj, reply_markup=haftaNomi3b , parse_mode="HTML")
            case "Shanba 📒":
                await bot.send_message(chat_id=message.from_user.id , text=uchlarbsh, reply_markup=haftaNomi3b , parse_mode="HTML")
            case "Dushanba 📒":
                await bot.send_message(chat_id=message.from_user.id , text=uchlarvd, reply_markup=haftaNomi3v , parse_mode="HTML")
            case "Seshanba 📒":
                await bot.send_message(chat_id=message.from_user.id , text=uchlarvs, reply_markup=haftaNomi3v , parse_mode="HTML")
            case "Chorshanba 📔":
                await bot.send_message(chat_id=message.from_user.id , text=uchlarvc, reply_markup=haftaNomi3v , parse_mode="HTML")
            case "Payshanba 📔":
                await bot.send_message(chat_id=message.from_user.id , text=uchlarvp, reply_markup=haftaNomi3v , parse_mode="HTML")
            case "Juma 📔":
                await bot.send_message(chat_id=message.from_user.id , text=uchlarvj, reply_markup=haftaNomi3v , parse_mode="HTML")
            case "Shanba 📔":
                await bot.send_message(chat_id=message.from_user.id , text=uchlarvsh, reply_markup=haftaNomi3v , parse_mode="HTML")

            case "Dushanba 📔":
                await bot.send_message(chat_id=message.from_user.id , text=birgd, reply_markup=haftaNomi1g , parse_mode="HTML")
            case "Seshanba 📔":
                await bot.send_message(chat_id=message.from_user.id , text=birgs, reply_markup=haftaNomi1g , parse_mode="HTML")
            case "Chorshanba 📔":
                await bot.send_message(chat_id=message.from_user.id , text=birgc, reply_markup=haftaNomi1g , parse_mode="HTML")
            case "Payshanba 📔":
                await bot.send_message(chat_id=message.from_user.id , text=birgp, reply_markup=haftaNomi1g , parse_mode="HTML")
            case "Juma 📔":
                await bot.send_message(chat_id=message.from_user.id , text=birgj, reply_markup=haftaNomi1g , parse_mode="HTML")
            case "Shanba 📔":
                await bot.send_message(chat_id=message.from_user.id , text=birgsh, reply_markup=haftaNomi1g , parse_mode="HTML")

            case _:
                await bot.send_message(chat_id=message.from_user.id , text="<i>Xato qiymat kiritdingiz...</i>", reply_markup=mainMenu , parse_mode="HTML")

    except Exception as e:
        print(e)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)