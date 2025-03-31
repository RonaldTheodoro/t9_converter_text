import pytest

from t9_converter import t9_converter


@pytest.mark.parametrize(
    "text,expected",
    [
        ("faca", "33322222"),
        ("carro", "2222777777666"),
        ("tijolao", "844456665552666"),
        ("carro do ovo", "2222777777666036660666888666"),
        ("cão com ração", "222266602226666077722222666"),
    ]
)
def test_t9_converter(text, expected):
    assert t9_converter(text) == expected