# Задача "Рассылка писем":
# Проверка на корректность e-mail


def send_email(message, recipient, sender="university.help@gmail.com"):
    a = [".com", ".ru", ".net"]
    #fl = 0

    if "@" not in recipient or "@" not in sender or \
            not any(recipient.endswith(end_r) for end_r in a) or \
            not any(sender.endswith(end_s) for end_s in a):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return

    #if "@" in recipient and "@" in sender:
        #for i in range(len(a)):
            #if a[i] in recipient:
                #for j in range(len(a)):
                    #if a[j] in sender:
                        #fl = 1
        #if fl == 0:
           #print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")

    if recipient == sender:
        print("Нельзя отправить письмо самому себе!")
        return

    if sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')

    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')


send_email('Это сообщение для проверки связи','vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

# Пример выполняемого кода (тесты):
# send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
# send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
# send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
# send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

# Вывод на консоль:
# Письмо успешно отправлено с адреса university.help@gmail.com на адрес vasyok1337@gmail.com
# НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса urban.info@gmail.com на адрес urban.fan@mail.ru
# Невозможно отправить письмо с адреса urban.teacher@mail.uk на адрес urban.student@mail.uk
# Нельзя отправить письмо самому себе!
