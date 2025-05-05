from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given("I open the login page")
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get("https://example.com/login")  # Změň na reálnou URL
    time.sleep(1)

@when("I enter valid credentials")
def step_impl(context):
    context.browser.find_element(By.ID, "username").send_keys("testuser")
    context.browser.find_element(By.ID, "password").send_keys("testpass")
    context.browser.find_element(By.ID, "login").click()
    time.sleep(1)

@then("I should see the dashboard")
def step_impl(context):
    assert "dashboard" in context.browser.current_url
    context.browser.quit()

