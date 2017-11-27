from idNumber import isFormatValid

def test_isFormatValid_succes():
    num = "736028/5163"
    assert isFormatValid(num) == True 

def test_isFormatValid_fail():
    num = "73602//5163"
    assert isFormatValid(num) == False