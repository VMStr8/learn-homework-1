"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""


def ask_user():
    dict_1 = {"как дела": "Хорошо!", "что делаешь?": "Программирую"}
    while True:
        try:
            question = str(input("Введите ваш запрос: ")).lower()
            if question in dict_1:
                print(dict_1[question])
            else:
                print("Я не знаю, что тебе ответить на это. Задай вопрос еще раз")
        except KeyboardInterrupt:
            print("\nПока!")
            break


if __name__ == "__main__":
    ask_user()
