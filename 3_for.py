"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""


def main():
    scores = [{'school_class': '4a', 'scores': [3, 4, 5, 4, 4, 2]},
              {'school_class': '5a', 'scores': [4, 5, 5, 5, 3, 5]},
              {'school_class': '6a', 'scores': [4, 4, 5, 4, 4, 3]}]

    for i in scores:
        class_middle = sum(i['scores']) / len(i['scores'])
        print(f'Средний балл по классу {i["school_class"]}: {class_middle}')

    school_middle = sum([sum(i['scores']) / len(i['scores']) for i in scores]) / len([i['scores'] for i in scores])
    print(f'Средний балл по школе: {school_middle}')


if __name__ == "__main__":
    main()
