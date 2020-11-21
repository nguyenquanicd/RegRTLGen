//--------------------------------------
//Project: The UVM environemnt for RegisterRTL
//Function: Register Config S
//Author:  Nguyen Hung Quan, Le Hoang Van, Le Tan Thinh
//Page:    VLSI Technology
//--------------------------------------

class RegConfig_Sequencer extends uvm_sequencer#(RegConfig_Transaction);

  `uvm_component_utils(RegConfig_Sequencer)
  
  function new (string name = "RegConfig_Sequencer", uvm_component parent = null);
    super.new(name,parent);
  endfunction: new
  
endclass: RegConfig_Sequencer
