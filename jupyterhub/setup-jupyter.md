# Intro

How I did set up the jupyter (ubuntu) VM in stupeflip.

# prep on stupeflip

    create-vm.sh -f vivid jupyter
    lce jupyter
 ***
Post-install and open up ssh access for pushing setup script

    cd ~/.ssh
    curl -O http://planete.inria.fr/Thierry.Parmentelat/keys/tparment.pub
    cat tparment.pub >> authorized_keys
    cd
    apt-get install -y rsync


# on the jupyter VM

* see script `setup-jupyter-ubuntu.sh`
* which does everything needed wrt python/jupyter/jupyterhub, 
* in particular the creation of user `bioinfo`
* it does not yet configure the VM so that jupyterhub gets started at boot-time

# browser

    http://jupyter.pl.sophia.inria.fr/
    
* Sign in works right away for `bioinfo`
* Can create scratch notebook 
* python2 or 3 are supported

For now this is mostly only a convenient way to show the notebooks in a running environment (esp. exercises)

# Additions

## configured **jupyterhub**

See jupyter/ subdir in git repo for
* initscript
* config file (see git) - run on port 80

##  **locale**

    locale-gen en_US.UTF-8
    update-locale LANG=en_US

## TODOs

* **configure `PYTHONPATH` for spawned kernels**
  
Currently I can't seem to import a sample exercice.


