import time
from behave.runner import Context
data = "data.properties.txt"


def loadurl(context: Context):
    file = open(data, "r+")
    url = file.readline()
    file.close()
    context.driver.get(url)

def checkloginstatus(context: Context):
    try:
        assert ("Error message") not in context.driver.page_source
    except AssertionError:
        print("Login failed")
    else:
        print("Login success")


def typeusername(context: Context, username):
    elem1 = context.driver.find_element_by_name('loginUsername')
    elem1.send_keys(username)


def typepassword(context: Context, password):
    elem2 = context.driver.find_element_by_name('loginPassword')
    elem2.send_keys(password)


def attemptlogin(context: Context):
    context.driver.find_element_by_css_selector("button[type='submit']").click()

def waitandquit(context: Context):
    time.sleep(5)
    context.driver.close()