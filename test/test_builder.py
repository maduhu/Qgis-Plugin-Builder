__author__ = 'timlinux'

# coding=utf-8
"""
InaSAFE Disaster risk assessment tool developed by AusAid -
**ISClipper test suite.**

Contact : ole.moller.nielsen@gmail.com

.. note:: This program is free software; you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation; either version 2 of the License, or
     (at your option) any later version.

"""


__author__ = 'tim@linfiniti.com'
__date__ = '20/01/2011'
__copyright__ = ('Copyright 2012, Australia Indonesia Facility for '
                 'Disaster Reduction')

import sys
import os
import unittest

from qgis.core import QgsProviderRegistry

PATH = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', 'plugin_template'))
sys.path.insert(0, PATH)

from test.utilities import get_qgis_app
from utilities import temp_dir, unique_filename

QGIS_APP = get_qgis_app()

from plugin_builder import copy


class QGISTest(unittest.TestCase):
    """Test the QGIS Environment"""

    def test_qgis_environment(self):
        """QGIS environment has the expected providers"""

        r = QgsProviderRegistry.instance()
        #for item in r.providerList():
        #    print str(item)

        #print 'Provider count: %s' % len(r.providerList())
        assert 'gdal' in r.providerList()
        assert 'ogr' in r.providerList()
        assert 'postgres' in r.providerList()
        #assert 'wfs' in r.providerList()


class BuilderTest(unittest.TestCase):
    """Test the plugin builder."""

    def test_dir_copy(self):
        """Test that we can copy a directory of files.

        Path to copy to must not pre-exist so we create a parent dir
        and generate a temp dir name without actually creating it.
        """
        temp_path = temp_dir()
        temp_name = unique_filename(prefix='plugin_builder_')
        new_path = os.path.join(temp_path, temp_name)
        copy(os.path.join(PATH, 'test'), new_path)
        test_file_path = os.path.join(new_path, 'test_init.py')
        self.assertTrue(os.path.exists(test_file_path), test_file_path)