from behave import *
from common.test_common import (loadurl, typeusername, typepassword, attemptlogin, checkloginstatus, waitandquit)
from behave.runner import Context

@given("User with correct credentials try’s to login into the portal")
def loadingurl(context: Context):
    loadurl(context)

@when(u"I type the correct data <Username> in the email field and type <Password> in the password field")
def typingcorrectusername(context:Context):
    typeusername(context,context.table[0][0])
    typepassword(context,context.table[0][1])

@when(u'I press the "Login" button with correct data')
def loginwithcorrectdata(context: Context):
    attemptlogin(context)


@then(u'I am successfully logged in and see the message  “Successfully logged in”')
def loginresultwithcorrectdata(context: Context):
    checkloginstatus(context)

@given("User with incorrect credentials try’s to login into the portal")
def loadingurl(context: Context):
    loadurl(context)

@when(u"I type the incorrect data <Username> in the email field and type <Password> in the password field")
def typingcorrectusername(context:Context):
    typeusername(context,context.table[0][0])
    typepassword(context,context.table[0][1])

@when(u'I press the "Login" button with incorrect data')
def loginwithcorrectdata(context: Context):
    attemptlogin(context)

@then(u'I am not successfully logged in and see the message  “error message”')
def loginresultwithcorrectdata(context: Context):
    checkloginstatus(context)