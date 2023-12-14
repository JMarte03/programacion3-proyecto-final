from seleniumbase import BaseCase

class Employees(BaseCase):

    # See
    emp_menu_opt = "/html/body/div[1]/aside[1]/div/ul[2]/li[1]"
    emp_heading = "/html/body/div[1]/div[2]/main/div/h2"

    # Add
    add_name_input = "/html/body/div[1]/div[2]/main/div/form/div/label[1]/input"
    add_lname_input = "/html/body/div[1]/div[2]/main/div/form/div/label[2]/input"
    add_role_input = "/html/body/div[1]/div[2]/main/div/form/div/label[3]/input"
    add_email_input = "/html/body/div[1]/div[2]/main/div/form/div/label[4]/input"
    add_team_input = "/html/body/div[1]/div[2]/main/div/form/div/label[5]/input"
    add_emp_btn = "/html/body/div[1]/div[2]/main/div/form/div/div/input"
    
    # Edit
    emp_edit_btn = "/html/body/div[1]/div[2]/main/div/div/div/table/tbody/tr[1]/td[7]/div/a/button"
    emp_edit_name_input = "/html/body/form/div/label[1]/input"
    emp_edit_save = "/html/body/form/div/div[1]/input"
    
    # Delete
    emp_delete_btn = "/html/body/div[1]/div[2]/main/div/div/div/table/tbody/tr[1]/td[8]/div/a/button"

    # TESTS

    def test_see_emps(self):
        self.open(self.workriv_link)
        self.click(self.emp_menu_opt)
        self.assert_element(self.emp_heading)
        self.scroll_to_bottom()
        self.save_screenshot("see_emps_sc", "screenshots")

    def test_add_emp(self):
        self.open(self.workriv_link)
        self.click(self.emp_menu_opt)
        self.assert_element(self.emp_heading)
        self.send_keys(self.add_name_input, "Jhon")
        self.send_keys(self.add_lname_input, "Miller")
        self.send_keys(self.add_role_input, "Frontend Developer")
        self.send_keys(self.add_email_input, "jhon@gmail.com")
        self.send_keys(self.add_team_input, "Web Dev Team")
        self.click(self.add_emp_btn)
        self.scroll_to_bottom()
        self.save_screenshot("add_emp_sc", "screenshots")

    def test_edit_emp(self):
        self.open(self.workriv_link)
        self.click(self.emp_menu_opt)
        self.assert_element(self.emp_heading)
        self.scroll_to_bottom()
        self.click(self.emp_edit_btn)
        self.clear(self.emp_edit_name_input)
        self.send_keys(self.emp_edit_name_input, "Mark")
        self.click(self.emp_edit_save)
        self.save_screenshot("edit_emp_sc", "screenshots")

    def test_delete_emp(self):
        self.open(self.workriv_link)
        self.click(self.emp_menu_opt)
        self.assert_element(self.emp_heading)
        self.scroll_to_bottom()
        self.click(self.emp_delete_btn)
        self.save_screenshot("delete_emp_sc", "screenshots")
