from Products.CMFCore.utils import ContentInit
from Products.CMFCore.DirectoryView import registerDirectory
from Products.CMFPlone.interfaces import IPloneSiteRoot
from Products.Archetypes.public import process_types, listTypes
from Products.GenericSetup import profile_registry, EXTENSION
from config import SKINS_DIR, GLOBALS, PROJECTNAME
from config import ADD_CONTENT_PERMISSION

registerDirectory(SKINS_DIR, GLOBALS)

def initialize(context):
    import MoneyField
    import FixedPointField
    import MoneyWidget

    # As time goes by, more things will move from Python into the
    # profile.
    profile_desc = "Extra setup stuff for FinanceFields."
    profile_registry.registerProfile('default',
                                     'FinanceFields',
                                     profile_desc,
                                     'profiles/default',
                                     'FinanceFields',
                                     EXTENSION,
                                     for_=IPloneSiteRoot,
                                     )

    content_types, constructors, ftis = process_types(
        listTypes(PROJECTNAME),
        PROJECTNAME)

    ContentInit(
        PROJECTNAME + ' Content',
        content_types      = content_types,
        permission         = ADD_CONTENT_PERMISSION,
        extra_constructors = constructors,
        fti                = ftis,
        ).initialize(context)
