from twttr import shorten

def main():
    test_upper()
    test_nummber()
    test_anther()
    
    
def test_upper():
    assert shorten("twitter") == 'twttr'
    assert shorten("TWITTER") == 'TWTTR'
    assert shorten("TwitteR") == 'TwttR'
    
def test_nummber():
    assert shorten ('1234') == '1234'
    
def test_anther():
    assert shorten('!@#') == '!@#'
    
    
    
    
    
if __name__ == '__main__':
    main()