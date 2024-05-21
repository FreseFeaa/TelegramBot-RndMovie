import telebot 
from telebot import types 
import random
from film import movies

bot = telebot.TeleBot('Apitoken был убран из соображений безопасности (Чтоб не украл никто)') 
 
@bot.message_handler(commands=['start']) 
 
def main(message): 
    markup = types.InlineKeyboardMarkup() 
    btn1 = types.InlineKeyboardButton('Перейти в меню',callback_data='menu') 
    markup.row(btn1) 
    bot.send_message(message.chat.id, 
f''' 
<b>Добро пожаловать, {message.from_user.first_name}!</b> 
              
Для начала можешь ознакомиться с базовыми командами: 
/start     - <em>Запускает бота</em> 
/menu    - <em>Выводит удобное меню</em> 
/help      - <em>Выводит доступные команды‹</em> 
/movie   - <em>Выдает полностью случайный фильм</em> 
/choice  - <em>Выводит небольшой фильтр по фильмам</em> 
                     ''',parse_mode='html', reply_markup=markup) 
     
 
@bot.message_handler(commands=['help']) 
def helps(message): 
    bot.send_message(message.chat.id, 
''' 
Вот список доступных команд: 
/start     - <em>Запускает бота</em> 
/menu    - <em>Выводит удобное меню</em> 
/help      - <em>Выводит доступные команды</em> 
/movie   - <em>Выдает полностью случайный фильм</em> 
/choice  - <em>Выводит небольшой фильтр по фильмам</em> 
''',parse_mode='html') 
 
 

@bot.message_handler(commands=['movie']) 
def movie(message): 
    markup = types.InlineKeyboardMarkup() 
    btn1 = types.InlineKeyboardButton('Следущий фильм',callback_data='randomfilm') 
    markup.row(btn1) 
    random_movie = random.choice(movies)
    bot.send_photo(message.chat.id, random_movie['Image'])
    bot.send_message(message.chat.id, 
    
f'''
<b>{random_movie['Name']}</b>

{random_movie['Description']}

<b>О фильме:</b>
Жанр: {random_movie['Genre']}
Год производства: {random_movie['Year']}
Режиссер: {random_movie['Director']}
'''

,parse_mode='html', reply_markup=markup) 
 
 
     
 
@bot.message_handler(commands=['choice']) 
def choice(message): 
    markup = types.InlineKeyboardMarkup() 
    btn1 = types.InlineKeyboardButton('Фантастика',callback_data='filtr_fentasy') 
    btn2 = types.InlineKeyboardButton('Драма',callback_data='filtr_drama') 
    btn3 = types.InlineKeyboardButton('Хоррор',callback_data='filtr_horror') 
    markup.row(btn1,btn2,btn3) 
    btn4 = types.InlineKeyboardButton('Комедия',callback_data='filtr_comedia') 
    btn5 = types.InlineKeyboardButton('Боевик',callback_data='filtr_boevik') 
    btn6 = types.InlineKeyboardButton('Триллер',callback_data='filtr_triller') 
    markup.row(btn4,btn5,btn6)
    btn7 = types.InlineKeyboardButton('Детектив',callback_data='filtr_detective') 
    btn8 = types.InlineKeyboardButton('Мультфильм',callback_data='filtr_multik') 
    btn9 = types.InlineKeyboardButton('Приключения',callback_data='filtr_adventures') 
    markup.row(btn7,btn8,btn9)
 
 
    bot.send_message(message.chat.id,'Выберите жанр для случайного фильма: ', reply_markup=markup) 
 
@bot.message_handler(commands=['menu']) 
def menu(message): 
        markup = types.InlineKeyboardMarkup() 
        btn1 = types.InlineKeyboardButton('Cлучайный фильм',callback_data='randomfilm') 
        btn2 = types.InlineKeyboardButton('Выбрать жанр для случайного фильма',callback_data='choicebutton') 

        markup.row(btn1) 
        markup.row(btn2) 
        bot.send_message(message.chat.id,
'''
<b>Меню команд: </b>
Здесь вы можете выбрать удобный способ для поиска фильма                           
''',parse_mode='html', reply_markup=markup) 
 

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'randomfilm':
        markup = types.InlineKeyboardMarkup() 
        btn1 = types.InlineKeyboardButton('Следущий фильм',callback_data='randomfilm')

        btn2 = types.InlineKeyboardButton('Выбрать жанр',callback_data='choicebutton')
        btn3 = types.InlineKeyboardButton('Меню',callback_data='menu')
        markup.row(btn1)
        markup.row(btn2,btn3) 

        random_movie = random.choice(movies)
        bot.send_photo(callback.message.chat.id, random_movie['Image'])
        bot.send_message(callback.message.chat.id, 
    
f'''
<b>{random_movie['Name']}</b>

{random_movie['Description']}

<b>О фильме:</b>
Жанр: {random_movie['Genre']}
Год производства: {random_movie['Year']}
Режиссер: {random_movie['Director']}
'''

,parse_mode='html', reply_markup=markup) 
    elif callback.data == 'filtr_horror':
        markup = types.InlineKeyboardMarkup() 
        btn1 = types.InlineKeyboardButton('Следущий фильм жанра: Хоррор',callback_data='filtr_horror') 
        btn2 = types.InlineKeyboardButton('Выбрать другой жанр',callback_data='choicebutton')
        btn3 = types.InlineKeyboardButton('Меню',callback_data='menu')
        markup.row(btn1)
        markup.row(btn2,btn3) 
        horror_movies = [movie for movie in movies if movie["Genre"] == "хоррор"]
        random_horror_movie = random.choice(horror_movies)
        bot.send_photo(callback.message.chat.id, random_horror_movie['Image'])
        bot.send_message(callback.message.chat.id, 
    
f'''
<b>{random_horror_movie['Name']}</b>

{random_horror_movie['Description']}

<b>О фильме:</b>
Жанр: {random_horror_movie['Genre']}
Год производства: {random_horror_movie['Year']}
Режиссер: {random_horror_movie['Director']}
'''
,parse_mode='html', reply_markup=markup)
    elif callback.data == 'filtr_fentasy':
        markup = types.InlineKeyboardMarkup() 
        btn1 = types.InlineKeyboardButton('Следущий фильм жанра: Фантастика',callback_data='filtr_fentasy') 
        btn2 = types.InlineKeyboardButton('Выбрать другой жанр',callback_data='choicebutton')
        btn3 = types.InlineKeyboardButton('Меню',callback_data='menu')
        markup.row(btn1)
        markup.row(btn2,btn3) 
        fentasy_movies = [movie for movie in movies if movie["Genre"] == "фантастика"]
        random_fentasy_movie = random.choice(fentasy_movies)
        bot.send_photo(callback.message.chat.id, random_fentasy_movie['Image'])
        bot.send_message(callback.message.chat.id, 
    
f'''
<b>{random_fentasy_movie['Name']}</b>

{random_fentasy_movie['Description']}

<b>О фильме:</b>
Жанр: {random_fentasy_movie['Genre']}
Год производства: {random_fentasy_movie['Year']}
Режиссер: {random_fentasy_movie['Director']}
'''
,parse_mode='html', reply_markup=markup)
    elif callback.data == 'filtr_drama':
        markup = types.InlineKeyboardMarkup() 
        btn1 = types.InlineKeyboardButton('Следущий фильм жанра: Драма',callback_data='filtr_drama') 
        btn2 = types.InlineKeyboardButton('Выбрать другой жанр',callback_data='choicebutton')
        btn3 = types.InlineKeyboardButton('Меню',callback_data='menu')
        markup.row(btn1)
        markup.row(btn2,btn3)  
        drama_movies = [movie for movie in movies if movie["Genre"] == "драма"]
        random_drama_movie = random.choice(drama_movies)
        bot.send_photo(callback.message.chat.id, random_drama_movie['Image'])
        bot.send_message(callback.message.chat.id, 
    
f'''
<b>{random_drama_movie['Name']}</b>

{random_drama_movie['Description']}

<b>О фильме:</b>
Жанр: {random_drama_movie['Genre']}
Год производства: {random_drama_movie['Year']}
Режиссер: {random_drama_movie['Director']}
'''
,parse_mode='html', reply_markup=markup)
    elif callback.data == 'filtr_comedia':
        markup = types.InlineKeyboardMarkup() 
        btn1 = types.InlineKeyboardButton('Следущий фильм жанра: Комедия',callback_data='filtr_comedia') 
        btn2 = types.InlineKeyboardButton('Выбрать другой жанр',callback_data='choicebutton')
        btn3 = types.InlineKeyboardButton('Меню',callback_data='menu')
        markup.row(btn1)
        markup.row(btn2,btn3)  
        comedia_movies = [movie for movie in movies if movie["Genre"] == "комедия"]
        random_comedia_movie = random.choice(comedia_movies)
        bot.send_photo(callback.message.chat.id, random_comedia_movie['Image'])
        bot.send_message(callback.message.chat.id, 
    
f'''
<b>{random_comedia_movie['Name']}</b>

{random_comedia_movie['Description']}

<b>О фильме:</b>
Жанр: {random_comedia_movie['Genre']}
Год производства: {random_comedia_movie['Year']}
Режиссер: {random_comedia_movie['Director']}
'''
,parse_mode='html', reply_markup=markup)
    elif callback.data == 'filtr_boevik':
        markup = types.InlineKeyboardMarkup() 
        btn1 = types.InlineKeyboardButton('Следущий фильм жанра: Боевик',callback_data='filtr_boevik') 
        btn2 = types.InlineKeyboardButton('Выбрать другой жанр',callback_data='choicebutton')
        btn3 = types.InlineKeyboardButton('Меню',callback_data='menu')
        markup.row(btn1)
        markup.row(btn2,btn3)  
        boevik_movies = [movie for movie in movies if movie["Genre"] == "боевик"]
        random_boevik_movie = random.choice(boevik_movies)
        bot.send_photo(callback.message.chat.id, random_boevik_movie['Image'])
        bot.send_message(callback.message.chat.id, 
    
f'''
<b>{random_boevik_movie['Name']}</b>

{random_boevik_movie['Description']}

<b>О фильме:</b>
Жанр: {random_boevik_movie['Genre']}
Год производства: {random_boevik_movie['Year']}
Режиссер: {random_boevik_movie['Director']}
'''
,parse_mode='html', reply_markup=markup)
    elif callback.data == 'filtr_triller':
        markup = types.InlineKeyboardMarkup() 
        btn1 = types.InlineKeyboardButton('Следущий фильм жанра: Триллер',callback_data='filtr_triller') 
        btn2 = types.InlineKeyboardButton('Выбрать другой жанр',callback_data='choicebutton')
        btn3 = types.InlineKeyboardButton('Меню',callback_data='menu')
        markup.row(btn1)
        markup.row(btn2,btn3)  
        triller_movies = [movie for movie in movies if movie["Genre"] == "триллер"]
        random_triller_movie = random.choice(triller_movies)
        bot.send_photo(callback.message.chat.id, random_triller_movie['Image'])
        bot.send_message(callback.message.chat.id, 
    
f'''
<b>{random_triller_movie['Name']}</b>

{random_triller_movie['Description']}

<b>О фильме:</b>
Жанр: {random_triller_movie['Genre']}
Год производства: {random_triller_movie['Year']}
Режиссер: {random_triller_movie['Director']}
'''
,parse_mode='html', reply_markup=markup)
    elif callback.data == 'filtr_detective':
        markup = types.InlineKeyboardMarkup() 
        btn1 = types.InlineKeyboardButton('Следущий фильм жанра: Детектив',callback_data='filtr_detective') 
        btn2 = types.InlineKeyboardButton('Выбрать другой жанр',callback_data='choicebutton')
        btn3 = types.InlineKeyboardButton('Меню',callback_data='menu')
        markup.row(btn1)
        markup.row(btn2,btn3)  
        detective_movies = [movie for movie in movies if movie["Genre"] == "детектив"]
        random_detective_movie = random.choice(detective_movies)
        bot.send_photo(callback.message.chat.id, random_detective_movie['Image'])
        bot.send_message(callback.message.chat.id, 
    
f'''
<b>{random_detective_movie['Name']}</b>

{random_detective_movie['Description']}

<b>О фильме:</b>
Жанр: {random_detective_movie['Genre']}
Год производства: {random_detective_movie['Year']}
Режиссер: {random_detective_movie['Director']}
'''
,parse_mode='html', reply_markup=markup)
    elif callback.data == 'filtr_multik':
        markup = types.InlineKeyboardMarkup() 
        btn1 = types.InlineKeyboardButton('Следущий фильм жанра: Мультфильм',callback_data='filtr_multik') 
        btn2 = types.InlineKeyboardButton('Выбрать другой жанр',callback_data='choicebutton')
        btn3 = types.InlineKeyboardButton('Меню',callback_data='menu')
        markup.row(btn1)
        markup.row(btn2,btn3)  
        multik_movies = [movie for movie in movies if movie["Genre"] == "мультфильм"]
        random_multik_movie = random.choice(multik_movies)
        bot.send_photo(callback.message.chat.id, random_multik_movie['Image'])
        bot.send_message(callback.message.chat.id, 
    
f'''
<b>{random_multik_movie['Name']}</b>

{random_multik_movie['Description']}

<b>О фильме:</b>
Жанр: {random_multik_movie['Genre']}
Год производства: {random_multik_movie['Year']}
Режиссер: {random_multik_movie['Director']}
'''
,parse_mode='html', reply_markup=markup)
    elif callback.data == 'filtr_adventures':
        markup = types.InlineKeyboardMarkup() 
        btn1 = types.InlineKeyboardButton('Следущий фильм жанра: Приключения',callback_data='filtr_adventures') 
        btn2 = types.InlineKeyboardButton('Выбрать другой жанр',callback_data='choicebutton')
        btn3 = types.InlineKeyboardButton('Меню',callback_data='menu')
        markup.row(btn1)
        markup.row(btn2,btn3)  
        adventures_movies = [movie for movie in movies if movie["Genre"] == "приключения"]
        random_adventures_movie = random.choice(adventures_movies)
        bot.send_photo(callback.message.chat.id, random_adventures_movie['Image'])
        bot.send_message(callback.message.chat.id, 
    
f'''
<b>{random_adventures_movie['Name']}</b>

{random_adventures_movie['Description']}

<b>О фильме:</b>
Жанр: {random_adventures_movie['Genre']}
Год производства: {random_adventures_movie['Year']}
Режиссер: {random_adventures_movie['Director']}
'''
,parse_mode='html', reply_markup=markup)
    elif callback.data == 'choicebutton':
        
        markup = types.InlineKeyboardMarkup() 
        btn1 = types.InlineKeyboardButton('Фантастика',callback_data='filtr_fentasy') 
        btn2 = types.InlineKeyboardButton('Драма',callback_data='filtr_drama') 
        btn3 = types.InlineKeyboardButton('Хоррор',callback_data='filtr_horror') 
        markup.row(btn1,btn2,btn3) 
        btn4 = types.InlineKeyboardButton('Комедия',callback_data='filtr_comedia') 
        btn5 = types.InlineKeyboardButton('Боевик',callback_data='filtr_boevik') 
        btn6 = types.InlineKeyboardButton('Триллер',callback_data='filtr_triller') 
        markup.row(btn4,btn5,btn6)
        btn7 = types.InlineKeyboardButton('Детектив',callback_data='filtr_detective') 
        btn8 = types.InlineKeyboardButton('Мультфильм',callback_data='filtr_multik') 
        btn9 = types.InlineKeyboardButton('Приключения',callback_data='filtr_adventures') 
        markup.row(btn7,btn8,btn9)
        bot.send_message(callback.message.chat.id,'Выберите жанр для случайного фильма: ', reply_markup=markup) 
    elif callback.data == 'menu':
        markup = types.InlineKeyboardMarkup() 
        btn1 = types.InlineKeyboardButton('Cлучайный фильм',callback_data='randomfilm') 
        btn2 = types.InlineKeyboardButton('Выбрать жанр для случайного фильма',callback_data='choicebutton') 

        markup.row(btn1) 
        markup.row(btn2) 
        bot.send_message(callback.message.chat.id,
                         '''
<b>Меню команд: </b>
Здесь вы можете выбрать удобный способ для поиска фильма                   
''',parse_mode='html', reply_markup=markup) 



@bot.message_handler() 
def info(message): 
    if message.text.lower() == 'создатель':           
        bot.send_message(message.chat.id,'Создателем этого бота является: <b>Палехов Федор</b>',parse_mode='html') 
    else:   
        bot.send_message(message.chat.id, f'{message.text} - <em>Неизвестная команда</em>',parse_mode='html') 
 
 
 
bot.polling(none_stop='True')