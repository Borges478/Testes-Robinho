from app.CodigoFuncao import Bhaskara


def test_Funcao():
   assert Bhaskara.valores(1, 12, -13) == [196, 1.0, -13.0]
