"""
Assignment #1: Assemble-Your-Own-System

Parameterized processor component

Name: Sebastian Acerbi
"""

from gem5.isas import ISA
from gem5.components.processors.base_cpu_core import BaseCPUCore
from gem5.components.processors.base_cpu_processor import BaseCPUProcessor
from m5.objects.RiscvCPU import RiscvMinorCPU
from m5.objects.FuncUnitConfig import *

class Riscv(RiscvMinorCPU):
    def __init__(self):
        super().__init__()
        self.decodeInputWidth = 4
        self.executeInputWidth = 4
        self.executeBranchDelay = 2

class RiscvCore(BaseCPUCore):
    def __init__(self):
        core = Riscv()
        super().__init__(core, ISA.RISCV)

class RiscvProcessor(BaseCPUProcessor):
    def __init__(self):
        super().__init__(
            cores = [RiscvCore(), RiscvCore()],
            clk_freq="4GHz"
        )

