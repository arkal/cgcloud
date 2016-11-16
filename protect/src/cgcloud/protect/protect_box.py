import logging

from cgcloud.core.box import fabric_task
from cgcloud.core.cluster import ClusterBox, ClusterWorker, ClusterLeader
from cgcloud.fabric.operations import pip, remote_sudo_popen, sudo, virtualenv

from cgcloud.toil.toil_box import ToilBoxSupport

log = logging.getLogger( __name__ )


class ProtectBoxSupport( ToilBoxSupport ):
    """
    A box with Mesos, Toil, Protect and their dependencies installed.
    """

    def _list_packages_to_install( self ):
        return super( ProtectBoxSupport, self )._list_packages_to_install( )

    def _post_install_mesos( self ):
        super( ProtectBoxSupport, self )._post_install_mesos( )
        self.__upgrade_s3am( )
        self.__install_protect( )

    @fabric_task
    def __upgrade_s3am( self ):
        sudo( '/opt/s3am/bin/pip install s3am' )

    @fabric_task
    def __install_protect(self):
        virtualenv(name='protect',
                   distributions=['protect==2.3.1a1.dev109'],
                   pip_distribution='pip==8.0.2',
                   executable='ProTECT',
                   system_site_packages=True )


class ProtectBox( ProtectBoxSupport ):
    """
    A box with Docker, Mesos, Protect, s3am, Toil, and all their dependencies installed.
    """

    def _toil_pip_args( self ):
        return [ 'toil[aws,mesos,encryption]==3.3.1' ]


class ProtectLeader( ProtectBox, ClusterLeader ):
    """
    Leader of a cluster of boxes booted from a protect-box image
    """
    pass


class ProtectWorker( ProtectBox, ClusterWorker ):
    """
    Worker in a cluster of boxes booted from a protect-box image
    """
    pass
