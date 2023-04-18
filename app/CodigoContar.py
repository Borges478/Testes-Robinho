
class TrocoNotas:
    def troco(custo, pago):
        calculo = pago - custo
        notas = [20, 10, 5, 2, 1]
        resultado = []
        for nota in notas:
            qtd_notas = calculo // nota
            if qtd_notas > 0:
                resultado.append((nota, qtd_notas))
                calculo -= qtd_notas * nota
            if calculo == 0:
                break
        return resultado


custo = 75
pago = 100
resultado = TrocoNotas.troco(custo, pago)

if not resultado:
    print("Gastou tudo, pode ir embora")
else:
    print(resultado)