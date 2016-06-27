set -x

# based on the result of create-vm.sh

cd .ssh
curl -O http://planete.inria.fr/Thierry.Parmentelat/keys/tparment.pub
cat tparment.pub >> authorized_keys

echo ====================
cat /etc/fedora-release
python --version
python3 --version
pip --version
pip2 --version
pip3 --version
echo ====================

dnf -y install  redhat-rpm-config gcc gcc-c++ python3-devel rsync less

pip3 install jupyter

type jupyter
jupyter --version
jupyter kernelspec list

### some messing around here to obtain a file
# ~/.jupyter/jupyter_notebook_config.py
jupyter migrate
jupyter notebook --generate-config
# edit to set instead of 'localhost':
# c.NotebookApp.ip = '0.0.0.0'

### operational python3 kernel at this point
# jupyter notebook

##########
dnf install python-devel
pip2 install ipykernel
jupyter kernelspec install /usr/lib/python2.7/site-packages/ipykernel/resources

jupyter kernelspec list
# only shows python2 but that's an artefact
# and both languages are supported (check in the 'new' dropdown)

