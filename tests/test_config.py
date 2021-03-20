import pytest


class NotInRange(Exception):
    def __init(self,message="Values are not in range"):
        self.message = message
        super.__init__(self.message)

def test_generic():
    a = 5
    with pytest.raises(NotInRange):
        if a not in range(4,10):
            raise NotInRange
        
def test_something():
    a = 5
    b = 6
    assert a != b
    
def test_range():
    a = 5
    assert a in range(1,10)
