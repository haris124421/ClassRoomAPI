'''
Created on 31-Aug-2021

@author: muhammad.haris
'''
import time, requests
from Settings import CommonFunctions as CF
from unittest import TestCase
from Settings import dataFunction as DataFunction


class UpdateLMSDetail(TestCase):
    
    global SheetName
    UrlToUpdateLMSDetail = '/Organization/UpdateLMSDetail'
    SheetName = '2-Organization'

    def testcase_01_UpdateLMSDetail(self, TestCasesStatus=True):
        
        TestCaseID = '02-01'
        #MethodName = 'testcase_01_UpdateLMSDetail'
        ds = DataFunction.dataStorage()
        
        common = CF.CommonFunctions()
        
        starttime = time.process_time()
        
        AuthToken = ds.GetAuthToken(False)
        organizationid = ds.GetOrganizationID(False)
        
        # Headers
        Parameters = {
            'AuthToken': '' + AuthToken + '',
            'Email': '' + common.EncrypEmail + '',
            }
        
        # Body
        data = {
            "id":''+organizationid+'',
            "lmsdetail": {
                "lmstype": 2
}
}
        URL = '' + common.Domain + '' + self.UrlToUpdateLMSDetail + ''
        
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

            
class GetOrganization(TestCase):
    
    UrlToGetOrganization = '/Organization/Get'
    
    def testcase_02_GetOrganization(self, TestCasesStatus=True):
        
        TestCaseID = '02-02'
        #MethodName = 'testcase_02_GetOrganization'
        ds = DataFunction.dataStorage()
        
        common = CF.CommonFunctions()
        
        starttime = time.process_time()
        
        AuthToken = ds.GetAuthToken(False)
        
        # Headers
        Parameters = {
            'AuthToken': '' + AuthToken + '',
            'Email': '' + common.authuser + '',
            }
        # Body
        data = {
            
            }
        
        URL = '' + common.Domain + '' + self.UrlToGetOrganization + ''
        
        response = requests.get(URL, headers=Parameters)
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
