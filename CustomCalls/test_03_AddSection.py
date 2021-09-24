'''
Created on 21-Sep-2021

@author: muhammad.haris
'''
import time, requests
from Settings import CommonFunctions as CF
from Settings import dataFunction as DataFunction
from unittest import TestCase

from pickle import FALSE

SheetName = '5-Section'


class AddSection(TestCase):
  
    global UrlToAddSection
    UrlToAddSection = '/Section/Add'
    
    def testcase_01_AddSection(self, TestCasesStatus=True):

        ds = DataFunction.dataStorage()
        common = CF.CommonFunctions()
       
        
        
        AuthToken = ds.GetAuthToken(FALSE)
        CourseId = ds.ReadDataFromDataFile('Course','courseid')
        SectionName = ds.ReadDataFromDataFile('Section','sectionname')

        time.sleep(2)
        # Headers
        Parameters = {
            'AuthToken': '' + AuthToken + '',
            
            }
        
        # Body
        data = {
            "courseid":'' + CourseId + '',
            "sectionname":'' + SectionName + '',
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
                    #status = 'Passed'
                else:
                    print('Failed')
                    #status = 'Failed'
            finally:
                print('Nothing')

        else:
            TestCasesStatus = False
            print("Add Course Excel need not to be Updated")
        ds.WriteDataToDataFile('Section','sectionid',sectionId)