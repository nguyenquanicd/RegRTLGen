#---------------------------------------------
#Compilation
#---------------------------------------------
vlog -work work +define+UVM_CMDLINE_NO_DPI +define+UVM_REGEX_NO_DPI +define+UVM_NO_DPI +define+INTERRUPT_COM -sv ./RegRTL_Top.sv timescale 1ns/1ns
#---------------------------------------------
#Simulation
#---------------------------------------------
#---------------------------------------------
#Add some signals to waveform before running
#---------------------------------------------
#do add_wave.do
#---------------------------------------------
#Run
#---------------------------------------------
#run -all
#---------------------------------------------
#Report the coverage result
#---------------------------------------------
#coverage report -file {D:/20.Project/3.Github/New folder/UvmEnvUartApb/sim/cov_report.txt} -byfile -assert -directive -cvg -codeAll
