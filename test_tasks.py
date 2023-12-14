from seleniumbase import BaseCase

class Pruebas(BaseCase):

    # See
    tks_menu_opt = "/html/body/div[1]/aside[1]/div/ul[2]/li[4]"
    tks_heading = "/html/body/div[1]/div[2]/main/div/h2"

    # Add
    add_ktitle_input = "/html/body/div[1]/div[2]/main/div/form/div/label[1]/input"
    add_kproject_input = "/html/body/div[1]/div[2]/main/div/form/div/label[2]/input"
    add_kemp_input = "/html/body/div[1]/div[2]/main/div/form/div/label[3]/input"
    add_tks_btn = "/html/body/div[1]/div[2]/main/div/form/div/div/input"
    
    # Edit
    tks_edit_btn = "/html/body/div[1]/div[2]/main/div/div/div/table/tbody/tr/td[6]/div/a/button"
    tks_edit_title_input = "/html/body/form/div/label[1]/input"
    tks_edit_save = "/html/body/form/div/div[1]/input"
    
    # Delete
    tks_delete_btn = "/html/body/div[1]/div[2]/main/div/div/div/table/tbody/tr/td[7]/div/a/button"

    # TESTS

    def test_see_tks(self):
        self.open(self.workriv_link)
        self.click(self.tks_menu_opt)
        self.assert_element(self.tks_heading)
        self.scroll_to_bottom()
        self.save_screenshot("see_tks_sc", "screenshots")

    def test_add_tks(self):
        self.open(self.workriv_link)
        self.click(self.tks_menu_opt)
        self.assert_element(self.tks_heading)
        self.send_keys(self.add_ktitle_input, "New task")
        self.send_keys(self.add_kproject_input, "Belongs to a certain project")
        self.send_keys(self.add_kemp_input, "Assigned to somebody")
        self.click(self.add_tks_btn)
        self.scroll_to_bottom()
        self.save_screenshot("add_tks_sc", "screenshots")

    def test_edit_tks(self):
        self.open(self.workriv_link)
        self.click(self.tks_menu_opt)
        self.assert_element(self.tks_heading)
        self.scroll_to_bottom()
        self.click(self.tks_edit_btn)
        self.clear(self.tks_edit_title_input)
        self.send_keys(self.tks_edit_title_input, "Old task")
        self.click(self.tks_edit_save)
        self.save_screenshot("edit_tks_sc", "screenshots")

    def test_delete_tks(self):
        self.open(self.workriv_link)
        self.click(self.tks_menu_opt)
        self.assert_element(self.tks_heading)
        self.scroll_to_bottom()
        self.click(self.tks_delete_btn)
        self.save_screenshot("delete_tks_sc", "screenshots")
