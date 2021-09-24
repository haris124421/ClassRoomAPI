
'''
Created on 31-Aug-2021

@author: muhammad.haris
'''
import time, requests
from Settings import CommonFunctions as CF
from Settings import dataFunction as DataFunction
from unittest import TestCase
import pytest
from pytest import CaptureFixture



class GetSessionKey(TestCase):
    
    global SheetName, TestCasesStatus, authtoken, subscriptionsettingsidTeacher, subscriptionsettingsidStudent
    UrlToGetSessionKey = '/Authenticate/GetSessionAuthToken'
    authToken = '1'
    SheetName = '1-Authenticate'
    
    def testcase_01_GetSessionKey(self, TestCasesStatus=True):

        TestCaseID = '01-01'

        MethodName = 'testcase_01_GetSessionKey'
        ds = DataFunction.dataStorage()
        common = CF.CommonFunctions()
        
        starttime = time.process_time()
        
        Parameters = {
            'AuthToken': '' + common.mastertoken + '',
            'AuthUser': '' + common.authuser + '',
            'AuthPassword': '' + common.authpasssword + '',
            }
        # Body
        data = {
          
            }
        
        UrlToGetSessionKey = '/Authenticate/GetSessionAuthToken'
        
        URL = '' + common.Domain + '' + UrlToGetSessionKey + ''
        
        response = requests.get(URL, headers=Parameters)
        resp = response.json()
        
        if TestCasesStatus == True:
            try:
                if resp['responseCode'] == 200:
                    print(common.SuccessMessage)
                    status = 'Passed'
                    subscriptionsettingsidStudent = resp['subscriptionsettings'][0]['id']
                    subscriptionsettingsidTeacher = resp['subscriptionsettings'][1]['id']
                    organizationid = resp['organization']['id']
                    print ('Organization ID returned from Authentication: '+organizationid)
                    authtoken = str(resp['authToken'])
                    
                else:
                    status = 'Failed'
            finally:
                ds.AddData(MethodName, Parameters, data, resp, URL)
                common.UpdateExcelTestCase(SheetName, TestCaseID, URL, Parameters, data, status, starttime, resp)

        else:
            TestCasesStatus = False
        try:
            common.authToken = authtoken 
        finally:
            print('AuthKey not generated')
        print ('AuthKey', authtoken)
        
        return authtoken, subscriptionsettingsidTeacher, subscriptionsettingsidStudent,organizationid
            # Test Case End
        


        
