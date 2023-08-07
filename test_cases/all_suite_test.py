import unittest

from unittest.loader import makeSuite


from test_cases.adding_a_player import TestAddingAPlayer
from test_cases.incorrect_adding_a_player import TestAddAnIncorrectPlayer
from test_cases.framework import Test, TestSelectLanguage
from test_cases.incorrect_login_to_the_system import TestLoginPageIncorrectData
from test_cases.log_out_of_the_system import TestLogOutOfTheSystem
from test_cases.login_to_the_system import TestLoginPage
from test_cases.selection_leg_of_a_player import TestSelectLeg
from test_cases.test_click_add_a_player import TestAddAPlayer


def full_suite():
   test_suite = unittest.TestSuite()
   test_suite.addTest(makeSuite(TestLoginPage))
   test_suite.addTest(makeSuite(TestSelectLanguage))
   test_suite.addTest(makeSuite(TestAddAPlayer))
   test_suite.addTest(makeSuite(TestAddingAPlayer))
   test_suite.addTest(makeSuite(TestAddAnIncorrectPlayer))
   test_suite.addTest(makeSuite(TestSelectLeg))
   test_suite.addTest(makeSuite(TestLogOutOfTheSystem))
   test_suite.addTest(makeSuite(TestLoginPageIncorrectData))
   return test_suite

if __name__ == '__main__':
   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(full_suite())
