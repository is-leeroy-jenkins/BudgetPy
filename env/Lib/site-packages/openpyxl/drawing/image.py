# Copyright (c) 2010-2022 openpyxl

from io import BytesIO

try:
    from PIL import Image as PILImage
except ImportError:
    PILImage = False

from openpyxl.xml.constants import IMAGE_NS
from openpyxl.descriptors import (
    Strict,
    Typed,
    Integer,
    String,
    Sequence,
)

from openpyxl.packaging.relationship import Relationship


def _import_image(img):
    if not PILImage:
        raise ImportError('You must install Pillow to fetch image objects')

    if not isinstance(img, PILImage.Image):
        img = PILImage.open(img)

    return img


class Image(object):
    """Image in a spreadsheet"""

    _id = 1
    _path = "/xl/media/image{0}.{1}"
    anchor = "A1"
    format = "PNG"
    rel_type = IMAGE_NS

    def __init__(self, img):

        self.ref = img
        mark_to_close = isinstance(img, str)
        image = _import_image(img)
        self.width, self.height = image.size

        try:
            self.format = image.format
        except AttributeError:
            pass
        if mark_to_close:
            # PIL instances created for metadata should be closed.
            image.close()


    def _data(self):
        """
        Return image data, convert to supported types if necessary
        """
        img = _import_image(self.ref)
        # don't convert these file formats
        if self.format in ['GIF', 'JPEG', 'PNG', "WMF", "EMF"]:
            img.fp.seek(0)
            fp = img.fp
        else:
            fp = BytesIO()
            img.save(fp, format="png")
            fp.seek(0)

        data = fp.read()
        fp.close()
        return data


    @property
    def path(self):
        return self._path.format(self._id, self.format.lower())


    def __eq__(self, other):
        return self.ref == other.ref


    def _write(self, archive):
        archive.writestr(self.path[1:], self._data())


class ImageGroup(Strict):

    """
    A way of grouping pictures in shapes
    """

    images = Sequence(expected_type=Image)
    counter = Integer()


    def __init__(self,
                 images=(),
                 counter=counter,
                 archive=None,
                 anchor=None):
        self.images = images
        self.counter = 0
        self.anchor = anchor


    def append(self, img):
        self.images.append(img)
        self.images = self.images


    @property
    def name(self):
        return f"Group {self.counter}"

