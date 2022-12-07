# Copyright (c) 2010-2022 openpyxl

from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.descriptors import (
    Typed,
    Bool,
    Integer,
    Set,
    NoneSet,
    String,
    Sequence,
)

from openpyxl.descriptors.excel import Relation
from openpyxl.xml.constants import (
    XL_2009,
    ACTIVEX_NS,
    REL_NS,
)
from .ole import ObjectAnchor

from openpyxl.packaging.relationship import (
    RelationshipList,
    Relationship,
    get_rels_path,
)
from openpyxl.packaging.manifest import ManifestObject
from openpyxl.xml.functions import tostring


class ControlProperty(Serialisable):

    tagname = "controlPr"

    anchor = Typed(expected_type=ObjectAnchor, )
    locked = Bool(allow_none=True)
    defaultSize = Bool(allow_none=True)
    print = Bool(allow_none=True)
    disabled = Bool(allow_none=True)
    recalcAlways = Bool(allow_none=True)
    uiObject = Bool(allow_none=True)
    autoFill = Bool(allow_none=True)
    autoLine = Bool(allow_none=True)
    autoPict = Bool(allow_none=True)
    macro = String(allow_none=True)
    altText = String(allow_none=True)
    linkedCell = String(allow_none=True)
    listFillRange = String(allow_none=True)
    cf = String(allow_none=True)
    id = Relation(allow_none=True)

    __elements__ = ('anchor',)

    image = None # where a related image is stored, the image data stored as a blob attribute

    def __init__(self,
                 anchor=None,
                 locked=True,
                 defaultSize=True,
                 print=True,
                 disabled=False,
                 recalcAlways=False,
                 uiObject=False,
                 autoFill=True,
                 autoLine=True,
                 autoPict=True,
                 macro=None,
                 altText=None,
                 linkedCell=None,
                 listFillRange=None,
                 cf='pict',
                 id=None,
                ):
        self.anchor = anchor
        self.locked = locked
        self.defaultSize = defaultSize
        self.print = print
        self.disabled = disabled
        self.recalcAlways = recalcAlways
        self.uiObject = uiObject
        self.autoFill = autoFill
        self.autoLine = autoLine
        self.autoPict = autoPict
        self.macro = macro
        self.altText = altText
        self.linkedCell = linkedCell
        self.listFillRange = listFillRange
        self.cf = cf
        self.id = id


class Control(Serialisable):

    tagname = "control"

    controlPr = Typed(expected_type=ControlProperty, allow_none=True)
    shapeId = Integer()
    name = String(allow_none=True)
    id = Relation()

    shape = None # related element

    __elements__ = ('controlPr',)

    def __init__(self,
                 controlPr=None,
                 shapeId=None,
                 name=None,
                 id=None,
                ):
        self.controlPr = controlPr
        self.shapeId = shapeId
        self.name = name
        self.id = id


class Choice(Serialisable):
    """Markup compatiblity choice"""

    tagname = "choice"

    control = Typed(expected_type=Control)
    Requires = String()


    def __init__(self, control=None, Requires=None):
        self.control = control


class AlternateContent(Serialisable):
    """Markup AlternateContent
    """

    tagname = "AlternateContent"

    Choice = Typed(expected_type=Choice)


    def __init__(self, Choice=None):
        self.Choice = Choice


class ControlList(Serialisable):

    tagname = "controls"

    AlternateContent = Sequence(expected_type=AlternateContent)
    control = Sequence(expected_type=Control)

    __elements__ = ('control',)

    def __init__(self,
                 AlternateContent=None,
                 control=(),
                ):
        if AlternateContent:
            control = [ac.Choice.control for ac in AlternateContent]
        self.control = control


    def __len__(self):
        return len(self.control)


class FormControl(Serialisable):

    tagname = "formControlPr"
    mime_type = "application/vnd.ms-excel.controlproperties+xml"
    rel_type = f"{REL_NS}/ctrlProp"
    namespace = XL_2009
    _path = "/xl/ctrlProps/ctrlProp{0}.xml"
    _counter = None

    objectType = String(allow_none=True)
    checked = String(allow_none=True)
    colored = Bool()
    dropLines = Integer(allow_none=True)
    dropStyle = String(allow_none=True)
    dx = Integer(allow_none=True)
    firstButton = Bool()
    fmlaGroup = String(allow_none=True)
    fmlaLink = String(allow_none=True)
    fmlaRange = String(allow_none=True)
    fmlaTxbx = String(allow_none=True)
    horiz = Bool()
    inc = Integer(allow_none=True)
    justLastX = Bool()
    lockText = Bool()
    max = Integer(allow_none=True)
    min = Integer(allow_none=True)
    multiSel = String(allow_none=True)
    noThreeD = Bool()
    noThreeD2 = Bool()
    page = Integer(allow_none=True)
    sel = Integer(allow_none=True)
    seltype = String(allow_none=True)
    textHAlign = String(allow_none=True)
    textVAlign = String(allow_none=True)
    val = Integer(allow_none=True)
    widthMin = Integer(allow_none=True)
    editVal = String(allow_none=True)
    multiLine = Bool()
    verticalBar = Bool()
    passwordEdit = Bool()

    itemLst = Sequence(expected_type=String)

    __elements__ = ("itemLst",)

    def __init__(self,
                 objectType=None,
                 checked=None,
                 colored=None,
                 dropLines=8,
                 dropStyle=None,
                 dx=80,
                 firstButton=None,
                 fmlaGroup=None,
                 fmlaLink=None,
                 fmlaRange=None,
                 fmlaTxbx=None,
                 horiz=None,
                 inc=None,
                 justLastX=None,
                 lockText=None,
                 max=None,
                 min=None,
                 multiSel=None,
                 noThreeD=None,
                 noThreeD2=None,
                 page=None,
                 sel=None,
                 seltype=None,
                 textHAlign=None,
                 textVAlign=None,
                 val=None,
                 widthMin=None,
                 editVal=None,
                 multiLine=None,
                 verticalBar=None,
                 passwordEdit=None,
                 itemLst=(),
                 extLst=None,
                 ):
        self.objectType = objectType
        self.checked = checked
        self.colored = colored
        self.dropLines = dropLines
        self.dropStyle = dropStyle
        self.dx = dx
        self.firstButton = firstButton
        self.fmlaGroup = fmlaGroup
        self.fmlaLink = fmlaLink
        self.fmlaRange = fmlaRange
        self.fmlaTxbx = fmlaTxbx
        self.horiz = horiz
        self.inc = inc
        self.justLastX = justLastX
        self.lockText = lockText
        self.max = max
        self.min = min
        self.multiSel = multiSel
        self.noThreeD = noThreeD
        self.noThreeD2 = noThreeD2
        self.page = page
        self.sel = sel
        self.seltype = seltype
        self.textHAlign = textHAlign
        self.textVAlign = textVAlign
        self.val = val
        self.widthMin = widthMin
        self.editVal = editVal
        self.multiLine = multiLine
        self.verticalBar = verticalBar
        self.passwordEdit = passwordEdit
        self.itemLst = itemLst


    @property
    def path(self):
        return self._path.format(self.counter)


    def _write(self, archive, manifest):
        """
        Add to zipfile and update manifest
        """
        xml = tostring(self.to_tree())
        archive.writestr(self.path[1:], xml)
        manifest.append(self)


class ActiveXControl(Serialisable):

    namespace = ACTIVEX_NS
    tagname = "ocx"
    mime_type = "application/vnd.ms-office.activeX+xml"
    rel_type = f"{REL_NS}/control"
    _path = "/xl/activeX/activeX{0}.xml"
    _rel_id = None # key in worksheet
    _counter = None # key in workbook
    bin_rel_type = "http://schemas.microsoft.com/office/2006/relationships/activeXControlBinary"

    id = Relation()
    classid = String(namespace=ACTIVEX_NS)
    persistence = NoneSet(values=["persistPropertyBag", "persistStream", "persistStreamInit", "persistStorage"],
                      namespace=ACTIVEX_NS)

    bin = None # active X binary
    #bin = b"\001"

    def __init__(self, id=None, classid="{8BD21D50-EC42-11CE-9E0D-00AA006002F3}", persistence=None):
        self.id = id
        self.classid = classid
        self.persistence = persistence


    @property
    def path(self):
        return self._path.format(self.counter)


    def _write(self, archive, manifest):
        """
        Add to zipfile and update manifest
        """
        self._write_rels(archive, manifest)
        tree = self.to_tree()
        xml = tostring(tree)
        archive.writestr(self.path[1:], xml)
        manifest.append(self)


    def _write_rels(self, archive, manifest):
        """
        Write the relevant child objects and add links
        """

        bin_path = f"/xl/activeX/activeX{self.counter}.bin"
        archive.writestr(bin_path[1:], self.bin)

        rels = RelationshipList()
        r = Relationship(Type=self.bin_rel_type, Target=bin_path)
        rels.append(r)
        self.id = r.id

        path = get_rels_path(self.path.format(self.counter))
        xml = tostring(rels.to_tree())
        archive.writestr(path[1:], xml)

        mo = ManifestObject(bin_path, "application/vnd.ms-office.activeX")
        manifest.append(mo)
