'''
Created on 14-Sep-2021

@author: muhammad.haris
'''
import time, requests
from Settings import CommonFunctions as CF
from Settings import dataFunction as DataFunction
from unittest import TestCase

from pickle import FALSE, TRUE


class AddMeeting(TestCase):
    
    global URLToAddGroup, SheetName
    
    URLToAddGroup = '/Group/Add'
    SheetName = '6-Meeting'
    
    def testcase_01_AddGroup(self, TestCasesStatus=True):
        TestCaseID = '06-01'
        MethodName = 'testcase_01_AddGroup'
        
        ds = DataFunction.dataStorage()
        common = CF.CommonFunctions()
         
         
       
        starttime = time.process_time()
        
        AuthToken = ds.GetAuthToken(FALSE)
        email = ds.GetTeacherDetails(FALSE, 'Email')
        time.sleep(3)
        # Headers
        Parameters = {
            'AuthToken': '' + AuthToken + '',
            
            }
        
        # Body
        data = {
                "groupid": '',
                "groupname": '' + common.GenrateSimpleStringLimit10() + '',
                "description":'' + common.GenrateSimpleStringLimit50() + '',
                "chat": 'true',
                "audio": 'true',
                "video": 'true',
                "screenshare": 'true',
                "fileshare": 'true',
                "participants": 
                [
                {
                "email": '' + email + '',
                "host": 'true'
                }
                ],
                "roaster": [
                {
                  "days": [
                ''
                ],
                  "starttimestamp": '',
                  "endtimestamp": ''
                }
                ]
                }
        
        URL = '' + common.Domain + '' + URLToAddGroup + ''
        
        response = requests.post(URL, json=data, headers=Parameters)
        resp = response.json()
        print(resp)
        showcode = str(resp['responseCode'])
        meetingid = str(resp['meetingid'])
        print(meetingid)
        
        print('ResponseCode: ' + showcode)
        
        if TestCasesStatus == True:
            try:
                if resp['responseCode'] == 200:
                    print(common.SuccessMessage)
                    status = 'Passed'
                    ds.AddData(MethodName, Parameters, data, resp, URL)
                else:
                    status = 'Failed'
            finally:
                
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, data, status, starttime, resp)

        else:
            TestCasesStatus = False
            print("Add Course Excel need not to be Updated")
            # Test Case End
        return meetingid, email


class UpdateMeeting(TestCase):
    
    global URLtoUpdateMeeting, URLtoUpdateMeetingOptions, URLtoAddMeetingParticipants, URLtoUpdateRoaster, URLtoRemoveParticipants
    URLtoUpdateMeeting = '/Group/Update'
    URLtoUpdateMeetingOptions = '/Group/UpdateOptions'
    URLtoAddMeetingParticipants = '/Group/AddParticipants'
    URLtoUpdateRoaster = '/Group/UpdateRoaster'
    URLtoRemoveParticipants = '/Group/RemoveParticipants'
    
    def testcase_01_UpdateGroup(self, TestCasesStatus=True):
        TestCaseID = '06-02'
        MethodName = 'testcase_01_UpdateGroup'
        
        ds = DataFunction.dataStorage()
        common = CF.CommonFunctions()
         
         
       
        starttime = time.process_time()
        
        AuthToken = ds.GetAuthToken(FALSE)
        MeetingID = ds.GetMeetingID(TRUE)[0]

        time.sleep(2)
        # Headers
        Parameters = {
            'AuthToken': '' + AuthToken + '',
            
            }
        
        # Body
        data = {
                "groupid": '' + MeetingID + '',
                "groupname": '' + common.GenrateSimpleStringLimit10() + '',
                "description":''
                }
        
        URL = '' + common.Domain + '' + URLtoUpdateMeeting + ''
        
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
                    ds.AddData(MethodName, Parameters, data, resp, URL)
                else:
                    status = 'Failed'
            finally:
                
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, data, status, starttime, resp)

        else:
            TestCasesStatus = False
            print("Add Course Excel need not to be Updated")
            # Test Case End
    
    def testcase_02_UpdateGroupOptions(self, TestCasesStatus=True):
        TestCaseID = '06-03'
        MethodName = 'testcase_01_UpdateGroupOptions'
        
        ds = DataFunction.dataStorage()
        common = CF.CommonFunctions()
         
         
       
        starttime = time.process_time()
        
        AuthToken = ds.GetAuthToken(FALSE)
        MeetingID = ds.GetMeetingID(FALSE)[0]

        time.sleep(2)
        # Headers
        Parameters = {
            'AuthToken': '' + AuthToken + '',
            
            }
        
        # Body
        data = {
                "groupid": '' + MeetingID + '',
                "chat": 'false',
                "audio": 'false',
                "video": 'true',
                "screenshare": 'false',
                "fileshare": 'true'
                }
        
        URL = '' + common.Domain + '' + URLtoUpdateMeetingOptions + ''
        
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
                    ds.AddData(MethodName, Parameters, data, resp, URL)
                else:
                    status = 'Failed'
            finally:
                
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, data, status, starttime, resp)

        else:
            TestCasesStatus = False
            print("Add Course Excel need not to be Updated")
            # Test Case End
        
    def testcase_03_AddGroupParticipants(self, TestCasesStatus=True):
        TestCaseID = '06-04'
        MethodName = 'testcase_03_AddGroupParticipants'
        
        ds = DataFunction.dataStorage()
        common = CF.CommonFunctions()
         
         
       
        starttime = time.process_time()
        
        AuthToken = ds.GetAuthToken(FALSE)
        MeetingID = ds.GetMeetingID(FALSE)[0]
        Email = ds.GetTeacherDetails(TRUE, "Email")
        Email1 = ds.GetStudentDetails(TRUE, "Email")
        Email2 = ds.GetStudentDetails(TRUE, "Email")

        time.sleep(2)
        # Headers
        Parameters = {
            'AuthToken': '' + AuthToken + '',
            
            }
        
        # Body
        data = {
                "groupid": '' + MeetingID + '',
                "participants": [
                    {
                        "email": '' + Email + ''
                    },
                    {
                        "email": '' + Email1 + ''
                    },
                    {
                        "email": '' + Email2 + ''
                    },
                    
                ]
}
        
        URL = '' + common.Domain + '' + URLtoAddMeetingParticipants + ''
        
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
                    ds.AddData(MethodName, Parameters, data, resp, URL)
                else:
                    status = 'Failed'
            finally:
                
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, data, status, starttime, resp)

        else:
            TestCasesStatus = False
            print("Add Course Excel need not to be Updated")
            # Test Case End
        
    def testcase_04_UpdateRoaster(self, TestCasesStatus=True):
        TestCaseID = '06-05'
        MethodName = 'testcase_04_UpdateRoaster'
        
        ds = DataFunction.dataStorage()
        common = CF.CommonFunctions()
         
         
       
        starttime = time.process_time()
        
        AuthToken = ds.GetAuthToken(FALSE)
        MeetingID = ds.GetMeetingID(FALSE)[0]
        #Email = ds.GetTeacherDetails(TRUE, "Email")

        time.sleep(2)
        # Headers
        Parameters = {
            'AuthToken': '' + AuthToken + '',
            
            }
        
        # Body
        data = {
                "groupid": '' + MeetingID + '',
                
            }
        
        URL = '' + common.Domain + '' + URLtoUpdateRoaster + ''
        
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
                    ds.AddData(MethodName, Parameters, data, resp, URL)
                else:
                    status = 'Failed'
            finally:
                
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, data, status, starttime, resp)

        else:
            TestCasesStatus = False
            print("Add Course Excel need not to be Updated")
            # Test Case End
     
    def testcase_05_RemoveParticipants(self, TestCasesStatus=True):
        TestCaseID = '06-06'
        MethodName = 'testcase_05_RemoveParticipants'
        
        ds = DataFunction.dataStorage()
        common = CF.CommonFunctions()
         
         
       
        starttime = time.process_time()
        
        AuthToken = ds.GetAuthToken(FALSE)
        MeetingID, Email = ds.GetMeetingID(FALSE)

        time.sleep(2)
        # Headers
        Parameters = {
            'AuthToken': '' + AuthToken + '',
            
            }
        
        # Body
        data = {
                "groupid": '' + MeetingID + '',
                "participants": [
                    {
                        "email": '' + Email + ''
                    }
                ]
                }
        
        URL = '' + common.Domain + '' + URLtoRemoveParticipants + ''
        
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
                    ds.AddData(MethodName, Parameters, data, resp, URL)
                else:
                    status = 'Failed'
            finally:
                
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, data, status, starttime, resp)

        else:
            TestCasesStatus = False
            print("Add Course Excel need not to be Updated")
            # Test Case End   

            
class DeleteMeeting(TestCase):
    
    global URLToDeleteMeeting, SheetName
    
    URLToDeleteMeeting = '/Group/Delete'
    SheetName = '6-Meeting'
    
    def testcase_01_DeleteGroup(self, TestCasesStatus=True):
        TestCaseID = '06-07'
        MethodName = 'testcase_01_DeleteGroup'
        
        ds = DataFunction.dataStorage()
        common = CF.CommonFunctions()
         
         
       
        starttime = time.process_time()
        
        AuthToken = ds.GetAuthToken(FALSE)
        MeetingID = ds.GetMeetingID(TRUE)[0]
        
        # Headers
        Parameters = {
            'AuthToken': '' + AuthToken + '',
            
            }
        
        # Body
        data = {
              
                }
        
        URL = '' + common.Domain + '' + URLToDeleteMeeting + '''?Id=''' + MeetingID + ''
        
        response = requests.delete(URL, json=data, headers=Parameters)
        resp = response.json()
        showcode = str(resp['responseCode'])
        
        print('ResponseCode: ' + showcode)
        
        if TestCasesStatus == True:
            try:
                if resp['responseCode'] == 200:
                    print(common.SuccessMessage)
                    status = 'Passed'
                    ds.AddData(MethodName, Parameters, data, resp, URL)
                else:
                    status = 'Failed'
            finally:
                
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, data, status, starttime, resp)

        else:
            TestCasesStatus = False
            print("Add Course Excel need not to be Updated")
            # Test Case End     
        

class GetMeeting(TestCase):
    
    global URLToGetGroup, SheetName
    
    URLToGetGroup = '/Group/Get'
    SheetName = '6-Meeting'
    
    def testcase_01_GetGroup(self, TestCasesStatus=True):
        TestCaseID = '06-08'
        MethodName = 'testcase_01_GetGroup'
        
        ds = DataFunction.dataStorage()
        common = CF.CommonFunctions()
         
         
       
        starttime = time.process_time()
        
        AuthToken = ds.GetAuthToken(FALSE)
        MeetingID = ds.GetMeetingID(FALSE)[0]
        
        # Headers
        Parameters = {
            'AuthToken': '' + AuthToken + '',
            
            }
        
        # Body
        data = {
              
                }
        
        URL = '' + common.Domain + '' + URLToGetGroup + '''?Id=''' + MeetingID + ''
        
        response = requests.get(URL, json=data, headers=Parameters)
        resp = response.json()
        showcode = str(resp['responseCode'])
        
        print('ResponseCode: ' + showcode)
        
        if TestCasesStatus == True:
            try:
                if resp['responseCode'] == 200:
                    print(common.SuccessMessage)
                    status = 'Passed'
                    ds.AddData(MethodName, Parameters, data, resp, URL)
                else:
                    status = 'Failed'
            finally:
                
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, data, status, starttime, resp)

        else:
            TestCasesStatus = False
            print("Add Course Excel need not to be Updated")
            # Test Case End     
        