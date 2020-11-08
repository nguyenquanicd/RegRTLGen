//--------------------------------------
//Project: The UVM environemnt for RegisterRTL
//Function: Register Config Transaction
//Author:  Le Hoang Van
//Page:    VLSI Technology
//--------------------------------------

class RegConfig_Driver extends uvm_driver #(RegConfig_Transaction);

  virtual RegConfig_Interface RegConfig_InterfaceMaster;
  RegConfig_Transaction ConfigPacket;

  `uvm_component_utils(RegConfig_Driver)

  function new (string name, uvm_component parent);
    super.new(name, parent);
  endfunction: new

  function void build_phase(uvm_phase phase);
    super.build_phase(phase);
    if (!uvm_config_db#(virtual interface RegConfig_Interface)::get(.cntxt(this),
        .inst_name(""),
        .field_name("V_RegConfig_InterfaceMaster"),
        .value(RegConfig_InterfaceMaster))) begin
      `uvm_fatal("NON-RegConfigIF", {"A virtual interface must be set for: ", get_full_name(), ".RegConfig_InterfaceMaster"})
    end
    `uvm_info(get_full_name(), "Build phase completed.", UVM_LOW)
  endfunction

  virtual task run_phase (uvm_phase phase);
    fork
      get_seq_and_drive ();
    join
  endtask


  virtual task get_seq_and_drive();
    forever begin
      seq_item_port.get_next_item(ConfigPacket);
      convert_seq2config(ConfigPacket);
      seq_item_port.item_done();
    end
  endtask: get_seq_and_drive

  virtual task convert_seq2config (RegConfig_Transaction userRegConfig_Transaction);
    uart_vifApbMaster.psel         = 1'b1;
    uart_vifApbMaster.pwrite       = userRegConfig_Transaction.pwrite;
    uart_vifApbMaster.paddr[31:0]  = userRegConfig_Transaction.paddr[31:0];
    uart_vifApbMaster.pwdata[31:0] = userRegConfig_Transaction.pwdata[31:0];
    uart_vifApbMaster.pstrb[3:0]   = userRegConfig_Transaction.pstrb[3:0];
    uart_vifApbMaster.penable = 1'b1;
    uart_vifApbMaster.psel    = 1'b0;
    uart_vifApbMaster.penable = 1'b0;
  endtask: convert_seq2config

endclass
