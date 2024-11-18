from bank import value

def main():
    test_value()

def test_value():
    assert value('hello gi') == 0
    assert value('Hello') == 0
    assert value('HelloGi') == 0
    assert value ('Hi') == 20
    assert value ('hey') == 20
    assert value ('wellcome') == 100
    
    
if __name__ == '__main__':
    main()