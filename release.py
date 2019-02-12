# -*- coding: utf-8 -*-

"""Release information"""


version = "0.0.2"
author = "Roland|Chima"
email = "Rolandazim@gmail.com"
copyright = "Copyright 2019~ Roland|Chima and contributors"
license = "MIT <http://www.opensource.org/licenses/mit-license.php>"
url = "https://github.com/ORC-1/ibolang"
download_url="https://github.com/ORC-1/ibolang"
description="programming language in Igbo"
long_description = """
.. contents::
  :depth: 2

Introduction
--------------

Igbo is an indigenous language popularly spoken in Nigeria, Ibolang is a full 
extension of the Igbo language in Python. 
With Ibolang, you can write and run python like programs in Igbo

Ibolang acts like python 3 and plays like python 3, it maintains all the python syntax 
and methods.
user could use it to learn programming in their native language.

Example
----------
ibolang is highly user friendly, the following is a simple "HelloWorld" program
       
       deputa("Uwa Aloo")

 
 running this, will diplay
         
         Uwa Aloo 

to console, which translated to English is "Hello World"

you can code more complex code by installing ibolang to your PC:


To run programs is as simple as:

     $ ibolang filename.ibl

  from your preferred shell or command line  

  you can go through the dictionary on: 
  * https://github.com/ORC-1/ibolang/blob/master/dictionary.txt
      
  to get an exhaustive list of all currently available commands and there English translation

Install
----------

If you'd like to play Ibolang with full features included, you should install Ibolang.

You could use pip or easy_install command to install Ibolang:

	$ pip install Ibolang 

			or

    $ easy_install -U Ibolang

to use easy_install command, you should install distribute module for python 3 first:

http://pypi.python.org/pypi/distribute/

And check your system path params if it contains python3.x/bin path.

ex: edit .bashrc to include "/Library/Frameworks/Python.framework/Versions/3.x/bin" in your PATH parameter.

For sytem running multiple version of python, you are better of using a virtual enviroment
with Ibolang:

	$ conda create -n Ibolang python==3.XX

			or using Virtualenv

	$ virtualenv ibolang python==3.XX 

Lastly you can clone the repo using this url https://github.com/ORC-1/ibolang.git : navigate to the folder path and run python setup.py 
Copy the source files into your script folder, you should highly consider using 
a virtual enviroment if you are using this option and the previous options are better 
off



Change Log
-------------

You could view the ChangeLog to see what's new in these version.

  * https://github.com/ORC-1/ibolang/blob/master/CHANGELOG.txt


"""
