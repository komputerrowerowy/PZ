# coding=utf-8
"""
MapView
=======

.. author:: Mathieu Virbel <mat@kivy.org>

MapView is a Kivy widget that display maps.
"""
from os import listdir, path
from os import makedirs
from os.path import join, exists


__all__ = ["Coordinate", "Bbox", "MapView", "MapSource", "MapMarker",
           "MapLayer", "MarkerMapLayer", "MapMarkerPopup"]
__version__ = "0.2"

if not exists('/sdcard/Bicom'):
    makedirs('/sdcard/Bicom')
if not exists('/sdcard/Bicom/Moje_trasy'):
    makedirs('/sdcard/Bicom/Moje_trasy')
fff = open("/sdcard/Bicom/cacheclear.dat", "w")
fff.write('/sdcard/Bicom/Mapy')
fff.close()

if not exists('/sdcard/Bicom/path/sav.dat'):
    makedirs('/sdcard/Bicom/path')
    ff = open("/sdcard/Bicom/path/sav.dat", "w")
    ff.write('/sdcard/Bicom/Mapy')
    ff.close()
f = open("/sdcard/Bicom/path/sav.dat", "r")
CACHE_DIR = str(f.readline())

f.close()

MIN_LATITUDE = -90.
MAX_LATITUDE = 90.
MIN_LONGITUDE = -180.
MAX_LONGITUDE = 180.
# CACHE_DIR = "cache"
#CACHE_DIR = "/sdcard/Bicom/Tiles"

try:
    # fix if used within garden
    import sys
    sys.modules['mapview'] = sys.modules['kivy.garden.mapview.mapview']
    del sys
except KeyError:
    pass

from mapview.types import Coordinate, Bbox
from mapview.source import MapSource
from mapview.view import MapView, MapMarker, MapLayer, MarkerMapLayer, \
    MapMarkerPopup
