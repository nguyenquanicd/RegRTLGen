//--------------------------------------
//Project: The UVM environemnt for RegisterRTL
//Function: Register Config Sequence
//Author:  Nguyen Hung Quan, Le Hoang Van, Le Tan Thinh
//Page:    VLSI Technology
//--------------------------------------

class RegConfig_Sequence extends uvm_sequence#(RegConfig_Transaction);

  RegConfig_Transaction co_RegConfig_Trans;
  rand logic [31:0] Reg_Addr;
  rand logic [31:0] Reg_Data;
  rand int   Reg_Upper_bit;
  rand int   Reg_Lower_bit;
  rand logic Reg_IWE_value;
  
  `uvm_object_utils(RegConfig_Sequence)
  `uvm_declare_p_sequencer(RegConfig_Sequencer)
  
  function new (string name = "RegConfig_Sequence");
    super.new(name);
    co_RegConfig_Trans = RegConfig_Transaction::type_id::create("co_RegConfig_Trans");
  endfunction: new

  virtual task body();
    start_item(co_RegConfig_Trans);
    assert(co_RegConfig_Trans.randomize() with {
      co_RegConfig_Trans.Addr      == Reg_Addr;
      co_RegConfig_Trans.Data      == Reg_Data;
      co_RegConfig_Trans.Upper_bit == Reg_Upper_bit;
      co_RegConfig_Trans.Lower_bit == Reg_Lower_bit;
      co_RegConfig_Trans.IWE_value == Reg_IWE_value;
    });
    finish_item(co_RegConfig_Trans);
  endtask: body
  
endclass: RegConfig_Sequence
