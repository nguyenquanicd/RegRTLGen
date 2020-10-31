//--------------------------------------
//Project: The UVM environemnt for RegisterRTL
//Function: Register Config sequence
//Author:  Le Hoang Van
//Page:    VLSI Technology
//--------------------------------------

//--------------------------------------
//Register Config sequence
//--------------------------------------
class RegConfig_Seq extends uvm_sequence#(RegConfig_Transaction);
	`uvm_object_utils(RegConfig_Seq)
	`uvm_declare_p_sequencer(RegConfig_Sequencer)
  
  RegConfig_Transaction RegConfig_Trans;
  
  rand logic [31:0] Reg_Addr;
  rand logic [31:0] Reg_Data;
  rand int   Reg_Upper_bit;
  rand int   Reg_Lower_bit;
  rand logic Reg_IWE_value;

	function new (string name = "RegConfig_Seq");
		super.new(name);
    RegConfig_Trans = RegConfig_Transaction::type_id::create("RegConfig_Trans");
	endfunction

	virtual task body();
		start_item(RegConfig_Trans);
		assert(RegConfig_Trans.randomize() with {
      RegConfig_Trans.Addr       == Reg_Addr;
      RegConfig_Trans.Data       == Reg_Data;
			RegConfig_Trans.Upper_bit  == Reg_Upper_bit;
			RegConfig_Trans.Lower_bit  == Reg_Lower_bit;
			RegConfig_Trans.IWE_value  == Reg_IWE_value;
		});
		finish_item(RegConfig_Trans);
	endtask
endclass
