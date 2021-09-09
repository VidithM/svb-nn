import pygame
from pygame.locals import *
import time
import sys 

sys.path.append('./objects')

BKG_COLOR = (0, 0, 0)

pygame.init()

from common_data import *
from block import Block
from jobs import *

class Job:
    def __init__(self, duringMotion, interval, f, *args):
        self.duringMotion = duringMotion # Job should only run while player is moving
        self.last_run = 0
        self.interval = interval 
        self.args = args
        self.f = f 

    def go(self):
        self.f(self.args)
        self.last_run = time.time_ns() // 1e6

curr_jobs = []

def fulfill():
    for job in curr_jobs:
        now = time.time_ns() // 1e6
        if(now - job.last_run >= job.interval):
            job.go()

def render():
    for blk in blocks:
        blk.render()


def advance():
    for blk in blocks:
        blk.move_down(7)

#put = Block(50, (20, 20), font, WINDOW)
#blocks.append(put)

running = True

block_gen = Job(True, 4000, generate_block_layer)
purge = Job(False, 500, purge_blocks)

curr_jobs.append(block_gen)
curr_jobs.append(purge)

while(running):
    screen.fill(BKG_COLOR)
    render()
    advance()
    fulfill()
    for event in pygame.event.get():
        if(event.type == QUIT):
            running = False
    
    time.sleep(0.05)
    pygame.display.flip()