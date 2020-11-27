import os

def make_config_dir(base_path, config):
	path = base_path + "/condor_" + config
	print("INFO: Jobs will be run in", path)
	os.mkdir(path)
	os.mkdir(path + "/error")
	os.mkdir(path + "/log")
	os.mkdir(path + "/output")
	
	return path

def make_run_script(path, output_path, host):
	if host == "tamsa":
		run_script = """#!/bin/sh
cd """ +  path + """
config=${1}
process=${2}

mkdir ${config}_${process}
cp ${config}_cfg.py ${config}_${process}
cd ${config}_${process}

source /cvmfs/cms.cern.ch/cmsset_default.sh
eval `scramv1 runtime -sh`

cmsRun ${config}_cfg.py
mv ${config}.root """ + output_path + """/${config}_${process}.root"""
	
	elif host == "lxplus":
		run_script = """$!/bin/sh
cd """ + path + """
config=${1}
process=${2}

mkdir ${config}_${process}
cp ${config}_cfg.py ${config}_${process}
cd ${config}_${process}

source /cvmfs/cms.cern.ch/cmsset_default.sh
pushd $CMSSW_RELEASE_BASE
eval `scramv1 runtime -sh`
popd
export LD_LIBRARY_PATH=$PWD/lib:$LD_LIBRARY_PATH

cmsRun ${config}_cfg.py
mv ${config}.root """ + output_path + """/${config}_${process}.root"""

	else:
		raise(NameError)

	f = open(path + "/run.sh", "w")
	f.write(run_script)
	f.close()

def make_condor_jdl(path, host, config, njobs):
	if host == "tamsa":
		condor_jdl = f"""Universe             = vanilla
Executable           = run.sh
GetEnv               = false

WhenToTransferOutput = On_Exit_Or_Evict
ShouldTransferFiles  = yes 
want_graceful_removal = True
request_memory       = 2000
request_disk         = 2048000

+JobFlavour = "workday"
arguments             = {config} $(Process)
output                = output/job_$(Process).out
error                 = error/job_$(Process).err
log                   = log/job_$(Process).log

queue {njobs}
"""
	elif host == "lxplus":
		condor_jdl = f"""Universe             = vanilla
Executable           = run.sh
GetEnv               = false

WhenToTransferOutput = On_Exit_Or_Evict
ShouldTransferFiles  = yes 
want_graceful_removal = True
use_x509userproxy = True

+JobFlavour = "workday"
rguments             = {config} $(Process)
output                = output/job_$(Process).out
error                 = error/job_$(Process).err
log                   = log/job_$(Process).log

queue {njobs}
"""
	else:
		raise(NameError)

	f = open(path + "/condor.jdl", "w")
	f.write(condor_jdl)
	f.close()

