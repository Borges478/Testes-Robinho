import cmath

class Bhaskara:
    def valores(a, b, c):
        if a == 0:
            print('O valor de "a" não pode ser igual a zero. :(')
            return
        else:
            resultado = (b**2) - (4*a*c)
            print(f'Valor de delta: {resultado}\n')
     
            if resultado < 0:
                print("As raízes são complexas. :( \n")
            else:
                x1 = (-b + cmath.sqrt(resultado)) / (2*a)
                x2 = (-b - cmath.sqrt(resultado)) / (2*a)
                print(f"As raízes são: {x1.real:.0f} e {x2.real:.0f} :)")
               
                if resultado == 0:
                    print(f"A única raiz é: {x1.real:.0f} :)")
 
Bhaskara.valores(1, 12, -13)


