#!/bin/bash/
#list=( 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80)
list=( 1 2 3 4 5 7 9 10 11 12 13 14 15 16 17 19 20 21 23 24 25 26 27 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 45 46 47 48 49 50 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80)

for ext in ${list[@]}
do
  echo "Processing C2V=" $ext
  sed -e 's/\(C2V\)\([0-9][0-9]\)/\1'${ext}'/g' run_extLimit_forC2V_.sh >run_extLimitC2V${ext}.sh
  sed -e 's/\(C2V\)\([0-9][0-9]\)/\1'${ext}'/g' condor_job_runLimit_forC2V_.sub >condor_job_runLimitC2V${ext}.sub
  #. runWS.sh
  condor_submit condor_job_runLimitC2V${ext}.sub 
done
