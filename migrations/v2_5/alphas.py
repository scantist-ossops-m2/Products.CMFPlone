import os
from zope.component import queryUtility

from Acquisition import aq_base
from Products.CMFPlone.migrations.migration_util import installOrReinstallProduct
from Products.CMFCore.interfaces import ISkinsTool
from Products.CMFCore.DirectoryView import createDirectoryView

def two5_alpha1(portal):
    """2.1.2 -> 2.5-alpha1
    """
    out = []

    # Install CMFPlacefulWorkflow
    installPlacefulWorkflow(portal, out)

    return out

def alpha1_alpha2(portal):
    """2.5-alpha1 -> 2.5-alpha2
    """
    out = []

    # Install PlonePAS
    installPlonePAS(portal, out)

    # Install plone_deprecated skin
    installDeprecated(portal, out)

    return out


def installPlacefulWorkflow(portal, out):
    """Quickinstalls CMFPlacefulWorkflow if not installed yet."""
    # CMFPlacefulWorkflow is not installed by e.g. tests
    if 'CMFPlacefulWorkflow' in portal.Control_Panel.Products.objectIds():
        installOrReinstallProduct(portal, 'CMFPlacefulWorkflow', out)

def installPlonePAS(portal, out):
    """Quickinstalls PlonePAS if not installed yet."""
    NO_PLONEPAS = os.environ.get('SUPPRESS_PLONEPAS_INSTALLATION',None)=='YES'
    if not NO_PLONEPAS:
        installOrReinstallProduct(portal, 'PasswordResetTool', out)
        installOrReinstallProduct(portal, 'PlonePAS', out)

def installDeprecated(portal, out):
    # register login skin
    st = queryUtility(ISkinsTool)
    if st is None:
        return
    if not hasattr(aq_base(st), 'plone_deprecated'):
        createDirectoryView(st, 'CMFPlone/skins/plone_deprecated')
        out.append('Added directory view for plone_deprecated')

    # add deprecated skin to default skins
    skins = ['Plone Default', 'Plone Tableless']
    selections = st._getSelections()
    for s in skins:
        if not selections.has_key(s):
           continue
        path = st.getSkinPath(s)
        path = [p.strip() for p in  path.split(',')]
        if not 'plone_deprecated' in path:
            if 'plone_3rdParty' in path:
                path.insert(path.index('plone_3rdParty'), 'plone_deprecated')
            else:
                path.append('plone_deprecated')
            st.addSkinSelection(s, ','.join(path))
            out.append('Added plone_deprecated to %s' % s)

