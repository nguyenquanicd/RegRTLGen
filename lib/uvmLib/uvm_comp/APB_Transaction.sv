//--------------------------------------
//Project: The UVM environemnt for RegisterRTL
//Function: APB Transaction
// - Create the APB transaction
//Author:  Nguyen Hung Quan, Le Hoang Van, Tran Huu Duy
//Page:    VLSI Technology
//--------------------------------------

class cApbTransaction extends uvm_sequence_item;
  //Parameters are used to control the procedure
  parameter APB_TRANSACTION_TIMEOUT = 32'd100;
  //Declare the data members controled by sequence
  rand logic pwrite;  //Determine the transfer type: (0) READ or (1) WRITE
  rand logic [31:0] paddr;
  rand logic [31:0] pwdata;
  rand logic [3:0]  pstrb;
  rand logic [2:0]  pprot;
  logic [31:0] prdata;
  logic        pslverr;
  rand logic wprot_en;
  //Internal parameter to set the expected delay
  rand logic apbSeqEn;
  rand logic apbConEn;
  rand int   apbDelay;
  int pready = 1;
  //Limit the delay value from 0 to 15 time unit
  constraint delay_time {apbDelay inside {[0:15]};};
  //Register this class with the factory
  `uvm_object_utils_begin (cApbTransaction)
    `uvm_field_int(pwrite, UVM_ALL_ON)
    `uvm_field_int(paddr, UVM_ALL_ON)
    `uvm_field_int(pwdata, UVM_ALL_ON)
    `uvm_field_int(pstrb, UVM_ALL_ON)
    `uvm_field_int(pprot, UVM_ALL_ON)
    `uvm_field_int(prdata, UVM_ALL_ON)
    `uvm_field_int(pslverr, UVM_ALL_ON)
    `uvm_field_int(wprot_en, UVM_ALL_ON)
    `uvm_field_int(apbSeqEn, UVM_ALL_ON)
    `uvm_field_int(apbConEn, UVM_ALL_ON)
    `uvm_field_int(apbDelay, UVM_ALL_ON)
    `uvm_field_int(pready, UVM_ALL_ON)
  `uvm_object_utils_end
  //Constructor
  function new (string name = "cApbTransaction");
    super.new(name);
  endfunction: new
  //Show the value of all variable
  virtual task print_apb_seq();
     //get_full_name returns the full hierarchical name of the driver object
    `uvm_info("APB_SEQ", $sformatf("pwrite = %0h, paddr = %0h, pwdata = %0h, pstrb = %0h, pprot = %0h, prdata = %0h, apbDelay = %0d", pwrite, paddr, pwdata, pstrb, pprot, prdata, apbDelay), UVM_LOW);
  endtask: print_apb_seq
endclass: cApbTransaction
