import pytest
from numerosA import numeros_amigos


def test_1():
    assert numeros_amigos(1,2)=="1 y 2 no son amigos"
    
def test_2():
    assert numeros_amigos(1,3)=="1 y 3 no son amigos"
    
def test_3():
    assert numeros_amigos(3,4)=="3 y 4 son amigos"
    
def test_4():
    assert numeros_amigos(4,5)=="4 y 5 son amigos"  
    
def test_5():
    assert numeros_amigos(7,8)=="7 y 8 no son numeros amigos"  

def test_6():
    assert numeros_amigos(110,121)=="110 y 121 no son amigos"
    
def test_7():
    assert numeros_amigos(1184, 1210)=="1184 y 1210 son amigos"
    
def test_8():
    assert numeros_amigos(2620, 2924)=="2620 y 2924 son amigos"
    
def test_9():
    assert numeros_amigos(17296, 18416)=="17296 y 18416 no son amigos"  
    
def test_10():
    assert numeros_amigos(7,8)=="7 y 8 no son numeros amigos"  
    
    
if  __name__ == '__main__':
    
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()
    test_6()
    test_7()
    test_8()
    test_9()
    test_10()
    