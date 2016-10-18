#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Blood pressure status checks"""


INPUT = int(raw_input(' What is your blood pressure? '))

if INPUT <= 89:
    BPSTATUS = 'Low'
elif INPUT >= 90 and INPUT <= 119:
    BPSTATUS = 'Ideal'
elif INPUT >= 120 and INPUT <= 139:
    BPSTATUS = 'Warning'
elif INPUT >= 140 and INPUT <= 159:
    BPSTATUS = 'High'
else:
    BPSTATUS = ' Emergency' 
            
BP_READING = 'Your Blood Pressure status is: {}'.format(BPSTATUS)
print BP_READING 
