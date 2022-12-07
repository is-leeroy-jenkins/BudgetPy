# Copyright (c) 2010-2022 openpyxl

from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.descriptors import (
    Sequence,
    String,
    Typed,
)

from openpyxl.packaging.relationship import (
    Relationship,
    RelationshipList,
)
from openpyxl.utils import coordinate_to_tuple
from openpyxl.utils.units import (
    cm_to_EMU,
    pixels_to_EMU,
)
from openpyxl.drawing.image import (
    Image,
    ImageGroup,
)

from openpyxl.xml.constants import SHEET_DRAWING_NS

from openpyxl.chart._chart import ChartBase
from .fill import Blip
from .graphic import (
     GraphicFrame,
     GroupShape,
    )
from .geometry import PresetGeometry2D
from .picture import PictureFrame
from .relation import ChartRelation
from .anchor import (
    AbsoluteAnchor,
    OneCellAnchor,
    TwoCellAnchor,
    _AnchorBase,
)


def _check_anchor(obj):
    """
    Check whether an object has an existing Anchor object
    If not create a OneCellAnchor using the provided coordinate
    """
    anchor = obj.anchor
    if not isinstance(anchor, _AnchorBase):
        row, col = coordinate_to_tuple(anchor.upper())
        anchor = OneCellAnchor()
        anchor._from.row = row -1
        anchor._from.col = col -1
        if isinstance(obj, ChartBase):
            anchor.ext.width = cm_to_EMU(obj.width)
            anchor.ext.height = cm_to_EMU(obj.height)
        elif isinstance(obj, Image):
            anchor.ext.width = pixels_to_EMU(obj.width)
            anchor.ext.height = pixels_to_EMU(obj.height)
    return anchor



class Choice(Serialisable):
    """Markup compatiblity choice"""

    tagname = "choice"

    twoCellAnchor = Typed(expected_type=TwoCellAnchor, allow_none=True)
    oneCellAnchor = Typed(expected_type=OneCellAnchor, allow_none=True)
    absoluteAnchor = Typed(expected_type=AbsoluteAnchor, allow_none=True)
    Requires = String()


    def __init__(self,
                 twoCellAnchor=None,
                 oneCellAnchor=None,
                 absoluteAnchor=None,
                 Requires=None):
        self.Requires = Requires
        self.twoCellAnchor = twoCellAnchor
        self.oneCellAnchor = oneCellAnchor
        self.absoluteAnchor = absoluteAnchor


class AlternateContent(Serialisable):
    """Markup AlternateContent
    """

    tagname = "AlternateContent"

    Choice = Typed(expected_type=Choice)


    def __init__(self, Choice=None):
        self.Choice = Choice


class SpreadsheetDrawing(Serialisable):

    tagname = "wsDr"
    mime_type = "application/vnd.openxmlformats-officedocument.drawing+xml"
    _rel_type = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/drawing"
    _path = PartName="/xl/drawings/drawing{0}.xml"
    _id = None

    twoCellAnchor = Sequence(expected_type=TwoCellAnchor)
    oneCellAnchor = Sequence(expected_type=OneCellAnchor)
    absoluteAnchor = Sequence(expected_type=AbsoluteAnchor)
    AlternateContent = Sequence(expected_type=AlternateContent)

    __elements__ = ("twoCellAnchor", "oneCellAnchor", "absoluteAnchor",)

    def __init__(self,
                 twoCellAnchor=(),
                 oneCellAnchor=(),
                 absoluteAnchor=(),
                 AlternateContent=(),
                 ):
        self.twoCellAnchor = twoCellAnchor
        self.oneCellAnchor = oneCellAnchor
        self.absoluteAnchor = absoluteAnchor
        self.charts = []
        self.images = []
        self.shapes = []
        self._rels = RelationshipList()
        if AlternateContent:
            for obj in AlternateContent:
                if obj.Choice.twoCellAnchor:
                    self.twoCellAnchor.append(obj.Choice.twoCellAnchor)
                elif obj.Choice.oneCellAnchor:
                    self.oneCellAnchor.append(obj.Choice.oneCellAnchor)
                elif obj.Choice.absoluteAnchor:
                    self.absoluteAnchor.append(obj.Choice.absoluteAnchor)


    def __hash__(self):
        """
        Just need to check for identity
        """
        return id(self)


    def __bool__(self):
        return bool(self.charts) or bool(self.images) or bool(self.shapes)


    def _write(self):
        """
        create required structure and the serialise
        """
        anchors = []
        for idx, obj in enumerate(self.charts + self.images + self.shapes, 1):
            rel = None
            anchor = _check_anchor(obj)
            if isinstance(obj, ChartBase):
                rel = Relationship(type="chart", Target=obj.path)
                anchor.graphicFrame = self._chart_frame(idx, anchor.graphicFrame)
                if obj.hidden:
                    anchor.graphicFrame.props.non_visual_props.hidden = True

            elif isinstance(obj, Image):
                rel = Relationship(type="image", Target=obj.path)
                if anchor.pic:
                    child = anchor.pic
                    child.blipFill.blip.embed = f"rId{idx}"

                else:
                    anchor.pic = self._picture_frame(idx)

            elif isinstance(obj, ImageGroup):
                for img, pic in zip(obj.images, anchor.groupShape.pic):
                    rel = Relationship(type="image", Target=img.path)
                    self._rels.append(rel)
                    pic.blipFill.blip.embed = rel.Id
                    rel = None # reset to stop it being added twice

            else:
                link = getattr(obj.nvSpPr.cNvPr, "hlinkClick")
                if link:
                    link.id = f"rId{idx}"
                    rel = Relationship(
                        type="hyperlink",
                        Target=link.target,
                        TargetMode=link.mode,
                        Id=f"rId{idx}",
                    )

            anchors.append(anchor)
            if rel:
                self._rels.append(rel)

        for a in anchors:
            if isinstance(a, OneCellAnchor):
                self.oneCellAnchor.append(a)
            elif isinstance(a, TwoCellAnchor):
                self.twoCellAnchor.append(a)
            else:
                self.absoluteAnchor.append(a)

        tree = self.to_tree()
        tree.set('xmlns', SHEET_DRAWING_NS)
        return tree


    def _chart_frame(self, idx, frame=None):
        chart_rel = ChartRelation(f"rId{idx}")
        if frame is None:
            frame = GraphicFrame()
            frame.props.non_visual_props.name = "Chart {0}".format(idx)
        frame.props.non_visual_props.id = idx
        frame.graphic.graphicData.chart = chart_rel
        return frame


    def _picture_frame(self, idx):
        pic = PictureFrame()
        pic.nvPicPr.cNvPr.descr = "Picture"
        pic.nvPicPr.cNvPr.id = idx
        pic.nvPicPr.cNvPr.name = "Image {0}".format(idx)

        pic.blipFill.blip = Blip()
        pic.blipFill.blip.embed = "rId{0}".format(idx)
        pic.blipFill.blip.cstate = "print"

        pic.spPr.prstGeom = PresetGeometry2D(prst="rect")
        pic.spPr.ln = None
        return pic


    def _write_rels(self):
        return self._rels.to_tree()


    @property
    def path(self):
        return self._path.format(self._id)


    @property
    def _chart_rels(self):
        """
        Get relationship information for each chart and bind anchor to it
        """
        rels = []
        anchors = self.absoluteAnchor + self.oneCellAnchor + self.twoCellAnchor
        for anchor in anchors:
            if anchor.graphicFrame is not None:
                graphic = anchor.graphicFrame.graphic
                rel = graphic.graphicData.chart
                if rel is not None:
                    rel.anchor = anchor
                    rels.append(rel)
        return rels


    @property
    def _blip_rels(self):
        """
        Get relationship information for each blip and bind anchor to it

        Images that are not part of the XLSX package will be ignored.
        """
        rels = []
        anchors = self.absoluteAnchor + self.oneCellAnchor + self.twoCellAnchor

        for anchor in anchors:
            child = anchor._content
            if isinstance(child, PictureFrame):
                img = child._image
                if img:
                    img.anchor = anchor
                    img.properties = child.spPr
                    rels.append(img)

        return rels


    @property
    def _group_rels(self):
        """
        Extract groups of images
        """
        rels = []
        anchors = self.absoluteAnchor + self.oneCellAnchor + self.twoCellAnchor

        for anchor in anchors:
            child = anchor._content

            if isinstance(child, GroupShape):
                group = [anchor]
                for pic in child.pic:
                    img = pic._image
                    if img is not None:
                        img.properties = pic.spPr
                        group.append(img)

                rels.append(group)

        return rels


    @property
    def _shapes(self):
        """Return a list of shapes"""
        shapes = []
        anchors = self.absoluteAnchor + self.oneCellAnchor + self.twoCellAnchor
        for anchor in anchors:
            if anchor.sp is not None:
                shape = anchor.sp
                shape.anchor = anchor
                shapes.append(shape)
        return shapes
