#export PYTHONPATH=:/home/bioinfo/modules

PID_FILE=/run/jupyterhub.pid
RUN_CWD=/root/jupyterhub

function start() {
    cd $RUN_CWD
    nohup jupyterhub >> /var/log/jupyterhub.log 2>&1 &
}

function stop () {
    pid=$(cat $PID_FILE)
    [ -z "$pid" ] && { echo nothing to stop; return; }
    ps $pid > /dev/null 2>&1 || {
	rm $PID_FILE
	echo nothing to stop
	return
    }
    kill $pid
    echo stopped
}

function status () {
    pids=$(pgrep jupyter)
    if [ -z "$pids" ] ; then
	echo no jupyter process
    else
	ps $pids
    fi
}

main() {
    case $1 in
	start|stop|status) $1;;
	*) echo command $1 not known
    esac
}

main "$@"
