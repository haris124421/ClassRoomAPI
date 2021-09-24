'''
Created on 22-Sep-2021

@author: muhammad.haris
'''
import requests
from Settings import CommonFunctions as CF
from Settings import dataFunction as DataFunction
from unittest import TestCase

from pickle import FALSE


class AddMeetingUsers(TestCase):
    
    global URLToAddParticipants, SheetName
    
    URLToAddParticipants = '/Group/AddParticipants'

    
    def testcase_01_AddParticipants(self, TestCasesStatus=True):
        
        ds = DataFunction.dataStorage()
        common = CF.CommonFunctions()
        
        AuthToken = ds.GetAuthToken(FALSE)
        meetingid = ds.ReadDataFromDataFile('Group','meetingid')
        EmailsList = ds.ReadDataFromDataFile('Teachers','teachersemail') + ','+ds.ReadDataFromDataFile("Students", "studentsemail")+ ','+ds.ReadDataFromDataFile("Guests", "guestsemail")
        EmailsList = EmailsList.split(',')
        i=len(EmailsList)
        while i>0:
            # Headers
            Parameters = {
                'AuthToken': '' + AuthToken + '',
                
                }
            
            # Body
            data = {
                    "groupid": ''+meetingid+'',
                    "participants": 
                    [
                    {
                    "email": ''+EmailsList[i-1]+''
                    }
                    ]
                    }
            i=i-1
            URL = '' + common.Domain + '' + URLToAddParticipants + ''
            
            response = requests.put(URL, json=data, headers=Parameters)
            resp = response.json()
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
                    #common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, data, status, starttime, resp)
    
            else:
                TestCasesStatus = False
                
            # Test Case End

