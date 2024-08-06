# module_11_3.py

# Домашнее задание по теме "Интроспекция"

# Необходимо создать функцию, которая принимает объект (любого типа) в качестве аргумента и проводит интроспекцию
# этого объекта, чтобы определить его тип, атрибуты, методы, модуль, и другие свойства.

# Создайте функцию introspection_info(obj), которая принимает объект obj.
def introspection_info(obj):
    # Верните словарь или строки с данными об объекте, включающий следующую информацию:
    info = {
        #    - Тип объекта.
        'type': type(obj).__name__,
        #    - Атрибуты объекта.
        'attributes': [],
        #    - Методы объекта.
        'methods': [],
        #    - Модуль, к которому объект принадлежит.
        # Функция hasattr() возвращает флаг, указывающий на то, содержит ли объект obj атрибут __module__.
        'module': obj.__module__ if hasattr(obj, '__module__') else None,
    }

    # Получаем список всех атрибутов объекта
    attributes = dir(obj)
    # print(attributes)

    # Для атрибута из списка всех атрибутов:
    for attribute in attributes:

        # Выбираем не служебные методы и атрибуты
        # if not attribute.startswith('__'):
        # Функция getattr() возвращает значение атрибута attr_value объекта obj по имени attribute.
        attr_value = getattr(obj, attribute)
        # print(attr_value)
        # Проверяем, если можно ли вызвать объект attr_value.
        if callable(attr_value):
            # Добавляем в конец списка методов элемент, переданный в качестве аргумента attribute.
            info['methods'].append(attribute)
        else:
            # Иначе, добавляем аргумент attribute в конец списка атрибутов.
            info['attributes'].append(attribute)

    # Добавляем строковое представление объекта, если доступно
    # info['str'] = str(obj) if hasattr(obj, '__str__') else None

    # Добавляем длину объекта, если он имеет длину
    # if hasattr(obj, '__len__'):
        # info['length'] = len(obj)

    # Возврат данных об объекте
    return info


# Рекомендуется создавать свой класс и объект для лучшего понимания
class MyClass:
    def __init__(self, value):
        self.value = value

    def my_method(self):
        return self.value


if __name__ == '__main__':
    # my_instance = MyClass(42)
    # object_info = introspection_info(my_instance)
    # print(object_info)
    # print(my_instance.__doc__)
    # print(my_instance.__dict__)
    # print(my_instance.__module__)
    # print(my_instance.__weakref__)
    # print(my_instance.__class__)
    # print(my_instance.__delattr__)
    # print(my_instance.__dir__)
    # print(my_instance.__eq__)
    # print(my_instance.__format__)
    # print(my_instance.__ge__)
    # print(my_instance.__getattribute__)
    # print(my_instance.__getstate__)
    # print(my_instance.__gt__)
    # print(my_instance.__hash__)
    # print(my_instance.__init__)
    # print(my_instance.__init_subclass__)
    # print(my_instance.__le__)
    # print(my_instance.__lt__)
    # print(my_instance.__ne__)
    # print(my_instance.__new__)
    # print(my_instance.__reduce__)
    # print(my_instance.__reduce_ex__)
    # print(my_instance.__repr__)
    # print(my_instance.__setattr__)
    # print(my_instance.__sizeof__)
    # print(my_instance.__str__)
    # print(my_instance.__subclasshook__)
    # print(my_instance.my_method)

    # Пример работы:
    number_info = introspection_info(42)
    print(number_info)

    # Вывод на консоль:
    # {'type': 'int', 'attributes': ['__abs__', '__add__', ...], 'methods': [], 'module': '__main__'}
