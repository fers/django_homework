from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:


def get_reciept(request, dish):

    # получаем рецепт конкретного блюда из словаря по параметру переденному через URL
    dish_description = DATA[dish]

    # получаем количество порций из параметра запроса
    servings = int(request.GET.get('servings', 1))

    # пересчитываем сколько в итоге на все блюдо нам понадобится инградиентов
    for x in dish_description:
        dish_description[x] = dish_description[x] * servings

    # заполняем контекст нпересчитанным словарем
    context = {
        'recipe': dish_description
    }
    return render(request, 'calculator/index.html', context)
