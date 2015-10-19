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
* sept. 30 2015 : 
jupyterhub (0.2.0)
jupyter (1.0.0)
jupyter-client (4.0.0)
jupyter-console (4.0.2)
jupyter-core (4.0.6)

# browser

    http://jupyter.pl.sophia.inria.fr/
    
* Sign in works right away for `bioinfo`
* Can create scratch notebook 
* python2 or 3 are supported

For now this is mostly only a convenient way to show the notebooks in a running environment (esp. exercises)

# Additions

## configured `jupyterhub`

See `jupyter/` subdir in git repo for

* initscript `jupyterhub.sh`
* config file `/root/jupyterhub/jupyterhub_config.py` - primarily run on port 80

##  locale and UniCode

    # locale-gen en_US.UTF-8
    # update-locale LANG=en_US

Plus, as this was not bad enough, I also had to apply manually this change 

    [jupyter] /usr/lib/python2.7 # diff site.py site.py.distrib
    495c495
    <     if True:
    ---
    >     if 0:
    
so that `sys.getdefaultencoding()` would finally return `UTF-8` and not stubbornly  `ascii` like it used to.

## git

    # aptg-et install -y git

## PYTHONPATH

In order to have all users find the `modules/` repo in their local dir, I wrote a file named `jupyter_notebook_config.py` as per [thie link](https://github.com/jupyter/jupyterhub/issues/227); it is intended to be installed in `/etc/jupyter`.


## Various customizations


### filenames
First off, there seems to be some confusion between `~/.ipython` and `~/.jupyter`. I symlink them together for now

### shortcuts
Then in order to install the keyboard shortcuts I had in place for developping flotpython:

  * I refactored older `devel_custom.js` to produce an extension 
  * stored in git under `nbextensions/author-keyboard.js`
  * that gets installed (manually) under `/home/bioinfo/.jupyter/nbextensions/author-keyboard.js`
  * Plus, I had to run a somewhat magical JS sentence that reads like this; not quite sure what this is all about..

#
    IPython.notebook.config.update({
      "load_extensions": {"author-keyboard":true}
    })
  
### rendering / CSS  
`custom.css` is for rendering, for now I just copied manually
  * `flotpython/html/custom.css` 
  * onto `bioinfo@jupyter:.jupyter/`
  *  and in `.jupyter/profile_default/static/custom/custom.css` 

### lightning
I wanted to give a try to [Lightning viz](http://lightning-viz.org/) after I had seen [a sample notebook here](http://nbviewer.ipython.org/github/lightning-viz/lightning-example-notebooks/blob/master/plots/scatter.ipynb)

    pip3 install lightning-python
    
I could do a bit with that; see the [test-lightning notebook](http://jupyter.pl.sophia.inria.fr/user/thierry/notebooks/flotbioinfo/tests/test-lightning.ipynb)

Should be easy enough to [run our own server, instructions here](http://lightning-viz.org/setup/#deploy-server); keeping this aside for now

### bokeh
Made similar tests with [bokeh](http://nbviewer.ipython.org/github/bokeh/bokeh-notebooks/blob/master/tutorial/02%20-%20plotting.ipynb)

    pip3 install bokeh

### spelling

    apt-get install aspell libaspell-dev
    pip3 install aspell-python-py3

## TODOs

Automate all this for creating new users on the fly