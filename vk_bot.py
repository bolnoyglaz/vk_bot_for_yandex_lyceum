import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import math
import random

TOKEN = 'e929992980fe6a2763bd91ad905343c3bef2640de0793df273ccef5429f3a9426d0d04aa90525b0595a67'
hi_words = ['Рад Вас видеть!', 'Приветствую!', 'Привет!', 'Здравствуйте!']
nez = ['Не за что!', 'Всегда пожалуйста!', 'Пожалуйста!']
stat_formula = "menu"


def isint(list):
    count = 0
    error = 0
    for elem in list:
        try:
            if float(elem) or int(elem):
                count += 1
        except ValueError:
            error = True
    if error:
        return False
    else:
        return True


def main():
    vk_session = vk_api.VkApi(
        token=TOKEN)

    longpoll = VkBotLongPoll(vk_session, 203095435)
    stat_formula = None
    for event in longpoll.listen():
        try:
            if event.type == VkBotEventType.MESSAGE_NEW:
                print("------------------------------------------------------------------")
                print('Новое сообщение:')
                if event.obj.message['from_id'] == 287541888:
                    print('Для бота от: Создатель')
                else:
                    print('Для бота от:', event.obj.message['from_id'])
                print('Текст:', event.obj.message['text'])
                vk = vk_session.get_api()
                if 'начать' in event.obj.message['text'].lower() or 'назад' in event.obj.message['text'].lower():
                    if 'назад' in event.obj.message['text'].lower():
                        stat_formula = 'menu'
                    if 'начать' in event.obj.message['text'].lower():
                        vk.messages.send(user_id=event.obj.message['from_id'],
                                         message=f'👋 {random.choice(hi_words)}',
                                         random_id=random.randint(0, 2 ** 64))
                        vk.messages.send(user_id=event.obj.message['from_id'],
                                         message='🤖💬 Вы попали к чат-боту по проекту \"Чернильное дерево\".',
                                         random_id=random.randint(0, 2 ** 64))
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message='✏ Напишите \"Пуассон\", чтобы воспользоваться формулой Пуассона',
                                     random_id=random.randint(0, 2 ** 64))
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message='✏ Напишите \"Муавр\", чтобы воспользоваться формулой Муавра',
                                     random_id=random.randint(0, 2 ** 64))
                elif "привет" in event.obj.message['text'].lower():
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message=f'👋 {random.choice(hi_words)}',
                                     random_id=random.randint(0, 2 ** 64))
                elif "ку" in event.obj.message['text'].lower():
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message=f'👋 {random.choice(hi_words)}',
                                     random_id=random.randint(0, 2 ** 64))
                elif "спасибо" in event.obj.message['text'].lower() or "спс" in event.obj.message['text'].lower():
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message=f'👍 {random.choice(nez)} Я рад Вам помочь.',
                                     random_id=random.randint(0, 2 ** 64))
                elif "назад" in event.obj.message['text'].lower():
                    stat_formula = None
                elif 'пуассон' in event.obj.message['text'].lower() or 'муавр' in event.obj.message['text'].lower():
                    if 'пуассон' in event.obj.message['text'].lower():
                        stat_formula = 'пуассон'
                    else:
                        stat_formula = 'муавр'
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message='🧮 Чтобы подсчитать по формуле мне нужно от Вас три значения:',
                                     random_id=random.randint(0, 2 ** 64))
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message='1️⃣ n - общее число выборки',
                                     random_id=random.randint(0, 2 ** 64))
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message='2️⃣ p - данная вероятность наступления события '
                                             '(например 0.2, то есть с точкой)',
                                     random_id=random.randint(0, 2 ** 64))
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message='3️⃣ m - количество данных событий.',
                                     random_id=random.randint(0, 2 ** 64))
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message='# формат ввода: \"n p m\".',
                                     random_id=random.randint(0, 2 ** 64))
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message='Чтобы перейти обратно в меню, напишите \"Назад\".',
                                     random_id=random.randint(0, 2 ** 64))
                elif (len(event.obj.message['text'].split()) == 3 and isint(event.obj.message['text'].split())) \
                        and stat_formula == 'пуассон':
                    n = list()
                    for elem in event.obj.message['text'].split():
                        n.append(float(elem))
                    e = 2.7
                    P = (((n[0] * n[1]) ** n[2]) * (e ** (- (n[0] * n[1])))) / math.factorial(n[2])
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message='✅ Результат по формуле Пуассона:',
                                     random_id=random.randint(0, 2 ** 64))
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message=P,
                                     random_id=random.randint(0, 2 ** 64))
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message='Чтобы перейти обратно в меню, напишите \"Назад\".',
                                     random_id=random.randint(0, 2 ** 64))

                elif (len(event.obj.message['text'].split()) == 3 and isint(event.obj.message['text'].split())) \
                        and stat_formula == 'муавр':
                    n = list()
                    for elem in event.obj.message['text'].split():
                        n.append(float(elem))
                    e = 2.7
                    n1 = n[0]
                    p = n[1]
                    m = n[2]
                    q = 1 - p
                    x = (m - n1 * p) / math.sqrt(n1 * p * q)
                    P = (1 / math.sqrt(n1 * p * q)) * (1 / math.sqrt(2 * 3.14)) * (e ** ((-x ** 2) / 2))
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message='✅ Результат по формуле Муавра:',
                                     random_id=random.randint(0, 2 ** 64))
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message=P,
                                     random_id=random.randint(0, 2 ** 64))
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message='Чтобы перейти обратно в меню, напишите \"Назад\".',
                                     random_id=random.randint(0, 2 ** 64))
                else:
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message='🚫 Я Вас не понимаю... Возможно Вы ошиблись.',
                                     random_id=random.randint(0, 2 ** 64))
        except OverflowError:
            print("------------------------------------------------------------------")
            print('Произошла ошибка OverflowError')
            vk.messages.send(user_id=event.obj.message['from_id'],
                             message='⚠ Ошибка. Слишком большое число.',
                             random_id=random.randint(0, 2 ** 64))


if __name__ == '__main__':
    main()
