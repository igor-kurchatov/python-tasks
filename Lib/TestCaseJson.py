#################################
# unittest class modified to load settings from json file 
# Desription: If you need to test your method it needs json file to perform test with predefined parameteres(arguments) of the test function 

# Test case file format: 
#{"paramNames": [<argumentName1>,...,<argumentNameN>],                                        #list of argument names 
# "testCases": [{<argument1>: <value1>,...,<argumentN>: <valueN>, "result": <resultValue>},   #list of test scenarios
#               ...
#               {<scenarioN>}
#		      ]
#}

#Sample json test file
#{"paramNames": ["weekday", "vacation"], 
# "testCases": [{"weekday": false, "vacation": false, "result": true},
#               {"weekday": true, "vacation": false, "result": false}
#		      ]
#}


# Author : Igor Kurchatov 8/12/2016
#################################

import unittest
import json

from enum import Enum

#Enum to list possible assertion methods
class AssertMethods(Enum):
    assertEqual = 1
    assertTrue = 2
    #to be continued...

class TestCaseJson(unittest.TestCase):
    
    """Testcase class from json file"""

    _failed = "Failed" 
    _succeed = "Succeed"
    _paramNames = "paramNames"
    _testCases = "testCases"
    _defaultTest = "defaultTest"
    _result = "result"
    
    def __choose_assert_func__(self, assertIndex, func, result, *args):
        
        if assertIndex == AssertMethods.assertEqual:
           self.assertEqual(func(*args), result)
        elif assertIndex == AssertMethods.assertTrue:
            res = func(*args)
            self.assertTrue(res)
        else:
            pass                        
    
    def __loadjson__(self):
        
        if self.fileName == "":
            return

        #loading json from file
        try:
            f_data = open(self.fileName).read()
        except FileNotFoundError as e:
            print("Test case file is not found. " + str(e))
            return

        #getting json object from string
        self.jsonData = json.loads(f_data);
        
        #storing in self
        self.paramNames = self.jsonData[self._paramNames]
        self.testCases = self.jsonData[self._testCases]
    
    #test initialization
    def __init__(self, *args, **kwargs):     
        super(TestCaseJson, self).__init__(*args, **kwargs)

        self.userFunc = None
        self.userFuncName = ""
        self.testName = ""
        self.fileName = ""
        self.assertMethod = None
        self.jsonData = None
        self.paramNames = None
        self.testCases = None
    
    #test start
    def __runTest__(self):
        args = []               #arguments
        res = None              #result
        strParams = ""          #arguments string 
        currTestCaseNum = 0     #current test
        failedCount = 0         #count of failed test cases
        
        if self.testCases is None:
            print("Test cases is not found.")
            return

        #test case count info
        print("\nTest case {} starts. Number of test cases: {}".format(self.testName, len(self.testCases)))

        if self.userFunc is None:
            print("User function is not defined. Test can't be completed.")
            return
        
        #test cases loop
        for v in self.testCases:
           
            currTestCaseNum += 1
            
            #clear the list of arguments
            args.clear()
           
            #arguments
            for p in self.paramNames:
                args.append(v[p])                  
            
            #the result
            res = v[self._result]
            
            #convert arguments to string using mapping       
            strParams = ','.join(map(str, args))            
            try:                
                
                #test case brief info
                print("{}. Performing {}({}) => {}".format(currTestCaseNum, self.userFuncName, strParams, res))
                
                #running the test
                self.__choose_assert_func__(self.assertMethod, self.userFunc, res, *args)
                                            
            except AssertionError as e:
                #in case of exception just print the formatted text
                print("Status: " + self._failed + ". " + str(e))
                failedCount += 1
            else:
                #in case of success just print the formatted text
                print("Status: " + self._succeed)
        
        #test case finishes
        if failedCount == 0:
            print("Test case completed successfully.")
        else:
            print("Test case failed. {} failure(s) occured.".format(failedCount))     
    
    def setUp(self):
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()                

    def Start(self, testName = _defaultTest, fileName = "", userFunc = None, assertMethod = AssertMethods.assertEqual):
        
        #settings
        self.userFunc = userFunc
        if self.userFunc is not None:             
            self.userFuncName = self.userFunc.__name__
        self.testName = testName
        self.fileName = fileName
        self.assertMethod = assertMethod
        self.jsonData = None
        self.paramNames = None
        self.testCases = None

        #read arguments from json
        self.__loadjson__()

        #test case implementation
        case = unittest.FunctionTestCase(self.__runTest__, self.setUp, self.tearDown)
                
        #suite = unittest.TestLoader().loadTestsFromName(TestCaseJson.__runTest__, TestCaseJson)
        caseResult = unittest.TextTestRunner(verbosity=2).run(case)
