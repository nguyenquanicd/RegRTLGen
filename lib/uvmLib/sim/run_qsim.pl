#!/bin/perl
use Switch;
#----------------------------------
#Website  :  http://nguyenquanicd.blogspot.com/
#Author   :  Le Hoang Van, Tran Huu Duy, Nguyen Hung Quan
#Function : Run QuestaSim tool
#Reversion and History:
# 2021.Apr.11 - Update the options
#----------------------------------

#----------------------------------
# Get the current script name
#----------------------------------
my $myScript   = $0;
$myScript =~ s/\.\///;
#----------------------------------
# Create the log file
#----------------------------------
my $myLog = "log_$myScript.log";
system "/usr/bin/rm -f log_$myScript.log";
open (LOGFILE, ">$myLog") or die because $!;
#----------------------------------
# Check input arguments
#----------------------------------
my $argNum  = @ARGV;
if ($argNum == 0) {
  printLog (LOGFILE, "[WARNING] Missing options - Simulation will run with default DUT ExampleCsr\n");
  printLog (LOGFILE, "          Please use the command .\/$myScript -help\n");
}
#----------------------------------
# Common information
#----------------------------------
#Account name
my $wName = getlogin();
#Generation time
my $wTime = localtime();
#Working directory
my $wDir  = $ENV{PWD};
$wDir =~ s/\/cygdrive\/d/D:/g;
#----------------------------------
# File header of output
#----------------------------------
my $headerFile;
$headerFile .= "#----------------------------------\n";
$headerFile .= "#Author              : $wName\n";
$headerFile .= "#Date                : $wTime\n";
$headerFile .= "#Working directory   : $wDir\n";
$headerFile .= "#Number of arguments : $argNum\n";
$headerFile .= "#Submitted command   : $myScript @ARGV\n";
$headerFile .= "#----------------------------------\n";
printLog (LOGFILE, $headerFile);
#---------------------------------------------
#The installed directory of Simulation tool 
#---------------------------------------------
#my $SRC_TOOL = "D:/Work/QuestaSim10.4/QS";
my $SRC_TOOL = "C:/questasim64_10.4c";
my $SIM_TOOL = "$SRC_TOOL/win64";
my $UVM_LIB  = "$SRC_TOOL/verilog_src/uvm-1.2/src";
printLog (LOGFILE, "----------------------------------------\n");
printLog (LOGFILE, "-- Simulation tool : $SIM_TOOL\n");
printLog (LOGFILE, "-- UVM library     : $UVM_LIB\n");
printLog (LOGFILE, "----------------------------------------\n");
#----------------------------------
# Scan arguments and assign the setting values
#----------------------------------
#Note: Must have "use Switch" when using switch
my $dut    = "ExampleCsr"; #Default DUT
my $covrpt = $dut; #Default coverage report
my $covm   = 0;
while ($argNum != 0) {
  my $arg = shift(@ARGV); #Get an argument
  switch($arg) {
    #Get DUT name
    case "-dut" {
      $dut = shift(@ARGV);
    }
    #Get coverage report name
    case "-cov" {
      $covrpt = shift(@ARGV);
    }
    #Merge coverage reports
    case "-covm" {
      $covm = 1;
    }
    case "-help" {
      printLog (LOGFILE, "#----------------------------------\n");
      printLog (LOGFILE, "Format: $myScript <option 0> <value 0> ... <option N> <value N>\n");
      printLog (LOGFILE, "  Option:\n");
      printLog (LOGFILE, "  -dut  : DUT name is a name of DUT top file. Default name is ExampleCsr\"\n");
      printLog (LOGFILE, "  -cov  : Coverage report name of the current testcase. Default name is ExampleCsr\"\n");
      printLog (LOGFILE, "  -covm : Perform merging all coverage reports in ../cov\"\n");
      printLog (LOGFILE, "  -help : Show all options.\n");
      printLog (LOGFILE, "#----------------------------------\n");
      exit;
    }
    else {
      printLog (LOGFILE, "[ERROR] Do NOT support the option: $arg\n");
      system "./$myScript -help";
      exit;
    }
  }
  $argNum  = @ARGV; #Update number of arguments
}

#---------------------------------------------
#Define all used tools
#---------------------------------------------
my $VLog    = "$SIM_TOOL/vlog.exe";
my $VSim    = "$SIM_TOOL/vsim.exe";
my $VCov    = "$SIM_TOOL/vcover.exe";

if ($covm eq "1") {
  #---------------------------------------------
  #Merge coverage
  #---------------------------------------------
  my $vmerge = "$VCov merge mergedCov.ucdb ../cov/*.ucdb";
  
  system "$vmerge";
  
  my $vcover = "$VCov report -html -htmldir ./ -code bcestf -cvg mergedCov.ucdb";
  #my $vcover = "$VCov report -html -htmldir ./ -stmtaltflow -cvg cov.ucdb";
  
  system "$vcover";
} else {
  #system "cp -f ../pat/$ARGV[1]/RegRTL_Sequence.sv ../uvm_comp/.";
  
  #---------------------------------------------
  #Compilation
  #---------------------------------------------
  #+incdir+C:/questasim64_10.2c/verilog_src/uvm-1.1d/src \\
  #+incdir+D:/GitHub/RegRTLGen/output/${dut}_uvm/uvm_comp \\
  my $vlog = "$VLog -work work \\
  +define+UVM_CMDLINE_NO_DPI \\
  +define+UVM_REGEX_NO_DPI \\
  +define+UVM_NO_DPI \\
  +incdir+$UVM_LIB \\
  +incdir+$wDir/../uvm_comp \\
  -sv \\
  ./RegRTL_Top.sv \\
  ../dut/$dut.sv \\
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
  -do \"coverage save -codeAll -cvg -onexit $cov.ucdb; do add_wave.do; run -all;\" \\
  -coverage \\
  -coveranalysis \\
  -cvgperinstance \\
  -l vsim.log";
  
  system "$vsim";
  
  #Save coverage database
  system "cp -rf $covrpt.ucdb ../cov/";
  
  #---------------------------------------------
  #Generate html report
  #---------------------------------------------
  #my $vcover = "$VCov report -html -htmldir ./ -code bcestf -stmtaltflow -cvg $covrpt.ucdb";
  #my $vcover = "$VCov report -html -code bcestf -stmtaltflow -cvg $covrpt.ucdb";
  my $vcover = "$VCov report -html -code bcestf -cvg $covrpt.ucdb";
  system "$vcover";
}
#----------------------------------
# Subrountines
#----------------------------------
#
#Print to a log file
#
sub printLog {
  my $fileHandle = shift;
  my $msg        = shift;
  #
  print "$msg";
  print $fileHandle $msg;
} #printLog
