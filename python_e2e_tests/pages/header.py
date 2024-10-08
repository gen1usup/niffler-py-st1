from python_e2e_tests.pages.base_logic import BaseLogic


class Header(BaseLogic):
    main_button = "//li[@data-tooltip-id='main']"
    friends_button = "//li[@data-tooltip-id='friends']"
    all_people_button = "//li[@data-tooltip-id='people']"
    profile_button = "//li[@data-tooltip-id='profile']"
    logout_button = "//button[@type='button' and @class='button-icon button-icon_type_logout']"

    def logout(self):
        self.page.wait_for_selector(self.logout_button)
        self.click(self.logout_button)
        return self.page

    def go_main(self):
        self.click(self.main_button)

    def go_friends(self):
        self.click(self.friends_button)

    def go_all_people(self):
        self.click(self.all_people_button)

    def go_profile(self):
        self.click(self.profile_button)
        return self.page

