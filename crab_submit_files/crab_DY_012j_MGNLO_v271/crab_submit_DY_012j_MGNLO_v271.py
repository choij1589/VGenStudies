from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'DYJetsToLL_mg271_amcatnlo-pythia8'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = '../../configs/DY_MGNLO_inclusive_012j_cfg.py'
config.JobType.allowUndistributedCMSSW = True
config.JobType.numCores = 1

config.Data.outputPrimaryDataset = 'DYJetsToLL_012j_MG271_amcatnlo-pythia8'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 6000 # num. of jobs to submit
NJOBS = 1000  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
#config.Data.outLFNDirBase = '/store/group/cmst3/user/kelong/' 
config.Data.outLFNDirBase = '/store/user/choij/' 
config.Data.publication = True
config.Data.outputDatasetTag = 'RunIISummer15wmLHEGS'

config.Site.storageSite = 'T2_KR_KNU'
