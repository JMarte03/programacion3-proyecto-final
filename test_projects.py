from seleniumbase import BaseCase

class Projects(BaseCase):

    # See
    projs_menu_opt = "/html/body/div[1]/aside[1]/div/ul[2]/li[3]"
    projs_heading = "/html/body/div[1]/div[2]/main/div/h2"

    # Add
    add_pname_input = "/html/body/div[1]/div[2]/main/div/form/div/label[1]/input"
    add_pdescription_input = "/html/body/div[1]/div[2]/main/div/form/div/label[2]/textarea"
    add_proj_btn = "/html/body/div[1]/div[2]/main/div/form/div/div/input"
    
    # Edit 
    edit_proj_btn = "/html/body/div[1]/div[2]/main/div/div/table/tbody/tr/td[4]/div/a/button"
    proj_edit_name_input = "/html/body/form/div/label[1]/input"
    proj_edit_save = "/html/body/form/div/div[1]/input"
    
    # Delete 
    proj_delete_btn = "/html/body/div[1]/div[2]/main/div/div/table/tbody/tr/td[5]/div/a/button"

    
    # TESTS

    def test_see_projs(self):
        self.open(self.workriv_link)
        self.click(self.projs_menu_opt)
        self.assert_element(self.projs_heading)
        self.scroll_to_bottom()
        self.save_screenshot("see_projs_sc", "screenshots")

    def test_add_proj(self):
        self.open(self.workriv_link)
        self.click(self.projs_menu_opt)
        self.assert_element(self.projs_heading)
        self.send_keys(self.add_pname_input, "New project")
        self.send_keys(self.add_pdescription_input, "A project created by somebody")
        self.click(self.add_proj_btn)
        self.scroll_to_bottom()
        self.save_screenshot("add_proj_sc", "screenshots")

    def test_edit_proj(self):
        self.open(self.workriv_link)
        self.click(self.projs_menu_opt)
        self.assert_element(self.projs_heading)
        self.scroll_to_bottom()
        self.click(self.edit_proj_btn)
        self.clear(self.proj_edit_name_input)
        self.send_keys(self.proj_edit_name_input, "Old project")
        self.click(self.proj_edit_save)
        self.save_screenshot("edit_proj_sc", "screenshots")

    def test_delete_proj(self):
        self.open(self.workriv_link)
        self.click(self.projs_menu_opt)
        self.assert_element(self.projs_heading)
        self.scroll_to_bottom()
        self.click(self.proj_delete_btn)
        self.save_screenshot("delete_proj_sc", "screenshots")

    
