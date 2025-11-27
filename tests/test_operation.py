from src.math_operations import add,sub
def test_add():
    assert add(2,3)==5
    assert add(10,-2)==8

def test_sub():
    assert sub(3,3)==0
    assert sub(4,3)==1
    assert sub(10,5)==5