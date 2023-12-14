from seleniumbase import BaseCase
import time

class Dashboard(BaseCase):

    workriv_link = "https://workriv-prog3-final-project.000webhostapp.com/"
    index_title = "Workriv Dashboard"
    theme_option = "/html/body/div[1]/div[2]/header/div/li/button"
    dashboard_title = "/html/body/div[1]/div[2]/main/div/h2"

    # DASHBOARD TESTS

    def test_open_page(self):
        self.open(self.workriv_link)
        self.assert_title(self.index_title)
        # self.save_screenshot("open_page_sc", "screenshots")

    def test_change_theme(self):
        self.open(self.workriv_link)
        self.click(self.theme_option)
        # self.save_screenshot("change_theme_sc", "screenshots")

    def test_totals(self):
        self.open("https://workriv-prog3-final-project.000webhostapp.com/index.php")
        self.assert_element(self.dashboard_title)
        # self.save_screenshot("totals_sc", "screenshots")

    def test_pending_tasks(self):
        self.open("https://workriv-prog3-final-project.000webhostapp.com/index.php")
        self.assert_element(self.dashboard_title)
        # self.save_screenshot("pending_tasks_sc", "screenshots")

  
