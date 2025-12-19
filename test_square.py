from square import get_square

def test_sq():
    x = 3
    res = get_square(x)
    assert res == 9

def test_square_negative():
    x = -4
    res = get_square(x)
    assert res == 16