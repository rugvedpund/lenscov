#!/bin/bash

date
##wait
##./cosmogpu_covariances.sh mpi _test_ Bmodes_params_lowAcc
##wait
##./cosmogpu_covariances.sh mpi _test_ Bmodes_params_lowAcc
wait
./cosmogpu_covariances.sh mpi CMB-S4_0.5uK Bmodes_params_lowAcc
wait
./cosmogpu_covariances.sh mpi CMB-S4_1.0uK Bmodes_params_lowAcc
wait
./cosmogpu_covariances.sh mpi CMB-S4_2.0uK Bmodes_params_lowAcc
wait
date