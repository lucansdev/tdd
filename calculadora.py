def soma(x,y):
    """ soma x e y

    >>> soma(10,20)
    30

    >>> soma(20,30)
    50
    
    """
    assert isinstance(x,(int,float)),"x precisa ser int ou float"
    assert isinstance(y,(int,float)),"y precisa ser int ou float"
    return x + y

def subtrai(x,y):
    """subtrai x e y

    >>> subtrai(5,10)
    -5

    >>> subtrai(10,5)
    5
    """
    assert isinstance(x,(int,float)),"x precisa ser int ou float"
    assert isinstance(y,(int,float)),"y precisa ser int ou float"
    return x - y

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

