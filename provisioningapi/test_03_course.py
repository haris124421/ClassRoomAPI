'''
Created on 02-Sep-2021

@author: nouman.ijaz
'''
import time, requests
from Settings import CommonFunctions as CF
from unittest import TestCase
from Settings import dataFunction as DataFunction
from pickle import TRUE, FALSE


class AddCourse(TestCase):
  
    global UrlToAddCourse, SheetName
    UrlToAddCourse = '/Course/Add'
    SheetName = '3-Course'
    
    def testcase_01_AddCourse(self, TestCasesStatus=True):
        
        TestCaseID = '03-01'
        # UrlToAddCourse = '/Course/Add'
        MethodName = 'testcase_01_AddCourse'
        ds = DataFunction.dataStorage()
        common = CF.CommonFunctions()
        
        starttime = time.process_time()
     
        AuthToken = ds.GetAuthToken(FALSE)
        
        courseName = common.GenerateCourseName()
        courseDescription = common.GenrateSimpleStringLimit50()
        print(courseName)
        print(courseDescription)
        # Headers
        Parameters = {
            'AuthToken': '' + AuthToken + '',
            
            }
        
        # Body
        data = {
            "coursename":'' + courseName + '',
            "description": '' + courseDescription + ''
            }
        
        URL = '' + common.Domain + '' + UrlToAddCourse + ''
        
        response = requests.post(URL, json=data, headers=Parameters)
        resp = response.json()
        print(resp)
        showcode = str(resp['responseCode'])
        courseId = str(resp['courseid'])
        
        print('ResponseCode: ' + showcode)
        print('Course ID: ' + courseId)
        
        if TestCasesStatus == True:
            try:
                if resp['responseCode'] == 200:
                    print(common.SuccessMessage)
                    status = 'Passed'
                else:
                    status = 'Failed'
            finally:
                ds.AddData(MethodName, Parameters, data, resp, URL)
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, data, status, starttime, resp)

        else:
            TestCasesStatus = False
            print("Add Course Excel need not to be Updated")
            # Test Case End
        return courseId;
    def testcase_02_ImportCourses(self, TestCasesStatus = True):
        
        TestCaseID = '03-06'
        MethodName = 'testcase_02_ImportCourses'
        
        common = CF.CommonFunctions()
        
        starttime = time.process_time()
        ds = DataFunction.dataStorage()
        AuthToken = ds.GetAuthToken(FALSE)
        
        
        #Headers
        Parameters ={
            'AuthToken' : ''+AuthToken+'',
            }
        
        #Body
        data= [
            {
            "coursename":''+common.GenerateCourseName()+'',
            "description": ''+common.GenrateSimpleStringLimit50()+''
            },
            {
            "coursename":''+common.GenerateCourseName()+'',
            "description": ''+common.GenrateSimpleStringLimit50()+''
            },
            {
            "coursename":''+common.GenerateCourseName()+'',
            "description": ''+common.GenrateSimpleStringLimit50()+''
            },
            ]
        
        UrlToImportCourse = '/Course/ImportCourses'
        URL = ''+common.Domain+''+UrlToImportCourse+''
        
        response = requests.post(URL, json=data, headers=Parameters)
        resp=response.json()
        print(resp)
        showcode = str(resp['responseCode'])
        
        print('ResponseCode: '+showcode)
        
        if TestCasesStatus==True:
            try:
                if resp['responseCode'] == 200:
                    print(common.SuccessMessage)
                    status = 'Passed'
                else:
                    status = 'Failed'
            finally:
                ds.AddData(MethodName, Parameters, data, resp, URL)
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, data, status, starttime, resp)

        else:
            TestCasesStatus=False
            # Test Case End
    
class UpdateCourse(TestCase):
    
    UrlToUpdateCourse = '/Course/Update'
    
    def testcase_01_UpdateCourse(self, TestCasesStatus=True):
        
        TestCaseID = '03-02'
        #MethodName = 'testcase_01_UpdateCourse'
        ds = DataFunction.dataStorage()
        
        common = CF.CommonFunctions()
        
        starttime = time.process_time()
           
        AuthToken = ds.GetAuthToken(FALSE)
        CourseId = ds.GetCourseID(TRUE)
        
        courseName = common.GenerateCourseName()
        print(courseName)

        # Headers
        Parameters = {
            'AuthToken': '' + AuthToken + '',
            
            }
        
        # Body
        data = {
            "courseid":'' + CourseId + '',
            "coursename":'' + courseName + '',
            
            }
        
        URL = '' + common.Domain + '' + self.UrlToUpdateCourse + ''
        
        response = requests.put(URL, json=data, headers=Parameters)
        resp = response.json()
        print(resp)
        showcode = str(resp['responseCode'])
        
        print('ResponseCode: ' + showcode)
        
        if TestCasesStatus == True:
            try:
                if resp['responseCode'] == 200:
                    print(common.SuccessMessage)
                    status = 'Passed'
                else:
                    status = 'Failed'
            finally:
                # ds.AddData(MethodName, Parameters, data, resp, URL)
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, data, status, starttime, resp)

        else:
            TestCasesStatus = False
            # Test Case End

         
class GetCourse(TestCase):
    
    UrlToGetCourse = '/Course/Get'
    UrlToGetAllCourse = '/Course/GetAllCourses'
    UrlToGetCourseByLMSID = '/Course/GetByLMSID'
    
    def testcase_01_GetCourse(self, TestCasesStatus=True):
        
        TestCaseID = '03-03'
        #MethodName = 'testcase_01_GetCourse'
        ds = DataFunction.dataStorage()
        
        common = CF.CommonFunctions()
        
        starttime = time.process_time()
           
        AuthToken = ds.GetAuthToken(FALSE)
        
        CourseId = ds.GetCourseID(False)
        
        courseName = common.GenrateSimpleStringLimit10()
        # courseDescription= common.GenrateSimpleStringLimit10()
        print(courseName)
        # print(courseDescription)
        # Headers
        Parameters = {
            'AuthToken': '' + AuthToken + '',
            
            }
        
        # Body
        data = {
            "courseid":'' + CourseId + '',
            
            }
        
        URL = '' + common.Domain + '' + self.UrlToGetCourse + ''
        
        response = requests.get(URL, json=data, headers=Parameters)
        resp = response.json()
        print(resp)
        showcode = str(resp['responseCode'])
        
        print('ResponseCode: ' + showcode)
        
        if TestCasesStatus == True:
            try:
                if resp['responseCode'] == 200:
                    print(common.SuccessMessage)
                    status = 'Passed'
                else:
                    status = 'Failed'
            finally:
                # ds.AddData(MethodName, Parameters, data, resp, URL)
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, data, status, starttime, resp)

        else:
            TestCasesStatus = False
            # Test Case End    
            
    def testcase_02_GetAllCourse(self, TestCasesStatus=True):
        
        TestCaseID = '03-04'
        
        #MethodName = 'testcase_02_GetAllCourse'
        ds = DataFunction.dataStorage()
        
        common = CF.CommonFunctions()
        
        starttime = time.process_time()
           
        AuthToken = ds.GetAuthToken(FALSE)
        courseName = common.GenrateSimpleStringLimit10()
        print(courseName)
       
        # Headers
        Parameters = {
            'AuthToken': '' + AuthToken + '',
            }
        
        # Body
        data = {
            
            }
        
        URL = '' + common.Domain + '' + self.UrlToGetAllCourse + ''
        
        response = requests.get(URL, json=data, headers=Parameters)
        resp = response.json()
        print(resp)
        showcode = str(resp['responseCode'])
        
        print('ResponseCode: ' + showcode)
        
        if TestCasesStatus == True:
            try:
                if resp['responseCode'] == 200:
                    print(common.SuccessMessage)
                    status = 'Passed'
                else:
                    status = 'Failed'
            finally:
                # ds.AddData(MethodName, Parameters, data, resp, URL)
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, data, status, starttime, resp)

        else:
            TestCasesStatus = False
            # Test Case End     
            
    def testcase_02_GetCourseByLMSID(self, TestCasesStatus=True):
        
        TestCaseID = '03-05'
        
        #MethodName = 'testcase_02_GetAllCourse'
        ds = DataFunction.dataStorage()
        
        common = CF.CommonFunctions()
        
        starttime = time.process_time()
           
        AuthToken = ds.GetAuthToken(FALSE)
        CourseId = ds.GetCourseID(False)
        
       
        # Headers
        Parameters = {
            'AuthToken': '' + AuthToken + '',
            }
        
        # Body
        data = {
            
            }
        
        URL = '' + common.Domain + '' + self.UrlToGetCourseByLMSID + '''?Id=''' +CourseId+''
        
        response = requests.get(URL, json=data, headers=Parameters)
        resp = response.json()
        print(resp)
        showcode = str(resp['responseCode'])
        
        print('ResponseCode: ' + showcode)
        
        if TestCasesStatus == True:
            try:
                if resp['responseCode'] == 200:
                    print(common.SuccessMessage)
                    status = 'Passed'
                else:
                    status = 'Failed'
            finally:
                # ds.AddData(MethodName, Parameters, data, resp, URL)
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, data, status, starttime, resp)

        else:
            TestCasesStatus = False
            # Test Case End      
