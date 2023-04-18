
class Palavras:
    def contagem_palavras(palavras, palavra_alvo):
        lista_palavras = palavras.split()
        indices = []
        for alvo, palavra in enumerate(lista_palavras):
            if palavra == palavra_alvo:
                indices.append(alvo)
        if not indices:
            return None
        return indices

palavras = "Hoje é um belo dia para fazer prova, melhor ainda se eu tirasse um total"
palavra_alvo = "um"
posicao = Palavras.contagem_palavras(palavras, palavra_alvo)

if posicao is not None:
    print(f'A palavra "{palavra_alvo}" aparece na(s) posição(ções) {posicao} da frase.')
else:
    print(f'Erro, "{palavra_alvo}" não está na frase.')