from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time

my_email = "your email"
my_password = "your password"

chrome_path = "C:/Users/ccesports2/Development/chromedriver"

driver = webdriver.Chrome(chrome_path)

driver.get("https://tinder.com/app/recs")
driver.maximize_window()

log_in = driver.find_element_by_xpath(
    '//*[@id="c-690079234"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
log_in.click()

cookies = driver.find_element_by_xpath(
    '//*[@id="c-690079234"]/div/div[2]/div/div/div[1]/button')
cookies.click()

time.sleep(3)

facebook_log_in = driver.find_element_by_xpath(
    '//*[@id="c1564682258"]/div/div/div[1]/div/div[3]/span/div[2]/button')
facebook_log_in.click()

time.sleep(3)

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

email = driver.find_element_by_id("email")
email.send_keys(my_email)

password = driver.find_element_by_id("pass")
password.send_keys(my_password)

log_in_button = driver.find_element_by_name("login")
log_in_button.click()

time.sleep(3)

driver.switch_to.window(base_window)
print(driver.title)

time.sleep(3)

location_allow = driver.find_element_by_xpath('//*[@id="c1564682258"]/div/div/div/div/div[3]/button[1]')
location_allow.click()

time.sleep(3)
not_disallow = driver.find_element_by_xpath('//*[@id="c1564682258"]/div/div/div/div/div[3]/button[2]')
not_disallow.click()

dislike = driver.find_element_by_xpath(
    '//*[@id="c-690079234"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button')

timeout = time.time() + 60
while time.time() < timeout:

    time.sleep(2)

    dislike.click()

    time.sleep(2)
