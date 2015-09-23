# Intro

Made a first attempt at setting up a jupyterhub VM based on debian.

Somehow I screwed up, started with `jupyterhub` before `jupyter` and ended up with only the python3 kernel.

Plus it was easy but a little error-prone, so I decided to redo it from scratch and take notes this time.

# prep on stupeflip

    create-vm.sh -f vivid jupyter
    lce jupyter
 ***

    cd ~/.ssh
    curl -O http://planete.inria.fr/Thierry.Parmentelat/keys/tparment.pub
    cat tparment.pub >> authorized_keys
    cd
    apt-get install -y rsync


# on the jupyter VM

* see script setup-ubuntu.sh
* which does everything needed
* which includes creation of user bioinfo
 
     
## browser

    http://jupyter.pl.sophia.inria.fr:8000/
    
* Sign in works right away
* Can create scratch notebook 
* python 3 is the only option

## I'm stuck there

As I can't seem to enable python2 notebooks, I can't publish the ones I have b/c

* FUN/MOOC notebooks infra is only python2
* and `corrections` only run python2 anyway