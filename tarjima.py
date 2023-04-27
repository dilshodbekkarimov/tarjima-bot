from googletrans import Translator

import logging
from bot_token import admin
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = 'admin'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
tr = Translator()

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):


    await message.reply("Assalomu Alaykum\nSo'zni kiriting: ")



@dp.message_handler()
async def echo(message: types.Message):
	global msg 
	msg = message.text
	markup = types.InlineKeyboardMarkup()

	knopka_1 = types.InlineKeyboardMarkup(text="🇺🇿 O'zbekcha",callback_data="uz")
	knopka_2 = types.InlineKeyboardMarkup(text="🇺🇿 english",callback_data="en")
	knopka_3 = types.InlineKeyboardMarkup(text="🇺🇿 afrikaans",callback_data="af")
	knopka_4 = types.InlineKeyboardMarkup(text="🇺🇿 shqip",callback_data="sq")
	knopka_5 = types.InlineKeyboardMarkup(text="🇺🇿 አማርኛ",callback_data="am")
	knopka_6 = types.InlineKeyboardMarkup(text="🇺🇿 عربي",callback_data="ar")
	knopka_7 = types.InlineKeyboardMarkup(text="🇺🇿 հայերեն",callback_data="hy")
	knopka_8 = types.InlineKeyboardMarkup(text="🇺🇿 azərbaycanlı",callback_data="az")
	knopka_9 = types.InlineKeyboardMarkup(text="🇺🇿 basque",callback_data="eu")
	knopka_10 = types.InlineKeyboardMarkup(text="🇺🇿 беларускі",callback_data="be")
	knopka_11 = types.InlineKeyboardMarkup(text="🇺🇿 বাংলা",callback_data="bn")
	knopka_12 = types.InlineKeyboardMarkup(text="🇺🇿 bosanski",callback_data="bs")
	knopka_13 = types.InlineKeyboardMarkup(text="🇺🇿 български",callback_data="bg")
	knopka_14 = types.InlineKeyboardMarkup(text="🇺🇿 català",callback_data="ca")
	knopka_15 = types.InlineKeyboardMarkup(text="🇺🇿 cebuano",callback_data="ceb")
	knopka_16 = types.InlineKeyboardMarkup(text="🇺🇿 chichewa",callback_data="ny")
	knopka_17 = types.InlineKeyboardMarkup(text="🇺🇿 简体中文）",callback_data="zh-cn")
	knopka_18 = types.InlineKeyboardMarkup(text="🇺🇿 中國傳統的）",callback_data="zh-tw")
	knopka_19 = types.InlineKeyboardMarkup(text="🇺🇿 corsican",callback_data="co")
	knopka_20 = types.InlineKeyboardMarkup(text="🇺🇿 Hrvatski",callback_data="hr")
	knopka_21 = types.InlineKeyboardMarkup(text="🇺🇿 czech",callback_data="cs")
	knopka_22 = types.InlineKeyboardMarkup(text="🇺🇿 danish",callback_data="da")
	knopka_23 = types.InlineKeyboardMarkup(text="🇺🇿 Nederlands",callback_data="nl")
	knopka_24 = types.InlineKeyboardMarkup(text="🇺🇿 ગુજરાતી",callback_data="gu")
	knopka_25 = types.InlineKeyboardMarkup(text="🇺🇿 esperanto",callback_data="eo")
	knopka_26 = types.InlineKeyboardMarkup(text="🇺🇿 estonian",callback_data="et")
	knopka_27 = types.InlineKeyboardMarkup(text="🇺🇿 filipino",callback_data="tl")
	knopka_28 = types.InlineKeyboardMarkup(text="🇺🇿 finnish",callback_data="fi")	
	knopka_29 = types.InlineKeyboardMarkup(text="🇺🇿 Français",callback_data="fr")
	knopka_30 = types.InlineKeyboardMarkup(text="🇺🇿 frisian",callback_data="fy")
	knopka_31 = types.InlineKeyboardMarkup(text="🇺🇿 galego",callback_data="gl")
	knopka_32 = types.InlineKeyboardMarkup(text="🇺🇿 ქართველი",callback_data="ka")
	knopka_33 = types.InlineKeyboardMarkup(text="🇺🇿 Deutsch",callback_data="de")
	knopka_34 = types.InlineKeyboardMarkup(text="🇺🇿 Ελληνικά",callback_data="el")
	knopka_35 = types.InlineKeyboardMarkup(text="🇺🇿 hausa",callback_data="ha")
	knopka_36 = types.InlineKeyboardMarkup(text="🇺🇿 ʻŌlelo Hawaiʻi",callback_data="haw")
	knopka_37 = types.InlineKeyboardMarkup(text="🇺🇿 עִברִית",callback_data="iw")
	knopka_38 = types.InlineKeyboardMarkup(text="🇺🇿 עִברִית",callback_data="he")
	knopka_39 = types.InlineKeyboardMarkup(text="🇺🇿 नहीं",callback_data="hi")
	knopka_40 = types.InlineKeyboardMarkup(text="🇺🇿 hmoob",callback_data="hmn")
	knopka_41 = types.InlineKeyboardMarkup(text="🇺🇿 hungarian",callback_data="hu")
	knopka_42 = types.InlineKeyboardMarkup(text="🇺🇿 icelandic",callback_data="is")
	knopka_43 = types.InlineKeyboardMarkup(text="🇺🇿 igbo",callback_data="ig")
	knopka_44 = types.InlineKeyboardMarkup(text="🇺🇿 bahasa Indonesia",callback_data="id")
	knopka_45 = types.InlineKeyboardMarkup(text="🇺🇿 Gaeilge",callback_data="ga")
	knopka_46 = types.InlineKeyboardMarkup(text="🇺🇿 italiano",callback_data="it")
	knopka_47 = types.InlineKeyboardMarkup(text="🇺🇿 日本",callback_data="ja")
	knopka_48 = types.InlineKeyboardMarkup(text="🇺🇿 javanese",callback_data="jw")
	knopka_49 = types.InlineKeyboardMarkup(text="🇺🇿 ಕನ್ನಡ",callback_data="kn")
	knopka_50 = types.InlineKeyboardMarkup(text="🇺🇿 қазақ",callback_data="kk")
	knopka_51 = types.InlineKeyboardMarkup(text="🇺🇿 ខ្មែរ",callback_data="km")
	knopka_52 = types.InlineKeyboardMarkup(text="🇺🇿 한국인",callback_data="ko")
	knopka_53 = types.InlineKeyboardMarkup(text="🇺🇿 kurdish (kurmanji)",callback_data="ku")
	knopka_54 = types.InlineKeyboardMarkup(text="🇺🇿 Кыргызча",callback_data="ky")
	knopka_55 = types.InlineKeyboardMarkup(text="🇺🇿 ແຮງ​ງານ",callback_data="lo")
	knopka_56 = types.InlineKeyboardMarkup(text="🇺🇿 latin",callback_data="la")	
	knopka_57 = types.InlineKeyboardMarkup(text="🇺🇿 latvian",callback_data="lv")
	knopka_58 = types.InlineKeyboardMarkup(text="🇺🇿 lietuvis",callback_data="lt")
	knopka_59 = types.InlineKeyboardMarkup(text="🇺🇿 luxembourgish",callback_data="lb")
	knopka_60 = types.InlineKeyboardMarkup(text="🇺🇿 македонски",callback_data="mk")
	knopka_61 = types.InlineKeyboardMarkup(text="🇺🇿 malagasy",callback_data="mg")
	knopka_62 = types.InlineKeyboardMarkup(text="🇺🇿 malay",callback_data="ms")
	knopka_63 = types.InlineKeyboardMarkup(text="🇺🇿 malayalam",callback_data="ml")
	knopka_64 = types.InlineKeyboardMarkup(text="🇺🇿 malti",callback_data="mt")
	knopka_65 = types.InlineKeyboardMarkup(text="🇺🇿 maori",callback_data="mi")
	knopka_66 = types.InlineKeyboardMarkup(text="🇺🇿 मराठी",callback_data="mr")
	knopka_67 = types.InlineKeyboardMarkup(text="🇺🇿 монгол",callback_data="mn")
	knopka_68 = types.InlineKeyboardMarkup(text="🇺🇿 မြန်မာ (ဗမာ)",callback_data="my")
	knopka_69 = types.InlineKeyboardMarkup(text="🇺🇿 नेपाली",callback_data="ne")
	knopka_70 = types.InlineKeyboardMarkup(text="🇺🇿 norwegian",callback_data="no")
	knopka_71 = types.InlineKeyboardMarkup(text="🇺🇿 ଓଡିଆ",callback_data="or")
	knopka_72 = types.InlineKeyboardMarkup(text="🇺🇿 پښتو",callback_data="ps")
	knopka_73 = types.InlineKeyboardMarkup(text="🇺🇿 فارسی",callback_data="fa")
	knopka_74 = types.InlineKeyboardMarkup(text="🇺🇿 polski",callback_data="pl")
	knopka_75 = types.InlineKeyboardMarkup(text="🇺🇿 português",callback_data="pt")
	knopka_76 = types.InlineKeyboardMarkup(text="🇺🇿 ਪੰਜਾਬੀ",callback_data="pa")
	knopka_77 = types.InlineKeyboardMarkup(text="🇺🇿 Română",callback_data="ro")
	knopka_78 = types.InlineKeyboardMarkup(text="🇺🇿 русский",callback_data="ru")
	knopka_79 = types.InlineKeyboardMarkup(text="🇺🇿 samoa",callback_data="sm")
	knopka_80 = types.InlineKeyboardMarkup(text="🇺🇿 Gàidhlig na h-Alba",callback_data="gd")
	knopka_81 = types.InlineKeyboardMarkup(text="🇺🇿 Српски",callback_data="sr")
	knopka_82 = types.InlineKeyboardMarkup(text="🇺🇿 sesotho",callback_data="st")
	knopka_83 = types.InlineKeyboardMarkup(text="🇺🇿 shona",callback_data="sn")
	knopka_84 = types.InlineKeyboardMarkup(text="🇺🇿 سنڌي",callback_data="sd")	
	knopka_85 = types.InlineKeyboardMarkup(text="🇺🇿 සිංහල",callback_data="si")
	knopka_86 = types.InlineKeyboardMarkup(text="🇺🇿 slovak",callback_data="sk")
	knopka_87 = types.InlineKeyboardMarkup(text="🇺🇿 Slovenščina",callback_data="sl")
	knopka_88 = types.InlineKeyboardMarkup(text="🇺🇿 somali",callback_data="so")
	knopka_89 = types.InlineKeyboardMarkup(text="🇺🇿 español",callback_data="es")
	knopka_90 = types.InlineKeyboardMarkup(text="🇺🇿 sundanese",callback_data="su")
	knopka_91 = types.InlineKeyboardMarkup(text="🇺🇿 swahili",callback_data="sw")
	knopka_92 = types.InlineKeyboardMarkup(text="🇺🇿 svenska",callback_data="sv")
	knopka_93 = types.InlineKeyboardMarkup(text="🇺🇿 тоҷикӣ",callback_data="tg")
	knopka_94 = types.InlineKeyboardMarkup(text="🇺🇿 தமிழ்",callback_data="ta")
	knopka_95 = types.InlineKeyboardMarkup(text="🇺🇿 తెలుగు",callback_data="te")
	knopka_96 = types.InlineKeyboardMarkup(text="🇺🇿 แบบไทย",callback_data="th")
	knopka_97 = types.InlineKeyboardMarkup(text="🇺🇿 Türkçe",callback_data="tr")
	knopka_98 = types.InlineKeyboardMarkup(text="🇺🇿 українська",callback_data="uk")
	knopka_99 = types.InlineKeyboardMarkup(text="🇺🇿 اردو",callback_data="ur")
	knopka_100 = types.InlineKeyboardMarkup(text="🇺🇿 uyghur",callback_data="ug")
	knopka_101 = types.InlineKeyboardMarkup(text="🇺🇿 haitian creole",callback_data="ht")
	knopka_102 = types.InlineKeyboardMarkup(text="🇺🇿 vietnamese",callback_data="vi")
	knopka_103 = types.InlineKeyboardMarkup(text="🇺🇿 welsh",callback_data="cy")
	knopka_104 = types.InlineKeyboardMarkup(text="🇺🇿 xhosa",callback_data="xh")
	knopka_105 = types.InlineKeyboardMarkup(text="🇺🇿 yiddish",callback_data="yi")
	knopka_106 = types.InlineKeyboardMarkup(text="🇺🇿 yoruba",callback_data="yo")
	knopka_107 = types.InlineKeyboardMarkup(text="🇺🇿 zulu",callback_data="zu")
	
	markup.add(knopka_1,knopka_2,knopka_3,knopka_4,knopka_5,knopka_6,knopka_7,knopka_8,knopka_9,knopka_10,knopka_11,knopka_12,knopka_13,knopka_14,knopka_15,knopka_16,knopka_17,knopka_18,knopka_19,knopka_20,knopka_21,knopka_22,knopka_23,knopka_24,knopka_25,knopka_26,knopka_27,knopka_28,knopka_29,knopka_30,knopka_31,knopka_32,knopka_33,knopka_34,knopka_35,knopka_36,knopka_37,knopka_38,knopka_39,knopka_40,knopka_41,knopka_42,knopka_43,knopka_44,knopka_45,knopka_46,knopka_47,knopka_48,knopka_49,knopka_50,knopka_51,knopka_52,knopka_53,knopka_54,knopka_55,knopka_56,knopka_57,knopka_58,knopka_59,knopka_60,knopka_61,knopka_62,knopka_63,knopka_64,knopka_65,knopka_66,knopka_67,knopka_68,knopka_69,knopka_70,knopka_71,knopka_72,knopka_73,knopka_74,knopka_75,knopka_76,knopka_77,knopka_78,knopka_79,knopka_80,knopka_81,knopka_82,knopka_83,knopka_84,knopka_85,knopka_86,knopka_87,knopka_88,knopka_89,knopka_90,knopka_91,knopka_92,knopka_93,knopka_94,knopka_95,knopka_96,knopka_97,knopka_98,knopka_99,knopka_100,knopka_101,knopka_102,knopka_103,knopka_104,knopka_105,knopka_106,knopka_107)
	await message.answer("tilni tanlang: ",reply_markup=markup)


@dp.callback_query_handler(text='uz')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='en')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)



@dp.callback_query_handler(text='af')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='sq')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)



@dp.callback_query_handler(text='am')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='ar')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)



@dp.callback_query_handler(text='hy')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='az')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)



@dp.callback_query_handler(text='eu')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='be')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)



@dp.callback_query_handler(text='bn')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='bs')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)



@dp.callback_query_handler(text='bg')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='ca')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)



@dp.callback_query_handler(text='ceb')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='ny')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)



@dp.callback_query_handler(text='zh-cn')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='zh-tw')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)



@dp.callback_query_handler(text='co')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='hr')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)



@dp.callback_query_handler(text='cs')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='da')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='nl')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='gu')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='eo')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)



@dp.callback_query_handler(text='et')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='tl')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='fi')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='fr')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)



@dp.callback_query_handler(text='fy')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='gl')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='ka')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='de')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)



@dp.callback_query_handler(text='el')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='ha')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='haw')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='iw')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)



@dp.callback_query_handler(text='he')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='hi')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='hmn')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='hu')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)



@dp.callback_query_handler(text='is')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='ig')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='id')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='ga')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)



@dp.callback_query_handler(text='it')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='ja')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='jw')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='kn')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)



@dp.callback_query_handler(text='kk')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='km')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='ko')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='ku')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)



@dp.callback_query_handler(text='ky')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='lo')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='la')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='lv')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)



@dp.callback_query_handler(text='lt')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='lb')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='mk')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='mg')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)



@dp.callback_query_handler(text='ms')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='ml')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='mt')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='mi')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)



@dp.callback_query_handler(text='mr')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='mn')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='my')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='ne')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)



@dp.callback_query_handler(text='no')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='or')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='ps')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='fa')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)



@dp.callback_query_handler(text='pl')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='pt')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='pa')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='ro')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)



@dp.callback_query_handler(text='ru')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='sm')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='gd')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='sr')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)



@dp.callback_query_handler(text='st')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='sn')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='sd')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='si')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)



@dp.callback_query_handler(text='sk')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='sl')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='so')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='es')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)



@dp.callback_query_handler(text='su')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='sw')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='sv')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='tg')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)



@dp.callback_query_handler(text='ta')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='te')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='th')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='tr')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)



@dp.callback_query_handler(text='uk')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='ur')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='ug')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='ht')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)



@dp.callback_query_handler(text='vi')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='cy')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='xh')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='yi')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)

@dp.callback_query_handler(text='yo')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)


@dp.callback_query_handler(text='zu')
async def foo(call: types.CallbackQuery):
	tarjima = tr.translate(msg,dest=call.data)
	await call.message.answer(tarjima.text)

# if __name__ == '__main__':
    # executor.start_polling(dp, skip_updates=True)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)