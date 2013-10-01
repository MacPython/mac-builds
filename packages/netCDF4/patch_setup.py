#!/usr/bin/env python

"""
patch_setup.py

this is a little script that patches the netCDF4 setup.py to add libcurl.

This is required if you link the netcdf libs statically (netcdf used libcurl)

NOTE: This is pretty fragile with respoect to changes in the original setup.py
      It's likely it will need to be adapted with new version os netCDF4

This is expected to be run with the current working dir as the netCDF4 dir
     (where the setup.py is)

"""

import os


contents = open('setup.py', 'rb').read()

contents = contents.replace("libs = ['netcdf','hdf5_hl','hdf5','z']",
                            "libs = ['netcdf','hdf5_hl','hdf5','z', 'curl']",
                             )

open('setup_static.py', 'wb').write(contents)




