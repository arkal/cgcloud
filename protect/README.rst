The CGCloud plugin for Toil lets you setup a fully configured Toil/Mesos
cluster in EC2 in just minutes, regardless of the number of nodes.


Prerequisites
=============

The ``cgcloud-protect`` package requires that the ``cgcloud-core`` and ``cgcloud-toil`` packages and
their prerequisites_ are present.

.. _prerequisites: ../core#prerequisites


Installation
============

Read the entire section before pasting any commands and ensure that all
prerequisites are installed. It is recommended to install this plugin into the 
virtualenv you created for CGCloud::

   source ~/cgcloud/bin/activate
   pip install cgcloud-protect

If you get ``DistributionNotFound: No distributions matching the version for
cgcloud-protect``, try running ``pip install --pre cgcloud-protect``.

Be sure to configure_ ``cgcloud-core`` before proceeding.

.. _configure: ../core/README.rst#configuration

Configuration
=============

Modify your ``.profile`` or ``.bash_profile`` by adding the following line::

   export CGCLOUD_PLUGINS="cgcloud.protect:$CGCLOUD_PLUGINS"

Login and out (or, on OS X, start a new Terminal tab/window).

Verify the installation by running::

   cgcloud list-roles

The output should include the ``protect-box`` role.

Usage
=====

Create a single ``t2.micro`` box to serve as the template for the cluster
nodes::

   cgcloud create -IT protect-box

The ``I`` option stops the box once it is fully set up and takes an image (AMI)
of it. The ``T`` option terminates the box after that.

Substitute ``protect-latest-box`` for ``protect-box`` if you want to use the latest
unstable release of Toil.

Now create a cluster by booting a leader and the workers from that AMI::

   cgcloud create-cluster protect -s 2 -t m3.large
   
This will launch a leader and two workers using the ``m3.large`` instance type.

SSH into the leader::

   cgcloud ssh protect-leader
   
... or the first worker::

   cgcloud ssh -o 0 protect-worker
   
... or the second worker::

   cgcloud ssh -o 1 protect-worker

