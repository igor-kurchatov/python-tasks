#################################
# Task 1
# Desription: We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in. Testing the method.
# Author : Igor Kurchatov 8/12/2016
#################################

import TestCaseJson
import sleep_in

##constants
#_failed = "Failed" 
#_succeed = "Succeed"
#_file_directory = "sleep_in_test_case.txt" #don't forget to change this!

#class Sleep_In_Iest(unittest.TestCase):

#    #Uncomment if separated test cases required 

#    #def testA(self):        
#    #    try:
#    #      print("Performing test A - sleep_in.sleep_in(False, False) => True")
#    #      self.assertEqual(sleep_in.sleep_in(False, False), True)          
#    #    except AssertionError as e:
#    #        print("Status: " + _failed + ". " + str(e))
#    #    else:
#    #        print("Status: " + _succeed)

                         
#    #def testB(self):
#    #    try:
#    #      print("Performing test B - sleep_in.sleep_in(True, False) => True")  
#    #      self.assertEqual(sleep_in.sleep_in(True, False), True)
#    #    except AssertionError as e:
#    #        print("Status: " + _failed + ". " + str(e))
#    #    else:
#    #        print("Status: " + _succeed)
    
#    #redefine initialization
#    def __init__(self, *args, **kwargs):
#        super(Sleep_In_Iest, self).__init__(*args, **kwargs)        
        
#        #loading json from file
#        f_data = open(_file_directory).read()
        
#        #getting json object from string
#        pdata = json.loads(f_data);
        
#        #storing in self
#        self.paramNames = pdata['paramNames']
#        self.testCases = pdata['testCases']
    
#    #test case            
#    def testAllSamples(self):
        
#        args = []               #arguments
#        res = None              #result
#        printParamsInfo = ""    #test case info    
        
#        for v in self.testCases:
            
#            #arguments
#            for p in self.paramNames:
#                args.append(v[p])                  
            
#            #the result
#            res = v['result']
            
#            #convert to string using mapping       
#            printParamsInfo = ','.join(map(str, args))
            
#            try:
#                #test case brief info
#                print("Performing sleep_in({}) => {}".format(printParamsInfo, res))
                
#                #running the test
#                self.assertEqual(sleep_in.sleep_in(*args), res)            
#            except AssertionError as e:
#                #in case of exception just print the formatted text
#                print("Status: " + _failed + ". " + str(e))
#            else:
#                #in case of success just print the formatted text
#                print("Status: " + _succeed)

#            #clear the list of arguments
#            args.clear()
    
#    #use before each test case runs if separated only
#    def setUp(self):
#        pass
    
#    #use after each test case runs if separated only    
#    def tearDown(self):        
#        pass

#test case implementation
#suite = unittest.TestLoader().loadTestsFromTestCase(Sleep_In_Iest)
#testResult = unittest.TextTestRunner(verbosity=2).run(suite)

testjson = TestCaseJson.TestCaseJson()
testjson.Start("sleep_in_test", r"sleep_in\sleep_in_test_case.txt", sleep_in.sleep_in)