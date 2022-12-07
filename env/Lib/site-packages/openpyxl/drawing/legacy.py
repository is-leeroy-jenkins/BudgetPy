# Copyright (c) 2010-2022 openpyxl

from openpyxl.xml.constants import (
    VML_NS,
)
from openpyxl.packaging.relationship import RelationshipList


class LegacyDrawing:

    mime_type = "application/vnd.openxmlformats-officedocument.vmlDrawing"
    rel_type = VML_NS
    _counter = 0
    _rel_id = None
    _path = "/xl/drawings/vmlDrawing{0}.vml"
    vml = None
    children = None # rels from the worksheet

    def __init__(self, vml):
        self.vml = vml
        self.children = RelationshipList()


    @property
    def path(self):
        return self._path.format(self._counter)


    def _write(self, archive):
        archive.writestr(self.path[1:], self.vml)

