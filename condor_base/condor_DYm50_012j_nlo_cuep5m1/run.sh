#!/bin/sh
cd /home/choij/genvalid/CMSSW_11_2_0_pre7/src/Configuration/VGenStudies/condor_base/condor_DYm50_012j_nlo_cuep5m1
config=${1}
process=${2}

mkdir ${config}_${process}
cp ${config}_cfg.py ${config}_${process}
cd ${config}_${process}

source /cvmfs/cms.cern.ch/cmsset_default.sh
eval `scramv1 runtime -sh`

cmsRun ${config}_cfg.py
mv ${config}.root /home/choij/genvalid/CMSSW_11_2_0_pre7/src/Configuration/VGenStudies/condor_base/condor_DYm50_012j_nlo_cuep5m1/${config}_${process}.root