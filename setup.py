#! /usr/bin/python
import sys, os
from distutils.core import setup
from glob import glob

# to install type: 
# python setup.py install --root=/

locales=map(lambda i: ('share/'+i,[''+i+'/othman.mo',]),glob('locale/*/LC_MESSAGES'))
data_files=[('share/othman/',glob('othman-data/*'))]
data_files.extend(locales)
setup (name='Othman', version='0.2.2',
      description='Othman Quran Browser',
      author='Muayyad Saleh Alsadi',
      author_email='alsadi@ojuba.org',
      url='http://othman.ojuba.org/',
      license='Waqf',
      packages=['othman'],
      scripts=['othman-browser'],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: End Users/Desktop',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          ],
      data_files=data_files
)


