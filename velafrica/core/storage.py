# -*- coding: utf-8 -*-
from django.utils.deconstruct import deconstructible
from storages.backends.ftp import FTPStorage

@deconstructible
class MyFTPStorage(FTPStorage):
    """
    TODO: write doc
    """
    pass