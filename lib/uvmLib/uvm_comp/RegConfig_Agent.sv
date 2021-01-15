//--------------------------------------
//Project: The UVM environemnt for RegisterRTL
//Function: Register Config Agent
//Author:  Nguyen Hung Quan, Le Hoang Van, Tran Huu Duy
//Page:    VLSI Technology
//--------------------------------------

class RegConfig_Agent extends uvm_agent;
  RegConfig_Driver    co_RegConfig_Driver;
  RegConfig_Sequencer co_RegConfig_Sequencer;
  RegConfig_Monitor   co_RegConfig_Monitor;

  `uvm_component_utils(RegConfig_Agent)

  function new(string name = "RegConfig_Agent", uvm_component parent);
      super.new(name, parent);
  endfunction: new

  function void build_phase(uvm_phase phase);
    super.build_phase(phase);
    co_RegConfig_Driver    = RegConfig_Driver::type_id::create("co_RegConfig_Driver",this);
    co_RegConfig_Sequencer = RegConfig_Sequencer::type_id::create("co_RegConfig_Sequencer",this);
    co_RegConfig_Monitor   = RegConfig_Monitor::type_id::create("co_RegConfig_Monitor",this);
  endfunction: build_phase

  function void connect_phase(uvm_phase phase);
    super.connect_phase(phase);
    co_RegConfig_Driver.seq_item_port.connect(co_RegConfig_Sequencer.seq_item_export);
  endfunction: connect_phase
    
endclass: RegConfig_Agent
