
import check_param
import split
import reverse

def testChecker():
	 return str(check_param.checkStr("mama") and 
	 	    not check_param.checkStr(123123))


def testSpliter():
	return str((split.splitStr("mama, mama") == ['mama', ', ', 'mama']) and 
			   (split.splitStr("123") == ["123"]))

def testReverser():
	return str((reverse.reverseStr("mama, mama") == "amam ,amam") and
			   (reverse.reverseStr("123") == "321"))

print ("cheker   : " + testChecker())
print ("splitter : " + testSpliter())
print ("reverser : " + testReverser())