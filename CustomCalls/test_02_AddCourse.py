'''
Created on 20-Sep-2021

@author: muhammad.haris
'''
import time, requests
from Settings import CommonFunctions as CF
from unittest import TestCase
from Settings import dataFunction as DataFunction
from pickle import  FALSE



class AddCourse(TestCase):
  
    global UrlToAddCourse, courseIdlst
    courseIdlst=[]
    UrlToAddCourse = '/Course/Add'
    
    def testcase_01_AddCourse(self, TestCasesStatus=True):

        ds = DataFunction.dataStorage()
        common = CF.CommonFunctions()
        courses = ds.ReadDataFromDataFile('Course','CourseName')
        courses = courses.split(',')
        print (type(courses))
        value = len(courses)
        
        while value > 0 :
            
            
            AuthToken = ds.GetAuthToken(FALSE)
            
            # Headers
            Parameters = {
                'AuthToken': '' + AuthToken + '',
                
                }
            
            # Body
            data = {
                "coursename":'' + courses[value-1]+ '',
                "description": '' + common.GenrateSimpleStringLimit50() + ''
                }
            
            URL = '' + common.Domain + '' + UrlToAddCourse + ''
            
            response = requests.post(URL, json=data, headers=Parameters)
            resp = response.json()
            print(resp)
            
            showcode = str(resp['responseCode'])
            courseId = str(resp['courseid'])
            courseIdlst.append(courseId)
            print(len(courseIdlst))
            print('ResponseCode: ' + showcode)
            print('Course ID: ' + courseId)
            
            if TestCasesStatus == True:
                try:
                    if resp['responseCode'] == 200:
                        print(common.SuccessMessage)
                        #status = 'Passed'
                    else:
                        print('TestCase Failed')
                finally:
                    print('Nothing')
                    
                    #ds.AddData(MethodName, Parameters, data, resp, URL)
                    #common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, data, status, starttime, resp)
    
            else:
                TestCasesStatus = False
                print("Add Course Excel need not to be Updated")
                # Test Case End
            value = value - 1
        ds.WriteDataToDataFile('Course','CourseId',courseId)