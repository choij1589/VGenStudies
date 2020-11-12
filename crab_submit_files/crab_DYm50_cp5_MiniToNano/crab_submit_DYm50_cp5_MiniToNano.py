from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'DYm50_cp5_MiniToNano'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '../../configs/DYm50_cp5_MiniToNano_cfg.py'
config.JobType.allowUndistributedCMSSW = True
config.JobType.numCores = 4

config.Data.inputDataset='/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM'
#config.Data.outputPrimaryDataset = 'DYm50_cp5_MiniToNano'
config.Data.inputDBS='global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
#config.Data.unitsPerJob = 6000 # num. of jobs to submit
#NJOBS = 1000  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
#config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/choij/' 
config.Data.publication = True
config.Data.outputDatasetTag = 'RunIIFall17MiniAODv2'

config.Site.storageSite = 'T2_KR_KNU'
