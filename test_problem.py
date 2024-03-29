import utils
import pytest
from math import floor, sqrt
from utils import is_prime

def test_squaring():
    """
    Positive Case: Возведение в квадрат
    """
    a = 16
    assert a*a == 256

def test_len_integer_type():
    """
    Negative Case:
    Проваливающийся тест. 
    Получение кол-ва элементов для целочисленного типа данных
    """
    with pytest.raises(TypeError):
        len(5)

@pytest.mark.parametrize("num, result",
                         [(-1, False),
                          (0, False),
                          (2, True),
                          (7, True)])
def test_is_prime(num, result):
    """
    Parametrize Case:
    Параметризированный тест: проверка на простоту
    """
    assert is_prime(num) == result




def test_concatenate_dictionary():
    """
    Positive Case:
    Конкатенация словарей
    """
    dict1 = {'a': 1, 'b': 2} 
    dict2 = {'c': 3, 'd': 2}
    dict3 = dict1.copy()
    dict3.update(dict2)
    assert  dict3 == {'a': 1, 'b': 2, 'c': 3, 'd': 2}



def test_on_key_error():
    """
    Negative case:
    Проваливающийся тест.
    Получение значения по несуществующему индексу
    """
    some_dict = {'a': 1, 'b': 2}
    with pytest.raises(KeyError):
        some_dict['z']


@pytest.mark.parametrize("text, result",
                         [('Python', {'P': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1}),
                          ('TttaA', {'T': 1, 't': 2, 'a': 1, 'A': 1}),
                          ('Visual Studio Code', {'V': 1, 'i': 2, 's': 1, 'u': 2, 'a': 1, 'l': 1, ' ': 2, 
                          'S': 1, 't': 1, 'd': 2, 'o': 2, 'C': 1, 'e': 1})])
def test_count_of_entry(text, result):
    """
    Parametrize case:
    Подсчёт вхождений символа в строку
    """
    assert {i: text.count(i) for i in text} == result
