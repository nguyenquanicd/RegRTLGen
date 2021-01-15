#---------------------------------------------
#Compilation
#---------------------------------------------
vlog -work work \
  +define+UVM_CMDLINE_NO_DPI \
  +define+UVM_REGEX_NO_DPI \
  +define+UVM_NO_DPI \
  +define+INTERRUPT_COM \
  +incdir+C:/questasim64_10.2c/verilog_src/uvm-1.1d/src \
  +incdir+D:/GitHub/RegRTLGen/output/ExampleCsr_uvm/uvm_comp \
  -y D:/GitHub/RegRTLGen/output/ExampleCsr_uvm/dut \
  -sv \
  ./RegRTL_Top.sv \
  ../dut/ExampleCsr.sv \
  -timescale 1ns/1ns \
  -l vlog.log \
  +cover
  
#---------------------------------------------
#Simulation
#---------------------------------------------
vsim -novopt work.RegRTL_Top \
  +UVM_TESTNAME=RegRTL_Test \
  +UVM_VERBOSITY=UVM_LOW \
  -coverage \
  -l vsim.log

#---------------------------------------------
#Add some signals to waveform before running
#---------------------------------------------
do add_wave.do

#---------------------------------------------
#Run
#---------------------------------------------
run -all

#---------------------------------------------
#Report the coverage result
#---------------------------------------------
#coverage report -file {D:/20.Project/3.Github/New folder/UvmEnvUartApb/sim/cov_report.txt} -byfile -assert -directive -cvg -codeAll
