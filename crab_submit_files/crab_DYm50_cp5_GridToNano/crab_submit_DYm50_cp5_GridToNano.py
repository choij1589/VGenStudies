from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'DYm50_cp5_GridToNano'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = '../../configs/DYm50_cp5_GridToNano_cfg.py'
#config.JobType.allowUndistributedCMSSW = True
#config.JobType.numCores = 1

config.Data.outputPrimaryDataset = 'DYm50_cp5_GridToNano'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 6000 # num. of jobs to submit
NJOBS = 1000  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/choij/' 
config.Data.publication = True
config.Data.outputDatasetTag = 'RunIISummer15wmLHEGS'

config.Site.storageSite = 'T2_KR_KNU'
