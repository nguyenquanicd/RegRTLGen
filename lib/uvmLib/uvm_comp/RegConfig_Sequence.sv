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
      RegConfig_Trans.Addr    == Reg_Addr;
      RegConfig_Trans.Data    == Reg_Data;
			RegConfig_Trans.IWE[31] == Reg_IWE_value if ((Reg_Lower_bit <= 31) && (31 <= Reg_Upper_bit)) else 0;
			RegConfig_Trans.IWE[30] == Reg_IWE_value if ((Reg_Lower_bit <= 30) && (30 <= Reg_Upper_bit)) else 0;
			RegConfig_Trans.IWE[29] == Reg_IWE_value if ((Reg_Lower_bit <= 29) && (29 <= Reg_Upper_bit)) else 0;
      RegConfig_Trans.IWE[28] == Reg_IWE_value if ((Reg_Lower_bit <= 28) && (28 <= Reg_Upper_bit)) else 0;
      RegConfig_Trans.IWE[27] == Reg_IWE_value if ((Reg_Lower_bit <= 27) && (27 <= Reg_Upper_bit)) else 0;
			RegConfig_Trans.IWE[26] == Reg_IWE_value if ((Reg_Lower_bit <= 26) && (26 <= Reg_Upper_bit)) else 0;
			RegConfig_Trans.IWE[25] == Reg_IWE_value if ((Reg_Lower_bit <= 25) && (25 <= Reg_Upper_bit)) else 0;
			RegConfig_Trans.IWE[24] == Reg_IWE_value if ((Reg_Lower_bit <= 24) && (24 <= Reg_Upper_bit)) else 0;
      RegConfig_Trans.IWE[23] == Reg_IWE_value if ((Reg_Lower_bit <= 23) && (23 <= Reg_Upper_bit)) else 0;
      RegConfig_Trans.IWE[22] == Reg_IWE_value if ((Reg_Lower_bit <= 22) && (22 <= Reg_Upper_bit)) else 0;
			RegConfig_Trans.IWE[21] == Reg_IWE_value if ((Reg_Lower_bit <= 21) && (21 <= Reg_Upper_bit)) else 0;
			RegConfig_Trans.IWE[20] == Reg_IWE_value if ((Reg_Lower_bit <= 20) && (20 <= Reg_Upper_bit)) else 0;
			RegConfig_Trans.IWE[19] == Reg_IWE_value if ((Reg_Lower_bit <= 19) && (19 <= Reg_Upper_bit)) else 0;
      RegConfig_Trans.IWE[18] == Reg_IWE_value if ((Reg_Lower_bit <= 18) && (18 <= Reg_Upper_bit)) else 0;
      RegConfig_Trans.IWE[17] == Reg_IWE_value if ((Reg_Lower_bit <= 17) && (17 <= Reg_Upper_bit)) else 0;
			RegConfig_Trans.IWE[16] == Reg_IWE_value if ((Reg_Lower_bit <= 16) && (16 <= Reg_Upper_bit)) else 0;
			RegConfig_Trans.IWE[15] == Reg_IWE_value if ((Reg_Lower_bit <= 15) && (15 <= Reg_Upper_bit)) else 0;
			RegConfig_Trans.IWE[14] == Reg_IWE_value if ((Reg_Lower_bit <= 14) && (14 <= Reg_Upper_bit)) else 0;
      RegConfig_Trans.IWE[13] == Reg_IWE_value if ((Reg_Lower_bit <= 13) && (13 <= Reg_Upper_bit)) else 0;
      RegConfig_Trans.IWE[12] == Reg_IWE_value if ((Reg_Lower_bit <= 12) && (12 <= Reg_Upper_bit)) else 0;
			RegConfig_Trans.IWE[11] == Reg_IWE_value if ((Reg_Lower_bit <= 11) && (11 <= Reg_Upper_bit)) else 0;
			RegConfig_Trans.IWE[10] == Reg_IWE_value if ((Reg_Lower_bit <= 10) && (10 <= Reg_Upper_bit)) else 0;
			RegConfig_Trans.IWE[9]  == Reg_IWE_value if ((Reg_Lower_bit <= 9)  && (9 <= Reg_Upper_bit)) else 0;
      RegConfig_Trans.IWE[8]  == Reg_IWE_value if ((Reg_Lower_bit <= 8)  && (8 <= Reg_Upper_bit)) else 0;
      RegConfig_Trans.IWE[7]  == Reg_IWE_value if ((Reg_Lower_bit <= 7)  && (7 <= Reg_Upper_bit)) else 0;
			RegConfig_Trans.IWE[6]  == Reg_IWE_value if ((Reg_Lower_bit <= 6)  && (6 <= Reg_Upper_bit)) else 0;
			RegConfig_Trans.IWE[5]  == Reg_IWE_value if ((Reg_Lower_bit <= 5)  && (5 <= Reg_Upper_bit)) else 0;
			RegConfig_Trans.IWE[4]  == Reg_IWE_value if ((Reg_Lower_bit <= 4)  && (4 <= Reg_Upper_bit)) else 0;
      RegConfig_Trans.IWE[3]  == Reg_IWE_value if ((Reg_Lower_bit <= 3)  && (3 <= Reg_Upper_bit)) else 0;
      RegConfig_Trans.IWE[2]  == Reg_IWE_value if ((Reg_Lower_bit <= 2)  && (2 <= Reg_Upper_bit)) else 0;
			RegConfig_Trans.IWE[1]  == Reg_IWE_value if ((Reg_Lower_bit <= 1)  && (1 <= Reg_Upper_bit)) else 0;
			RegConfig_Trans.IWE[0]  == Reg_IWE_value if ((Reg_Lower_bit <= 0)  && (0 <= Reg_Upper_bit)) else 0;
		});
		finish_item(RegConfig_Trans);
	endtask
endclass
