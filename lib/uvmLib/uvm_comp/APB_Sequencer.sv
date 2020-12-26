//--------------------------------------
//Project: The UVM environemnt for RegisterRTL
//Function: APB sequencer
//Author:  Nguyen Hung Quan, Le Hoang Van, Tran Huu Duy
//Page:    VLSI Technology
//--------------------------------------

class cApbMasterSequencer extends uvm_sequencer#(cApbTransaction);
  //Register to Factory
  `uvm_component_utils(cApbMasterSequencer)
  
  //Constructor
  function new (string name = "cApbMasterSequencer", uvm_component parent = null);
    super.new(name,parent);
  endfunction
endclass
