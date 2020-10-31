//--------------------------------------
//Project: The UVM environemnt for RegisterRTL
//Function: Register Config Transaction
//Author:  Le Hoang Van
//Page:    VLSI Technology
//--------------------------------------

class RegConfig_Transaction extends uvm_sequence_item;
  
  rand logic [31:0] Addr;
  rand logic [31:0] Data;
  rand int   Upper_bit;
  rand int   Lower_bit;
  rand logic IWE_value;

  constraint upper_bit_range {Upper_bit inside {[0:31]};};
  constraint lower_bit_range {Lower_bit inside {[0:31]};};

  `uvm_object_utils_begin (RegConfig_Transaction)
    `uvm_field_int(Addr, UVM_ALL_ON)
    `uvm_field_int(Data, UVM_ALL_ON)
    `uvm_field_int(Upper_bit, UVM_ALL_ON)
    `uvm_field_int(Lower_bit, UVM_ALL_ON)
    `uvm_field_int(IWE_value, UVM_ALL_ON)
  `uvm_object_utils_end
  
  function new (string name = "RegConfig_Transaction");
    super.new(name);
  endfunction: new
  
  virtual task print_config_seq();
    `uvm_info("CONFIG_SEQ", $sformatf("Addr = %0h, Data = %0h, Bitrange = [%0d:%0d], IWE = %0h", Addr, Data, Upper_bit, Lower_bit, IWE_value), UVM_LOW);
  endtask: print_config_seq

endclass: RegConfig_Transaction
