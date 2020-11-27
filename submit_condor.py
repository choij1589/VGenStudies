import os
import argparse
import subprocess
from Interfaces import condor as interface

# get command arguments
parser = argparse.ArgumentParser(description="llll")
parser.add_argument("--config", "-c", type=str, required=True, help="config name")
parser.add_argument("--njobs", "-n", type=int, default=1, help="number of jobs")
parser.add_argument("--output_path", "-o", type=str, required=True, help="Output path")

args = parser.parse_args()
config = args.config
njobs = args.njobs
output_path = args.output_path
print("INFO: Using comfig:", config)
print("INFO: Required jobs:", njobs)
print("INFO: Output will be stored at", output_path)

# Hostname
# currently checked for lxplus and tamsa
if "tamsa" in os.environ['HOSTNAME']:
	host = "tamsa"
if "lxplus" in os.environ['HOSTNAME']:
	host = "lxplus"

pwd = os.environ['PWD']
condor_base = pwd + "/condor_base"

path = interface.make_config_dir(condor_base, config)
interface.make_run_script(path, output_path, host)
interface.make_condor_jdl(path, host, config, njobs)
os.system("cp configs/" + config + "_cfg.py " + path)
os.chdir(path)
os.system("condor_submit condor.jdl")
