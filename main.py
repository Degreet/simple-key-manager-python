from keys import KeyManager
import secrets
import string
import os

alphabet = string.ascii_letters + string.digits
keyManager = KeyManager()
hasKey = keyManager.hasKey()


def set():
    website = input("Введите адрес сайта >> ")
    
    if not 'https' in website:
        return print("Некорректная ссылка")

    key = ''.join(secrets.choice(alphabet) for i in range(16))
    keyManager.newKey(key, website)

    print(f"Пароль сгенерирован: \"{key}\"")
    actionTransition()

def get():
    website = input("Введите адрес сайта >> ")
    print(f"Ваш пароль: \"{keyManager.getKey(website)}\"")
    actionTransition()

def actionTransition():
    input("Нажмите Enter чтобы продолжить ...")
    action()

def action():
    os.system('cls')
    print("1 - Сгенирировать и сохранить пароль")
    print("2 - Получить пароль")
    print("3 - Выход")

    action = input("Что будем делать? >> ")

    if int(action) == 1:
        set()
    elif int(action) == 2:
        get()
    else:
        quit()

def main():
    key = input("Введите пароль >> ")

    if hasKey:
        checkKey = keyManager.checkKey(key)

        if not checkKey:
            print("Неправильный пароль!")
            main()
        else:
            action()
    else:
        keyManager.saveKey(key)
        print("Пароль успешно сохранен!")
        action()


if __name__ == "__main__":
    main()