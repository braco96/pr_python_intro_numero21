import os, io, json, math, re, importlib
import pytest
mod = importlib.import_module('main')


@pytest.mark.parametrize("s,esperado", [
    ("", 0),
    ("1,2,3", 6),
    ("//;1;2;3", 6),
    ("1\n2,3", 6),
])
def test_sumar_cadena(s, esperado):
    assert mod.sumar_cadena(s) == esperado
