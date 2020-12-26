//--------------------------------------
//Project: The UVM environemnt for RegisterRTL
//Function: UVM Testbench
//Author:  Nguyen Hung Quan, Le Hoang Van, Tran Huu Duy
//Page:    VLSI Technology
//--------------------------------------

class RegRTL_Test extends uvm_test;
  RegRTL_Env co_RegRTL_Env;
  RegRTL_Sequence co_RegRTL_Sequence;
  
 `uvm_component_utils(RegRTL_Test)

  function new(string name = "RegRTL_Test", uvm_component parent = null);
    super.new(name,parent);
  endfunction: new

  function void build_phase(uvm_phase phase);
    super.build_phase(phase);
    co_RegRTL_Env = RegRTL_Env::type_id::create("co_RegRTL_Env",this);
    co_RegRTL_Sequence = RegRTL_Sequence::type_id::create("co_RegRTL_Sequence",this);
  endfunction: build_phase

  task run_phase(uvm_phase phase);
    super.run_phase(phase);
    phase.raise_objection(this);
    fork
      begin
        co_RegRTL_Sequence.start(co_RegRTL_Env.co_RegRTL_Sequencer);
      end
      
      begin
        #1ms;
        $display("#---------------------------------");
        `uvm_warning("RegRTL_Test WARNING", "TIMEOUT TIMEOUT TIMEOUT TIMEOUT TIMEOUT!!!")
        $display("#---------------------------------");
      end
    join_any
    disable fork;
    phase.drop_objection(this);
  endtask: run_phase
endclass: RegRTL_Test
