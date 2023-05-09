from collections import namedtuple
import pytest

Dinner = namedtuple('Dinner', ['food', 'cook', 'ready', 'id'])
Dinner.__new__.__defaults__ = (None, None, False, None)


@pytest.mark.skip(reason='fui un test skipeado, pero debemos poner la razon del porque')
@pytest.mark.back
@pytest.mark.ejecutar
def test_defaults():
    t1 = Dinner()
    t2_expected = Dinner(None, None, False, None)
    assert t1 == t2_expected



@pytest.mark.back
@pytest.mark.ejecutar
@pytest.mark.xfail(reason='falla porque necesitamos probar el xFail()')
def test_num_access():
    t = Dinner('Fritas', 'Marto')
    assert t.food == 'Fritas'
    assert t.cook == 'Marto'
    assert (t.ready, t.id) == (False, None)
