#################################
# unittest class modified to load settings from json file 
# Desription: If you need to test your methods it needs json file to perform test within predefined parameteres(arguments) of the test functions 

# Single test case file format: 
# {"testCases": [{<argument1>: <value1>,...,<argumentN>: <valueN>, "result": <resultValue>},   #list of test scenarios
#               ...
#               {<scenarioN>}
#		      ]
# }

# Single sample json test file
# {"testCases": [{"weekday": false, "vacation": false, "result": true},
#               {"weekday": true, "vacation": false, "result": false}
#		      ]
# }

# Multiple test case file format: 
# {"<func_name1>": [{<argument1>: <value1>,...,<argumentN>: <valueN>, "result": <resultValue>},   #list of test scenarios
#                 ...
#                  {<scenarioN>}
#		          ],
#  "<func_nameN>": [...]
# }

# Multiple sample json test file
# {"string_times": [{"str": "Hi", "n": 2, "result": "HiHi"},
# 		            {"str": "Hi", "n": 3, "result": "HiHiHi"},
#				    {"str": "Hi", "n": 1, "result": "Hi"}
#		           ],
# "front_times": [{"str": "Chocolate", "n": 2, "result": "ChoCho"},
#		          {"str": "Chocolate", "n": 3, "result": "ChoChoCho"},
#				  {"str": "Abc", "n": 3, "result": "AbcAbcAbc"}  
#		         ]
# }

# Author : Igor Kurchatov 8/12/2016
#################################

import unittest
import json
import inspect
from collections import OrderedDict

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
    
    def __choose_assert_func__(self, assertIndex, func, result, kwargs):
        
        if assertIndex == AssertMethods.assertEqual:
           self.assertEqual(func(**kwargs), result)
        elif assertIndex == AssertMethods.assertTrue:
            self.assertTrue(func(**kwargs))
        else:
            pass                        
    
    def __loadjson__(self, fileName):
        
        if fileName == "":
            return

        #loading json from file
        try:
            f_data = open(fileName).read()
        except FileNotFoundError as e:
            print("Test case file is not found. " + str(e))
            return

        self.jsonData = json.loads(f_data)
    
    #test initialization
    def __init__(self, *args, **kwargs):     
        super(TestCaseJson, self).__init__(*args, **kwargs)

        self.userFunc = None
        self.testName = ""
        self.assertMethod = None
        self.jsonData = None
        self.module = None
        self.testCases = {}

    #actions before the test
    def setUp(self):
        return super().setUp()

    #actions after the test
    def tearDown(self):
        return super().tearDown()

    #getting new dict from json file with func arguments and values
    def get_func_paramvalues(self, func, params):
        
        if func is None:
            return None
                       
        arginfo = {}
        arg_names = {}
        values = {}
        arg_names_len = 0
        arg_defaults_len = 0

        try:
            arginfo = inspect.getargspec(func)
            if arginfo.args is not None:
                arg_names = arginfo.args
                arg_names_len = len(arg_names)
            if arginfo.defaults is not None:
                arg_defaults_len = len(arginfo.defaults)
        except TypeError:
            print("Error in reading arguments from function.")
            return None                
                    
        values = OrderedDict.fromkeys(arg_names)

        for arg in arg_names:                    
            values[arg] = dict(params).get(arg)             

        if arg_names_len - arg_defaults_len > len(values):
            print("Not enough parameters to send to the function {}.".format(func.__name__))
            return None
        
        return values

    #return a pair of key = value
    def getFormattedDictString(self, pv):
        l = list()
        for k,v in pv.items():
            l.append('{} = {}'.format(k,str(v)))
        return ','.join(map(str,l))
    
    #single test start
    def __runTest__(self):
        
        res = None              #result
        pvalues = {}            #arguments with values
        strParams = ""          #string of arguments separated by comma   
        currTestCaseNum = 0     #current test
        failedCount = 0         #count of failed test cases

        self.setUp()            #some actions before the test
        
        #test case count info
        print("\nTest case \"{}\" starts. Number of test cases: {}".format(self.testName, len(self.testCases)))        
        
        #test cases loop
        for tc_params in self.testCases:
           
            currTestCaseNum += 1
            
            pvalues = self.get_func_paramvalues(self.userFunc, tc_params)
            
            if not pvalues:
                return
            
            #the result
            res = tc_params[self._result]            
            
            #convert arguments to string using mapping
            strParams = self.getFormattedDictString(pvalues)           
                              
            try:                
                
                #test case brief info
                print("{}. Start {}({}) => {}".format(currTestCaseNum, self.userFunc.__name__, strParams, res))
                
                #running the test
                self.__choose_assert_func__(self.assertMethod, self.userFunc, res, pvalues)
                                            
            except AssertionError as e:
                #in case of exception just print the formatted text
                print("Status: " + self._failed + ". " + str(e))
                failedCount += 1
            else:
                #in case of success just print the formatted text
                print("Status: " + self._succeed)
        
        #test case finishes
        print("Result: {} / {} completed successfully.".format(len(self.testCases) - failedCount, len(self.testCases)))
        
        self.tearDown()            #some actions after the test     
                            
    #start multiple test cases from a module
    def __runAllTest__(self):
        
        res = None              #result
        pvalues = {}            #arguments with values
        strParams = ""          #string of arguments separated by comma 
        testCases = {}          #test cases    
        currTestCaseNum = 0     #current test
        failedCount = 0         #count of failed test cases
        func_list = list()      #list of all test functions from a module
                
        for name in dir(self.module):
            obj = getattr(self.module, name)
            if inspect.ismethod(obj) or inspect.isfunction(obj):
              func_list.append(obj)
        
        if len(func_list) == 0:
            print("There are no test functions were found.")
            return
        
        #start each test function
        for f in func_list:
            
            self.testCases = dict(self.jsonData).get(f.__name__)  
            
            #self.testCases = self.jsonData[f.__name__]

            if not self.testCases:
                continue
            
            self.userFunc = f
            self.testName = f.__name__

            self.__runTest__() #run a single function test
                
    #entry to start test case
    def Start(self, testName = _defaultTest, fileName = "", userFunc = None, assertMethod = AssertMethods.assertEqual):
        
        #settings
        self.userFunc = userFunc
        self.testName = testName
        self.assertMethod = assertMethod
        self.jsonData = None

        #read arguments from json
        self.__loadjson__(fileName)

        if self.jsonData is None:
            print("Test file is empty.")
            return

        #reading test case scenarios
        self.testCases = self.jsonData[self._testCases]

        if self.testCases is None:
            print("There are not any test cases to perform.")
            return

        if self.userFunc is None:
            print("User function is not defined.")
            return

        #test case implementation
        case = unittest.FunctionTestCase(self.__runTest__, self.setUp, self.tearDown)
                
        #suite = unittest.TestLoader().loadTestsFromName(TestCaseJson.__runTest__, TestCaseJson)
        caseResult = unittest.TextTestRunner(verbosity=2).run(case)

    #entry to start all test cases from chosen module
    def StartAll(self, module = None, fileName = "", assertMethod = AssertMethods.assertEqual):
        
        if module is None:
            print("Test module is not found.")
            return
        
        self.module = module
        self.assertMethod = assertMethod
        self.jsonData = None        

        #read test parameteres from json file
        self.__loadjson__(fileName)

        if self.jsonData is None:
            print("Test file is empty.")
            return
      
        #test case implementation
        case = unittest.FunctionTestCase(self.__runAllTest__, self.setUp, self.tearDown)
                
        caseResult = unittest.TextTestRunner(verbosity=2).run(case)
