from Domoblaze_Web.Page.contact_page import Contact
import allure
import pytest
class Test_Contact():
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_contact_valid(self):
        contact = Contact()
        contact.open()
        contact.Contact_Link()
        contact.Contact_Email()
        contact.Contact_Name()
        contact.Contact_Message()
        contact.Send_Button()
        CHECK = contact.Switch_Alert
        assert 'Thanks for the message!!' == CHECK


    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_contact_invalid_name(self):
        contact = Contact()
        contact.open()
        contact.Contact_Link()
        contact.Contact_Email()
        contact.Contact_Invalid_Name()
        contact.Contact_Message()
        contact.Send_Button()
        CHECK = contact.Switch_Alert
        assert 'Thanks for the mes' == CHECK


    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_contact_invalid_email(self):
        contact = Contact()
        contact.open()
        contact.Contact_Link()
        contact.Contact_Email()
        contact.Contact_Invalid_Name()
        contact.Contact_Message()
        contact.Send_Button()
        CHECK = contact.Switch_Alert
        assert 'Thanks fore mege!!' == CHECK


    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_contact_empty_message(self):
        contact = Contact()
        contact.open()
        contact.Contact_Link()
        contact.Contact_Email()
        contact.Contact_Name()
        contact.Contact_Empty_Message()
        contact.Send_Button()
        CHECK = contact.Switch_Alert
        assert 'Thanks foessage!!' == CHECK


    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_contact_empty_email(self):
        contact = Contact()
        contact.open()
        contact.Contact_Link()
        contact.Contact_Empty_Email()
        contact.Contact_Name()
        contact.Contact_Message()
        contact.Send_Button()
        CHECK = contact.Switch_Alert
        assert 'Thanks for t meage!!' == CHECK


    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_contact_empty_name(self):
        contact = Contact()
        contact.open()
        contact.Contact_Link()
        contact.Contact_Email()
        contact.Contact_Empty_Name()
        contact.Contact_Message()
        contact.Send_Button()
        CHECK = contact.Switch_Alert
        assert 'Thanks for t mge!!' == CHECK


    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_contact_empty_name_email(self):
        contact = Contact()
        contact.open()
        contact.Contact_Link()
        contact.Contact_Empty_Email()
        contact.Contact_Empty_Name()
        contact.Contact_Message()
        contact.Send_Button()
        CHECK = contact.Switch_Alert
        assert 'Thanks fo msage!!' == CHECK


    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_contact_empty_name_email_message(self):
        contact = Contact()
        contact.open()
        contact.Contact_Link()
        contact.Contact_Empty_Email()
        contact.Contact_Empty_Name()
        contact.Contact_Empty_Message()
        contact.Send_Button()
        CHECK = contact.Switch_Alert
        assert 'Thanks for tssage!!' == CHECK


    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @allure.step
    @allure.description("")
    def test_contact_close_button(self):
        contact = Contact()
        contact.open()
        contact.Contact_Link()
        contact.Contact_Email()
        contact.Contact_Name()
        contact.Contact_Close_Button()
