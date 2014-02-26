mac-builds
==========

This repository is a home for various recipes for building assorted python packages for the Mac.

It is hoped that by putting this all in one place, anyone that needs to build a python package for Mac OS-X can use (or adapt) one of these recipes, rather than having to figure it all out over and over again. 


Goals of this project
======================

The primary goal of this project is not just to provide recipes for bulding pacakges, but to provide a way for them to be built in a standard, re-distributable way. The idea is to build packages in such a way as to have them be fully compatible with the python builds on python.org, so that anyone running a given python build can also run the packages resulting from this project, and re-distribute them successfuly with py2app, etc.


About Gattai
=============

Gattai is a python-based system for building python packages -- you might ask "isn't that what distutils and setuptools are for?" -- well, yes, but the complication comes in when there are non-python dependencies. Gattai is a system that allows you to provide a single recipe that will download, build and install the external dependencies, then build your python package against it.

It's not a requirment for this project to use Gattai, and indeed, when I started, I found myself writting custom scripts to do all this -- but I decided to stap re-inventing the wheel, and just go with gattai. You will find gattai on sourceforge, at:

<https://sourceforge.net/projects/gattai/>

Ideally, this project will be managed / discussed on the pytonmac email list:

<http://mail.python.org/mailman/listinfo/pythonmac-sig>

What about Windows / Linux ?
=============================

Gattai is designed to be cross-platfrom, it will build packages for all of the major packages. However, there are already folks building many packages for Windows (Chris Gohlke's repository is wonderful -- I wonder how he automates that?), and Linux distros provide many packages themselves, and those that don't, they do provide most of the dependencies.

That being said, if someone wants to extend this project, and/or an individual gattai recipe, to cover Windows or Linux, or... go for it!





