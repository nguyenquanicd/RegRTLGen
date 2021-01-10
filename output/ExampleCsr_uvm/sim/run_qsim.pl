#!/bin/perl

#---------------------------------------------
#The installed directory of Simulation tool 
#---------------------------------------------
my $SIM_TOOL = "D:/Work/QuestaSim10.4/QS/win64";
print "-- Simulate on $SIM_TOOL\n";

#---------------------------------------------
#Define all used tools
#---------------------------------------------
my $VLog    = "$SIM_TOOL/vlog.exe";
my $VSim    = "$SIM_TOOL/vsim.exe";
my $VCov    = "$SIM_TOOL/vcover.exe";

if ($ARGV[0] eq "MERGE_COVERAGE") {
	#---------------------------------------------
	#Merge coverage
	#---------------------------------------------
	my $vmerge = "$VCov merge mergedCov.ucdb ../cov/*.ucdb";
	
	system "$vmerge";
	
	my $vcover = "$VCov report -html -htmldir ./ -code bcestf -cvg mergedCov.ucdb";
	#my $vcover = "$VCov report -html -htmldir ./ -stmtaltflow -cvg cov.ucdb";

	system "$vcover";
} else {
	#system "cp -f ../pat/$ARGV[0]/RegRTL_Sequence.sv ../uvm_comp/.";

	#---------------------------------------------
	#Compilation
	#---------------------------------------------
	my $vlog = "$VLog -work work \\
	+define+UVM_CMDLINE_NO_DPI \\
	+define+UVM_REGEX_NO_DPI \\
	+define+UVM_NO_DPI \\
	+define+INTERRUPT_COM \\
	+incdir+D:/Work/QuestaSim10.4/QS/verilog_src/uvm-1.2/src \\
	+incdir+D:/Work/RegRTLGen/output/ExampleCsr_uvm/uvm_comp \\
    -y D:/Work/RegRTLGen/output/ExampleCsr_uvm/dut \\
	-sv \\
	./RegRTL_Top.sv \\
	-timescale 1ns/1ns \\
	-l vlog.log \\
	+cover=bcestf \\
    -coveropt 1";
	
	system "$vlog";
	
	#---------------------------------------------
	#Simulation
	#---------------------------------------------
	my $vsim = "$VSim -c -novopt work.RegRTL_Top \\
	+UVM_TESTNAME=RegRTL_Test \\
	+UVM_VERBOSITY=UVM_LOW \\
	-do \"coverage save -codeAll -cvg -onexit $ARGV[0].ucdb; run -all;\" \\
	-coverage \\
    -coveranalysis \\
	-cvgperinstance \\
	-l vsim.log";
	
	system "$vsim";
	
	#Save coverage database
	system "cp -rf $ARGV[0].ucdb ../cov/";
	
	#---------------------------------------------
	#Generate html report
	#---------------------------------------------
    #my $vcover = "$VCov report -html -htmldir ./ -code bcestf -stmtaltflow -cvg $ARGV[0].ucdb";
    # my $vcover = "$VCov report -html -code bcestf -stmtaltflow -cvg $ARGV[0].ucdb";
    my $vcover = "$VCov report -html -code bcestf -cvg $ARGV[0].ucdb";
	
	#system "$vcover";
}
