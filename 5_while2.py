"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например: 
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user_dict() которая с помощью input() просит 
  пользователя ввести вопрос, а затем, если вопрос есть в словаре, 
  программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""


def ask_user():
    dict_1 = {"как дела": "Хорошо!", "что делаешь?": "Программирую"}
    while True:
        question = str(input("Введите ваш запрос: ")).lower()
        if question in dict_1:
            print(dict_1[question])
        else:
            print("Я не знаю, что тебе ответить на это. Задай вопрос еще раз")


if __name__ == "__main__":
    ask_user()
