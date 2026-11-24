from gem5.components.boards.riscv_board import RiscvBoard
from a1_processor import RiscvProcessor
from a1_memory import DualChannelDDR5
from a1_cache_hierarchy import PrivateL1SharedL2SharedL3CacheHierarchy

# to run the simulation and get workload
from gem5.simulate.simulator import Simulator
from gem5.resources.resource import obtain_resource

from gem5.components.cachehierarchies.classic.private_l1_shared_l2_cache_hierarchy import PrivateL1SharedL2CacheHierarchy


"""
Assignment #1: Assemble-Your-Own-System

Name: 
"""

processor = RiscvProcessor()

cache = PrivateL1SharedL2SharedL3CacheHierarchy(
    l1d_size="24KiB", 
    l1i_size="32KiB",
    l2_size="2MiB",
    l3_size="4MiB",
    l1d_assoc=2,
    l1i_assoc=2,
    l2_assoc=8,
    l3_assoc=16
)

memory = DualChannelDDR5("16GiB")

board = RiscvBoard(
    clk_freq="4GHz",
    processor = processor,
    cache_hierarchy = cache,
    memory = memory
)

board.set_workload(
    obtain_resource("riscv-matrix-multiply-run")
)

# Run the simulation until its end
sim = Simulator(board)
sim.run()
