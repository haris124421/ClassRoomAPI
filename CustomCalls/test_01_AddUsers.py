import requests
from Settings import CommonFunctions as CF

from Settings import dataFunction as DataFunction
from unittest import TestCase
from pickle import FALSE





class AddUser(TestCase):
  
    global UrlToAddUser, SheetName, value, teacherslst
    UrlToAddUser = '/User/Add'
    SheetName = '4-User'
    def testcase_01_AddUserAsTeacher(self, TestCasesStatus=True):
        
        
        
        ds = DataFunction.dataStorage()
        common = CF.CommonFunctions()
        emails = ds.ReadDataFromDataFile('Teachers','TeachersEmail')
    
        emails = emails.split(',')
        print (type(emails))
        value = len(emails)
        

        AuthToken = ds.GetAuthToken(FALSE)
        subscriptionsettingsidTeacher = ds.GetTeacherSubID(FALSE)
        while value > 0: 
            # Headers
            Parameters = {
                'AuthToken': '' + AuthToken + '',
                
                }
            
            # Body
            data = [
                {
                "firstname":'' + common.GenerateFirstName()+ '',
                "lastname": '' + common.GenerateLastName() + '',
                "email": '' + emails[value-1] + '',
                "role": '' + common.GenerateRoleAsTeacher()+ '',
                "active": 'true',
                "subscriptionid": '' + subscriptionsettingsidTeacher + '',
                }
                ]
            
            URL = '' + common.Domain + '' + UrlToAddUser + ''
            
            response = requests.post(URL, json=data, headers=Parameters)
            teacherslst.append(data)
            resp = response.json()
            print(resp)
            showcode = str(resp['responseCode'])
            
            print('ResponseCode: ' + showcode)
            
            if TestCasesStatus == True:
                try:
                    if resp['responseCode'] == 200:
                        print(common.SuccessMessage)
                    else:
                        print('Failed')
                finally:
                    print('Nothing')
                    #ds.AddData(MethodName, Parameters, data, resp, URL)
                    #common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, data, status, starttime, resp)
    
            else:
                TestCasesStatus = False
                print("Add Course Excel need not to be Updated")
            value = value - 1
        #return email, firstName, lastName, role

            # Test Case End
    
    
    def testcase_02_AddUserAsStudent(self, TestCasesStatus=True):
        
        
        
        
        ds = DataFunction.dataStorage()
        common = CF.CommonFunctions()
        emails = ds.ReadDataFromDataFile('Students','StudentsEmail')
        emails = emails.split(',')
        print (type(emails))
        value = len(emails)

        AuthToken = ds.GetAuthToken(FALSE)
        subscriptionsettingsidStudent =ds.GetStudentSubID(FALSE)
        while value > 0: 
            print('Running test Case for Value :' +str(value))
            
            
            # Headers
            Parameters = {
                'AuthToken': '' + AuthToken + '',
                
                }
            
            # Body
            data = [
                {
                "firstname":'' + common.GenerateFirstName()+ '',
                "lastname": '' + common.GenerateLastName() + '',
                "email": '' + emails[value-1] + '',
                "role": '' + common.GenerateRoleAsStudent()+ '',
                "active": 'true',
                "subscriptionid": '' + subscriptionsettingsidStudent + '',
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
                        
                    else:
                        print('Failed')
                finally:
                    print('Nothing')
                    #ds.AddData(MethodName, Parameters, data, resp, URL)
                    #common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, data, status, starttime, resp)
    
            else:
                TestCasesStatus = False
                print("Add Course Excel need not to be Updated")
            value = value - 1
        #return email, firstName, lastName, role

            # Test Case End   
    def testcase_03_AddUserAsGuest(self, TestCasesStatus=True):
        
        
        
        
        ds = DataFunction.dataStorage()
        common = CF.CommonFunctions()
        emails = ds.ReadDataFromDataFile('Guests','guestsemail')
        emails = emails.split(',')
        print (type(emails))
        value = len(emails)

        AuthToken = ds.GetAuthToken(FALSE)
        subscriptionsettingsidStudent =ds.GetStudentSubID(FALSE)
        while value > 0: 
            print('Running test Case for Value :' +str(value))
            #MethodName = 'testcase_03_AddUserAsGuest'
            
            # Headers
            Parameters = {
                'AuthToken': '' + AuthToken + '',
                
                }
            
            # Body
            data = [
                {
                "firstname":'' + common.GenerateFirstName()+ '',
                "lastname": '' + common.GenerateLastName() + '',
                "email": '' + emails[value-1] + '',
                "role": '' + common.GenerateRoleAsGuest()+ '',
                "active": 'true',
                "subscriptionid": '' + subscriptionsettingsidStudent + '',
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
                        #status = 'Passed'
                    else:
                        print('Failed')
                finally:
                    print('Nothing')
                    #ds.AddData(MethodName, Parameters, data, resp, URL)
                    #common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, data, status, starttime, resp)
    
            else:
                TestCasesStatus = False
                print("Add Course Excel need not to be Updated")
            value = value - 1
        #return email, firstName, lastName, role

            # Test Case End