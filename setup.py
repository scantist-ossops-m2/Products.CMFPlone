from setuptools import setup
from setuptools import find_packages

version = '6.0.0a1.dev2'


setup(
    name='Products.CMFPlone',
    version=version,
    description="The Plone Content Management System (core)",
    long_description=open("README.rst").read() + "\n" +
    open("CHANGES.rst").read(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 6.0",
        "Framework :: Plone :: Core",
        "Framework :: Zope :: 5",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords='Plone CMF Python Zope CMS Webapplication',
    author='Plone Foundation',
    author_email='releasemanager@plone.org',
    url='https://plone.org',
    license='GPL version 2',
    packages=find_packages(),
    namespace_packages=['Products'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'AccessControl >= 4.0',
        'Acquisition',
        'borg.localrole',
        'calmjs.parse',
        'DateTime',
        'ExtensionClass',
        'five.customerize',
        'five.localsitemanager',
        'mockup',
        'Pillow',
        'plone.api >= 1.4.4',
        'plone.app.content',
        'plone.app.contentlisting',
        'plone.app.contentmenu >= 2.0.1',
        'plone.app.contentrules',
        'plone.app.contenttypes',
        'plone.app.customerize',
        'plone.app.dexterity',
        'plone.app.discussion',
        'plone.app.i18n',
        'plone.app.layout >= 2.5.15',
        'plone.app.linkintegrity >=1.0.3',
        'plone.app.locales',
        'plone.app.multilingual',
        'plone.app.portlets',
        'plone.app.redirector',
        'plone.app.registry',
        'plone.app.theming',
        'plone.app.users',
        'plone.app.uuid',
        'plone.app.viewletmanager',
        'plone.app.vocabularies',
        'plone.app.workflow',
        'plone.batching',
        'plone.browserlayer >= 2.1.5',
        'plone.contentrules',
        'plone.folder',
        'plone.i18n >= 4.0.5',
        'plone.indexer',
        'plone.intelligenttext',
        'plone.locking',
        'plone.memoize',
        'plone.outputfilters',
        'plone.portlet.collection',
        'plone.portlet.static',
        'plone.portlets',
        'plone.protect >= 3.0.0',
        'plone.registry',
        'plone.schema',
        'plone.session',
        'plone.staticresources',
        'plone.subrequest',
        'plone.theme',
        'plonetheme.barceloneta',
        'Products.CMFCore',
        'Products.CMFDiffTool',
        'Products.CMFDynamicViewFTI',
        'Products.CMFEditions',
        'Products.CMFUid',
        'Products.DCWorkflow',
        'Products.ExtendedPathIndex',
        'Products.GenericSetup >= 2.0',
        'Products.isurlinportal',
        'Products.MimetypesRegistry',
        'Products.PlonePAS',
        'Products.PluggableAuthService',
        'Products.PluginRegistry',
        'Products.PortalTransforms',
        'Products.SiteErrorLog',
        'Products.statusmessages',
        'pyScss',
        'setuptools>=36.2',
        'transaction',
        'z3c.autoinclude',
        'ZODB3',
        'Zope[wsgi] >= 4.0',
        'zope.app.locales >= 3.6.0',
        'zope.cachedescriptors',
        'zope.component',
        'zope.container',
        'zope.deferredimport',
        'zope.deprecation',
        'zope.dottedname',
        'zope.event',
        'zope.i18n',
        'zope.i18nmessageid',
        'zope.interface',
        'zope.location',
        'zope.pagetemplate',
        'zope.publisher',
        'zope.site',
        'zope.structuredtext',
        'zope.tal',
        'zope.tales',
        'zope.traversing',
    ],
    extras_require={
        'test': [
            'lxml',
            'mock',
            'plone.app.robotframework>=1.0',
            'robotframework-debuglibrary',
            'plone.app.testing',
            'zope.globalrequest',
            'zope.testing',
        ]
    },
)
