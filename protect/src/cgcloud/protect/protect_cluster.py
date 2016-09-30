from cgcloud.core.cluster import Cluster
from cgcloud.protect.protect_box import ProtectLeader, ProtectWorker


class ProtectCluster( Cluster ):
    @property
    def worker_role( self ):
        return ProtectWorker

    @property
    def leader_role( self ):
        return ProtectLeader
