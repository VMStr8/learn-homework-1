"""

Домашнее задание №1

Цикл while: ask_user

* Напишите функцию ask_user(), которая с помощью input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def ask_user():
    question = str(input("Как дела? "))
    while question.lower() != "хорошо":
        question = str(input("Как дела? "))


'''
Более короткий вариант. Не сразу до недо додумался, поэтому выше оставляю первоначальный.

def ask_user_second():
    while str(input('Как дела? ')).lower() != 'хорошо':
        str(input('Как дела? ')).lower()
'''

if __name__ == "__main__":
    ask_user()
