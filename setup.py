#import setuptools
from distutils.core import setup, Extension
import glob
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="stereo_vision",
    version="0.0.1",
    author="Aditya NG, Dhruval PB",
    author_email="adityang5@gmail.com, dhruvalpb@gmail.com",
    packages=['stereo_vision'],
    package_dir={'stereo_vision': 'stereo_vision'},
    include_package_data=True,
    package_data={'stereo_vision': glob.glob("build/bin/*.so") + glob.glob("data/*")},
    #scripts=['bin/vivp'],
    license='LICENSE.txt',
    url='https://github.com/AdityaNG/Depth-Perception-from-Stereoscopic-Vision-on-Edge-Devices',
    description="A library to simplify disparity calculation and 3D depth map generation from a stereo pair",
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.6',
)

"""
To upload :
rm -rf dist/
python3 setup.py sdist bdist_wheel
python3 -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
"""
