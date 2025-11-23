
import uuid
import copy
from ..SHRMACE_Data import SHRMACEResult
from ..SHRMACE_ErrorBase import SHRMACEException

def get_mac_info() -> None:
    try:
        mac_address = uuid.UUID(int=uuid.getnode()).hex[-12:].upper()
        mac_address = '-'.join([mac_address[i:i+2] for i in range(0, 11, 2)])
        SHRMACEResult['MACAddress'] = copy.deepcopy(mac_address)
    except:
        raise SHRMACEException('SHRMACEException [ERROR.2012] unable to get MAC info.')