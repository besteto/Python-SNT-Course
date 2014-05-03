#test

import check_param
import split
import reverse
#import main

def testParamChecker():
	test = 0
	if check_param.checkStr("mama"):
		test +=1
	if not check_param.checkStr(123123):
		test +=1

	if test == 2:
		return "check_param: All tests OK"
	else:
		return "check_param: " + str(test) + " from 2 tests is OK"

def testParamSpliter():
	test = 0
	testDict = ['mama', ', ', 'mama']
	if split.splitStr("mama, mama") == testDict:
		test +=1
	if split.splitStr("123") == ["123"]:
		test +=1

	if test == 2:
		return "split: All tests OK"
	else:
		return "split: " + str(test) + " from 2 tests is OK"

def testParamReverser():
	test = 0
	if reverse.reverseStr("mama, mama") == "amam ,amam":
		test +=1
	if reverse.reverseStr("123") == "321":
		test +=1

	if test == 2:
		return "reverse: All tests OK"
	else:
		return "reverse: " + str(test) + " from 2 tests is OK"

print testParamChecker()
print testParamSpliter()
print testParamReverser()