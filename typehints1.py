from typing import List,Union,Tuple,Dict,Any,NewType,Callable,Sequence,Iterable

#sequencias
lista: List[int] = [1,2,3]
lista_str_int:List[Union[int,str]] = [1,2,3,"luiz"]
tupla:Tuple[int,int,int] = (1,2,3)

#dicionario e conjuntos
meuDict = Dict[str,Union[str,int,list[int]]] #alias

pessoa:Dict[str,Union[str,int]] = {"nome":"lucas","idade":30}
pessoa2:meuDict = {"nome":"lucas","idade":30}

#meu outro tipo
UserId = NewType("UserId",int)
user_id = UserId(323242)

def retorna_funcao(funcao: Callable[[int, int], int]) -> Callable:
    return funcao


def soma(x: int, y: int) -> int:
    return x + y


print(retorna_funcao(soma)(10, 20))


class Pessoa:
    def __init__(self, nome: str, sobrenome: str, idade: int) -> None:
        self.nome: str = nome
        self.sobrenome: str = sobrenome
        self.idade: int = idade

    def fala(self) -> None:
        print(f'{self.nome} {self.sobrenome} está falando...')


def iterar(sequencia: Sequence[int]):
    return [x for x in sequencia]


def iterar2(sequencia: Iterable[int]):
    return [x for x in sequencia]


print(iterar([1, 2, 3]))
print(iterar((1, 2, 3)))
print(iterar2([1, 2, 3]))
print(iterar2((1, 2, 3)))

