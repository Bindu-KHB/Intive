import unittest
import HtmlTestRunner
from Test_Scripts.test_Pokemon_Main_Page import *



suite = unittest.TestSuite()
suite.addTests([
    unittest.defaultTestLoader.loadTestsFromTestCase(test_Pokemon_Encyclopedia),
])
test_runner = HtmlTestRunner.HTMLTestRunner(output="../TestReports", report_title="Pokemon Web Automation Results", combine_reports=True)
test_runner.run(suite)