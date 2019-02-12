try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

from pkg_resources import DistributionNotFound

import sys
import os
import glob
import release
#execfile('release.py')


# setup params
required_modules = ["setuptools"]
#if mac, install readline
#if(sys.platform=="darwin"):
#    required_modules.append("readline >= 2.6.4")

# nose is used for test
extra_modules = {}

setup(
    name="ibolang",
    version=release.version,
    author=release.author,
    author_email=release.email,
    download_url=release.download_url,
    py_modules=['core','ibolang','ig_tran','igbolang',],
    license=license,
    keywords = "traditional, simplified, Igbo, Afrocode, language, tokenize",
    description=release.description,
    long_description=release.long_description,
    url=release.url,
    zip_safe=False,
    install_requires = required_modules,
    extras_require = extra_modules,
    include_package_data = True,
    packages=find_packages(exclude=["ez_setup", 'examples', 'apidocs', "tests", "ibl"]),
    entry_points = """
    [console_scripts]
    ibolang = ibolang:commandline
    
    """,
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Education',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Code Generators'],
    #test_suite = 'nose.collector',
    )

