//--------------------------------------
//Project: The UVM environemnt for RegisterRTL
//Function: Register Config Monitor
//Author:  Nguyen Hung Quan, Le Hoang Van, Le Tan Thinh
//Page:    VLSI Technology
//--------------------------------------

`uvm_analysis_imp_decl(_frmMonitor_ACTRL) 
`uvm_analysis_imp_decl(_frmMonitor_BCTRL) 

class RegRTL_Scoreboard extends uvm_scoreboard;

  uvm_analysis_imp_frmMonitor_ACTRL #(ACTRL_monitor, RegRTL_Scoreboard) aimp_frmMonitor_ACTRL; 
  uvm_analysis_imp_frmMonitor_BCTRL #(BCTRL_monitor, RegRTL_Scoreboard) aimp_frmMonitor_BCTRL; 
  
  logic [31:0] ACTRL_reg; 
  logic [3:0] ACTRL_byte_we; 
  logic [31:0] ACTRL_ivalue; 
  logic ACTRL_RESERVED_iwe; 
  logic ACTRL_BAUND1_3_w1; 
  logic ACTRL_BAUND1_2_w1; 
  logic ACTRL_BAUND0_1_w0; 
  logic ACTRL_RWI_iwe; 
  logic [31:0] BCTRL_reg; 
  logic BCTRL_read_en; 
  logic [3:0] BCTRL_byte_we; 
  logic [31:0] BCTRL_ivalue; 
  logic BCTRL_RESERVED_iwe; 
  logic BCTRL_ROS_iwe; 
  logic BCTRL_ROC_iwe; 
  logic BCTRL_RO_iwe; 
  
  `uvm_component_utils(RegRTL_Scoreboard)

  function new(string name = "RegRTL_Scoreboard", uvm_component parent);
    super.new(name, parent);
  endfunction: new
  
  function void build_phase(uvm_phase phase);
    super.build_phase(phase);
    aimp_frmMonitor_ACTRL = new("aimp_frmMonitor_ACTRL", this); 
    aimp_frmMonitor_BCTRL = new("aimp_frmMonitor_BCTRL", this); 
 endfunction: build_phase
  

  function void write_frmMonitor_ACTRL (ACTRL_monitor ACTRL_Trans);
    ACTRL_reg = ACTRL_Trans.ACTRL_reg; 
    ACTRL_byte_we = ACTRL_Trans.ACTRL_byte_we; 
    ACTRL_ivalue = ACTRL_Trans.ACTRL_ivalue; 
    ACTRL_RESERVED_iwe = ACTRL_Trans.ACTRL_RESERVED_iwe; 
    ACTRL_BAUND1_3_w1 = ACTRL_Trans.ACTRL_BAUND1_3_w1; 
    ACTRL_BAUND1_2_w1 = ACTRL_Trans.ACTRL_BAUND1_2_w1; 
    ACTRL_BAUND0_1_w0 = ACTRL_Trans.ACTRL_BAUND0_1_w0; 
    ACTRL_RWI_iwe = ACTRL_Trans.ACTRL_RWI_iwe; 

  endfunction

  function void write_frmMonitor_BCTRL (BCTRL_monitor BCTRL_Trans);
    BCTRL_reg = BCTRL_Trans.BCTRL_reg; 
    BCTRL_read_en = BCTRL_Trans.BCTRL_read_en; 
    BCTRL_byte_we = BCTRL_Trans.BCTRL_byte_we; 
    BCTRL_ivalue = BCTRL_Trans.BCTRL_ivalue; 
    BCTRL_RESERVED_iwe = BCTRL_Trans.BCTRL_RESERVED_iwe; 
    BCTRL_ROS_iwe = BCTRL_Trans.BCTRL_ROS_iwe; 
    BCTRL_ROC_iwe = BCTRL_Trans.BCTRL_ROC_iwe; 
    BCTRL_RO_iwe = BCTRL_Trans.BCTRL_RO_iwe; 

  endfunction

 function void report_phase(uvm_phase phase);
    super.report_phase(phase);
 endfunction: report_phase
  
endclass: RegRTL_Scoreboard 
