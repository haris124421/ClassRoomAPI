import time, requests
from Settings import CommonFunctions as CF
from Settings import dataFunction as DataFunction
from unittest import TestCase
import json

from pickle import FALSE




class AddSectionParticipants(TestCase):
  
    global UrlToAddParticipants
    UrlToAddParticipants = '/Section/AddParticipants'
    
    def testcase_01_AddParticipants(self, TestCasesStatus=True):

        ds = DataFunction.dataStorage()
        common = CF.CommonFunctions()
       
        
        
        AuthToken = ds.GetAuthToken(FALSE)
        CourseId = ds.ReadDataFromDataFile('Course','courseid')
        SectionId = ds.ReadDataFromDataFile('Section','sectionid')
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
                "courseid":'' + CourseId + '',
                "sectionid":'' + SectionId + '',
                "participants": [
                    {
                        "email": ''+EmailsList[i-1]+''
                    }
                ],
                
                }
            i=i-1
            URL = '' + common.Domain + '' + UrlToAddParticipants + ''
            
            print(data)
          
            response = requests.put(URL, json=data, headers=Parameters)
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
                        #status = 'Failed'
                finally:
                    print('Nothing')
    
            else:
                TestCasesStatus = False
                print("Add Course Excel need not to be Updated")
            