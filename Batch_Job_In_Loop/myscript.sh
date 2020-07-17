#!/bin/bash

cd $HOME/TEST

if [ -f FINISHED ]
then
	
	rm FINISHED
	/opt/torque/6.1.3/bin/qsub runjob.PBS
else
	echo "FINISHED not found"

fi
