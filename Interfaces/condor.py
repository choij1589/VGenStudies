import os

def make_config_dir(base_path, config):
	path = base_path + "/condor_" + config
	print("INFO: Jobs will be run in", path)
	print("WARNING: Base directory will be overwritten")
	if os.path.isdir(path):
		os.system("rm -rf " + path)
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

	elif host == "knu":
		run_script = """#!/bin/sh
cd """ + path + """
config=${1}
process=${2}

mkdir ${config}_${process}
cp ${config}_cfg.py ${config}_${process}
cd ${config}_${process}

source /cvmfs/cms.cern.ch/cmsset_default.sh
eval `scramv1 runtime -sh`
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/cvmfs/cms.cern.ch/slc7_amd64_gcc493/external/gcc/4.9.3/lib64

cmsRun ${config}_cfg.py
mv ${config}.root """ + output_path + """/${config}_${process}.root"""
	
	elif host == "lxplus":
		run_script = """#!/bin/sh
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

# stop jobs from running if they blow up in size or memory
periodic_hold        = (DiskUsage/1024 > 10.0*2000 ||  ImageSize/1024 > RequestMemory*2)

+JobFlavour = "workday"
arguments             = {config} $(Process)
output                = output/job_$(Process).out
error                 = error/job_$(Process).err
log                   = log/job_$(Process).log

queue {njobs}
"""
	elif host=="knu":
		condor_jdl = f"""Universe             = vanilla
Executable           = run.sh
GetEnv               = false

WhenToTransferOutput = On_Exit_Or_Evict
ShouldTransferFiles  = yes
want_graceful_removal = True
request_memory       = 2000
request_disk         = 2048000
use_x509userproxy = True

# stop jobs from running if they blow up in size or memory
periodic_hold        = (DiskUsage/1024 > 10.0*2000 ||  ImageSize/1024 > RequestMemory*2)

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
request_memory       = 2000
request_disk         = 2048000
use_x509userproxy = True

# stop jobs from running if they blow up in size or memory
periodic_hold        = (DiskUsage/1024 > 10.0*2000 ||  ImageSize/1024 > RequestMemory*2)

+JobFlavour = "workday"

error                 = error/job_$(Process).err
log                   = log/job_$(Process).log

queue {njobs}
"""
	else:
		raise(NameError)

	f = open(path + "/condor.jdl", "w")
	f.write(condor_jdl)
	f.close()

