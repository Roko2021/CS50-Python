from numb3rs import validate

def main():
    test_format()
    test_range()
    
def test_format():
    assert validate(r'1.2.3.4') == True
    assert validate(r'1.2.3') == False
    assert validate(r'1.2') == False
    assert validate(r'1') == False
    
    
def test_range():
    assert validate(r'255.255.255.255') == True
    assert validate(r'255.258.257.256') == False
    assert validate(r'255.260.270.280') == False
    
    
    
if __name__ == '__main__':
    main()