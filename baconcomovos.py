"""
1 - receber um numero inteiro
2 - saber se o numero e multiplo de 3 e 5:
    bacon com ovos
3 - saber se o numero e multiplo somente de 3:
    bacon
4 - saber se o numero e multiplo somento de 5:
    ovos
5 - saber se o numero NÃO e mutiplo de 3 e 5:
    passa fome
"""
def bacon_com_ovos(n):
    assert isinstance(n,(int)),"n deve ser int"

    if n % 3 == 0 and n % 5 == 0:
        return "Bacon com ovos"
    
    if n % 3 == 0:
        return "Bacon"
    if n % 5 == 0:
        return "ovos"
    return "Passar fome"