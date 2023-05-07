from collections import namedtuple

Dinner = namedtuple('Dinner', ['food', 'cook', 'ready', 'id'])
Dinner.__new__.__defaults__ = (None, None, False, None)

def test_asdict():
    t_Dinner = Dinner('Fritas', 'Guada', True, 35)
    # con ._asdict() creamos un dict a partir de una tupla
    t_dict = t_Dinner._asdict()
    expectedDict = {'food':'Fritas',
                    'cook':'Guada',
                    'ready': True,
                    'id': 35}
    assert t_dict == expectedDict


def test_replace():
     t_before = Dinner('carne', 'Marto', False)
     # modificamos la tupla con el ._replace(key=value, key=value) ejemplo
     t_after = t_before._replace(id=40, ready=True)
     t_expected = Dinner('carne', 'Marto', True, 40)
     assert t_after == t_expected
