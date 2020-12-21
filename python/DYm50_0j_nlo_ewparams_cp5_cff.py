import FWCore.ParameterSet.Config as cms

externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    #args = cms.vstring('/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/madgraph/V5_2.4.2/VVV/WWWJets_4f_NLO_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz'),
    args = cms.vstring('root://eosuser.cern.ch//eos/user/c/choij/GenValidation/gridpacks/ewparams/dyellell0j_5f_NLO_FXFX_slc7_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz'),
	nEvents = cms.untracked.uint32(5000),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_xrootd.sh')
)
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *
from Configuration.Generator.Pythia8aMCatNLOSettings_cfi import *
from Configuration.Generator.PSweightsPythia.PythiaPSweightsSettings_cfi import *

generator = cms.EDFilter("Pythia8HadronizerFilter",
                         maxEventsToPrint = cms.untracked.int32(1),
                         pythiaPylistVerbosity = cms.untracked.int32(1),
                         filterEfficiency = cms.untracked.double(1.0),
                         pythiaHepMCVerbosity = cms.untracked.bool(False),
                         comEnergy = cms.double(13000.),
                         PythiaParameters = cms.PSet(
                            pythia8CommonSettingsBlock,
                            pythia8CP5SettingsBlock,
                            pythia8aMCatNLOSettingsBlock,
                            pythia8PSweightsSettingsBlock,
                            processParameters = cms.vstring(
                                'TimeShower:nPartonsInBorn = 0', #number of coloured particles (before resonance decays) in born matrix element
                                ),
                            parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CP5Settings',
                                    'pythia8aMCatNLOSettings',
                                    'pythia8PSweightsSettings',
                                    'processParameters',
                                    )
                            )
                         )

llgenfilter = cms.EDFilter("MCMultiParticleFilter",
                           Status = cms.vint32(23, 23),
                           src = cms.untracked.InputTag('generator','unsmeared'),
                           ParticleID = cms.vint32(11, 13),
                           PtMin = cms.vdouble(0, 0),
                           NumRequired = cms.int32(2),
                           EtaMax = cms.vdouble(9999, 9999),
                           AcceptMore = cms.bool(True)
                           )

ProductionFilterSequence = cms.Sequence(generator + llgenfilter)
