'''
Created on 10-Sep-2021

@author: nouman.ijaz
'''

from provisioningapi import test_01_authentication as TokenGeneration
from provisioningapi import test_03_course as Course
from provisioningapi import test_04_user as User
from provisioningapi import test_05_Section as Section
from Settings import CommonFunctions as CF
from provisioningapi import test_06_Group as Group
from pickle import FALSE, TRUE
from configparser import ConfigParser


# from provisioningapi.test_05_Section import AddSection
global DataList, common
DataList = {}
common = CF.CommonFunctions()


class dataStorage():
    
    def AddData(self, MethodName, Header, Body, Resp, URL, resultsmodified=FALSE):
        value = [Header, Body, Resp, URL, resultsmodified]
        key = MethodName
        DataList[key] = value
        
        print(DataList)
        
    def GetAuthToken(self, resultsmodified): 
        
        '''
        @ resultsmodified = TRUE if on calling this function results are modifcated (Put and Delete methods)
        '''
        
        if(DataList.__contains__('testcase_01_GetSessionKey')):
            
            modificationstatus = DataList.get('testcase_01_GetSessionKey')[4]
            
            if(modificationstatus == TRUE):
                AuthTokenGenerationCall = TokenGeneration.GetSessionKey
                AuthToken = AuthTokenGenerationCall.testcase_01_GetSessionKey(common.PrereqTestCasesStatusUpdate)[0]
                print(" AuthToken  in Dictionary got modified,Regenerating AuthToken")
        
            else:
            
                AuthToken = DataList.get('testcase_01_GetSessionKey')[2]['authToken']
                print("Successfully Got AuthToken : " + AuthToken + " from Dictionary")
                
                if(resultsmodified == TRUE):
                    DataList.get('testcase_01_GetSessionKey')[4] = TRUE
           
        else:
            AuthTokenGenerationCall = TokenGeneration.GetSessionKey
            AuthToken = AuthTokenGenerationCall.testcase_01_GetSessionKey(common.PrereqTestCasesStatusUpdate)[0]
            if(resultsmodified == TRUE):
                    DataList.get('testcase_01_GetSessionKey')[4] = TRUE
        return AuthToken
    
    def GetTeacherSubID(self, resultsmodified):
        '''
        @ resultsmodified = TRUE if on calling this function results in modifcation of the return values (Put and Delete methods)
        '''
        
        if(DataList.__contains__('testcase_01_GetSessionKey')):
            modificationstatus = DataList.get('testcase_01_GetSessionKey')[4]
            
            if(bool(modificationstatus) == TRUE):
                AuthTokenGenerationCall = TokenGeneration.GetSessionKey
                subscriptionsettingsidTeacher = AuthTokenGenerationCall.testcase_01_GetSessionKey(common.PrereqTestCasesStatusUpdate)[1]
            
            else:
            
                subscriptionsettingsidTeacher = DataList.get('testcase_01_GetSessionKey')[2]['subscriptionsettings'][1]['id']
                print("Successfully Got subscriptionsettingsidTeacher : " + subscriptionsettingsidTeacher + " from Dictionary")
                if(resultsmodified == TRUE):
                    DataList.get('testcase_01_GetSessionKey')[4] = TRUE
           
        else:
            AuthTokenGenerationCall = TokenGeneration.GetSessionKey
            subscriptionsettingsidTeacher = AuthTokenGenerationCall.testcase_01_GetSessionKey(common.PrereqTestCasesStatusUpdate)[1]
            if(resultsmodified == TRUE):
                    DataList.get('testcase_01_GetSessionKey')[4] = TRUE
        return subscriptionsettingsidTeacher
    
    def GetStudentSubID(self, resultsmodified):
        '''
        @ resultsmodified = TRUE if on calling this function results in modifcation of the return values (Put and Delete methods)
        '''
        
        if(DataList.__contains__('testcase_01_GetSessionKey')):
            modificationstatus = DataList.get('testcase_01_GetSessionKey')[4]
            if(bool(modificationstatus) == TRUE):
                AuthTokenGenerationCall = TokenGeneration.GetSessionKey
                subscriptionsettingsidStudent = AuthTokenGenerationCall.testcase_01_GetSessionKey(common.PrereqTestCasesStatusUpdate)[2]
                
            else: 
                subscriptionsettingsidStudent = DataList.get('testcase_01_GetSessionKey')[2]['subscriptionsettings'][0]['id']
                print("Successfully Got subscriptionsettingsidStudent : " + subscriptionsettingsidStudent + " from Dictionary")
                if(resultsmodified == TRUE):
                    DataList.get('testcase_01_GetSessionKey')[4] = TRUE
           
        else:
            AuthTokenGenerationCall = TokenGeneration.GetSessionKey
            subscriptionsettingsidStudent = AuthTokenGenerationCall.testcase_01_GetSessionKey(common.PrereqTestCasesStatusUpdate)[2]
            if(resultsmodified == TRUE):
                    DataList.get('testcase_01_GetSessionKey')[4] = TRUE
        return subscriptionsettingsidStudent
    
    def GetOrganizationID(self, resultsmodified):
        '''
        @ resultsmodified = TRUE if on calling this function results in modifcation of the return values (Put and Delete methods)
        '''
        
        if(DataList.__contains__('testcase_01_GetSessionKey')):
            modificationstatus = DataList.get('testcase_01_GetSessionKey')[4]
            
            if(bool(modificationstatus) == TRUE):
                AuthTokenGenerationCall = TokenGeneration.GetSessionKey
                organizationid = AuthTokenGenerationCall.testcase_01_GetSessionKey(common.PrereqTestCasesStatusUpdate)[3]
            
            else:
            
                organizationid = DataList.get('testcase_01_GetSessionKey')[2]['organization']['id']
                print("Successfully Got organizationid : " + organizationid + " from Dictionary")
                if(resultsmodified == TRUE):
                    DataList.get('testcase_01_GetSessionKey')[4] = TRUE
           
        else:
            AuthTokenGenerationCall = TokenGeneration.GetSessionKey
            organizationid = AuthTokenGenerationCall.testcase_01_GetSessionKey(common.PrereqTestCasesStatusUpdate)[3]
            if(resultsmodified == TRUE):
                    DataList.get('testcase_01_GetSessionKey')[4] = TRUE
        return organizationid
    
    def GetCourseID(self, resultsmodified):
        '''
        @ resultsmodified = TRUE if on calling this function results in modifcation of the return values (Put and Delete methods)
        '''
        
        if(DataList.__contains__('testcase_01_AddCourse')):
            modificationstatus = DataList.get('testcase_01_AddCourse')[4]
            
            if(modificationstatus == TRUE):
                AddCourseCall = Course.AddCourse
                CourseId = AddCourseCall.testcase_01_AddCourse(common.PrereqTestCasesStatusUpdate)
            else:
            
                CourseId = DataList.get('testcase_01_AddCourse')[2]['courseid']
                print("Successfully Got CourseId : " + CourseId + " from Dictionary")
                if(resultsmodified == TRUE):
                    DataList.get('testcase_01_AddCourse')[4] = TRUE
                
        else:
            AddCourseCall = Course.AddCourse
            CourseId = AddCourseCall.testcase_01_AddCourse(common.PrereqTestCasesStatusUpdate)
            if(resultsmodified == TRUE):
                DataList.get('testcase_01_AddCourse')[4] = TRUE
        
        print(CourseId)
        return CourseId
    
    def GetTeacherDetails(self, resultsmodified, DataRequired):
        '''
        @ resultsmodified = TRUE if on calling this function results in modifcation of the return values (Put and Delete methods)
        '''
        
        if(DataList.__contains__('testcase_01_AddUserAsTeacher')):
            
            modificationstatus = DataList.get('testcase_01_AddUserAsTeacher')[4]
            
            if(modificationstatus == TRUE):
                
                AddUserCall = User.AddUser
                Email, firstName, lastName, role = AddUserCall.testcase_01_AddUserAsTeacher(common.PrereqTestCasesStatusUpdate)
                print('Teachers Details got Modifed, Generating New User as Teaher')
            else:
                
                Email = DataList.get('testcase_01_AddUserAsTeacher')[1][0]['email']
                firstName = DataList.get('testcase_01_AddUserAsTeacher')[1][0]['firstname']
                lastName = DataList.get('testcase_01_AddUserAsTeacher')[1][0]['lastname']
                role = DataList.get('testcase_01_AddUserAsTeacher')[1][0]['role']
                print("Successfully Got TeacherDetails from Dictionary")
                if(resultsmodified == TRUE):
                    DataList.get('testcase_01_AddUserAsTeacher')[4] = TRUE
           
        else:
            AddUserCall = User.AddUser
            Email, firstName, lastName, role = AddUserCall.testcase_01_AddUserAsTeacher(common.PrereqTestCasesStatusUpdate)
            if(resultsmodified == TRUE):
                DataList.get('testcase_01_AddUserAsTeacher')[4] = TRUE
        
        if(DataRequired.lower().__contains__("email")):
            print(Email)
            return Email
        
        if(DataRequired.lower().__contains__("firstname")):
            print(firstName)
            return firstName
        
        if(DataRequired.lower().__contains__("lastname")):
            print(lastName)
            return lastName
        if(DataRequired.lower().__contains__("role")):
            print(role)
            return role
        else:
            print("Required Data incorrect_Add Teacher" + DataRequired)
            
    def GetStudentDetails(self, resultsmodified, DataRequired):
        '''
        @ resultsmodified = TRUE if on calling this function results in modifcation of the return values (Put and Delete methods)
        '''
        
        if(DataList.__contains__('testcase_02_AddUserAsStudent')):
            
            modificationstatus = DataList.get('testcase_02_AddUserAsStudent')[4]
            
            if(modificationstatus == TRUE):
                
                AddUserCall = User.AddUser
                Email, firstName, lastName, role = AddUserCall.testcase_02_AddUserAsStudent(common.PrereqTestCasesStatusUpdate)
                print('Students Details got Modifed, Generating New User as Student')
            else:
                
                Email = DataList.get('testcase_02_AddUserAsStudent')[1][0]['email']
                firstName = DataList.get('testcase_02_AddUserAsStudent')[1][0]['firstname']
                lastName = DataList.get('testcase_02_AddUserAsStudent')[1][0]['lastname']
                role = DataList.get('testcase_02_AddUserAsStudent')[1][0]['role']
                print("Successfully Got StudentDetails from Dictionary")
                if(resultsmodified == TRUE):
                    DataList.get('testcase_02_AddUserAsStudent')[4] = TRUE
           
        else:
            AddUserCall = User.AddUser
            Email, firstName, lastName, role = AddUserCall.testcase_02_AddUserAsStudent(common.PrereqTestCasesStatusUpdate)
            if(resultsmodified == TRUE):
                DataList.get('testcase_02_AddUserAsStudent')[4] = TRUE
        
        if(DataRequired.lower().__contains__("email")):
            print(Email)
            return Email
        if(DataRequired.lower().__contains__("firstname")):
            print(firstName)
            return firstName
        if(DataRequired.lower().__contains__("lastname")):
            print(lastName)
            return lastName
        if(DataRequired.lower().__contains__("role")):
            print(role)
            return role
        else:
            print("Required Data incorrect_Add Student" + DataRequired)

    def GetSectionDetails(self, resultsmodified, DataRequired):
        
        '''
        @ resultsmodified = TRUE if on calling this function results in modifcation of the return values (Put and Delete methods)
        '''
        
        if(DataList.__contains__('testcase_01_AddSection')):
            
            modificationstatus = DataList.get('testcase_01_AddSection')[4]
            
            if(modificationstatus == TRUE):
                
                AddSectionCall = Section.AddSection
                SectionID, CourseId = AddSectionCall.testcase_01_AddSection(common.PrereqTestCasesStatusUpdate)
                print('Section Details got Modifed, Generating New Section')
            else:
                
                SectionID = DataList.get('testcase_01_AddSection')[2]['sectionid']
                CourseId = DataList.get('testcase_01_AddSection')[1]['courseid']
               
                print("Successfully Got SectionDetails from Dictionary")
                if(resultsmodified == TRUE):
                    DataList.get('testcase_01_AddSection')[4] = TRUE
           
        else:
            SectionID, CourseId = AddSectionCall.testcase_01_AddSection(common.PrereqTestCasesStatusUpdate)
            if(resultsmodified == TRUE):
                DataList.get('testcase_01_AddSection')[4] = TRUE
        
        if(DataRequired.lower().__contains__("sectorid")):
            print(SectionID)
            return SectionID
        if(DataRequired.lower().__contains__("courseid")):
            print(CourseId)
            return CourseId

        else:
            print("Required Data incorrect_Section  Details  " + DataRequired)

    def GetSectionUserDetails(self, resultsmodified, DataRequired):
        
        if(DataList.__contains__('testcase_02_AddSectionUser')):
            
            modificationstatus = DataList.get('testcase_02_AddSectionUser')[4]
            
            if(modificationstatus == TRUE):
                
                AddSectionCall = Section.AddSection
                SectionID, email = AddSectionCall.testcase_02_AddSectionUser(common.PrereqTestCasesStatusUpdate)
                print('SectionUser Details got Modifed, Generating New SectionUser')
            else:
                
                SectionID = DataList.get('testcase_02_AddSectionUser')[1]['sectionid']
                email = DataList.get('testcase_02_AddSectionUser')[1]['useremail']
               
                print("Successfully Got SectionUserDetails from Dictionary")
                if(resultsmodified == TRUE):
                    DataList.get('testcase_02_AddSectionUser')[4] = TRUE
           
        else:
            AddSectionCall = Section.AddSection
            SectionID, email = AddSectionCall.testcase_02_AddSectionUser(common.PrereqTestCasesStatusUpdate)
            if(resultsmodified == TRUE):
                    DataList.get('testcase_01_AddSection')[4] = TRUE
        
        if(DataRequired.lower().__contains__("sectionid")):
            print(SectionID)
            return SectionID
        if(DataRequired.lower().__contains__("email")):
            print(email)
            return email

        else:
            print("Required Data incorrect_Section User Details  " + DataRequired)
    
    def GetMeetingID(self, resultsmodified):
        '''
        @ resultsmodified = TRUE if on calling this function results in modifcation of the return values (Put and Delete methods)
        '''
        
        if(DataList.__contains__('testcase_01_AddGroup')):
            modificationstatus = DataList.get('testcase_01_AddGroup')[4]
            
            if(modificationstatus == TRUE):
                AddGroupCall = Group.AddMeeting
                MeetingID, Email = AddGroupCall.testcase_01_AddGroup(common.PrereqTestCasesStatusUpdate)
            else:
            
                MeetingID = DataList.get('testcase_01_AddGroup')[2]['meetingid']
                Email = DataList.get('testcase_01_AddGroup')[1]['participants'][0]['email']
                print("Successfully Got MeetingID : " + MeetingID + " from Dictionary")
                if(resultsmodified == TRUE):
                    DataList.get('testcase_01_AddGroup')[4] = TRUE
                
        else:
            AddGroupCall = Group.AddMeeting
            MeetingID, Email = AddGroupCall.testcase_01_AddGroup(common.PrereqTestCasesStatusUpdate)
            if(resultsmodified == TRUE):
                DataList.get('testcase_01_AddGroup')[4] = TRUE
        
        print(MeetingID, Email)
        return MeetingID, Email
    
    def ReadDataFromDataFile(self,section, key):
            
            file= common.datainifilepath
            config = ConfigParser()
            config.read(file)
            
            value= config[section][key]
            
            return value
        
    
    
    def WriteDataToDataFile(self,secton,key, value):
        
        file= common.datainifilepath
        
        config = ConfigParser()
        config.read(file)
        
        config.set(secton, key, str(value).replace("'","").replace(" ",""))
        with open(file,'w') as configfile:
            config.write(configfile)   
            # p.store(f, encoding="utf-8")
        

