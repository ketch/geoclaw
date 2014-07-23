#!/usr/bin/env python

r"""Regression tests.  Execute via:
    python regression_tests.py
to test, or
    python regression_tests.py True
to create new regression data for archiving.
"""

import os
import sys
import unittest
import shutil

import numpy

import clawpack.geoclaw.tests as tests
import clawpack.geoclaw.topotools as topotools
import clawpack.geoclaw.dtopotools as dtopotools

class DTopoTests(tests.GeoClawTest):
    
    def setUp(self):

        super(DTopoTests, self).setUp()

        # Make topography
        h0 = 1000.0
        topo_func = lambda x,y: -h0*(1 + 0.5 * numpy.cos(x - y))
        topo = topotools.Topography(topo_func=topo_func)
        topo.topo_type = 2
        topo.x = numpy.linspace(-10.0, 10.0, 201)
        topo.y = numpy.linspace(-10.0, 10.0, 201)
        topo.write(os.path.join(self.temp_path, "topo1.topotype2"))

        h0 = 1000.0
        topo_func = lambda x,y: -h0*(1. + numpy.exp(x+y))
        topo = topotools.Topography(topo_func=topo_func)
        topo.topo_type = 2
        topo.x = numpy.linspace(-0.5, -0.3, 21)
        topo.y = numpy.linspace(-0.1, 0.4, 51)
        topo.write(os.path.join(self.temp_path, "topo2.topotype2"))

        # Make dtopography
        subfault_path = os.path.join(self.test_path, "dtopo1.csv")
        fault = dtopotools.CSVFault(path=subfault_path)
        fault.t = numpy.linspace(0.0, 1.0, 25)
        fault.write(os.path.join(self.temp_path, "dtopo1.tt3"))

        subfault_path = os.path.join(self.test_path, "dtopo2.csv")
        fault = dtopotools.CSVFault(path=subfault_path)
        fault.t = numpy.linspace(0.5, 1.2, 25)
        fault.write(os.path.join(self.temp_path, "dtopo2.tt3"))

        shutil.copy(os.path.join(self.test_path, "dtopo3.tt1"),
                                 self.temp_path)


if __name__=="__main__":
    if len(sys.argv) > 1:
        if bool(sys.argv[1]):
            # Fake the setup and save out output
            test = DTopoTests()
            try:
                test.setUp()
                test.runTest(save=True)
            finally:
                test.tearDown()
            sys.exit(0)
    unittest.main()

