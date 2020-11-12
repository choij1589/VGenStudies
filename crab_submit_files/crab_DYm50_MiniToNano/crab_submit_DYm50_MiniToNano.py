from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'DYJetsToLL_official_MiniAOD_to_NanoAOD'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '../../configs/DYm50_cfg.py'
config.JobType.allowUndistributedCMSSW = True
config.JobType.numCores = 4

config.Data.inputDataset= '/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/MINIAODSIM'
#config.Data.outputPrimaryDataset = 'DYJetsToLL_MG271_amcatnlo-pythia8'
config.Data.inputDBS='global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1 # num. of jobs to submit
#NJOBS = 100  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
#config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
#config.Data.outLFNDirBase = '/store/group/cmst3/user/kelong/' 
config.Data.outLFNDirBase = '/store/user/choij/' 
config.Data.publication = True
config.Data.outputDatasetTag = 'RunIISummer15wmLHEGS'

config.Site.storageSite = 'T2_KR_KNU'
