import re
from playwright.sync_api import Page, expect

'''
1. Test to check if the index page redirects to login page when not logged in.
2. Test if the login page has the correct title and url.
3. Test if the login page contains the login form and all the right elements.
'''

def test_login_page(page: Page):
    page.goto("http://127.0.0.1:5000/")

    # Expect it to redirect to the login page.
    expect(page).to_have_url("http://127.0.0.1:5000/login")
    expect(page).to_have_title("Login Page")

    expect(page.locator("body > form")).to_be_visible()

    expect(page.get_by_role("textbox", name="username")).to_be_visible()
    expect(page.get_by_role("textbox", name="password")).to_be_visible()
    expect(page.get_by_role("button", name="Login")).to_be_visible()

'''
1. Test to check if the index page redirects to login page when not logged in.
2. Test if the login page has the correct title and url.
3. Test to check if login fails when form is empty.  
'''

def test_login_empty_failure(page: Page):
    # Test to check if trying to submit an empty form will fail.
    page.goto("http://127.0.0.1:5000/")

    # Expect it to redirect to the login page.
    expect(page).to_have_url("http://127.0.0.1:5000/login")
    expect(page).to_have_title("Login Page")

    # Click on the submit button.
    page.get_by_role("button", name="Login").click()

    # Expect the page to still be the login page.
    expect(page).to_have_url("http://127.0.0.1:5000/login")
    expect(page).to_have_title("Login Page")

    # Button should be disabled.
    expect(page.get_by_role("button", name="Login")).to_be_disabled()

'''
1. Test to check if the index page redirects to login page when not logged in.
2. Test if the login page has the correct title and url.
3. Test to check if login fails when username is correct but password is wrong.
'''

def test_login_incorrect_password(page: Page):
    # Test to check if trying to submit an incorrect password will fail.
    page.goto("http://127.0.0.1:5000/")

    # Expect it to redirect to the login page.
    expect(page).to_have_url("http://127.0.0.1:5000/login")
    expect(page).to_have_title("Login Page")

    # Fill in the form.
    page.get_by_role("textbox", name="username").fill("admin")
    page.get_by_role("textbox", name="password").fill("wrongPassword123")

    # Click on the submit button.
    page.get_by_role("button", name="Login").click()

     # Expect the page to still be the login page.
    expect(page).to_have_url("http://127.0.0.1:5000/login")
    expect(page).to_have_title("Login Page")

    # Expect the page to have an error message.    
    expect(page.locator("body > div > div")).to_have_text(re.compile(r"Username and password do not match. Please try again."))

'''
1. Test to check if the index page redirects to login page when not logged in.
2. Test if the login page has the correct title and url.
3. Test to check if login fails when username is incorrect.
'''

def test_login_incorrect_username(page: Page):
    # Test to check if trying to submit an incorrect username will fail.
    page.goto("http://127.0.0.1:5000/")

    # Expect it to redirect to the login page.
    expect(page).to_have_url("http://127.0.0.1:5000/login")
    expect(page).to_have_title("Login Page")

    # Fill in the form.
    page.get_by_role("textbox", name="username").fill("admin123")
    page.get_by_role("textbox", name="password").fill("anyPassword123")

    # Click on the submit button.
    page.get_by_role("button", name="Login").click()

     # Expect the page to still be the login page.
    expect(page).to_have_url("http://127.0.0.1:5000/login")
    expect(page).to_have_title("Login Page")

    # Expect the page to have an error message.    
    expect(page.locator("body > div > div")).to_have_text(re.compile(r"Username does not exist. Please sign up and try again."))

'''
1. Test to check if the index page redirects to login page when not logged in.
2. Test if the login page has the correct title and url.
3. Test to check if login is successful.
4. Test if the index page has the correct title and url.
5. Test if the index page contains the welcome message.
6. Test if the index page contains the logout button.
7. Test if the logout button works.
'''    

def test_login_success(page: Page):
    # Test to check if trying to submit an incorrect username will fail.
    page.goto("http://127.0.0.1:5000/")

    # Expect it to redirect to the login page.
    expect(page).to_have_url("http://127.0.0.1:5000/login")
    expect(page).to_have_title("Login Page")

    # Fill in the form.
    page.get_by_role("textbox", name="username").fill("admin")
    page.get_by_role("textbox", name="password").fill("Password123")

    # Click on the submit button.
    page.get_by_role("button", name="Login").click()

    # Expect it to redirect to the index page.
    expect(page).to_have_url("http://127.0.0.1:5000/")
    expect(page).to_have_title("Home Page")

    # Expect the page to have a flash message welcoming the user by their username.
    expect(page.locator("body > section > h3")).to_have_text(re.compile(r"admin"))

    # Expect the page to have a logout button.
    expect(page.get_by_role("button", name="Logout")).to_be_enabled()

    # Click on the logout button.
    page.get_by_role("button", name="Logout").click()

    # Expect it to redirect to the login page.
    expect(page).to_have_url("http://127.0.0.1:5000/login")
    expect(page).to_have_title("Login Page")




   

