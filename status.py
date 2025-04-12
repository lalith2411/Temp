import time
import ctypes
from ctypes import wintypes


def is_workstation_locked():
    WTS_CURRENT_SERVER_HANDLE = None
    WTS_CURRENT_SESSION = -1
    WTS_SESSIONSTATE_LOCK = 0x7  # WTSConnectState
    WTS_SESSIONSTATE_UNLOCK = 0x8

    WTSActive = 0  # active session
    WTSDisconnected = 6

    WTSConnectStateClass = 0

    WTSQuerySessionInformation = ctypes.windll.wtsapi32.WTSQuerySessionInformationW
    WTSFreeMemory = ctypes.windll.wtsapi32.WTSFreeMemory

    WTSQuerySessionInformation.restype = wintypes.BOOL

    buffer = ctypes.c_void_p()
    bytes_returned = wintypes.DWORD()

    result = WTSQuerySessionInformation(
        WTS_CURRENT_SERVER_HANDLE,
        WTS_CURRENT_SESSION,
        14,  # WTSConnectState
        ctypes.byref(buffer),
        ctypes.byref(bytes_returned)
    )

    if result:
        state = ctypes.cast(buffer, ctypes.POINTER(
            wintypes.DWORD)).contents.value
        WTSFreeMemory(buffer)
        print(f"{state=}")
        # 0 = Active, 1 = Connected, 2 = ConnectQuery, 3 = Shadow, 4 = Disconnected, 5 = Idle, 6 = Listen, 7 = Reset, 8 = Down, 9 = Init
        return state != 0  # True if not active (i.e., likely locked)

    return False


time.sleep(3)
# Usage
if is_workstation_locked():
    print("🔒 Workstation is locked")
else:
    print("🔓 Workstation is unlocked")
