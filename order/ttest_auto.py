# test_acceptance.py
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

class AcceptanceTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.base_url = "http://localhost:8000"  # Adjust this if your server is running on a different port

    def test_hello_world_view(self):
        driver = self.driver
        driver.get(f"{self.base_url}/hello/")
        self.assertIn("Hello, world!", driver.page_source)

    def test_create_order(self):
        driver = self.driver
        driver.get(f"{self.base_url}/")
        driver.find_element(By.NAME, "title").send_keys("Selenium Order")
        driver.find_element(By.NAME, "price").send_keys("100.00")
        driver.find_element(By.NAME, "poster_phone_number").send_keys("12345678901")
        driver.find_element(By.NAME, "description").send_keys("Order created via Selenium")
        driver.find_element(By.NAME, "category").send_keys("Test Category")
        driver.find_element(By.NAME, "is_digital").click()
        driver.find_element(By.TAG_NAME, "button").click()
        time.sleep(2)  # Wait for the order to be saved
        self.assertIn("Order saved successfully.", driver.page_source)

    def test_search_order(self):
        driver = self.driver
        driver.get(f"{self.base_url}/search/?query=12345678901")
        self.assertIn("Selenium Order", driver.page_source)

    def test_list_orders(self):
        driver = self.driver
        driver.get(f"{self.base_url}/orders/")
        self.assertIn("Selenium Order", driver.page_source)

    def test_mark_order_as_accepted(self):
        driver = self.driver
        # You might need to adjust this part based on how the order ID is handled
        driver.get(f"{self.base_url}/orders/1/mark_accepted/")
        self.assertIn("Order 1 has been marked as accepted.", driver.page_source)

    def test_delete_order(self):
        driver = self.driver
        # You might need to adjust this part based on how the order ID is handled
        driver.get(f"{self.base_url}/orders/1/delete/")
        self.assertIn("Order 1 has been deleted.", driver.page_source)
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
