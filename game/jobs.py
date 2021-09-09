import random as rand 
import sys 

sys.path.append('./objects')

from common_data import *
from block import Block

def generate_block_layer(*args):
    POSITIONS = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900]
    for i in range(10):
        put = rand.randint(0, 10)
        if(put >= 2):
            val = rand.randint(0, 100)
            put = Block(val, [POSITIONS[i], -200], font, screen)
            blocks.append(put)

def purge_blocks(*args):
    global blocks
    for blk in blocks:
        if(blk.pos[1] >= 600):
            blocks.remove(blk)


def check_collision(*args):
    pass