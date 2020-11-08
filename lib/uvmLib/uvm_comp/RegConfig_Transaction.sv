//--------------------------------------
//Project: The UVM environemnt for RegisterRTL
//Function: Register Config Transaction
//Author:  Le Hoang Van
//Page:    VLSI Technology
//--------------------------------------

class RegConfig_Transaction extends uvm_sequence_item;
  
  rand logic [31:0] Addr;
  rand logic [31:0] Data;
  rand logic [31:0] IWE;

  `uvm_object_utils_begin (RegConfig_Transaction)
    `uvm_field_int(Addr, UVM_ALL_ON)
    `uvm_field_int(Data, UVM_ALL_ON)
    `uvm_field_int(IWE,  UVM_ALL_ON)
  `uvm_object_utils_end
  
  function new (string name = "RegConfig_Transaction");
    super.new(name);
  endfunction: new
  
  virtual task print_config_seq();
		`uvm_info("CONFIG_SEQ", $sformatf("Addr = %0h, Data = %0h, IWE = %04b_%04b_%04b_%04b_%04b_%04b_%04b_%04b", 
    Addr, 
    Data, 
    IWE[31:28],
    IWE[27:24], 
    IWE[23:20], 
    IWE[19:16]), 
    IWE[15:12], 
    IWE[11:8], 
    IWE[7:4], 
    IWE[3:0]),
    UVM_LOW);
  endtask: print_config_seq

endclass: RegConfig_Transaction
