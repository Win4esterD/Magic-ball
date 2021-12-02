import random

def main_func():
    def Russian_func():
        answers = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом',
                   'Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да',
                   'Пока неясно, попробуй позже', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать',
                   'Сконцентрируйся и спроси опять', 'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет',
                   'Перспективы не очень хорошие', 'Весьма сомнительно']
        print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')

        print('Как тебя зовут?')
        name = input()

        while True:
            print('Введите свой вопрос')
            question = input()
            print(random.choice(answers))
            print('Хотите задать ещё вопрос?')
            answer = input()
            if answer.lower() == 'да':
                continue
            else:
                break
        pass

    def English_func():
        answers = ['Indisputably', 'Sure wil be', 'No doubts', 'Definetely yes', 'You can be sure about it',
                   'I think, yes', 'Possibly yes', 'Good perspectives', 'Signs are saying "yes"', 'Yes',
                   'It\'s not clear yet, try later', 'Ask later', 'It\s better not to tell',
                   'Now it\'s impossible to predict ',
                   'Concentrate and ask again', 'Don\'t even think about it',
                   'My answer is - no', 'According to my data - no',
                   'The perspectives are not very good', 'Doubtable']
        print('Hello world, I\'m a magic ball, I know the answer for your question.')

        print('What is your name?')
        name = input()

        while True:
            print('Type your question')
            question = input()
            print(random.choice(answers))
            print('Do you want to ask another question?')
            answer = input()
            if answer.lower() == 'yes':
                continue
            else:
                break
        pass

    def Spanish_func():
        answers = ['Indiscutiblemente', 'Seguro que lo será', 'Sin dudas', 'Definitivamente si',
         'Puedes estar seguro por eso',
                   'Creo que si', 'Posiblemente si', 'Buenas perspectivas', 'Las señales dicen "sí"', 'Si',
                   'Aún no está claro, inténtalo otra vez', 'Preguntalo después', 'Es mejor no decir',
                   'Ahora es imposible a predecir ',
                   'Concéntrate y pregunta otra vez', 'Ni lo pienses',
                   'Mi respuesta es - no', 'Según mis datos - no',
                   'Las perspectivas no son muy buenas', 'Dudoso']
        print('Hola, Soy una bola magica, yo sé respuesta por tu pregunta.')

        print('¿Como te llamas?')
        name = input()

        while True:
            print('Escriba tu pregunta')
            question = input()
            print(random.choice(answers))
            print('¿Quieres hacer otra pregunta?')
            answer = input()
            if answer.lower() == 'si':
                continue
            else:
                break
        pass
    print("Type '1' to sellect English language.")
    print("Haga clic en '2' para seleccionar el idioma Español.")
    print("Нажмите '3' чтобы выбрать Русский язык.")
    langnum = int(input())
    while langnum < 1 or langnum > 3:
        print("Number is incorrect, try again.")
        print("El numero no es correcto. Intente de nuevo.")
        print("Номер не правильный, попробуйте ещё раз.")
        langnum = int(input())
    if langnum == 1:
        English_func()
    elif langnum == 2:
        Spanish_func()
    else:
        Russian_func()


main_func()
