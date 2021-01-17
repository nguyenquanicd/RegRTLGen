//--------------------------------------
//Project: The UVM environemnt for RegisterRTL
//Function: User UVM Sequence - This is the TEST PATTERN created by user
//  - User modifty this class to create the expected transactions for the test purpose
//Author:  Nguyen Hung Quan, Le Hoang Van, Tran Huu Duy
//Page:    VLSI Technology
//--------------------------------------

class RegRTL_Sequence extends uvm_sequence#(cApbTransaction);
  cApbMasterWriteSeq WriteSeq;
  cApbMasterReadSeq ReadSeq;
  RegConfig_Sequence RegConfigSeq;
  
  `uvm_object_utils(RegRTL_Sequence)
  `uvm_declare_p_sequencer(RegRTL_Sequencer)

  function new (string name = "RegRTL_Sequence");
    super.new(name);
  endfunction: new

  task body();
    #50ns
    `RegConfig(32'h00000008,32'hffffffff,31,0,1)
    #50ns
    `ApbWrite(32'h00000008,32'haaaaaaaa)
    `ApbRead(32'h00000008,32'haaaaaaaa,32'hffffffff)
  endtask: body
endclass: RegRTL_Sequence
