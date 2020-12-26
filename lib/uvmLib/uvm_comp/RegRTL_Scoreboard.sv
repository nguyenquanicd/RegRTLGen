//--------------------------------------
//Project: The UVM environemnt for RegisterRTL
//Function: Register Config Scoreboard
//Author:  Nguyen Hung Quan, Le Hoang Van, Tran Huu Duy
//Page:    VLSI Technology
//--------------------------------------

`uvm_analysis_imp_decl(_transAPB)
`uvm_analysis_imp_decl(_resetAPB)
// Content declare

class RegRTL_Scoreboard extends uvm_scoreboard;
  uvm_analysis_imp_transAPB #(cApbTransaction, RegRTL_Scoreboard) aimp_transAPB;
  uvm_analysis_imp_resetAPB #(logic, RegRTL_Scoreboard) aimp_resetAPB;
  // Content create
  
  bit rst_flg;
  // Content internal variables
  
  `uvm_component_utils(RegRTL_Scoreboard)

  function new(string name = "RegRTL_Scoreboard", uvm_component parent);
    super.new(name, parent);
  endfunction: new
  
  function void build_phase(uvm_phase phase);
    super.build_phase(phase);
    aimp_transAPB = new("aimp_transAPB", this);
    aimp_resetAPB = new("aimp_resetAPB", this);
    // Content regist
 endfunction: build_phase
  
  function void write_resetAPB (logic preset_n);
   if (~preset_n) begin
    rst_flg = 1'b1;
    `uvm_info("RegRTL RESET", $sformatf("[%t] preset_n signal is acting", $time), UVM_LOW)
   end
   else begin
    rst_flg = 1'b0;
   end
  endfunction
  
  function void write_transAPB(cApbTransaction TransAPB);
    `uvm_info("RegRTL APB", $sformatf("[%t] APB transaction", $time), UVM_LOW)
  endfunction
  // Content function

 function void report_phase(uvm_phase phase);
    super.report_phase(phase);
 endfunction: report_phase
  
endclass: RegRTL_Scoreboard 
