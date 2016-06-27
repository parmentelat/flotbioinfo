# don't log this
set -x
apt-get update > /dev/null 2>&1
apt-get -y upgrade > /dev/null 2>&1

echo ====================
cat /etc/lsb-release
python --version
python3 --version
echo ====================

apt-get install -y python-pip python-dev libzmq-dev > /dev/null 2>&1

pip install jupyter

apt-get install -y npm nodejs-legacy > /dev/null 2>&1
npm install -g configurable-http-proxy > /dev/null 2>&1

apt-get install -y python3-pip > /dev/null 2>&1
pip3 install jupyterhub notebook > /dev/null 2>&1

# kernelspecs dir is this one
# ls -l /usr/local/share/jupyter/kernels/

ipython kernelspec install-self
pip3 install ipython jupyter_client ipykernel
ipython3 kernelspec install-self

echo ==================== "(3)"
jupyter kernelspec list
echo ====================

# at this point we have both kernels known to ipython kernelspec
# and we can create notebooks running both kernels

########## matplotlib
apt-get install -y python-matplotlib python3-matplotlib

### JS console was complaining about this, so ...
pip3 install ipywidgets

# at this point:
# I manually start jupyterhub in a terminal as root
# I can login at jupyter:8000 as bioinfo
# I can run plots in both python[23] but I need to explicitly say
# %matplotlib inline
# in the notebook

# need to try if I can run
# jupyterhub --matplotlib=inlne
# which would be just fine
# 
###

##########
useradd -m bioinfo
(echo infobio; echo infobio) | passwd bioinfo

mkdir ~bioinfo/.ssh
cp /root/.ssh/authorized_keys /home/bioinfo/.ssh
chmod 700 /home/bioinfo/.ssh
chmod 600 /home/bioinfo/.ssh/authorized_keys
chown -R bioinfo:bioinfo /home/bioinfo/.ssh
