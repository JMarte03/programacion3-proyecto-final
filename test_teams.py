from seleniumbase import BaseCase

class Teams(BaseCase):

    # See
    teams_menu_opt = "/html/body/div[1]/aside[1]/div/ul[2]/li[2]"
    teams_heading = "/html/body/div[1]/div[2]/main/div/h2"

    # Add
    add_ttitle_input = "/html/body/div[1]/div[2]/main/div/form/div/label[1]/input"
    add_tleader_input = "/html/body/div[1]/div[2]/main/div/form/div/label[2]/input"
    add_tdescription_input = "/html/body/div[1]/div[2]/main/div/form/div/label[3]/textarea"
    add_team_btn = "/html/body/div[1]/div[2]/main/div/form/div/div/input"

    # Edit
    edit_team_btn = "/html/body/div[1]/div[2]/main/div/div/table/tbody/tr[1]/td[5]/div/a/button"
    team_edit_title_input = "/html/body/form/div/label[1]/input"
    team_edit_save = "/html/body/form/div/div[1]/input"

    # Delete
    team_delete_btn = "/html/body/div[1]/div[2]/main/div/div/table/tbody/tr[1]/td[6]/div/a/button"

    
    # TESTS

    def test_see_teams(self):
        self.open(self.workriv_link)
        self.click(self.teams_menu_opt)
        self.assert_element(self.teams_heading)
        self.scroll_to_bottom()
        # self.save_screenshot("see_teams_sc", "screenshots")

    def test_add_team(self):
        self.open(self.workriv_link)
        self.click(self.teams_menu_opt)
        self.assert_element(self.teams_heading)
        self.send_keys(self.add_ttitle_input, "New team")
        self.send_keys(self.add_tleader_input, "Somebody")
        self.send_keys(self.add_tdescription_input, "A team with a function")
        self.click(self.add_team_btn)
        self.scroll_to_bottom()
        # self.save_screenshot("add_team_sc", "screenshots")

    def test_edit_team(self):
        self.open(self.workriv_link)
        self.click(self.teams_menu_opt)
        self.assert_element(self.teams_heading)
        self.scroll_to_bottom()
        self.click(self.edit_team_btn)
        self.clear(self.team_edit_title_input)
        self.send_keys(self.team_edit_title_input, "Old team")
        self.click(self.team_edit_save)
        # self.save_screenshot("edit_team_sc", "screenshots")

    def test_delete_team(self):
        self.open(self.workriv_link)
        self.click(self.teams_menu_opt)
        self.assert_element(self.teams_heading)
        self.scroll_to_bottom()
        self.click(self.team_delete_btn)
        # self.save_screenshot("delete_team_sc", "screenshots")
