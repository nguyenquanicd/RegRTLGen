//--------------------------------------
//Project: The UVM environemnt for RegisterRTL
//Function: Register Config Monitor
//Author:  Nguyen Hung Quan, Le Hoang Van, Le Tan Thinh
//Page:    VLSI Technology
//--------------------------------------

// Content declare

class RegRTL_Scoreboard extends uvm_scoreboard;

  // Content create
  
  // Content internal variables
  
  `uvm_component_utils(RegRTL_Scoreboard)

  function new(string name = "RegRTL_Scoreboard", uvm_component parent);
    super.new(name, parent);
  endfunction: new
  
  function void build_phase(uvm_phase phase);
    super.build_phase(phase);
    // Content regist
 endfunction: build_phase
  
  // Content function

 function void report_phase(uvm_phase phase);
    super.report_phase(phase);
 endfunction: report_phase
  
endclass: RegRTL_Scoreboard 
