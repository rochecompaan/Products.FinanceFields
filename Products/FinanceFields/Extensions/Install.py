from Products.CMFCore.utils import getToolByName
from Products.Archetypes.public import listTypes
from Products.Archetypes.Extensions.utils import installTypes, install_subskin
from Products.FinanceFields.config import PROJECTNAME, GLOBALS

from StringIO import StringIO

def install(self):
    out = StringIO()
    portal = getToolByName(self,'portal_url').getPortalObject()
    classes = listTypes(PROJECTNAME)

    installTypes(self, out, classes, PROJECTNAME)

    install_subskin(self, out, GLOBALS)

    setup_tool = getToolByName(self, 'portal_setup')
    setup_tool.setImportContext('profile-FinanceFields:default')
    result = setup_tool.runImportStep('propertiestool')
    out.write( 'Steps run: %s \n' % ', '.join(result['steps']) )

    out.write("Successfully installed %s." % PROJECTNAME)
    return out.getvalue()
