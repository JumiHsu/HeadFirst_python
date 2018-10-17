# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 03:18:02 2018

@author: SCM80
"""


print('\n'.join([''.join([('LoveKC11'[(x-y)%8] if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <=0 else' ')for x in range(-30,30)])for y in range(20,-20,-1)]))
