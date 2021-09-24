'''
Created on 22-Sep-2021

@author: muhammad.haris
'''
import time, requests
from Settings import CommonFunctions as CF
from Settings import dataFunction as DataFunction
from unittest import TestCase

from pickle import FALSE


class AddMeeting(TestCase):
    
    global URLToAddGroup, SheetName
    
    URLToAddGroup = '/Group/Add'

    
    def testcase_01_AddGroup(self, TestCasesStatus=True):
        
        ds = DataFunction.dataStorage()
        common = CF.CommonFunctions()
        
        AuthToken = ds.GetAuthToken(FALSE)
        meetingname = ds.ReadDataFromDataFile('Group','meetingname')
        time.sleep(3)
            # Headers
        Parameters = {
                'AuthToken': '' + AuthToken + '',
                
                }
            
            # Body
        data = {
                "groupid": '',
                "groupname": '' + meetingname + '',
                "description":'' + common.GenrateSimpleStringLimit50() + '',
                "chat": 'true',
                "audio": 'true',
                "video": 'true',
                "screenshare": 'true',
                "fileshare": 'true',
                "participants": 
                [
                {
                "email": '',
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
        showcode = str(resp['responseCode'])
     
        meetingid = str(resp['meetingid'])
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
        ds.WriteDataToDataFile('Group','meetingid',meetingid)
            # Test Case End