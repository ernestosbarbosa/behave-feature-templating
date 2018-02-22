# -*- coding: utf-8 -*-

from behave import given, when, then
from features.pages.dialog_page import DialogPage
from features.pages.home_page import HomePage

@given('I went to menu "{menu}", submenu "{submenu}"')
def menu(step, menu, submenu):
    home_page = HomePage(step)
    home_page.clickMenu(menu)
    home_page.clickSubMenu(submenu)

@when('I fill the input field with "{text}"')
def fill_input(step, text):
    DialogPage(step).fillInput(text)

@when('select the Pick one option')
def click_pick_one(step):
    DialogPage(step).clickPickOne()

@then('should display a modal with the message "{text}"')
def expect_result(step, text):
    assert DialogPage(step).getDialogTitle().find(text) >= 0