#from distutils.core import setup
from setuptools import setup

import openfaux_proxy

setup(
    
    name             = openfaux_proxy.__name__ ,
    description      = openfaux_proxy.__desc__ ,
    long_description = openfaux_proxy.__ldesc__  ,    # on the main script/file/code! So we will 
    version          = openfaux_proxy.__version__ , # It's a good idea put all this stuff 
    license          = openfaux_proxy.__license__ , # not need to edit this file on every push/release !

    url              = openfaux_proxy.__url__ ,

    author           = openfaux_proxy.__author__ ,
    author_email     = openfaux_proxy.__email__  ,


    
    py_modules=['cosmos'] , # library

    scripts=['openfaux_proxy.py'], # these files will be placed on /usr/bin
                           # Since the daemon binarys (like sshd) were placed
                           # on the /bin too, so the openfaux_proxy script must be there too!

    install_requires=[ # this keyword will deprecate the bootstrap.sh efficiently :D
    
        "Twisted >= 13.2.0"
    
    ]
)
