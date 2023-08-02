import smtplib
import os

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

import telebot
from telebot import types

a = 0
email_login = 'общий логин'
email_pass = 'пароль'
to_email = ''
to_subject = ''
to_text = ''
src_holy = ''
email_from = ''

bot = telebot.TeleBot('токен');


@bot.message_handler(content_types=['text', 'sticker', 'photo'])
def hello(message):  # приветственная функция

    while a == 0:

        if message.text == '/help' or message.text == '/stop':
            bot.send_message(message.from_user.id, '/start - написать обращение\n'
                                                   '/stop - остановить создание обращения\n'
                                                   '/info - подробная информация по службам поддержки')
            break
        if message.text == '/info':
            bot.send_message(message.from_user.id, '*Admins* - _любые вопросы, связанные с IT._\n'
                                                   '\n*Delivery Help* - _оперативные вопросы по доставке заказов (в т.ч. смена порта)._\n'
                                                   '\n*Order Help* - _оперативные вопросы по прохождению заказа через ПСК (сроки изменения, отклонения от стандартных БП)._\n'
                                                   '\n*Cert Help* - _вопросы сертификации продукции (при отсутствии или ненадлежащей информации в реестре сертификатов), консультации по обязательной маркировке (честныйзнак.рф), оформление штрих-кодов (GTIN)._\n'
                                                   '\n*Product Help* - _оперативные вопросы по характеристикам артикулов (цвет по пантону, живые фото товара, информация об упаковке, вопросы по конкретной партии (уточнение материалов отдельных частей предмета, сравнение габаритов предметов, совместное фото нескольких предметов, чтобы проверить сочетаемость цвета, и др.))._\n'
                                                   '\n*Print Help* - _оперативные консультации по срокам и ценам производства и технологические вопросы по КОНКРЕТНЫМ макетам._\n'
                                                   '\n*Test Help* - _вопросы по возможностям нанесения, тестированию артикулов, конструкторам, фото примеров в КТ._\n'
                                                   '\n*Supply Help* - _оперативные вопросы о сроках поставки и приемки на склад (в т.ч. и возвраты)._\n'
                                                   '\n*Return* - _изменения в заказах, поставленных в работу, изменение/разделение заказа, изменение ТЗ, недогруз, снятие заказа с работы, откаты макетов, вопросы по резервам, вопросы компенсации (ФО, бухгалтерия)._\n'
                                                   '\n*Tech Help* - _заявки в техническую службу._\n'
                                                   '\n*Закупка* - _запросы на закупку товаров для внутреннего пользования._',
                             parse_mode='Markdown')
            break
        if message.text == '/start':

            bot.send_message(message.from_user.id, 'Введите адрес своей почты в формате "example@gifts.ru".')
            bot.register_next_step_handler(message, login);
            break
        else:
            bot.send_message(message.from_user.id, 'Напишите /help')
            break


def login(message):  # пользователь вводит адрес своей электронной почты и выбирает, куда будет писать
    global email_from
    email_from = str(message.text)
    while a == 0:
        if message.text == '/stop':  # возможность остановить процесс и откатиться к функции hello
            try:
                os.remove(src_holy)
                bot.send_message(message.from_user.id, 'Ваше обращение отменено. Выберите:')
                bot.send_message(message.from_user.id, '/start - написать новое обращение\n'
                                                       '/info - подробная информация по службам поддержки')
                bot.register_next_step_handler(message, hello);
            except:

                bot.send_message(message.from_user.id, 'Ваше обращение отменено. Выберите:')
                bot.send_message(message.from_user.id, '/start - написать новое обращение\n'
                                                       '/info - подробная информация по службам поддержки')
                bot.register_next_step_handler(message, hello);
            break
        else:

            keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
            button1 = types.KeyboardButton('Admins')
            button2 = types.KeyboardButton('Delivery Help')
            button3 = types.KeyboardButton('Order Help')
            button4 = types.KeyboardButton('Cert Help')
            button5 = types.KeyboardButton('Print Help')
            button6 = types.KeyboardButton('Product Help')
            button7 = types.KeyboardButton('Test Help')
            button8 = types.KeyboardButton('Supply Help')
            button9 = types.KeyboardButton('Return')
            button10 = types.KeyboardButton('Tech Help')
            button11 = types.KeyboardButton('Закупка')
            button12 = types.KeyboardButton('ТЕСТ')
            keyboard.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10,
                         button11, button12)
            bot.send_message(message.from_user.id, 'Выберите службу, в которую хотите обратиться.\n'
                                                   '_Чтобы получить справку по работе каждой службы,\n'
                                                   'наберите /info._', reply_markup=keyboard, parse_mode='Markdown')
            bot.register_next_step_handler(message, writing_to);
            break


def writing_to(message):  # почта выбранной службы поддержки вносится в переменную email_to
    while a == 0:
        if message.text == '/stop':  # возможность остановить процесс и откатиться к функции hello
            try:
                os.remove(src_holy)
                bot.send_message(message.from_user.id, 'Ваше обращение отменено. Выберите:')
                bot.send_message(message.from_user.id, '/start - написать новое обращение\n'
                                                       '/info - подробная информация по службам поддержки')
                bot.register_next_step_handler(message, hello);
            except:

                bot.send_message(message.from_user.id, 'Ваше обращение отменено. Выберите:')
                bot.send_message(message.from_user.id, '/start - написать новое обращение\n'
                                                       '/info - подробная информация по службам поддержки')
                bot.register_next_step_handler(message, hello);
            break
        if message.text == '/info':  # вызов справочной информации + возможность выбрать службу
            bot.send_message(message.from_user.id, '*Admins* - _любые вопросы, связанные с IT._\n'
                                                   '\n*Delivery Help* - _оперативные вопросы по доставке заказов (в т.ч. смена порта)._\n'
                                                   '\n*Order Help* - _оперативные вопросы по прохождению заказа через ПСК (сроки изменения, отклонения от стандартных БП)._\n'
                                                   '\n*Cert Help* - _вопросы сертификации продукции (при отсутствии или ненадлежащей информации в реестре сертификатов), консультации по обязательной маркировке (честныйзнак.рф), оформление штрих-кодов (GTIN)._\n'
                                                   '\n*Product Help* - _оперативные вопросы по характеристикам артикулов (цвет по пантону, живые фото товара, информация об упаковке, вопросы по конкретной партии (уточнение материалов отдельных частей предмета, сравнение габаритов предметов, совместное фото нескольких предметов, чтобы проверить сочетаемость цвета, и др.))._\n'
                                                   '\n*Print Help* - _оперативные консультации по срокам и ценам производства и технологические вопросы по КОНКРЕТНЫМ макетам._\n'
                                                   '\n*Test Help* - _вопросы по возможностям нанесения, тестированию артикулов, конструкторам, фото примеров в КТ._\n'
                                                   '\n*Supply Help* - _оперативные вопросы о сроках поставки и приемки на склад (в т.ч. и возвраты)._\n'
                                                   '\n*Return* - _изменения в заказах, поставленных в работу, изменение/разделение заказа, изменение ТЗ, недогруз, снятие заказа с работы, откаты макетов, вопросы по резервам, вопросы компенсации (ФО, бухгалтерия)._\n'
                                                   '\n*Tech Help* - _заявки в техническую службу._\n'
                                                   '\n*Закупка* - _запросы на закупку товаров для внутреннего пользования._',
                             parse_mode='Markdown')

            keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
            button1 = types.KeyboardButton('Admins')
            button2 = types.KeyboardButton('Delivery Help')
            button3 = types.KeyboardButton('Order Help')
            button4 = types.KeyboardButton('Cert Help')
            button5 = types.KeyboardButton('Print Help')
            button6 = types.KeyboardButton('Product Help')
            button7 = types.KeyboardButton('Test Help')
            button8 = types.KeyboardButton('Supply Help')
            button9 = types.KeyboardButton('Return')
            button10 = types.KeyboardButton('Tech Help')
            button11 = types.KeyboardButton('Закупка')
            button12 = types.KeyboardButton('ТЕСТ')
            keyboard.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10,
                         button11, button12)
            bot.send_message(message.from_user.id, 'Выберите службу, в которую хотите обратиться.',
                             reply_markup=keyboard)

            bot.register_next_step_handler(message, writing_to);

            break
        if message.text == 'Admins':
            global to_email
            to_email = 'admins@gifts.ru'
            bot.send_message(message.from_user.id, 'Введите тему письма')
            bot.register_next_step_handler(message, subject);
            break
        if message.text == 'Delivery Help':
            to_email = 'delivery-help@gifts.ru'
            bot.send_message(message.from_user.id, 'Введите тему письма')
            bot.register_next_step_handler(message, subject);
            break
        if message.text == 'Order Help':
            to_email = 'order-help@gifts.ru'
            bot.send_message(message.from_user.id, 'Введите тему письма')
            bot.register_next_step_handler(message, subject);
            break
        if message.text == 'Cert Help':
            to_email = 'cert-help@gifts.ru'
            bot.send_message(message.from_user.id, 'Введите тему письма')
            bot.register_next_step_handler(message, subject);
            break
        if message.text == 'Print Help':
            to_email = 'print-help@gifts.ru'
            bot.send_message(message.from_user.id, 'Введите тему письма')
            bot.register_next_step_handler(message, subject);
            break
        if message.text == 'Product Help':
            to_email = 'product-help@gifts.ru'
            bot.send_message(message.from_user.id, 'Введите тему письма')
            bot.send_message(message.from_user.id,
                             '_В теме необходимо указать номер артикула (с точностью до цвета и размера)_',
                             parse_mode='Markdown')

            bot.register_next_step_handler(message, subject);
            break
        if message.text == 'Test Help':
            to_email = 'test-help@gifts.ru'
            bot.send_message(message.from_user.id, 'Введите тему письма')
            bot.register_next_step_handler(message, subject);
            break
        if message.text == 'Supply Help':
            to_email = 'supply-help@gifts.ru'
            bot.send_message(message.from_user.id, 'Введите тему письма')
            bot.send_message(message.from_user.id,
                             '_В теме необходимо указать номер артикула (с точностью до цвета и размера) '
                             'и ОДНО из ключевых слов: «В пути», «Приемка» или «Россия»_', parse_mode='Markdown')
            bot.register_next_step_handler(message, subject);
            break
        if message.text == 'Return':
            to_email = 'return@gifts.ru'
            bot.send_message(message.from_user.id, 'Введите тему письма')
            bot.register_next_step_handler(message, subject);
            break
        if message.text == 'Tech Help':
            to_email = 'tech-help@gifts.ru'
            bot.send_message(message.from_user.id, 'Введите тему письма')
            bot.register_next_step_handler(message, subject);
            break
        if message.text == 'Закупка':
            to_email = 'zakupka@gifts.ru'
            bot.send_message(message.from_user.id, 'Введите тему письма')
            bot.register_next_step_handler(message, subject);
            break
        if message.text == 'ТЕСТ':
            to_email = 'test01@gifts.ru'
            bot.send_message(message.from_user.id, 'Введите тему письма')
            bot.register_next_step_handler(message, subject);
            break

        else:  # ловушка для дурака
            bot.send_message(message.from_user.id,
                             'Пожалуйста, выберите канал обращения из кнопок, представленных ниже. '
                             'Вызвать кнопки можно кликнув на значок, отмеченный на фото.')
            bot.send_photo(message.from_user.id,
                           'https://sun9-31.userapi.com/impf/V7j-8eMBXI6mmYrrCtA0mqePLSEpf91qmK8SuA/shngMk08RYQ.jpg?size=663x373&quality=95&sign=54b522d735383002795e1bfb3bec42ee&type=album')
            bot.register_next_step_handler(message, writing_to);
            break


def subject(message):  # пользователь пишет тему письма
    global to_subject
    while a == 0:
        if message.text == '/stop':  # возможность остановить процесс и откатиться к функции hello
            try:
                os.remove(src_holy)
                bot.send_message(message.from_user.id, 'Ваше обращение отменено. Выберите:')
                bot.send_message(message.from_user.id, '/start - написать новое обращение\n'
                                                       '/info - подробная информация по службам поддержки')
                bot.register_next_step_handler(message, hello);
            except:

                bot.send_message(message.from_user.id, 'Ваше обращение отменено. Выберите:')
                bot.send_message(message.from_user.id, '/start - написать новое обращение\n'
                                                       '/info - подробная информация по службам поддержки')
                bot.register_next_step_handler(message, hello);
            break
        else:
            to_subject = str(message.text)
            bot.send_message(message.from_user.id, 'Введите текст сообщения')
            bot.register_next_step_handler(message, text_try);
            break


def text_try(message):  # пользователь пишет текст сообщения и выбирает, отправлять фотку или нет
    global to_text
    while a == 0:
        if message.text == '/stop':  # возможность остановить процесс и откатиться к функции hello
            try:
                os.remove(src_holy)
                bot.send_message(message.from_user.id, 'Ваше обращение отменено. Выберите:')
                bot.send_message(message.from_user.id, '/start - написать новое обращение\n'
                                                       '/info - подробная информация по службам поддержки')
                bot.register_next_step_handler(message, hello);
            except:

                bot.send_message(message.from_user.id, 'Ваше обращение отменено. Выберите:')
                bot.send_message(message.from_user.id, '/start - написать новое обращение\n'
                                                       '/info - подробная информация по службам поддержки')
                bot.register_next_step_handler(message, hello);
            break
        else:
            to_text = str(message.text)

            keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
            button1 = types.KeyboardButton('Да')
            button2 = types.KeyboardButton('Нет')
            keyboard.add(button1, button2)
            bot.send_message(message.from_user.id, 'Хотите ли Вы приложить фотографию к обращению?',
                             reply_markup=keyboard)
            bot.register_next_step_handler(message, pic_try);
            break


def pic_try(
        message):  # пользователь либо отправляет фотку, либо отказывается и получает итоговый вид письма перед отправкой для заверения

    while a == 0:
        if message.text == '/stop':  # возможность остановить процесс и откатиться к функции hello
            try:
                os.remove(src_holy)
                bot.send_message(message.from_user.id, 'Ваше обращение отменено. Выберите:')
                bot.send_message(message.from_user.id, '/start - написать новое обращение\n'
                                                       '/info - подробная информация по службам поддержки')
                bot.register_next_step_handler(message, hello);
            except:

                bot.send_message(message.from_user.id, 'Ваше обращение отменено. Выберите:')
                bot.send_message(message.from_user.id, '/start - написать новое обращение\n'
                                                       '/info - подробная информация по службам поддержки')
                bot.register_next_step_handler(message, hello);
            break

        if message.text == 'Да':  # пользователь отправляет фотку
            bot.send_message(message.from_user.id, 'Пришлите *одно* изображение.\n'
                                                   '_Не забудьте поставить галочку напротив строки "Сжать изображение"._',
                             parse_mode='Markdown')

            bot.register_next_step_handler(message, pic_try2);
            break
        if message.text == 'Нет':  # пользователь получает итоговый вид письма перед отправкой для заверения
            bot.send_message(message.from_user.id,
                             '*Проверьте данные письма:*\n\n*От кого:* {email_from}\n*Кому:* {to_email}\n*Тема:* {to_subject}\n'
                             '*Текст:* {to_text}'.format(email_from=email_from, to_email=to_email,
                                                         to_subject=to_subject, to_text=to_text),
                             parse_mode='Markdown')
            try:
                img = open(src_holy, 'rb')
                bot.send_message(message.from_user.id, '*Прикрепленная фотография:*', parse_mode='Markdown')
                bot.send_photo(message.chat.id, img)
            except:
                bot.send_message(message.from_user.id, '*Прикрепленная фотография отсутствует*', parse_mode='Markdown')

            bot.send_message(message.from_user.id, '_Чтобы полностью отменить отправку этого письма,\n'
                                                   'наберите /stop_', parse_mode='Markdown')

            keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
            button1 = types.KeyboardButton('Да')
            button2 = types.KeyboardButton('Нет')
            keyboard.add(button1, button2)
            bot.send_message(message.from_user.id, 'Всё верно?', reply_markup=keyboard)

            bot.register_next_step_handler(message, check);
            break
        else:  # ловушка для дурака
            bot.send_message(message.from_user.id,
                             'Пожалуйста, выберите ответ из кнопок, представленных ниже.\n'
                             'Вызвать кнопки можно кликнув на значок, отмеченный на фото.')
            bot.send_photo(message.from_user.id,
                           'https://sun9-31.userapi.com/impf/V7j-8eMBXI6mmYrrCtA0mqePLSEpf91qmK8SuA/shngMk08RYQ.jpg?size=663x373&quality=95&sign=54b522d735383002795e1bfb3bec42ee&type=album')
            bot.register_next_step_handler(message, pic_try);
            break


def pic_try2(message):  # фотка пользователя сохраняется на сервере и выводится полный вид письма для заверения
    global src_holy
    while a == 0:
        if message.text == '/stop':  # возможность остановить процесс и откатиться к функции hello
            try:
                os.remove(src_holy)
                bot.send_message(message.from_user.id, 'Ваше обращение отменено. Выберите:')
                bot.send_message(message.from_user.id, '/start - написать новое обращение\n'
                                                       '/info - подробная информация по службам поддержки')
                bot.register_next_step_handler(message, hello);
            except:

                bot.send_message(message.from_user.id, 'Ваше обращение отменено. Выберите:')
                bot.send_message(message.from_user.id, '/start - написать новое обращение\n'
                                                       '/info - подробная информация по службам поддержки')
                bot.register_next_step_handler(message, hello);
            break
        else:
            try:
                file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
                downloaded_file = bot.download_file(file_info.file_path)
                src_holy = 'локальный адрес, куда будет сохраняться фотка' + file_info.file_path
                with open(src_holy, 'wb') as new_file:
                    new_file.write(downloaded_file)

                bot.send_message(message.from_user.id,
                                 '*Проверьте данные письма:*\n\n*От кого:* {email_from}\n*Кому:* {to_email}\n*Тема:* {to_subject}\n'
                                 '*Текст:* {to_text}'.format(email_from=email_from, to_email=to_email,
                                                             to_subject=to_subject, to_text=to_text),
                                 parse_mode='Markdown')
                try:
                    img = open(src_holy, 'rb')
                    bot.send_message(message.from_user.id, '*Прикрепленная фотография:*', parse_mode='Markdown')
                    bot.send_photo(message.chat.id, img)
                except:
                    bot.send_message(message.from_user.id, '*Прикрепленная фотография отсутствует*',
                                     parse_mode='Markdown')
                bot.send_message(message.from_user.id, '_Чтобы полностью отменить отправку этого письма,\n'
                                                       'наберите /stop_', parse_mode='Markdown')

                keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
                button1 = types.KeyboardButton('Да')
                button2 = types.KeyboardButton('Нет')
                keyboard.add(button1, button2)
                bot.send_message(message.from_user.id, 'Всё верно?', reply_markup=keyboard)

                bot.register_next_step_handler(message, check);



            except:
                bot.send_message(message.from_user.id, 'Некорректный формат изображения.\n'
                                                       '*Проверьте, что напротив строки "Сжать изображение" стоит галочка, и загрузите фотографию еще раз*',
                                 parse_mode='Markdown')

                bot.register_next_step_handler(message, pic_try2);
            break


def check(message):  # письмо либо отправляется, либо выбирается параметр для изменения
    while a == 0:
        if message.text == '/stop':  # возможность остановить процесс и откатиться к функции hello
            try:
                os.remove(src_holy)
                bot.send_message(message.from_user.id, 'Ваше обращение отменено. Выберите:')
                bot.send_message(message.from_user.id, '/start - написать новое обращение\n'
                                                       '/info - подробная информация по службам поддержки')
                bot.register_next_step_handler(message, hello);
            except:

                bot.send_message(message.from_user.id, 'Ваше обращение отменено. Выберите:')
                bot.send_message(message.from_user.id, '/start - написать новое обращение\n'
                                                       '/info - подробная информация по службам поддержки')
                bot.register_next_step_handler(message, hello);
            break
        if message.text == 'Да':  # письмо отправляется

            connecting_post = smtplib.SMTP('почтовый сервер', код)
            connecting_post.starttls()
            connecting_post.login(email_login, email_pass)

            msg = MIMEMultipart()
            msg['From'] = email_from
            msg['To'] = to_email
            msg['Subject'] = to_subject

            txt = MIMEText(to_text, 'plain')
            msg.attach(txt)

            html = """\
            <html>
              <head></head>
              <body>

                <br>
                <hr size="5">
                <p style="font-style:italic;">
                <br>
                    Это письмо отправлено с помощью телеграм-бота.
                </p>
              </body>
            </html>
            """
            msg.attach(MIMEText(html, 'html', 'utf-8'))

            try:
                part = MIMEApplication(open(src_holy, 'rb').read())
                part.add_header('Content-Disposition', 'attachment', filename='image.jpg')
                msg.attach(part)

                try:
                    connecting_post.send_message(msg)
                    connecting_post.quit()
                    bot.send_message(message.from_user.id, 'Письмо отправлено')
                    try:
                        os.remove(src_holy)
                        bot.send_message(message.from_user.id, '_Чтобы написать еще одно обращение, наберите /start_',
                                         parse_mode='Markdown')
                    except:
                        bot.send_message(message.from_user.id, '_Чтобы написать еще одно обращение, наберите /start_',
                                         parse_mode='Markdown')

                except:
                    bot.send_message(message.from_user.id,
                                     '_Ваша почта введена неверно, пожалуйста введите корректный почтовый адрес отправителя в формате "example@gifts.ru"._',
                                     parse_mode='Markdown')
                    bot.register_next_step_handler(message, email_from_new);
            except:
                try:
                    connecting_post.send_message(msg)
                    connecting_post.quit()
                    bot.send_message(message.from_user.id, 'Письмо отправлено')
                    try:
                        os.remove(src_holy)
                        bot.send_message(message.from_user.id, '_Чтобы написать еще одно обращение, наберите /start_',
                                         parse_mode='Markdown')
                    except:
                        bot.send_message(message.from_user.id, '_Чтобы написать еще одно обращение, наберите /start_',
                                         parse_mode='Markdown')

                except:
                    bot.send_message(message.from_user.id,
                                     '_Ваша почта введена неверно, пожалуйста введите корректный почтовый адрес отправителя в формате "example@gifts.ru"._',
                                     parse_mode='Markdown')
                    bot.register_next_step_handler(message, email_from_new);

            break

        if message.text == 'Нет':  # выбирается параметр для изменения

            keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
            button0 = types.KeyboardButton('От кого')
            button1 = types.KeyboardButton('Кому')
            button2 = types.KeyboardButton('Тема сообщения')
            button3 = types.KeyboardButton('Текст сообщения')
            button4 = types.KeyboardButton('Изображение')
            keyboard.add(button0, button1, button2, button3, button4)
            bot.send_message(message.from_user.id, 'Выберите параметр, который хотели бы изменить:',
                             reply_markup=keyboard)
            bot.register_next_step_handler(message, changing);
            break

        else:  # ловушка для дурака
            bot.send_message(message.from_user.id, 'Пожалуйста, выберите ответ из кнопок, представленных ниже, '
                                                   'либо напишите "Да" или "Нет".\n'
                                                   'Вызвать кнопки можно кликнув на значок, отмеченный на фото.')
            bot.send_photo(message.from_user.id,
                           'https://sun9-31.userapi.com/impf/V7j-8eMBXI6mmYrrCtA0mqePLSEpf91qmK8SuA/shngMk08RYQ.jpg?size=663x373&quality=95&sign=54b522d735383002795e1bfb3bec42ee&type=album')
            bot.register_next_step_handler(message, check);
            break


def changing(message):  # перенаправления на дополнительные функции, которые меняют выбранные параметры
    while a == 0:
        if message.text == '/stop':  # возможность остановить процесс и откатиться к функции hello
            try:
                os.remove(src_holy)
                bot.send_message(message.from_user.id, 'Ваше обращение отменено. Выберите:')
                bot.send_message(message.from_user.id, '/start - написать новое обращение\n'
                                                       '/info - подробная информация по службам поддержки')
                bot.register_next_step_handler(message, hello);
            except:

                bot.send_message(message.from_user.id, 'Ваше обращение отменено. Выберите:')
                bot.send_message(message.from_user.id, '/start - написать новое обращение\n'
                                                       '/info - подробная информация по службам поддержки')
                bot.register_next_step_handler(message, hello);
            break
        if message.text == 'От кого':
            bot.send_message(message.from_user.id, 'Введите адрес своей почты в формате "example@gifts.ru".')
            bot.register_next_step_handler(message, email_from_new);
            break

        if message.text == 'Кому':
            keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
            button1 = types.KeyboardButton('Admins')
            button2 = types.KeyboardButton('Delivery Help')
            button3 = types.KeyboardButton('Order Help')
            button4 = types.KeyboardButton('Cert Help')
            button5 = types.KeyboardButton('Print Help')
            button6 = types.KeyboardButton('Product Help')
            button7 = types.KeyboardButton('Test Help')
            button8 = types.KeyboardButton('Supply Help')
            button9 = types.KeyboardButton('Return')
            button10 = types.KeyboardButton('Tech Help')
            button11 = types.KeyboardButton('Закупка')
            button12 = types.KeyboardButton('ТЕСТ')
            keyboard.add(button1, button2, button3, button4, button5, button6, button7, button8,
                         button9, button10, button11, button12)
            bot.send_message(message.from_user.id, 'Выберите, в какую службу Вы хотите написать.\n'
                                                   '_Чтобы получить справку по работе каждой службы наберите /info._',
                             reply_markup=keyboard, parse_mode='Markdown')

            bot.register_next_step_handler(message, writing_to2);
            break

        if message.text == 'Тема сообщения':
            bot.send_message(message.from_user.id, 'Введите тему письма')
            bot.register_next_step_handler(message, subject2);
            break

        if message.text == 'Текст сообщения':
            bot.send_message(message.from_user.id, 'Введите текст сообщения')
            bot.register_next_step_handler(message, text2);
            break

        if message.text == 'Изображение':
            keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
            button1 = types.KeyboardButton('Изменить')
            button2 = types.KeyboardButton('Удалить')
            keyboard.add(button1, button2)
            bot.send_message(message.from_user.id, 'Вы хотите изменить или удалить изображение?', reply_markup=keyboard)

            bot.register_next_step_handler(message, pic_new);
            break

        else:
            bot.send_message(message.from_user.id,
                             'Пожалуйста, выберите ответ из кнопок, представленных ниже.\n'
                             'Вызвать кнопки можно кликнув на значок, отмеченный на фото')
            bot.send_photo(message.from_user.id,
                           'https://sun9-31.userapi.com/impf/V7j-8eMBXI6mmYrrCtA0mqePLSEpf91qmK8SuA/shngMk08RYQ.jpg?size=663x373&quality=95&sign=54b522d735383002795e1bfb3bec42ee&type=album')
            bot.register_next_step_handler(message, changing);
            break


def email_from_new(
        message):  # новый адрес отправителя заносится в переменную, предлагается проверка корректности всего письма
    global email_from
    while a == 0:
        if message.text == '/stop':  # возможность остановить процесс и откатиться к функции hello
            try:
                os.remove(src_holy)
                bot.send_message(message.from_user.id, 'Ваше обращение отменено. Выберите:')
                bot.send_message(message.from_user.id, '/start - написать новое обращение\n'
                                                       '/info - подробная информация по службам поддержки')
                bot.register_next_step_handler(message, hello);
            except:

                bot.send_message(message.from_user.id, 'Ваше обращение отменено. Выберите:')
                bot.send_message(message.from_user.id, '/start - написать новое обращение\n'
                                                       '/info - подробная информация по службам поддержки')
                bot.register_next_step_handler(message, hello);
            break

        else:
            email_from = str(message.text)

            bot.send_message(message.from_user.id,
                             '*Проверьте данные письма:*\n\n*От кого:* {email_from}\n*Кому:* {to_email}\n*Тема:* {to_subject}\n'
                             '*Текст:* {to_text}'.format(email_from=email_from, to_email=to_email,
                                                         to_subject=to_subject, to_text=to_text),
                             parse_mode='Markdown')
            try:
                img = open(src_holy, 'rb')
                bot.send_message(message.from_user.id, '*Прикрепленная фотография:*', parse_mode='Markdown')
                bot.send_photo(message.chat.id, img)
            except:
                bot.send_message(message.from_user.id, '*Прикрепленная фотография отсутствует*', parse_mode='Markdown')

            bot.send_message(message.from_user.id, '_Чтобы полностью отменить отправку этого письма,\n'
                                                   'наберите /stop_', parse_mode='Markdown')

            keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
            button1 = types.KeyboardButton('Да')
            button2 = types.KeyboardButton('Нет')
            keyboard.add(button1, button2)
            bot.send_message(message.from_user.id, 'Всё верно?', reply_markup=keyboard)

            bot.register_next_step_handler(message, check);
            break


def pic_new(
        message):  # пользователь выбирает либо изменить фотку и загрузить новую, либо удалить фотку, предлагается проверка корректности всего письма
    global src_holy
    while a == 0:
        if message.text == '/stop':  # возможность остановить процесс и откатиться к функции hello
            try:
                os.remove(src_holy)
                bot.send_message(message.from_user.id, 'Ваше обращение отменено. Выберите:')
                bot.send_message(message.from_user.id, '/start - написать новое обращение\n'
                                                       '/info - подробная информация по службам поддержки')
                bot.register_next_step_handler(message, hello);
            except:

                bot.send_message(message.from_user.id, 'Ваше обращение отменено. Выберите:')
                bot.send_message(message.from_user.id, '/start - написать новое обращение\n'
                                                       '/info - подробная информация по службам поддержки')
                bot.register_next_step_handler(message, hello);
            break

        if message.text == 'Изменить':
            try:
                os.remove(src_holy)
                bot.send_message(message.from_user.id, 'Прикрепите новое изображение\n'
                                                       '_Не забудьте поставить галочку напротив строки "Сжать изображение"._',
                                 parse_mode='Markdown')
                bot.register_next_step_handler(message, pic_new1);
                break
            except:
                bot.send_message(message.from_user.id, 'Прикрепите новое изображение\n'
                                                       '_Не забудьте поставить галочку напротив строки "Сжать изображение"._',
                                 parse_mode='Markdown')
                bot.register_next_step_handler(message, pic_new1);
                break
        if message.text == 'Удалить':
            try:
                os.remove(src_holy)
                bot.send_message(message.from_user.id,
                                 '*Проверьте данные письма:*\n\n*От кого:* {email_from}\n*Кому:* {to_email}\n*Тема:* {to_subject}\n'
                                 '*Текст:* {to_text}'.format(email_from=email_from, to_email=to_email,
                                                             to_subject=to_subject, to_text=to_text),
                                 parse_mode='Markdown')
                try:
                    img = open(src_holy, 'rb')
                    bot.send_message(message.from_user.id, '*Прикрепленная фотография:*', parse_mode='Markdown')
                    bot.send_photo(message.chat.id, img)
                except:
                    bot.send_message(message.from_user.id, '*Прикрепленная фотография отсутствует*',
                                     parse_mode='Markdown')

                bot.send_message(message.from_user.id, '_Чтобы полностью отменить отправку этого письма,\n'
                                                       'наберите /stop_', parse_mode='Markdown')

                keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
                button1 = types.KeyboardButton('Да')
                button2 = types.KeyboardButton('Нет')
                keyboard.add(button1, button2)
                bot.send_message(message.from_user.id, 'Всё верно?', reply_markup=keyboard)

                bot.register_next_step_handler(message, check);
                break
            except:
                bot.send_message(message.from_user.id, '_Изображение отсутствует_', parse_mode='Markdown')
                bot.send_message(message.from_user.id,
                                 '*Проверьте данные письма:*\n\n*От кого:* {email_from}\n*Кому:* {to_email}\n*Тема:* {to_subject}\n'
                                 '*Текст:* {to_text}'.format(email_from=email_from, to_email=to_email,
                                                             to_subject=to_subject, to_text=to_text),
                                 parse_mode='Markdown')
                try:
                    img = open(src_holy, 'rb')
                    bot.send_message(message.from_user.id, '*Прикрепленная фотография:*', parse_mode='Markdown')
                    bot.send_photo(message.chat.id, img)
                except:
                    bot.send_message(message.from_user.id, '*Прикрепленная фотография отсутствует*',
                                     parse_mode='Markdown')

                bot.send_message(message.from_user.id, '_Чтобы полностью отменить отправку этого письма,\n'
                                                       'наберите /stop_', parse_mode='Markdown')

                keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
                button1 = types.KeyboardButton('Да')
                button2 = types.KeyboardButton('Нет')
                keyboard.add(button1, button2)
                bot.send_message(message.from_user.id, 'Всё верно?', reply_markup=keyboard)

                bot.register_next_step_handler(message, check);
                break
        else:
            bot.send_message(message.from_user.id,
                             'Пожалуйста, выберите ответ из кнопок, представленных ниже.\n'
                             'Вызвать кнопки можно кликнув на значок, отмеченный на фото')
            bot.send_photo(message.from_user.id,
                           'https://sun9-31.userapi.com/impf/V7j-8eMBXI6mmYrrCtA0mqePLSEpf91qmK8SuA/shngMk08RYQ.jpg?size=663x373&quality=95&sign=54b522d735383002795e1bfb3bec42ee&type=album')
            bot.register_next_step_handler(message, pic_new);
            break


def pic_new1(
        message):  # новая фотка пользователя скачивается на сервер, предлагается проверка корректности всего письма
    global src_holy
    while a == 0:
        if message.text == '/stop':  # возможность остановить процесс и откатиться к функции hello
            try:
                os.remove(src_holy)
                bot.send_message(message.from_user.id, 'Ваше обращение отменено. Выберите:')
                bot.send_message(message.from_user.id, '/start - написать новое обращение\n'
                                                       '/info - подробная информация по службам поддержки')
                bot.register_next_step_handler(message, hello);
            except:

                bot.send_message(message.from_user.id, 'Ваше обращение отменено. Выберите:')
                bot.send_message(message.from_user.id, '/start - написать новое обращение\n'
                                                       '/info - подробная информация по службам поддержки')
                bot.register_next_step_handler(message, hello);
            break
        else:
            try:

                file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
                downloaded_file = bot.download_file(file_info.file_path)
                src_holy = 'локальный адрес хранения фото' + file_info.file_path
                with open(src_holy, 'wb') as new_file:
                    new_file.write(downloaded_file)

                bot.send_message(message.from_user.id,
                                 '*Проверьте данные письма:*\n\n*От кого:* {email_from}\n*Кому:* {to_email}\n*Тема:* {to_subject}\n'
                                 '*Текст:* {to_text}'.format(email_from=email_from, to_email=to_email,
                                                             to_subject=to_subject, to_text=to_text),
                                 parse_mode='Markdown')

                try:
                    img = open(src_holy, 'rb')
                    bot.send_message(message.from_user.id, '*Прикрепленная фотография:*', parse_mode='Markdown')
                    bot.send_photo(message.chat.id, img)
                except:
                    bot.send_message(message.from_user.id, '*Прикрепленная фотография отсутствует*',
                                     parse_mode='Markdown')

                bot.send_message(message.from_user.id, '_Чтобы полностью отменить отправку этого письма,\n'
                                                       'наберите /stop_', parse_mode='Markdown')

                keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
                button1 = types.KeyboardButton('Да')
                button2 = types.KeyboardButton('Нет')
                keyboard.add(button1, button2)
                bot.send_message(message.from_user.id, 'Всё верно?', reply_markup=keyboard)

                bot.register_next_step_handler(message, check);

            except Exception as e:
                bot.reply_to(message, e)
            break


def subject2(message):  # новая тема письма заносится в переменную, предлагается проверка корректности всего письма
    global to_subject
    while a == 0:
        if message.text == '/stop':  # возможность остановить процесс и откатиться к функции hello
            try:
                os.remove(src_holy)
                bot.send_message(message.from_user.id, 'Ваше обращение отменено. Выберите:')
                bot.send_message(message.from_user.id, '/start - написать новое обращение\n'
                                                       '/info - подробная информация по службам поддержки')
                bot.register_next_step_handler(message, hello);
            except:

                bot.send_message(message.from_user.id, 'Ваше обращение отменено. Выберите:')
                bot.send_message(message.from_user.id, '/start - написать новое обращение\n'
                                                       '/info - подробная информация по службам поддержки')
                bot.register_next_step_handler(message, hello);
            break
        else:
            to_subject = str(message.text)

            bot.send_message(message.from_user.id,
                             '*Проверьте данные письма:*\n\n*От кого:* {email_from}\n*Кому:* {to_email}\n*Тема:* {to_subject}\n'
                             '*Текст:* {to_text}'.format(email_from=email_from, to_email=to_email,
                                                         to_subject=to_subject, to_text=to_text),
                             parse_mode='Markdown')
            try:
                img = open(src_holy, 'rb')
                bot.send_message(message.from_user.id, '*Прикрепленная фотография:*', parse_mode='Markdown')
                bot.send_photo(message.chat.id, img)
            except:
                bot.send_message(message.from_user.id, '*Прикрепленная фотография отсутствует*', parse_mode='Markdown')

            bot.send_message(message.from_user.id, '_Чтобы полностью отменить отправку этого письма,\n'
                                                   'наберите /stop_', parse_mode='Markdown')

            keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
            button1 = types.KeyboardButton('Да')
            button2 = types.KeyboardButton('Нет')
            keyboard.add(button1, button2)
            bot.send_message(message.from_user.id, 'Всё верно?', reply_markup=keyboard)

            bot.register_next_step_handler(message, check);
            break


def text2(message):  # новый текст письма заносится в переменную, предлагается проверка корректности всего письма
    global to_text
    while a == 0:
        if message.text == '/stop':  # возможность остановить процесс и откатиться к функции hello
            try:
                os.remove(src_holy)
                bot.send_message(message.from_user.id, 'Ваше обращение отменено. Выберите:')
                bot.send_message(message.from_user.id, '/start - написать новое обращение\n'
                                                       '/info - подробная информация по службам поддержки')
                bot.register_next_step_handler(message, hello);
            except:

                bot.send_message(message.from_user.id, 'Ваше обращение отменено. Выберите:')
                bot.send_message(message.from_user.id, '/start - написать новое обращение\n'
                                                       '/info - подробная информация по службам поддержки')
                bot.register_next_step_handler(message, hello);
            break
        else:
            to_text = str(message.text)

            bot.send_message(message.from_user.id,
                             '*Проверьте данные письма:*\n\n*От кого:* {email_from}\n*Кому:* {to_email}\n*Тема:* {to_subject}\n'
                             '*Текст:* {to_text}'.format(email_from=email_from, to_email=to_email,
                                                         to_subject=to_subject, to_text=to_text),
                             parse_mode='Markdown')
            try:
                img = open(src_holy, 'rb')
                bot.send_message(message.from_user.id, '*Прикрепленная фотография:*', parse_mode='Markdown')
                bot.send_photo(message.chat.id, img)
            except:
                bot.send_message(message.from_user.id, '*Прикрепленная фотография отсутствует*', parse_mode='Markdown')

            bot.send_message(message.from_user.id, '_Чтобы полностью отменить отправку этого письма,\n'
                                                   'наберите /stop_', parse_mode='Markdown')

            keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
            button1 = types.KeyboardButton('Да')
            button2 = types.KeyboardButton('Нет')
            keyboard.add(button1, button2)
            bot.send_message(message.from_user.id, 'Всё верно?', reply_markup=keyboard)

            bot.register_next_step_handler(message, check);
            break


def writing_to2(
        message):  # новый адрес получателя заносится в переменную, предлагается проверка корректности всего письма
    while a == 0:
        if message.text == '/stop':
            try:
                os.remove(src_holy)
                bot.send_message(message.from_user.id, 'Ваше обращение отменено. Выберите:')
                bot.send_message(message.from_user.id, '/start - написать новое обращение\n'
                                                       '/info - подробная информация по службам поддержки')
                bot.register_next_step_handler(message, hello);
            except:

                bot.send_message(message.from_user.id, 'Ваше обращение отменено. Выберите:')
                bot.send_message(message.from_user.id, '/start - написать новое обращение\n'
                                                       '/info - подробная информация по службам поддержки')
                bot.register_next_step_handler(message, hello);
            break

        if message.text == '/info':
            bot.send_message(message.from_user.id, '*Admins* - _любые вопросы, связанные с IT._\n'
                                                   '\n*Delivery Help* - _оперативные вопросы по доставке заказов (в т.ч. смена порта)._\n'
                                                   '\n*Order Help* - _оперативные вопросы по прохождению заказа через ПСК (сроки изменения, отклонения от стандартных БП)._\n'
                                                   '\n*Cert Help* - _вопросы сертификации продукции (при отсутствии или ненадлежащей информации в реестре сертификатов), консультации по обязательной маркировке (честныйзнак.рф), оформление штрих-кодов (GTIN)._\n'
                                                   '\n*Product Help* - _оперативные вопросы по характеристикам артикулов (цвет по пантону, живые фото товара, информация об упаковке, вопросы по конкретной партии (уточнение материалов отдельных частей предмета, сравнение габаритов предметов, совместное фото нескольких предметов, чтобы проверить сочетаемость цвета, и др.))._\n'
                                                   '\n*Print Help* - _оперативные консультации по срокам и ценам производства и технологические вопросы по КОНКРЕТНЫМ макетам._\n'
                                                   '\n*Test Help* - _вопросы по возможностям нанесения, тестированию артикулов, конструкторам, фото примеров в КТ._\n'
                                                   '\n*Supply Help* - _оперативные вопросы о сроках поставки и приемки на склад (в т.ч. и возвраты)._\n'
                                                   '\n*Return* - _изменения в заказах, поставленных в работу, изменение/разделение заказа, изменение ТЗ, недогруз, снятие заказа с работы, откаты макетов, вопросы по резервам, вопросы компенсации (ФО, бухгалтерия)._\n'
                                                   '\n*Tech Help* - _заявки в техническую службу._\n'
                                                   '\n*Закупка* - _запросы на закупку товаров для внутреннего пользования._',
                             parse_mode='Markdown')

            keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
            button1 = types.KeyboardButton('Admins')
            button2 = types.KeyboardButton('Delivery Help')
            button3 = types.KeyboardButton('Order Help')
            button4 = types.KeyboardButton('Cert Help')
            button5 = types.KeyboardButton('Print Help')
            button6 = types.KeyboardButton('Product Help')
            button7 = types.KeyboardButton('Test Help')
            button8 = types.KeyboardButton('Supply Help')
            button9 = types.KeyboardButton('Return')
            button10 = types.KeyboardButton('Tech Help')
            button11 = types.KeyboardButton('Закупка')
            button12 = types.KeyboardButton('ТЕСТ')
            keyboard.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10,
                         button11, button12)
            bot.send_message(message.from_user.id, 'Выберите, в какую службу Вы хотите написать.',
                             reply_markup=keyboard)

            bot.register_next_step_handler(message, writing_to2);

        if message.text == 'Admins':
            global to_email
            to_email = 'admins@gifts.ru'
            bot.send_message(message.from_user.id,
                             '*Проверьте данные письма:*\n\n*От кого:* {email_from}\n*Кому:* {to_email}\n*Тема:* {to_subject}\n'
                             '*Текст:* {to_text}'.format(email_from=email_from, to_email=to_email,
                                                         to_subject=to_subject, to_text=to_text),
                             parse_mode='Markdown')
            try:
                img = open(src_holy, 'rb')
                bot.send_message(message.from_user.id, '*Прикрепленная фотография:*', parse_mode='Markdown')
                bot.send_photo(message.chat.id, img)
            except:
                bot.send_message(message.from_user.id, '*Прикрепленная фотография отсутствует*', parse_mode='Markdown')

            bot.send_message(message.from_user.id, '_Чтобы полностью отменить отправку этого письма,\n'
                                                   'наберите /stop_', parse_mode='Markdown')

            keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
            button1 = types.KeyboardButton('Да')
            button2 = types.KeyboardButton('Нет')
            keyboard.add(button1, button2)
            bot.send_message(message.from_user.id, 'Всё верно?', reply_markup=keyboard)

            bot.register_next_step_handler(message, check);
            break
        if message.text == 'Delivery Help':
            to_email = 'delivery-help@gifts.ru'
            bot.send_message(message.from_user.id,
                             '*Проверьте данные письма:*\n\n*От кого:* {email_from}\n*Кому:* {to_email}\n*Тема:* {to_subject}\n'
                             '*Текст:* {to_text}'.format(email_from=email_from, to_email=to_email,
                                                         to_subject=to_subject, to_text=to_text),
                             parse_mode='Markdown')
            try:
                img = open(src_holy, 'rb')
                bot.send_message(message.from_user.id, '*Прикрепленная фотография:*', parse_mode='Markdown')
                bot.send_photo(message.chat.id, img)
            except:
                bot.send_message(message.from_user.id, '*Прикрепленная фотография отсутствует*', parse_mode='Markdown')

            bot.send_message(message.from_user.id, '_Чтобы полностью отменить отправку этого письма,\n'
                                                   'наберите /stop_', parse_mode='Markdown')

            keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
            button1 = types.KeyboardButton('Да')
            button2 = types.KeyboardButton('Нет')
            keyboard.add(button1, button2)
            bot.send_message(message.from_user.id, 'Всё верно?', reply_markup=keyboard)

            bot.register_next_step_handler(message, check);
            break
        if message.text == 'Order Help':
            to_email = 'order-help@gifts.ru'
            bot.send_message(message.from_user.id,
                             '*Проверьте данные письма:*\n\n*От кого:* {email_from}\n*Кому:* {to_email}\n*Тема:* {to_subject}\n'
                             '*Текст:* {to_text}'.format(email_from=email_from, to_email=to_email,
                                                         to_subject=to_subject, to_text=to_text),
                             parse_mode='Markdown')
            try:
                img = open(src_holy, 'rb')
                bot.send_message(message.from_user.id, '*Прикрепленная фотография:*', parse_mode='Markdown')
                bot.send_photo(message.chat.id, img)
            except:
                bot.send_message(message.from_user.id, '*Прикрепленная фотография отсутствует*', parse_mode='Markdown')

            bot.send_message(message.from_user.id, '_Чтобы полностью отменить отправку этого письма,\n'
                                                   'наберите /stop_', parse_mode='Markdown')

            keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
            button1 = types.KeyboardButton('Да')
            button2 = types.KeyboardButton('Нет')
            keyboard.add(button1, button2)
            bot.send_message(message.from_user.id, 'Всё верно?', reply_markup=keyboard)

            bot.register_next_step_handler(message, check);
            break
        if message.text == 'Cert Help':
            to_email = 'cert-help@gifts.ru'
            bot.send_message(message.from_user.id,
                             '*Проверьте данные письма:*\n\n*От кого:* {email_from}\n*Кому:* {to_email}\n*Тема:* {to_subject}\n'
                             '*Текст:* {to_text}'.format(email_from=email_from, to_email=to_email,
                                                         to_subject=to_subject, to_text=to_text),
                             parse_mode='Markdown')
            try:
                img = open(src_holy, 'rb')
                bot.send_message(message.from_user.id, '*Прикрепленная фотография:*', parse_mode='Markdown')
                bot.send_photo(message.chat.id, img)
            except:
                bot.send_message(message.from_user.id, '*Прикрепленная фотография отсутствует*', parse_mode='Markdown')

            bot.send_message(message.from_user.id, '_Чтобы полностью отменить отправку этого письма,\n'
                                                   'наберите /stop_', parse_mode='Markdown')

            keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
            button1 = types.KeyboardButton('Да')
            button2 = types.KeyboardButton('Нет')
            keyboard.add(button1, button2)
            bot.send_message(message.from_user.id, 'Всё верно?', reply_markup=keyboard)

            bot.register_next_step_handler(message, check);
            break
        if message.text == 'Print Help':
            to_email = 'print-help@gifts.ru'
            bot.send_message(message.from_user.id,
                             '*Проверьте данные письма:*\n\n*От кого:* {email_from}\n*Кому:* {to_email}\n*Тема:* {to_subject}\n'
                             '*Текст:* {to_text}'.format(email_from=email_from, to_email=to_email,
                                                         to_subject=to_subject, to_text=to_text),
                             parse_mode='Markdown')
            try:
                img = open(src_holy, 'rb')
                bot.send_message(message.from_user.id, '*Прикрепленная фотография:*', parse_mode='Markdown')
                bot.send_photo(message.chat.id, img)
            except:
                bot.send_message(message.from_user.id, '*Прикрепленная фотография отсутствует*', parse_mode='Markdown')

            bot.send_message(message.from_user.id, '_Чтобы полностью отменить отправку этого письма,\n'
                                                   'наберите /stop_', parse_mode='Markdown')

            keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
            button1 = types.KeyboardButton('Да')
            button2 = types.KeyboardButton('Нет')
            keyboard.add(button1, button2)
            bot.send_message(message.from_user.id, 'Всё верно?', reply_markup=keyboard)

            bot.register_next_step_handler(message, check);
            break
        if message.text == 'Product Help':
            to_email = 'product-help@gifts.ru'
            bot.send_message(message.from_user.id,
                             '*Проверьте данные письма:*\n\n*От кого:* {email_from}\n*Кому:* {to_email}\n*Тема:* {to_subject}\n'
                             '*Текст:* {to_text}'.format(email_from=email_from, to_email=to_email,
                                                         to_subject=to_subject, to_text=to_text),
                             parse_mode='Markdown')
            try:
                img = open(src_holy, 'rb')
                bot.send_message(message.from_user.id, '*Прикрепленная фотография:*', parse_mode='Markdown')
                bot.send_photo(message.chat.id, img)
            except:
                bot.send_message(message.from_user.id, '*Прикрепленная фотография отсутствует*', parse_mode='Markdown')

            bot.send_message(message.from_user.id, '_Чтобы полностью отменить отправку этого письма,\n'
                                                   'наберите /stop_', parse_mode='Markdown')

            keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
            button1 = types.KeyboardButton('Да')
            button2 = types.KeyboardButton('Нет')
            keyboard.add(button1, button2)
            bot.send_message(message.from_user.id, 'Всё верно?', reply_markup=keyboard)

            bot.register_next_step_handler(message, check);
            break
        if message.text == 'Test Help':
            to_email = 'test-help@gifts.ru'
            bot.send_message(message.from_user.id,
                             '*Проверьте данные письма:*\n\n*От кого:* {email_from}\n*Кому:* {to_email}\n*Тема:* {to_subject}\n'
                             '*Текст:* {to_text}'.format(email_from=email_from, to_email=to_email,
                                                         to_subject=to_subject, to_text=to_text),
                             parse_mode='Markdown')
            try:
                img = open(src_holy, 'rb')
                bot.send_message(message.from_user.id, '*Прикрепленная фотография:*', parse_mode='Markdown')
                bot.send_photo(message.chat.id, img)
            except:
                bot.send_message(message.from_user.id, '*Прикрепленная фотография отсутствует*', parse_mode='Markdown')

            bot.send_message(message.from_user.id, '_Чтобы полностью отменить отправку этого письма,\n'
                                                   'наберите /stop_', parse_mode='Markdown')

            keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
            button1 = types.KeyboardButton('Да')
            button2 = types.KeyboardButton('Нет')
            keyboard.add(button1, button2)
            bot.send_message(message.from_user.id, 'Всё верно?', reply_markup=keyboard)

            bot.register_next_step_handler(message, check);
            break
        if message.text == 'Supply Help':
            to_email = 'supply-help@gifts.ru'
            bot.send_message(message.from_user.id,
                             '*Проверьте данные письма:*\n\n*От кого:* {email_from}\n*Кому:* {to_email}\n*Тема:* {to_subject}\n'
                             '*Текст:* {to_text}'.format(email_from=email_from, to_email=to_email,
                                                         to_subject=to_subject, to_text=to_text),
                             parse_mode='Markdown')
            try:
                img = open(src_holy, 'rb')
                bot.send_message(message.from_user.id, '*Прикрепленная фотография:*', parse_mode='Markdown')
                bot.send_photo(message.chat.id, img)
            except:
                bot.send_message(message.from_user.id, '*Прикрепленная фотография отсутствует*', parse_mode='Markdown')

            bot.send_message(message.from_user.id, '_Чтобы полностью отменить отправку этого письма,\n'
                                                   'наберите /stop_', parse_mode='Markdown')

            keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
            button1 = types.KeyboardButton('Да')
            button2 = types.KeyboardButton('Нет')
            keyboard.add(button1, button2)
            bot.send_message(message.from_user.id, 'Всё верно?', reply_markup=keyboard)

            bot.register_next_step_handler(message, check);
            break
        if message.text == 'Return':
            to_email = 'return@gifts.ru'
            bot.send_message(message.from_user.id,
                             '*Проверьте данные письма:*\n\n*От кого:* {email_from}\n*Кому:* {to_email}\n*Тема:* {to_subject}\n'
                             '*Текст:* {to_text}'.format(email_from=email_from, to_email=to_email,
                                                         to_subject=to_subject, to_text=to_text),
                             parse_mode='Markdown')
            try:
                img = open(src_holy, 'rb')
                bot.send_message(message.from_user.id, '*Прикрепленная фотография:*', parse_mode='Markdown')
                bot.send_photo(message.chat.id, img)
            except:
                bot.send_message(message.from_user.id, '*Прикрепленная фотография отсутствует*', parse_mode='Markdown')

            bot.send_message(message.from_user.id, '_Чтобы полностью отменить отправку этого письма,\n'
                                                   'наберите /stop_', parse_mode='Markdown')

            keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
            button1 = types.KeyboardButton('Да')
            button2 = types.KeyboardButton('Нет')
            keyboard.add(button1, button2)
            bot.send_message(message.from_user.id, 'Всё верно?', reply_markup=keyboard)

            bot.register_next_step_handler(message, check);
            break
        if message.text == 'Tech Help':
            to_email = 'tech-help@gifts.ru'
            bot.send_message(message.from_user.id,
                             '*Проверьте данные письма:*\n\n*От кого:* {email_from}\n*Кому:* {to_email}\n*Тема:* {to_subject}\n'
                             '*Текст:* {to_text}'.format(email_from=email_from, to_email=to_email,
                                                         to_subject=to_subject, to_text=to_text),
                             parse_mode='Markdown')
            try:
                img = open(src_holy, 'rb')
                bot.send_message(message.from_user.id, '*Прикрепленная фотография:*', parse_mode='Markdown')
                bot.send_photo(message.chat.id, img)
            except:
                bot.send_message(message.from_user.id, '*Прикрепленная фотография отсутствует*', parse_mode='Markdown')

            bot.send_message(message.from_user.id, '_Чтобы полностью отменить отправку этого письма,\n'
                                                   'наберите /stop_', parse_mode='Markdown')

            keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
            button1 = types.KeyboardButton('Да')
            button2 = types.KeyboardButton('Нет')
            keyboard.add(button1, button2)
            bot.send_message(message.from_user.id, 'Всё верно?', reply_markup=keyboard)

            bot.register_next_step_handler(message, check);
            break
        if message.text == 'Закупка':
            to_email = 'zakupka@gifts.ru'
            bot.send_message(message.from_user.id,
                             '*Проверьте данные письма:*\n\n*От кого:* {email_from}\n*Кому:* {to_email}\n*Тема:* {to_subject}\n'
                             '*Текст:* {to_text}'.format(email_from=email_from, to_email=to_email,
                                                         to_subject=to_subject, to_text=to_text),
                             parse_mode='Markdown')
            try:
                img = open(src_holy, 'rb')
                bot.send_message(message.from_user.id, '*Прикрепленная фотография:*', parse_mode='Markdown')
                bot.send_photo(message.chat.id, img)
            except:
                bot.send_message(message.from_user.id, '*Прикрепленная фотография отсутствует*', parse_mode='Markdown')

            bot.send_message(message.from_user.id, '_Чтобы полностью отменить отправку этого письма,\n'
                                                   'наберите /stop_', parse_mode='Markdown')

            keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
            button1 = types.KeyboardButton('Да')
            button2 = types.KeyboardButton('Нет')
            keyboard.add(button1, button2)
            bot.send_message(message.from_user.id, 'Всё верно?', reply_markup=keyboard)

            bot.register_next_step_handler(message, check);
            break
        if message.text == 'ТЕСТ':
            to_email = 'test01@gifts.ru'

            bot.send_message(message.from_user.id,
                             '*Проверьте данные письма:*\n\n*От кого:* {email_from}\n*Кому:* {to_email}\n*Тема:* {to_subject}\n'
                             '*Текст:* {to_text}'.format(email_from=email_from, to_email=to_email,
                                                         to_subject=to_subject, to_text=to_text),
                             parse_mode='Markdown')
            try:
                img = open(src_holy, 'rb')
                bot.send_message(message.from_user.id, '*Прикрепленная фотография:*', parse_mode='Markdown')
                bot.send_photo(message.chat.id, img)
            except:
                bot.send_message(message.from_user.id, '*Прикрепленная фотография отсутствует*', parse_mode='Markdown')

            bot.send_message(message.from_user.id, '_Чтобы полностью отменить отправку этого письма,\n'
                                                   'наберите /stop_', parse_mode='Markdown')

            keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
            button1 = types.KeyboardButton('Да')
            button2 = types.KeyboardButton('Нет')
            keyboard.add(button1, button2)
            bot.send_message(message.from_user.id, 'Всё верно?', reply_markup=keyboard)

            bot.register_next_step_handler(message, check);
            break

        else:
            bot.send_message(message.from_user.id, 'Пожалуйста, выберите канал обращения из кнопок, '
                                                   'представленных ниже. Вызвать кнопки можно кликнув на значок, '
                                                   'отмеченный на фото')
            bot.send_photo(message.from_user.id,
                           'https://sun9-31.userapi.com/impf/V7j-8eMBXI6mmYrrCtA0mqePLSEpf91qmK8SuA/shngMk08RYQ.jpg?size=663x373&quality=95&sign=54b522d735383002795e1bfb3bec42ee&type=album')
            bot.register_next_step_handler(message, writing_to2);
            break


bot.polling(none_stop=True, interval=0)
