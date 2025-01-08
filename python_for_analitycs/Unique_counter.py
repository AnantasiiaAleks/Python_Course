'''
Вам дан список покупок, где каждый элемент — это название продукта.
Напишите функцию unique_products_count, которая возвращает
количество уникальных продуктов в списке.
Пример:
products = ['apple', 'banana', 'apple', 'orange', 'banana', 'grape']
print(unique_products_count(products))
На выходе: 4
'''

def unique_products_count(products: list) -> int:
    """
    возвращает колдичество уникальных записей в списке
    :param products: список
    :return: число уникальных

    >>> print(unique_products_count(['apple', 'banana', 'apple', 'orange', 'banana', 'grape']))
    4
    """
    return len(set(products))

if __name__ == '__main__':
    products = ['apple', 'banana', 'apple', 'orange', 'banana', 'grape']
    print(unique_products_count(products))