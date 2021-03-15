from selenium import webdriver
import time
import datetime
import unittest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class test_Pokemon_Encyclopedia(unittest.TestCase):

    def setUp(self):
        print("Test Execution started at:" + str(datetime.datetime.now()))
        self.driver = webdriver.Chrome(executable_path="../Browser_Drivers/chromedriver")
        self.driver.get("https://bulbapedia.bulbagarden.net/wiki/Main_Page")
        time.sleep(5)
        self.driver.save_screenshot("../Screenshots/Bulbapedia_Main_Page.png")

    def test_Communities_Events_Filter_Results(self):
        time.sleep(5)
        self.driver.find_element_by_xpath("//*[@id='tyche_cmp_modal']/div/div/div/div[5]/div[2]/a/span[text()='Continue to Site']").click()
        time.sleep(5)
        self.driver.find_element_by_id("searchInput").send_keys("communities and events")
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()
        time.sleep(3)
        self.driver.save_screenshot("../Screenshots/Communities_Events.png")
        self.driver.find_element_by_link_text("Advanced").click()
        time.sleep(2)
        self.driver.save_screenshot("../Screenshots/Advanced_Settings.png")
        self.driver.find_element_by_xpath("//label[text()='Bulbapedia talk']/../input").click()
        self.driver.find_element_by_xpath("//label[text()='Bulbapedia']/../input").click()
        self.driver.find_element_by_xpath("//span[text()='Search']").click()
        time.sleep(10)

    def test_Verify_Pokemon_Names_Starting_Y(self):
        time.sleep(5)
        self.driver.find_element_by_xpath("//*[@id='tyche_cmp_modal']/div/div/div/div[5]/div[2]/a/span[text()='Continue to Site']").click()
        time.sleep(5)
        self.driver.find_element_by_id("searchInput").send_keys("List of Pokémon by name")
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()
        time.sleep(2)
        self.driver.save_screenshot("../Screenshots/Listofpokemon_names.png")
        self.driver.find_element_by_xpath("//*[@id='mw-content-text']/div[1]/div[2]/a[26]").click()
        self.driver.save_screenshot("../Screenshots/Listofnames_startswith_Y.png")
        time.sleep(2)
        print("Names starting with Y has been listed")

    def tearDown(self):
        self.driver.close()
        print("Test Execution Finished at:" + str(datetime.datetime.now()))


if __name__ == "__main__":
    unittest.main(verbosity=2)





