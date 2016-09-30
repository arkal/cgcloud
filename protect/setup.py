from __future__ import absolute_import
from setuptools import setup, find_packages
from version import cgcloud_version, bd2k_python_lib_dep, fabric_dep

setup( name='cgcloud-protect',
       version=cgcloud_version,

       author='Arjun Rao',
       author_email='aarao@ucsc.edu',
       url='https://github.com/BD2KGenomics/cgcloud',
       description='Setup and manage a protect and Apache Mesos cluster in EC2',

       package_dir={ '': 'src' },
       packages=find_packages( 'src' ),
       namespace_packages=[ 'cgcloud' ],
       install_requires=[ 'cgcloud-lib==' + cgcloud_version,
                          'cgcloud-core==' + cgcloud_version,
                          'cgcloud-mesos==' + cgcloud_version,
                          'cgcloud-toil==' + cgcloud_version,
                          bd2k_python_lib_dep,
                          fabric_dep ] )
