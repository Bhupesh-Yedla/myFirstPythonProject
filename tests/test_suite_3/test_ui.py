
import time
import unittest
import allure
from allure_commons._allure import attach
from allure_commons.types import AttachmentType
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
    
    
    @unittest.skip
    @allure.title("Get leader details and verify latest")
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
        btn_i_agree = self.driver.find_element(By.XPATH,"//*[@id='onetrust-accept-btn-handler']")
        btn_i_agree.click()
        elem_leader_name.click()
        time.sleep(2)
        elem_description = self.driver.find_element(By.XPATH,"(//p[contains(text(),'Leonard Livschit')])[2]/../../following-sibling::div[1]/p")
        text = "director of Grid Dynamics’ board of directors since 2006 and the Chief Executive Officer of Grid Dynamics since 2014"
        time.sleep(1)
        assert text in elem_description.text
    
    @unittest.skip
    def test_filter_topic(self):
        filter = self.driver.find_element(By.CLASS_NAME,"filterwrap").find_element(By.XPATH,"//b")
        assert filter.is_displayed
        select_topic_filter = self.driver.find_element(By.ID,"topiclist")
        select_topic_filter.click()
        time.sleep(1)
        select_topic_cloud = self.driver.find_element(By.XPATH,"//div[@id='topiclist']//span[contains(text(),'Cloud and DevOps')]")
        select_topic_cloud.click()
        time.sleep(2)
        list_articles_cloud = self.driver.find_elements(By.XPATH,"//a[contains(text(),'Cloud and DevOps')]/..//following-sibling::div//article")
        no_of_articles = len(list_articles_cloud)
        first_article_in_cloud_topic_text = self.driver.find_element(By.XPATH,"(//a[contains(text(),'Cloud and DevOps')]/../following-sibling::div//article/div[@class='cardbody'])[1]/h4").text
        assert no_of_articles>1
        select_topic_filter.click()
        time.sleep(2)
        select_all_topic = self.driver.find_element(By.XPATH,"//div[@id='topiclist']//span[contains(text(),'All topics')]")
        select_all_topic.click()
        time.sleep(2)
        first_article_in_all_topics_text = self.driver.find_element(By.XPATH,"//a[contains(text(),'Media and News')]/../following-sibling::div//article/preceding-sibling::img").get_attribute("alt")
        assert first_article_in_cloud_topic_text != first_article_in_all_topics_text
        list_articles_all_topics = self.driver.find_elements(By.XPATH,"//a[contains(text(),'Media and News')]/../following-sibling::div//article")
        assert len(list_articles_all_topics)>1


    def test_contact_page(self):
        btn_get_in_touch = self.driver.find_element(By.XPATH,"(//a[contains(@class,'contact-button')])[1]")
        btn_get_in_touch.click()
        time.sleep(2)
        elem_get_in_touch = self.driver.find_element(By.XPATH,"//*[@id='get-in-touch-form']/div[2]/h2")
        assert elem_get_in_touch.is_displayed

        textfield_first_name = self.driver.find_element(By.XPATH,"//label[contains(text(),'First name')]/following-sibling::span/input")
        textfield_last_name = self.driver.find_element(By.XPATH,"//label[contains(text(),'Last name')]/following-sibling::span/input")
        textfield_email = self.driver.find_element(By.XPATH,"//label[contains(text(),'E-mail')]/following-sibling::span/input")

        textfield_first_name.send_keys("Bhupesh")
        textfield_last_name.send_keys("Yedla")
        textfield_email.send_keys("byedla@griddynamics.com")
        time.sleep(1)
        dropdown_hear_about_us = self.driver.find_element(By.XPATH,"//label[contains(text(),'How did you hear about us?*')]/following-sibling::div")
        dropdown_hear_about_us.click()
        time.sleep(1)
        dropdown_online_ads = self.driver.find_element(By.XPATH,"//label[contains(text(),'How did you hear about us?*')]/following-sibling::div/div[2]/div[contains(text(),'Online Ads')]")
        dropdown_online_ads.click()
        time.sleep(1)
        checkbox_allow_griddynamics = self.driver.find_element(By.XPATH,"//input[@value='I allow Grid Dynamics to contact me.*']/following-sibling::span")
        checkbox_allow_griddynamics.click()
        time.sleep(1)
        btn_submit = self.driver.find_element(By.XPATH,"//input[@value='Submit']")
        assert not btn_submit.is_enabled()


    def tearDown(self):
        self.driver.quit()


if __name__=="__main__":
    unittest.main()

