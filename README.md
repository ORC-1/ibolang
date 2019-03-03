Introduction
--------------

Igbo is an indigenous language popularly spoken in Nigeria, Ibolang is a full 
extension of the Igbo language in Python. <br />
With Ibolang, you can write and run python like programs in Igbo

Ibolang acts like python 3 and plays like python 3, it maintains all the python syntax 
and methods.
user could use it to learn programming in their native language.

Example
----------
ibolang is highly user friendly, the following is a simple "HelloWorld" program
       
       deputa("Uwa Aloo")

 <br />
 running this, will diplay
         
         Uwa Aloo 

to console, which translated to English is "Hello World"

you can code more complex code by installing ibolang to your PC or by using the ibolang online IDE(coming soon...).

  * https://github.com/ORC-1/ibolang/tree/master/examples (example codes)

<br />
To run programs is as simple as:

     $ ibolang filename.ibl

  from your preferred shell or command line  

  you can go through to the dictionary on: 
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

	$ virtualenv ibolang  

Lastly you can clone the repo using this url https://github.com/ORC-1/ibolang.git : navigate to the folder path and run python setup.py 
Copy the source files into your script folder, you should highly consider using 
a virtual enviroment if you are using this option and the previous options are better 
off

For <h1>Absolute Beginners</h1>:


      follow this link: 
      https://www.python.org/ftp/python/3.7.2/python-3.7.2.exe
      download python 3 install it and ensure it's working

<h1>Then:</h1>
          
  You can use pip to install Ibolang:

      $ pip install Ibolang 
    
  Go to the example here , clone the repository and run them with ibolang filename.ibl

Change Log
-------------

You could view the ChangeLog to see what's new in these version.

  * https://github.com/ORC-1/ibolang/blob/master/CHANGELOG.txt


