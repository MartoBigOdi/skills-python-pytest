"""
Manera de indicar un elemento deprecado.
Lo manejamos con Warnings
"""
import warnings
import pytest


def lame_function():
    warnings.warn('Funcion deprecada', DeprecationWarning)


def test_lame_function(recwarn):
    lame_function()
    assert len(recwarn) == 1
    # obtenemos el objeto para w
    w = recwarn.pop()
    assert w.category == DeprecationWarning
    assert str(w.message) == 'Funcion deprecada'


def test_lame_function2():
    with pytest.warns(None) as warnings_list:
        lame_function()
    assert len(warnings_list) == 1
    # obtenemos el objeto para w
    w = warnings_list.pop()
    assert w.category == DeprecationWarning
    assert str(w.message) == 'Funcion deprecada'
