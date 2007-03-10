#
# CSSRegistry tests
#

import os, sys
if __name__ == '__main__':
    execfile(os.path.join(sys.path[0], 'framework.py'))

from Products.CMFPlone.tests import PloneTestCase

from zope.component import getUtility
from Products.ResourceRegistries.config import CSSTOOLNAME, JSTOOLNAME
from Products.ResourceRegistries.interfaces import ICSSRegistry
from Products.ResourceRegistries.interfaces import IJSRegistry


class TestCSSRegistry(PloneTestCase.PloneTestCase):

    def afterSetUp(self):
        self.tool = getUtility(ICSSRegistry)

    def testToolExists(self):
        self.failUnless(CSSTOOLNAME in self.portal.objectIds())

    def testDefaultCssIsInstalled(self):
        installedStylesheetIds = self.tool.getResourceIds()
        expected = ['ploneCustom.css',
                    'authoring.css', 
                    'public.css',
                    'base.css',
                    'portlets.css',
                    'deprecated.css',
                    'member.css',
                    'print.css',
                    'presentation.css',
                    'RTL.css',
                    'mobile.css',
                    'textSmall.css',
                    'textLarge.css']
        for e in expected:
            self.failUnless(e in installedStylesheetIds, e)


class TestJSRegistry(PloneTestCase.PloneTestCase):

    def afterSetUp(self):
        self.tool = getUtility(IJSRegistry)

    def testToolExists(self):
        self.failUnless(JSTOOLNAME in self.portal.objectIds())

    def testDefaultJSIsInstalled(self):
        installedScriptIds = self.tool.getResourceIds()
        expected = [
             'correctPREformatting.js',
             'plone_minwidth.js',
             'calendar_formfield.js',
             'ie5fixes.js',
             'calendarpopup.js',
             'collapsiblesections.js',
             'first_input_focus.js',
             'folder_contents_filter.js',
             'fullscreenmode.js',
             'highlightsearchterms.js',
             'mark_special_links.js',
             'select_all.js',
             'styleswitcher.js',
             'livesearch.js',
             'table_sorter.js',
             'dropdown.js',
             'dragdropreorder.js',
             'cssQuery.js',
             'cookie_functions.js',
             'nodeutilities.js',
             'plone_javascript_variables.js',
             'register_function.js', 
             'formUnload.js',
             'formsubmithelpers.js',
             'form_tabbing.js']
        for e in expected:
            self.failUnless(e in installedScriptIds, e)

    def testJSIsInsertedInPage(self):
        page = self.portal.index_html()
        self.failUnless("" in page)


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestCSSRegistry))
    suite.addTest(makeSuite(TestJSRegistry))
    return suite

if __name__ == '__main__':
    framework()
