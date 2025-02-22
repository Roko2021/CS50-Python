from plates import is_valid

def main():
    test_min_max_chracters()
    start_with_two_letters()
    test_nummbers_middle()
    test_number_zero()
    test_punctuation()
    # min_max()
    
    
def test_min_max_chracters():
    assert is_valid('AA') == True
    assert is_valid('ABCDEF') == True
    assert is_valid('A') == False
    assert is_valid('ABCDEFGH') == False

def start_with_two_letters():
    assert is_valid('AA') == True
    assert is_valid('A2') == False
    assert is_valid('2A') == False
    assert is_valid('22') == False
    
def test_nummbers_middle():
    assert is_valid('AAA222') == True
    assert is_valid('AAA22A') == False
    
def test_number_zero():
    assert is_valid('CS50') == True
    assert is_valid('CS05') == False

def test_punctuation():
    assert is_valid('PI3.14') == False
    assert is_valid('PI3!14') == False
    assert is_valid('PI 14') == False

# def min_max():
    # assert is_valid('QQ') == True
    # assert is_valid('MNHGYH') == True
    # assert is_valid('Q') == True
    # assert is_valid('LKJMNHY') == True
    
if __name__ == '__main__':
    main()