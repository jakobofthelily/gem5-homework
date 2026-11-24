"""
Assignment #1: Assemble-Your-Own-System

Parameterized memory component

Name: 
"""

from gem5.components.memory.dram_interfaces.ddr5 import DDR5_6400_4x8
from gem5.components.memory.abstract_memory_system import AbstractMemorySystem
from gem5.components.memory.memory import ChanneledMemory

def DualChannelDDR5(size):
    return ChanneledMemory(
        dram_interface_class=DDR5_6400_4x8,
        num_channels=2,
        interleaving_size=64,
        size=size
    )