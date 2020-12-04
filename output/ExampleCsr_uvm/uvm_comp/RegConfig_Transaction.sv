//--------------------------------------
//Project: The UVM environemnt for RegisterRTL
//Function: Register Config Transaction
//Author:  Nguyen Hung Quan, Le Hoang Van, Le Tan Thinh
//Page:    VLSI Technology
//--------------------------------------

class RegConfig_Transaction extends uvm_sequence_item;
  
  rand logic [31:0] Addr;
  rand logic [31:0] Data;
  rand int   Upper_bit;
  rand int   Lower_bit;
  rand logic IWE_value;
  
  constraint Upper_cons {Upper_bit inside {[0:31]};};
  constraint Lower_cons {Lower_bit inside {[0:31]};};
  
  `uvm_object_utils_begin (RegConfig_Transaction)
    `uvm_field_int(Addr, UVM_ALL_ON)
    `uvm_field_int(Data, UVM_ALL_ON)
    `uvm_field_int(Upper_bit, UVM_ALL_ON)
    `uvm_field_int(Lower_bit, UVM_ALL_ON)
    `uvm_field_int(IWE_value, UVM_ALL_ON)
  `uvm_object_utils_end
  
  function new(string name = "RegConfig_Transaction");
    super.new(name);
  endfunction: new
  
  virtual task print_config_seq();
    if (IWE_value == 0) begin 
      `uvm_info("CONFIG_SEQ", $sformatf("Addr = %0h, Data = %0h, [%0d:%0d] is disable", Addr, Data, Upper_bit, Lower_bit), UVM_LOW);
    end
    else begin
      `uvm_info("CONFIG_SEQ", $sformatf("Addr = %0h, Data = %0h, [%0d:%0d] is enable", Addr, Data, Upper_bit, Lower_bit), UVM_LOW);
    end
  endtask: print_config_seq

endclass: RegConfig_Transaction


class ACTRL_monitor extends uvm_sequence_item;
  
  rand logic [31:0] ACTRL_reg; 
  rand logic [3:0] ACTRL_byte_we; 
  rand logic [31:0] ACTRL_ivalue; 
  rand logic ACTRL_RESERVED_iwe; 
  rand logic ACTRL_BAUND1_3_w1; 
  rand logic ACTRL_BAUND1_2_w1; 
  rand logic ACTRL_BAUND0_1_w0; 
  rand logic ACTRL_RWI_iwe; 

  `uvm_object_utils_begin (ACTRL_monitor)
    `uvm_field_int(ACTRL_reg, UVM_ALL_ON) 
    `uvm_field_int(ACTRL_byte_we, UVM_ALL_ON) 
    `uvm_field_int(ACTRL_ivalue, UVM_ALL_ON) 
    `uvm_field_int(ACTRL_RESERVED_iwe, UVM_ALL_ON) 
    `uvm_field_int(ACTRL_BAUND1_3_w1, UVM_ALL_ON) 
    `uvm_field_int(ACTRL_BAUND1_2_w1, UVM_ALL_ON) 
    `uvm_field_int(ACTRL_BAUND0_1_w0, UVM_ALL_ON) 
    `uvm_field_int(ACTRL_RWI_iwe, UVM_ALL_ON) 

  `uvm_object_utils_end
  
  function new (string name = "ACTRL_monitor");
    super.new(name);
  endfunction: new

endclass: ACTRL_monitor

class BCTRL_monitor extends uvm_sequence_item;
  
  rand logic [31:0] BCTRL_reg; 
  rand logic BCTRL_read_en; 
  rand logic [3:0] BCTRL_byte_we; 
  rand logic [31:0] BCTRL_ivalue; 
  rand logic BCTRL_RESERVED_iwe; 
  rand logic BCTRL_ROS_iwe; 
  rand logic BCTRL_ROC_iwe; 
  rand logic BCTRL_RO_iwe; 

  `uvm_object_utils_begin (BCTRL_monitor)
    `uvm_field_int(BCTRL_reg, UVM_ALL_ON) 
    `uvm_field_int(BCTRL_read_en, UVM_ALL_ON) 
    `uvm_field_int(BCTRL_byte_we, UVM_ALL_ON) 
    `uvm_field_int(BCTRL_ivalue, UVM_ALL_ON) 
    `uvm_field_int(BCTRL_RESERVED_iwe, UVM_ALL_ON) 
    `uvm_field_int(BCTRL_ROS_iwe, UVM_ALL_ON) 
    `uvm_field_int(BCTRL_ROC_iwe, UVM_ALL_ON) 
    `uvm_field_int(BCTRL_RO_iwe, UVM_ALL_ON) 

  `uvm_object_utils_end
  
  function new (string name = "BCTRL_monitor");
    super.new(name);
  endfunction: new

endclass: BCTRL_monitor
