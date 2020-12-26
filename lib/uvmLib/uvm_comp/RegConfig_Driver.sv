//--------------------------------------
//Project: The UVM environemnt for RegisterRTL
//Function: Register Config Driver
//Author:  Nguyen Hung Quan, Le Hoang Van, Tran Huu Duy
//Page:    VLSI Technology
//--------------------------------------

class RegConfig_Driver extends uvm_driver#(RegConfig_Transaction);

  virtual RegConfig_Interface v_RegConfig_IF;
  RegConfig_Transaction Config_Packet;
  logic [31:0] Driver_IWE;
  
  `uvm_component_utils(RegConfig_Driver)
  
  function new(string name, uvm_component parent);
    super.new(name, parent);
  endfunction: new

  function void build_phase(uvm_phase phase);
    super.build_phase(phase);
    if (!uvm_config_db#(virtual interface RegConfig_Interface)::get(.cntxt(this),
        .inst_name(""),
        .field_name("vif_RegConfig_IF"),
        .value(v_RegConfig_IF))) begin
      `uvm_fatal("NON-RegConfigIF", {"A virtual interface must be set for: ", get_full_name(), ".v_RegConfig_IF"})
    end
    `uvm_info(get_full_name(), "Build phase completed.", UVM_LOW)
  endfunction: build_phase

  virtual task run_phase(uvm_phase phase);
    fork
      get_seq_and_drive();
    join
  endtask: run_phase

  virtual task get_seq_and_drive();
    forever begin
      seq_item_port.get_next_item(Config_Packet);
      convert_seq2config(Config_Packet);
      seq_item_port.item_done();
    end
  endtask: get_seq_and_drive

  virtual task convert_seq2config(RegConfig_Transaction Config_Trans);
    Driver_IWE[31] = Config_Trans.IWE_value if ((Config_Trans.Lower_bit <= 31) && (31 <= Config_Trans.Upper_bit)) else 0;
    Driver_IWE[30] = Config_Trans.IWE_value if ((Config_Trans.Lower_bit <= 30) && (30 <= Config_Trans.Upper_bit)) else 0;
    Driver_IWE[29] = Config_Trans.IWE_value if ((Config_Trans.Lower_bit <= 29) && (29 <= Config_Trans.Upper_bit)) else 0;
    Driver_IWE[28] = Config_Trans.IWE_value if ((Config_Trans.Lower_bit <= 28) && (28 <= Config_Trans.Upper_bit)) else 0;
    Driver_IWE[27] = Config_Trans.IWE_value if ((Config_Trans.Lower_bit <= 27) && (27 <= Config_Trans.Upper_bit)) else 0;
    Driver_IWE[26] = Config_Trans.IWE_value if ((Config_Trans.Lower_bit <= 26) && (26 <= Config_Trans.Upper_bit)) else 0;
    Driver_IWE[25] = Config_Trans.IWE_value if ((Config_Trans.Lower_bit <= 25) && (25 <= Config_Trans.Upper_bit)) else 0;
    Driver_IWE[24] = Config_Trans.IWE_value if ((Config_Trans.Lower_bit <= 24) && (24 <= Config_Trans.Upper_bit)) else 0;
    Driver_IWE[23] = Config_Trans.IWE_value if ((Config_Trans.Lower_bit <= 23) && (23 <= Config_Trans.Upper_bit)) else 0;
    Driver_IWE[22] = Config_Trans.IWE_value if ((Config_Trans.Lower_bit <= 22) && (22 <= Config_Trans.Upper_bit)) else 0;
    Driver_IWE[21] = Config_Trans.IWE_value if ((Config_Trans.Lower_bit <= 21) && (21 <= Config_Trans.Upper_bit)) else 0;
    Driver_IWE[20] = Config_Trans.IWE_value if ((Config_Trans.Lower_bit <= 20) && (20 <= Config_Trans.Upper_bit)) else 0;
    Driver_IWE[19] = Config_Trans.IWE_value if ((Config_Trans.Lower_bit <= 19) && (19 <= Config_Trans.Upper_bit)) else 0;
    Driver_IWE[18] = Config_Trans.IWE_value if ((Config_Trans.Lower_bit <= 18) && (18 <= Config_Trans.Upper_bit)) else 0;
    Driver_IWE[17] = Config_Trans.IWE_value if ((Config_Trans.Lower_bit <= 17) && (17 <= Config_Trans.Upper_bit)) else 0;
    Driver_IWE[16] = Config_Trans.IWE_value if ((Config_Trans.Lower_bit <= 16) && (16 <= Config_Trans.Upper_bit)) else 0;
    Driver_IWE[15] = Config_Trans.IWE_value if ((Config_Trans.Lower_bit <= 15) && (15 <= Config_Trans.Upper_bit)) else 0;
    Driver_IWE[14] = Config_Trans.IWE_value if ((Config_Trans.Lower_bit <= 14) && (14 <= Config_Trans.Upper_bit)) else 0;
    Driver_IWE[13] = Config_Trans.IWE_value if ((Config_Trans.Lower_bit <= 13) && (13 <= Config_Trans.Upper_bit)) else 0;
    Driver_IWE[12] = Config_Trans.IWE_value if ((Config_Trans.Lower_bit <= 12) && (12 <= Config_Trans.Upper_bit)) else 0;
    Driver_IWE[11] = Config_Trans.IWE_value if ((Config_Trans.Lower_bit <= 11) && (11 <= Config_Trans.Upper_bit)) else 0;
    Driver_IWE[10] = Config_Trans.IWE_value if ((Config_Trans.Lower_bit <= 10) && (10 <= Config_Trans.Upper_bit)) else 0;
    Driver_IWE[9]  = Config_Trans.IWE_value if ((Config_Trans.Lower_bit <= 9)  && (9  <= Config_Trans.Upper_bit)) else 0;
    Driver_IWE[8]  = Config_Trans.IWE_value if ((Config_Trans.Lower_bit <= 8)  && (8  <= Config_Trans.Upper_bit)) else 0;
    Driver_IWE[7]  = Config_Trans.IWE_value if ((Config_Trans.Lower_bit <= 7)  && (7  <= Config_Trans.Upper_bit)) else 0;
    Driver_IWE[6]  = Config_Trans.IWE_value if ((Config_Trans.Lower_bit <= 6)  && (6  <= Config_Trans.Upper_bit)) else 0;
    Driver_IWE[5]  = Config_Trans.IWE_value if ((Config_Trans.Lower_bit <= 5)  && (5  <= Config_Trans.Upper_bit)) else 0;
    Driver_IWE[4]  = Config_Trans.IWE_value if ((Config_Trans.Lower_bit <= 4)  && (4  <= Config_Trans.Upper_bit)) else 0;
    Driver_IWE[3]  = Config_Trans.IWE_value if ((Config_Trans.Lower_bit <= 3)  && (3  <= Config_Trans.Upper_bit)) else 0;
    Driver_IWE[2]  = Config_Trans.IWE_value if ((Config_Trans.Lower_bit <= 2)  && (2  <= Config_Trans.Upper_bit)) else 0;
    Driver_IWE[1]  = Config_Trans.IWE_value if ((Config_Trans.Lower_bit <= 1)  && (1  <= Config_Trans.Upper_bit)) else 0;
    Driver_IWE[0]  = Config_Trans.IWE_value if ((Config_Trans.Lower_bit <= 0)  && (0  <= Config_Trans.Upper_bit)) else 0;
    
    case (Config_Trans.Addr)
      // Content
    endcase
  endtask: convert_seq2config

endclass: RegConfig_Driver
