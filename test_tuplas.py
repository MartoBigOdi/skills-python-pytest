from collections import namedtuple
import pytest

Dinner = namedtuple('Dinner', ['food', 'cook', 'ready', 'id'])
Dinner.__new__.__defaults__ = (None, None, False, None)

@pytest.mark.ejecutar
def test_defaults():
    t1 = Dinner()
    t2_expected = Dinner(None, None, False, None)
    assert t1 == t2_expected

@pytest.mark.ejecutar
def test_num_access():
    t = Dinner('Fritas', 'Marto')
    assert t.food == 'Fritas'
    assert t.cook == 'Marto'
    assert (t.ready, t.id) == (False, None)

