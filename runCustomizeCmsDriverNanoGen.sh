#! /bin/bash

#TODO: Make this a proper script that also creates a crab_submit file
if [[ $# -lt 2 ]]; then
    echo "Must have at least two arguments: runCmsDriverNanoGen.sh <config fragment> <outputfile> <numcores>"
    exit 1
fi

#customize="--customise_commands process.RandomNumberGeneratorService.externalLHEProducer.initialSeed=999"
customize="--customise PhysicsTools/NanoAOD/nanogen_cff.setLHEFullPrecision"
if [[ $# -gt 2 ]]; then
    #customize="${customize}\nprocess.externalLHEProducer.generateConcurrently=True --nThreads $3"
	customize="${customize} --nThreads $3"
fi

fragment=${1/python\//}

cmsDriver.py Configuration/VGenStudies/python/$fragment \
    --fileout file:$2 --mc --eventcontent NANOAODGEN \
    --datatier NANOAOD --conditions auto:mc --step LHE,GEN,NANOGEN \
    --python_filename configs/${fragment/cff/cfg} \
    $customize \
	--customise PhysicsTools/NanoAOD/nanogen_cff.pruneGenParticlesMini \
    -n 100 --no_exec
