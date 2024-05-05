# Изображение проекции полиэдра

Построение изображения полиэдра с удалением невидимых линий — пример
классической задачи, для успешного решения которой необходимо знакомство
с основами вычислительной геометрии.

![Шахматный король](images/king.png)

## Задание на модификацию

Назовём точку в пространстве «хорошей», если она находится на расстоянии строго меньше 1 
от плоскости x = 2. Модифицируйте эталонный проект таким образом, чтобы определялась и 
печаталась следующая характеристика полиэдра: сумма длин проекций рёбер, оба из концов 
которых — «хорошие» точки.

## Проверка соблюдения соглашений о стиле программного кода

~~~{.sh}
find . -name '*.py' -exec pycodestyle {} \;
~~~

## Проверка покрытия тестами кода программы

~~~{.sh}
python -B -m coverage run -m unittest discover tests && coverage report -m ; rm -f .coverage
~~~
