'''
Created on 08-Sep-2021

@author: nouman.ijaz
'''
import time, requests
from Settings import CommonFunctions as CF
from Settings import dataFunction as DataFunction
from unittest import TestCase

from pickle import FALSE, TRUE

SheetName = '5-Section'


class AddSection(TestCase):
  
    global UrlToAddSection, SheetName, sectionId, UrlToAddSectionUser, UrlToRemoveSectionUser
    UrlToAddSection = '/Section/Add'
    UrlToAddSectionUser = '/Section/AddUser'
    UrlToRemoveSectionUser = '/Section/RemoveUser'
    SheetName = '5-Section'
    
    def testcase_01_AddSection(self, TestCasesStatus=True):
        
        TestCaseID = '05-01'
        MethodName = 'testcase_01_AddSection'
        
        ds = DataFunction.dataStorage()
        common = CF.CommonFunctions()
       
        starttime = time.process_time()
        
        AuthToken = ds.GetAuthToken(FALSE)
        CourseId = ds.GetCourseID(FALSE)

        time.sleep(2)
        # Headers
        Parameters = {
            'AuthToken': '' + AuthToken + '',
            
            }
        
        # Body
        data = {
            "courseid":'' + CourseId + '',
            "sectionname":'' + common.GenerateSectionName() + '',
            "description": '' + common.GenrateSimpleStringLimit50() + '',
            
            }
        
        URL = '' + common.Domain + '' + UrlToAddSection + ''
        
        response = requests.post(URL, json=data, headers=Parameters)
        resp = response.json()
        print(resp)
        showcode = str(resp['responseCode'])
        
        print('ResponseCode: ' + showcode)
        
        if TestCasesStatus == True:
            try:
                if resp['responseCode'] == 200:
                    print(common.SuccessMessage)
                    sectionId = str(resp['sectionid'])
                    status = 'Passed'
                else:
                    status = 'Failed'
            finally:
                ds.AddData(MethodName, Parameters, data, resp, URL)
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, data, status, starttime, resp)

        else:
            TestCasesStatus = False
            print("Add Course Excel need not to be Updated")
            
        return sectionId, CourseId

            # Test Case End
    def testcase_02_AddSectionUser(self, TestCasesStatus=True):
        
        TestCaseID = '05-02'
        MethodName = 'testcase_02_AddSectionUser'
    
        common = CF.CommonFunctions()
        ds = DataFunction.dataStorage()
        starttime = time.process_time()
        
        AuthToken = ds.GetAuthToken(FALSE)
        UserEmail = ds.GetTeacherDetails(FALSE, "email")
        SectionID = ds.GetSectionDetails(FALSE, "SectorID")
        CourseId = ds.GetSectionDetails(FALSE, "courseid")
        time.sleep(2)
        # Headers
        Parameters = {
            'AuthToken': '' + AuthToken + '',
            
            }
        
        # Body
        data = {
            "courseid":'' + CourseId + '',
            "sectionid":'' + SectionID + '',
            "useremail": '' + UserEmail + '',
            
            }
        
        URL = '' + common.Domain + '' + UrlToAddSectionUser + ''
        
        response = requests.post(URL, json=data, headers=Parameters)
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
                ds.AddData(MethodName, Parameters, data, resp, URL)
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, data, status, starttime, resp)

        else:
            TestCasesStatus = False
            print("Add Course Excel need not to be Updated")

        return SectionID, UserEmail
            # Test Case End
            
    def testcase_03_RemoveSectionUser(self, TestCasesStatus=True):
        
        TestCaseID = '05-03'
        # UrlToAddCourse = '/Course/Add'
        
        common = CF.CommonFunctions()
        ds = DataFunction.dataStorage()
        starttime = time.process_time()
        
        AuthToken = ds.GetAuthToken(FALSE)

        UserEmail = ds.GetStudentDetails(TRUE, 'Email')
        SectionID = ds.GetSectionDetails(TRUE, "SectorID")
        CourseId = ds.GetSectionDetails(TRUE, "courseid")
        time.sleep(2)
        # Headers
        Parameters = {
            'AuthToken': '' + AuthToken + '',
            
            }
        
        # Body
        data = {
            "courseid":'' + CourseId + '',
            "sectionid":'' + SectionID + '',
            "useremail": '' + UserEmail + '',
            
            }
        
        URL = '' + common.Domain + '' + UrlToRemoveSectionUser + ''
        
        response = requests.post(URL, json=data, headers=Parameters)
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
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, data, status, starttime, resp)

        else:
            TestCasesStatus = False
            print("Add Course Excel need not to be Updated")

            # Test Case End

            
class DeleteSection(TestCase):
  
    global UrlToDeleteSessionLMSUserByBubbleId, SheetName
    UrlToDeleteSessionLMSUserByBubbleId = '/Section/DeleteLMSUserByBubbleID'
    
    def testcase_01_DeleteSectionLMSUserBubbleID(self, TestCasesStatus=True):
        
        TestCaseID = '05-04'
        # UrlToAddCourse = '/Course/Add'a
        
        common = CF.CommonFunctions()
        ds = DataFunction.dataStorage()
        starttime = time.process_time()
        
        AuthToken = ds.GetAuthToken(FALSE)
        
        email, Bid, SectionID = GetSection.testcase_01_GetSection(common.PrereqTestCasesStatusUpdate)
        print (Bid,SectionID)

        Endsession = 'true'
        
        Parameters = {
            'AuthToken': '' + AuthToken + '',
            
            }
        
        # Body
        data = {
         
            }
        
        URL = '' + common.Domain + '' + UrlToDeleteSessionLMSUserByBubbleId + '''?ID=''' + Bid + '''&Email=''' + email.lower() + '''&EndSession=''' + Endsession + ''
        
        print(URL)
        response = requests.delete(URL, json=data, headers=Parameters)
        print(response)
        resp = response.json()
        print(resp)
        showcode = str(resp['responseCode'])
        
        print('ResponseCode: ' + showcode)
        
        if TestCasesStatus == True:
            try:
                if resp['responseCode'] == 200:
                    print(common.SuccessMessage)
                    # sectionId= str(resp['sectionid'])
                    status = 'Passed'
                else:
                    status = 'Failed'
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, data, status, starttime, resp)

        else:
            TestCasesStatus = False
            print("Add Course Excel need not to be Updated")
    

            # Test Case End
class GetSection(TestCase):
    
    global UrlToGetSection
    UrlToGetSection = '/Section/GetSectionByID'
    
    def testcase_01_GetSection(self, TestCasesStatus=True):
        
        TestCaseID = '05-05'
        
        common = CF.CommonFunctions()
        ds = DataFunction.dataStorage()
        
        starttime = time.process_time()
        
        AuthToken = ds.GetAuthToken(FALSE)
        SectionID = ds.GetSectionUserDetails(FALSE, "SectionID")
        email = ds.GetSectionUserDetails(FALSE, "Email")
 
        # Headers
        Parameters = {
            'AuthToken': '' + AuthToken + '',
            }
        
        # Body
        data = {
           
            }
        
        URL = '' + common.Domain + '' + UrlToGetSection + '''?Id=''' + SectionID + ''
        
        print(URL)
    
        response = requests.get(URL, json=data, headers=Parameters)
        resp = response.json()
        print(resp)
        showcode = str(resp['responseCode'])
        bubbleid = resp['list'][0]['bubbleid']
        print(bubbleid)
        
        print('ResponseCode: ' + showcode)
        
        if TestCasesStatus == True:
            try:
                if resp['responseCode'] == 200:
                    print(common.SuccessMessage)
                    status = 'Passed'
                else:
                    status = 'Failed'
            finally:
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, data, status, starttime, resp)

        else:
            TestCasesStatus = False
        return email, bubbleid, SectionID
            # Test Case End  
    
