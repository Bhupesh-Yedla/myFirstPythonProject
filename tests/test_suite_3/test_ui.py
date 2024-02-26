
import time
import unittest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUsersUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("https://blog.griddynamics.com")
        self.driver.maximize_window()
    
    @allure.title("Get leader details and verify")
    def test_leader_details(self):
        actions = ActionChains(self.driver)
        elem_about = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,"(//a[contains(text(),'About')])[1]")))
        actions.move_to_element(elem_about).perform()
        time.sleep(2)
        elem_leadership = self.driver.find_element(By.XPATH,"//span[contains(text(),'Leadership')]/..")
        self.driver.execute_script("arguments[0].scrollIntoView(true);",elem_leadership) 
        self.driver.execute_script("arguments[0].click();",elem_leadership) 
        time.sleep(2)
        elem_leader_name = self.driver.find_element(By.XPATH,"(//p[contains(text(),'Leonard Livschit')])[1]")
        elem_leader_name.click()
        time.sleep(2)
        elem_description = self.driver.find_element(By.XPATH,"(//p[contains(text(),'Leonard Livschit')])[2]/../../following-sibling::div[1]/p")
        text = "director of Grid Dynamics’ board of directors since 2006 and the Chief Executive Officer of Grid Dynamics since 2014"
        time.sleep(1)
        assert text in elem_description.text

    def tearDown(self):
        self.driver.quit()


if __name__=="__main__":
    unittest.main()

