@echo off
setlocal EnableDelayedExpansion

	if "%$ecbId%" == "" (
		:Proc1
		echo Enter '1' to Execute whole Project
		echo Enter '2' to Execute any single module
		echo Enter '3' to Execute Complete CustomCalls Project
		echo Enter anything else to abort.
		echo.
		set "UserChoice=abort"
		set /P "UserChoice=Type input: "
		
		if "!UserChoice!"=="1" (
			pytest -v E:\Automation\workspace\ClassroomAPI\provisioningapi
		)
		if "!UserChoice!"=="3" (
			pytest -v E:\Automation\workspace\ClassroomAPI\CustomCalls
		)
		if "!UserChoice!"=="2" (
			
			:Proc2
			echo Single Modules List
			echo Enter '3' to Execute Authentication
			echo Enter '4' to Execute Organization
			echo Enter '5' to Execute Course
			echo Enter '6' to Execute User
			echo Enter '7' to Execute Section 
			echo Enter '8' to Execute Group
			echo Enter '9' to Add Users from INI file
			echo Enter '10' to Add Course from INI file
			echo Enter '11' to Add Section from INI file
			echo Enter '12' to Add UsersInSection from INI file
			echo Enter '13' to Add Meeting from INI file
			echo Enter '14' to Add UsersInMeeting from INI file
			echo Enter anything else to abort
			echo Enter 'r' to return main menu
			echo.
			set "UserChoice=abort"
			set /P "UserChoice=Type input: "
			if "%$ecbId%" == "" (
			
				if "!UserChoice!"=="3" (
					pytest -v E:\Automation\workspace\ClassroomAPI\provisioningapi\test_01_authentication.py
					goto :Proc2
				)
				if "!UserChoice!"=="4" (
					pytest -v E:\Automation\workspace\ClassroomAPI\provisioningapi\test_02_organization.py
					goto :Proc2
				)
				if "!UserChoice!"=="5" (
					pytest -v E:\Automation\workspace\ClassroomAPI\provisioningapi\test_03_course.py
					goto :Proc2
				)
				if "!UserChoice!"=="6" (
					pytest -v E:\Automation\workspace\ClassroomAPI\provisioningapi\test_04_user.py
					goto :Proc2
				)
				if "!UserChoice!"=="7" (
					pytest -v E:\Automation\workspace\ClassroomAPI\provisioningapi\test_05_Section.py
					goto :Proc2
				)
				if "!UserChoice!"=="8" (
					pytest -v E:\Automation\workspace\ClassroomAPI\provisioningapi\test_06_Group.py
					goto :Proc2
				)
				if "!UserChoice!"=="9" (
					pytest -rA E:\Automation\workspace\ClassroomAPI\CustomCalls\test_01_AddUsers.py
					goto :Proc2
				)
				if "!UserChoice!"=="10" (
					pytest -rA E:\Automation\workspace\ClassroomAPI\CustomCalls\test_02_AddCourse.py
					goto :Proc2
				)
				if "!UserChoice!"=="11" (
					pytest -rA E:\Automation\workspace\ClassroomAPI\CustomCalls\test_03_AddSection.py
					goto :Proc2
				)
				if "!UserChoice!"=="12" (
					pytest -rA E:\Automation\workspace\ClassroomAPI\CustomCalls\test_04_AddUserInSection.py
					goto :Proc2
				)
				if "!UserChoice!"=="13" (
					pytest -rA E:\Automation\workspace\ClassroomAPI\CustomCalls\test_05_AddMeeting.py
					goto :Proc2
				)
				if "!UserChoice!"=="14" (
					pytest -rA E:\Automation\workspace\ClassroomAPI\CustomCalls\test_06_AddUsersInMeeting.py
					goto :Proc2
				)
				if not "!UserChoice!"=="1" (
					if not "!UserChoice!"=="2" (
						if not "!UserChoice!"=="3" (
							if not "!UserChoice!"=="4" (
								if not "!UserChoice!"=="5" (
									if not "!UserChoice!"=="6" (
										if not "!UserChoice!"=="7" (
											if not "!UserChoice!"=="8" (
												if not "!UserChoice!"=="9" (
													if not "!UserChoice!"=="10" (
														if not "!UserChoice!"=="11" (
															if not "!UserChoice!"=="12" (
																if not "!UserChoice!"=="13" (
																	if not "!UserChoice!"=="14" (
																		echo Unknown input ... Aborting script
																		timeout 5
																		exit /B 500
																	)	
																)	
															)	
														)	
													)	
												)	
											)
										)	
									)
								)
							)
						)
					)
				)
			)
		)
	)
endlocal
pause
				