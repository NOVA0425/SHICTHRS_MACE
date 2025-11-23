
import subprocess
import copy
from ..SHRMACE_Data import SHRMACEResult
from ..SHRMACE_ErrorBase import SHRMACEException

def get_cpu_info() -> None:
    try:
        output = subprocess.check_output('wmic cpu get name' , shell=True).decode().split('\n')[1].strip()
        SHRMACEResult['CPUINFO'] = copy.deepcopy(output if output else None)
    except:
        raise SHRMACEException('SHRMACEException [ERROR.2002] unable to get CPU info.')