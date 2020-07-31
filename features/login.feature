Feature: Login

	Scenario: Successful login when appropriate credentials are provided
		Given User with correct credentials try’s to login into the portal
		When I type the correct data <Username> in the email field and type <Password> in the password field
			| Username          | Password  |
			| test@qa-experience.com | Password1 |
		And I press the "Login" button with correct data
		Then I am successfully logged in and see the message  “Successfully logged in”

	Scenario: Unsuccessful login when inappropriate credentials are provided
		Given User with incorrect credentials try’s to login into the portal
		When I type the incorrect data <Username> in the email field and type <Password> in the password field
			| Username          | Password  |
			| test1qa-experience.com | Password1 |
		And I press the "Login" button with incorrect data
		Then I am not successfully logged in and see the message  “error message”


