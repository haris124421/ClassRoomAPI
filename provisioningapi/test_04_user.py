'''
Created on 06-Sep-2021

@author: nouman.ijaz
'''

import time, requests
from Settings import CommonFunctions as CF
import base64
from Settings import dataFunction as DataFunction
from unittest import TestCase
from pickle import FALSE, TRUE


class AddUser(TestCase):
  
    global UrlToAddUser, SheetName
    UrlToAddUser = '/User/Add'
    SheetName = '4-User'
    
    def testcase_01_AddUserAsTeacher(self, TestCasesStatus=True):
        
        
        
        TestCaseID = '04-01'
        # UrlToAddCourse = '/Course/Add'
        MethodName = 'testcase_01_AddUserAsTeacher'
        ds = DataFunction.dataStorage()
        common = CF.CommonFunctions()
        
        starttime = time.process_time()
        
        AuthToken = ds.GetAuthToken(FALSE)
        
        firstName = common.GenerateFirstName()
        lastName = common.GenerateLastName()
        email = common.GenerateEmail(firstName, lastName)
        role = common.GenerateRoleAsTeacher()
        print(firstName)
        print(lastName)
        print(email)
        print(role)
        # Headers
        Parameters = {
            'AuthToken': '' + AuthToken + '',
            
            }
        
        # Body
        data = [
            {
            "firstname":'' + firstName + '',
            "lastname": '' + lastName + '',
            "email": '' + email + '',
            "role": '' + role + '',
            }
            ]
        
        URL = '' + common.Domain + '' + UrlToAddUser + ''
        
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
            
        return email, firstName, lastName, role

            # Test Case End
    
    def testcase_02_AddUserAsStudent(self, TestCasesStatus=True):
        
        TestCaseID = '04-02'
        MethodName = 'testcase_02_AddUserAsStudent'
        
        common = CF.CommonFunctions()
        ds = DataFunction.dataStorage()
        
        starttime = time.process_time()
        
        AuthToken = ds.GetAuthToken(FALSE)
        
        firstName = common.GenerateFirstName()
        lastName = common.GenerateLastName()
        email = common.GenerateEmail(firstName, lastName)
        role = common.GenerateRoleAsStudent()
        print(firstName)
        print(lastName)
        print(email)
        print(role)
        # Headers
        Parameters = {
            'AuthToken': '' + AuthToken + '',
            
            }
        
        # Body
        data = [
            {
            "firstname":'' + firstName + '',
            "lastname": '' + lastName + '',
            "email": '' + email + '',
            "role": '' + role + '',
            }
            ]
        
        URL = '' + common.Domain + '' + UrlToAddUser + ''
        
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
        
        return email, firstName, lastName, role
            # Test Case End
    
    def testcase_03_AddUserAsGuest(self, TestCasesStatus=True):
        
        TestCaseID = '04-03'
        #MethodName = 'testcase_03_AddUserAsGuest'
        
        ds = DataFunction.dataStorage()
        common = CF.CommonFunctions()
        
        starttime = time.process_time()
        
        AuthToken = ds.GetAuthToken(FALSE)
        
        firstName = common.GenerateFirstName()
        lastName = common.GenerateLastName()
        email = common.GenerateEmail(firstName, lastName)
        role = common.GenerateRoleAsGuest()
        print(firstName)
        print(lastName)
        print(email)
        print(role)
        # Headers
        Parameters = {
            'AuthToken': '' + AuthToken + '',
            
            }
        
        # Body
        data = [
            {
            "firstname":'' + firstName + '',
            "lastname": '' + lastName + '',
            "email": '' + email + '',
            "role": '' + role + '',
            }
            ]
        
        URL = '' + common.Domain + '' + UrlToAddUser + ''
        
        response = requests.post(URL, json=data, headers=Parameters)
        resp = response.json()
        
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
            print("Add Course Excel need not to be Updated")

        # Test Case End
        
    def testcase_04_AddMultipleUsers(self, TestCasesStatus=True):
        
        TestCaseID = '04-12'
        #MethodName = 'testcase_03_AddUserAsGuest'
        
        ds = DataFunction.dataStorage()
        common = CF.CommonFunctions()
        
        starttime = time.process_time()
        
        AuthToken = ds.GetAuthToken(FALSE)
        
        # Headers
        Parameters = {
            'AuthToken': '' + AuthToken + '',
            
            }
        
        # Body
        data = [
            {
            "firstname":'' + common.GenerateFirstName() + '',
            "lastname": '' + common.GenerateLastName()+ '',
            "email": '' +common.GenerateEmail(common.GenerateFirstName(), common.GenerateLastName())+ '',
            "role": '' +common.GenerateRoleAsTeacher() + '',
            },
            {
            "firstname":'' + common.GenerateFirstName() + '',
            "lastname": '' + common.GenerateLastName()+ '',
            "email": '' +common.GenerateEmail(common.GenerateFirstName(), common.GenerateLastName())+ '',
            "role": '' +common.GenerateRoleAsStudent()+ '',  
            },
            {
            "firstname":'' + common.GenerateFirstName() + '',
            "lastname": '' + common.GenerateLastName()+ '',
            "email": '' +common.GenerateEmail(common.GenerateFirstName(), common.GenerateLastName())+ '',
            "role": '' +common.GenerateRoleAsGuest()+ '',  
            }
            ]
        
        URL = '' + common.Domain + '' + UrlToAddUser + ''
        
        response = requests.post(URL, json=data, headers=Parameters)
        resp = response.json()
        
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
            print("Add Course Excel need not to be Updated")

        # Test Case End
    def testcase_05_AddMultipleUsersWithActiveStatus(self, TestCasesStatus=True):
        
        TestCaseID = '04-12'
        #MethodName = 'testcase_03_AddUserAsGuest'
        
        ds = DataFunction.dataStorage()
        common = CF.CommonFunctions()
        
        starttime = time.process_time()
        
        AuthToken = ds.GetAuthToken(FALSE)
        subscriptionsettingsidTeacher = ds.GetTeacherSubID(FALSE)
        subscriptionsettingsidStudent =ds.GetStudentSubID(FALSE)
        
        # Headers
        Parameters = {
            'AuthToken': '' + AuthToken + '',
            
            }
        
        # Body
        data = [
            {
            "firstname":'' + common.GenerateFirstName() + '',
            "lastname": '' + common.GenerateLastName()+ '',
            "email": '' +common.GenerateEmail(common.GenerateFirstName(), common.GenerateLastName())+ '',
            "role": '' +common.GenerateRoleAsTeacher() + '',
            "active": 'true',
            "subscriptionid": '' + subscriptionsettingsidTeacher + '',
            },
            {
            "firstname":'' + common.GenerateFirstName() + '',
            "lastname": '' + common.GenerateLastName()+ '',
            "email": '' +common.GenerateEmail(common.GenerateFirstName(), common.GenerateLastName())+ '',
            "role": '' +common.GenerateRoleAsStudent()+ '',
            "active": 'true',
            "subscriptionid": '' + subscriptionsettingsidStudent + '',  
            },
            {
            "firstname":'' + common.GenerateFirstName() + '',
            "lastname": '' + common.GenerateLastName()+ '',
            "email": '' +common.GenerateEmail(common.GenerateFirstName(), common.GenerateLastName())+ '',
            "role": '' +common.GenerateRoleAsGuest()+ '',
            "active": 'true',
            "subscriptionid": '' + subscriptionsettingsidStudent + '',  
            }
            ]
        
        URL = '' + common.Domain + '' + UrlToAddUser + ''
        
        response = requests.post(URL, json=data, headers=Parameters)
        resp = response.json()
        
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
            print("Add Course Excel need not to be Updated")

        # Test Case End
        
class UpdateUser(TestCase):
    
    UrlToUpdateUsers = '/User/Update'
    UrlToForgetPassword = '/User/ForgotPassword'
    
    def testcase_01_UpdateUser(self, TestCasesStatus=True):
        
        TestCaseID = '04-04'
        MethodName = 'testcase_01_UpdateUser'
        
        common = CF.CommonFunctions()
        ds = DataFunction.dataStorage()
        
        starttime = time.process_time()
        
        AuthToken = ds.GetAuthToken(FALSE)
        subscriptionsettingsidTeacher = ds.GetTeacherSubID(FALSE)
        
        firstName = common.GenerateFirstName()
        lastName = common.GenerateLastName()
        email = ds.GetTeacherDetails(TRUE, 'Email')
       
        # Headers
        Parameters = {
            'AuthToken': '' + AuthToken + '',
            
            }
        
        # Body
        data = {
            "firstname":'' + firstName + '',
            "lastname": '' + lastName + '',
            "email": '' + email + '',
            "role": '1',
            "active": 'true',
            "subscriptionid": '' + subscriptionsettingsidTeacher + '',
            
            }
        
        URL = '' + common.Domain + '' + self.UrlToUpdateUsers + ''
        time.sleep(3)
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
                ds.AddData(MethodName, Parameters, data, resp, URL)
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, data, status, starttime, resp)

        else:
            TestCasesStatus = False
            # Test Case End
            
    def testcase_02_UserForgotPassword(self, TestCasesStatus=True):
        
        TestCaseID = '04-11'
        MethodName = 'testcase_02_UserForgotPassword'
        ds = DataFunction.dataStorage()
        
        common = CF.CommonFunctions()
        
        starttime = time.process_time()
      
        email = ds.GetTeacherDetails(TRUE, "Email")
        ByteEncEmail = email.encode('ascii')
        base64_bytes = str(base64.b64encode(ByteEncEmail))
        EncEmail = base64_bytes[2:-1]
       
        # Headers
        Parameters = {
            'AuthToken': '' + common.mastertoken + '',
             "email": '' + EncEmail + '',
            
            }
        
        # Body
        data = {
            
            }
        
        URL = '' + common.Domain + '' + self.UrlToForgetPassword + ''
        time.sleep(1)
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
                ds.AddData(MethodName, Parameters, data, resp, URL)
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, data, status, starttime, resp)

        else:
            TestCasesStatus = False
            # Test Case End

            
class GetUser(TestCase):
    
    UrlToGetUser = '/User/Get'
    UrlToGetUserByEmail = '/User/GetByEmail'
    UrlToGetUserLMSUser = '/User/GetLMSUsers'
    UrlToSearchLMSUsers = '/User/SearchLMSUsers'
    UrlToSearchUserGlobally = '/User/SearchUserGlobally'
    
    def testcase_01_GetUser(self, TestCasesStatus=True):
        
        TestCaseID = '04-05'
        MethodName = 'testcase_01_GetUser'
        
        ds = DataFunction.dataStorage()
        common = CF.CommonFunctions()
        
        starttime = time.process_time()
        
        AuthToken = ds.GetAuthToken(FALSE)
        subscriptionsettingsidTeacher = ds.GetTeacherSubID(FALSE)

        
        email = ds.GetTeacherDetails(FALSE, "email")
        firstName = ds.GetTeacherDetails(FALSE, "firstName")
        lastName = ds.GetTeacherDetails(FALSE, 'LastName')
        role = ds.GetTeacherDetails(FALSE, "role")
        print(lastName)
        time.sleep(1)
        
        courseName = common.GenrateSimpleStringLimit10()
        print(courseName)

        # Headers
        Parameters = {
            'AuthToken': '' + AuthToken + '',
            }
        
        # Body
        data = {
            
            "firstname":'' + firstName + '',
            "lastname": '' + lastName + '',
            "email": '' + email + '',
            "role": '' + role + '',
            "active": 'true',
            "subscriptionid": '' + subscriptionsettingsidTeacher + '',
           
            }
        
        URL = '' + common.Domain + '' + self.UrlToGetUser
        
        print(URL)
    
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
                ds.AddData(MethodName, Parameters, data, resp, URL)
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, data, status, starttime, resp)

        else:
            TestCasesStatus = False
            # Test Case End  
    
    def testcase_02_GetUserByEmail(self, TestCasesStatus=True):
        
        TestCaseID = '04-06'
        MethodName = 'testcase_02_GetUserByEmail'
        ds = DataFunction.dataStorage()
        common = CF.CommonFunctions()
        
        starttime = time.process_time()
        
        AuthToken = ds.GetAuthToken(FALSE)

        email = ds.GetTeacherDetails(FALSE, "email")
        courseName = common.GenrateSimpleStringLimit10()
        print(courseName)
        # Headers
        Parameters = {
            'AuthToken': '' + AuthToken + '',
            }
        
        # Body
        data = {
           
            }
        
        URL = '' + common.Domain + '' + self.UrlToGetUserByEmail + '''?email=''' + email + ''
        
        print(URL)
    
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
                ds.AddData(MethodName, Parameters, data, resp, URL)
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, data, status, starttime, resp)

        else:
            TestCasesStatus = False
            # Test Case End  
            
    def testcase_03_GetLMSUsers(self, TestCasesStatus=True):
        
        TestCaseID = '04-08'
        MethodName = 'testcase_03_GetLMSUsers'
        ds = DataFunction.dataStorage()
        common = CF.CommonFunctions()
        
        starttime = time.process_time()
        
        AuthToken = ds.GetAuthToken(FALSE)
        role = 'Teacher' # need to pass Role as string in URL
        courseName = common.GenrateSimpleStringLimit10()
        courseDescription = common.GenrateSimpleStringLimit10()
        print(courseName)
        print(courseDescription)
        # Headers
        Parameters = {
            'AuthToken': '' + AuthToken + '',
            }
        
        # Body
        data = {
           
            }
        
        URL = '' + common.Domain + '' + self.UrlToGetUserLMSUser + '''?Role=''' + role + '''&FilterunConfigure=true&PageStart=1&PageSize=15'''
        
        print(URL)
    
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
                ds.AddData(MethodName, Parameters, data, resp, URL)
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, data, status, starttime, resp)

        else:
            TestCasesStatus = False
            # Test Case End  

    def testcase_04_SearchLMSUser(self, TestCasesStatus=True):
        
        TestCaseID = '04-08'
        MethodName = 'testcase_04_SearchLMSUser'
        ds = DataFunction.dataStorage()
        
        common = CF.CommonFunctions()
        
        starttime = time.process_time()

        Email = ds.GetTeacherDetails(FALSE, "email")
 
        # Headers
        Parameters = {
            'AuthToken': '' + common.mastertoken + '', 
            }
        
        # Body
        data = [
            Email,
           
            ]
        
        URL = '' + common.Domain + '' + self.UrlToSearchLMSUsers
        
        print(URL)
    
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
                ds.AddData(MethodName, Parameters, data, resp, URL)
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, data, status, starttime, resp)

        else:
            TestCasesStatus = False
            # Test Case End  
            
    def testcase_05_SearchUserGlobally(self, TestCasesStatus=True):
        
        TestCaseID = '04-09'
        
        MethodName = 'testcase_05_SearchUserGlobally'
        ds = DataFunction.dataStorage()
        common = CF.CommonFunctions()
        
        starttime = time.process_time()
        
        AuthToken = ds.GetAuthToken(FALSE)
 
        Email = ds.GetTeacherDetails(FALSE, "email")
        # Headers
        Parameters = {
            'AuthToken': '' + AuthToken + '',
           
            }
        
        # Body
        data = {
            }
        
        URL = '' + common.Domain + '' + self.UrlToSearchUserGlobally + '''?Email=''' + Email + ''
        
        print(URL)
    
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
                ds.AddData(MethodName, Parameters, data, resp, URL)
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, data, status, starttime, resp)

        else:
            TestCasesStatus = False
            # Test Case End  

            
class DeleteUser(TestCase):
  
    global UrlToDeleteUser
    UrlToDeleteUser = '/User/Delete'
    
    def testcase_01_DeleteUser(self, TestCasesStatus=True):
        
        TestCaseID = '04-10'
        MethodName = 'testcase_01_DeleteUser'
        
        ds = DataFunction.dataStorage()
        common = CF.CommonFunctions()
        
        starttime = time.process_time()
        
        AuthToken = ds.GetAuthToken(FALSE)
        email = ds.GetTeacherDetails(TRUE, "email")

        ByteEncEmail = email.encode('ascii')
        base64_bytes = str(base64.b64encode(ByteEncEmail))
        EncEmail = base64_bytes[2:-1]
  
        time.sleep(3)
        
        Parameters = {
            'AuthToken': '' + AuthToken + '',
            'Email': '' + EncEmail + '',
            
            }
        
        # Body
        data = {
         
            }
        
        URL = '' + common.Domain + '' + UrlToDeleteUser 
    
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
