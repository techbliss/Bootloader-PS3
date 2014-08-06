import os
import sys
import idaapi
import idc 

idc.SetProcessorType('spu', SETPROC_USER), idaapi.load_and_run_plugin("gdb_user.plw", 0)
sEA = 0x0
eEA = MaxEA()
analyze_area(sEA, eEA)
