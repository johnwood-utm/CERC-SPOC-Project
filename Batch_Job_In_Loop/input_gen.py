#!/usr/bin/env python3

import os

trns=[ x for x in os.listdir('.') if x[-3:]=='trn']

ret={}
    
for i in trns:
    ret[i]=[float(i[13:18]),float(i[22:27])]
    
       
maxi=-1
case=''
for i in ret:
    if ret[i][0]>maxi:
        maxi=ret[i][0]
        case=i
        
newstart=ret[case][1]
newfinish=newstart+0.08

newtrn='outputfile_t=%5.3fs_t=%5.3fs_standby.trn' % (newstart,newfinish)
savefile= 'SPOC_LES_17CH4_DYNAMICSTRESS_0.001_%5.3fs.dat' % newfinish
newdat='SPOC_LES_17CH4_DYNAMICSTRESS_0.001_%5.3fs.dat' % newstart

input_str="""; start transcript file
/file/start-transcript %s

report/system/sys-stats
chdir /gpfs20/scratch/ai0013/gideon
file/read-case SPOC_LES_10CH4_DYNAMICSTRESS_0.001_1stOrderImplicit_t=5.407s_continuation.cas
file/read-data %s
;solve/report-files/edit/x_0.25m_temperature-rfile file-name 
;/gpfs20/scratch/ai0013/DDPM/x_0.25m_temperature/x_0.25m_temperature.out
q
q
q
q
q
solve/dual-time-iterate 
80 
20
file/write-data %s
exit
yes
""" % (newtrn,newdat, savefile)

newinput='input.in_%5.3f_%5.3f' % (newstart,newfinish)

wf=open(newinput, 'w')
wf.write(input_str)
wf.close()

if os.path.exists('input.in'):
   os.remove('input.in')

os.symlink(newinput,'input.in')
