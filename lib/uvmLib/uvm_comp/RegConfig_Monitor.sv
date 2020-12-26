//--------------------------------------
//Project: The UVM environemnt for RegisterRTL
//Function: Register Config Monitor
//Author:  Nguyen Hung Quan, Le Hoang Van, Tran Huu Duy
//Page:    VLSI Technology
//--------------------------------------

class RegConfig_Monitor extends uvm_monitor;
  virtual interface RegConfig_Interface vif_RegConfig_IF;
  
  // Content create

  `uvm_component_utils(RegConfig_Monitor)
  
  function new(string name = "RegConfig_Monitor", uvm_component parent = null);
    super.new(name,parent);
  endfunction: new

  function void build_phase(uvm_phase phase);
    super.build_phase(phase);
    if(!uvm_config_db#(virtual interface RegConfig_Interface)::get(this,"","vif_RegConfig_IF",vif_RegConfig_IF)) begin
      `uvm_error("RegConfig_Driver","Can NOT get vif_RegConfig_IF!!!")
    end
    
    // Content regist
  endfunction: build_phase

  virtual task run_phase(uvm_phase phase);
    super.run_phase(phase);
    fork
      // Content collect
    join
  endtask: run_phase
  
  // Content task
  
endclass: RegConfig_Monitor
