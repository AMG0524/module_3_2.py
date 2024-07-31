def send_email(message, recipient, sender="university.help@gmail.com"):
    valid_domains = ('.com', '.ru', '.net')

    def is_valid_email(email):
        return '@' in email and email.endswith(valid_domains)

    if not is_valid_email(sender) or not is_valid_email(recipient):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return

    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
        return
    elif sender == "university.help@gmail.com":
        print("Письмо успешно отправлено с адреса <sender> на адрес <recipient>.")
        return
    else:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес <recipient>.")
        return


send_email('Это сообщение для проверки связи', 'abdul.g@bk.ru')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru',
           sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
