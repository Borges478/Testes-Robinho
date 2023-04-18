from app.CodigoContar import TrocoNotas


def test_Troco():
    assert TrocoNotas.troco(75,100) == [(20, 1), (5, 1)]

