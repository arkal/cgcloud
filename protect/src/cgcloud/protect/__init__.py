def roles( ):
    from cgcloud.protect.protect_box import (ProtectBox,
                                             ProtectLeader,
                                             ProtectWorker)
    return sorted( locals( ).values( ), key=lambda cls: cls.__name__ )


def cluster_types( ):
    from cgcloud.protect.protect_cluster import ProtectCluster
    return sorted( locals( ).values( ), key=lambda cls: cls.__name__ )
