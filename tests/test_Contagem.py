from app.CodigoPalavras import Palavras

def test_contagem():
    assert Palavras.contagem_palavras("Hoje é um belo dia para fazer prova, melhor ainda se eu tirasse um total","um") == [2, 13]
