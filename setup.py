from setuptools import setup
from setuptools import find_packages

version = '6.0.0b1.dev0'


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
        'borg.localrole',
        'five.customerize',
        'lxml',
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
        'plone.base',
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
        'plone.resource',
        'plone.schema',
        'plone.session',
        'plone.staticresources',
        'plone.theme',
        'plonetheme.barceloneta',
        'Products.CMFEditions',
        'Products.DCWorkflow',
        'Products.ExtendedPathIndex',
        'Products.isurlinportal',
        'Products.MimetypesRegistry',
        'Products.PlonePAS',
        'Products.PortalTransforms',
        'Products.SiteErrorLog',
        'Products.statusmessages',
        'setuptools>=36.2',
        'plone.autoinclude',
        'webresource>=1.1',
        'Zope[wsgi] >= 5.0',
        'zope.app.locales >= 3.6.0',
        'zope.cachedescriptors',
        'zope.deferredimport',
        'zope.deprecation',
        'zope.dottedname',
        'zope.i18n',
        'zope.i18nmessageid',
        'zope.structuredtext',
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
            'gunicorn',
        ]
    },
)
