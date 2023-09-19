import subprocess
import re
import os
import time

def save_simulation_with_id(id: int, length: float, width: float, force1: float, force2: float, force3: float, force4: float, young_modulus: str, poisson_ratio: str):
    cli_command = f"FreeCAD freeCAD\simulation.py {id} {length} {width} {force1} {force2} {force3} {force4} {young_modulus} {poisson_ratio}"
    try:
        subprocess.run(cli_command, encoding="utf8", capture_output=True, shell=True, check=True)
    except: pass

    

def get_displacement_magnitude(length: float, width: float, force1: float, force2: float, force3: float, force4: float, young_modulus: str, poisson_ratio: str):
    cli_command = f"FreeCADcmd freeCAD\simulation_cmd.py {length} {width} {force1} {force2} {force3} {force4} {young_modulus} {poisson_ratio}"
    console_output = subprocess.run(cli_command, encoding="utf8", capture_output=True, shell=True, check=True).stdout
    res = re.search(r'(?<=(Value  : ))\d+.\d+', console_output).group(0)
    return float(res)
