//--------------------------------------
//Project: The UVM environemnt for RegisterRTL
//Function: Sequencer wraps Scoreboard, APB Agent, Register Config Agent
//Author:  Nguyen Hung Quan, Le Hoang Van, Tran Huu Duy
//Page:    VLSI Technology
//--------------------------------------

class RegRTL_Sequencer extends uvm_sequencer#(cApbTransaction);
  cApbMasterAgent coApbMasterAgent;
  RegConfig_Agent co_RegConfig_Agent;
  RegRTL_Scoreboard co_RegRTL_Scoreboard;

  `uvm_component_utils(RegRTL_Sequencer)

  function new(string name = "RegRTL_Sequencer", uvm_component parent = null);
    super.new(name,parent);
  endfunction: new

  function void build_phase(uvm_phase phase);
    super.build_phase(phase);
  endfunction: void
endclass: RegRTL_Sequencer
