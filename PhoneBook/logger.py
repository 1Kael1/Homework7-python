from datetime import datetime


def Log(message):
    time = datetime.now().strftime('%D %H:%M:%S')
    with open('PhoneBook\log.txt', 'a', encoding="UTF-8") as file:
        file.write(f'{time} - {message}\n')