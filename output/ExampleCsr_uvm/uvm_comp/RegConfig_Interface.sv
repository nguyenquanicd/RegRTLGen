//--------------------------------------
//Project: The UVM environemnt for RegisterRTL
//Function: Register Config Interface
//Author:  Nguyen Hung Quan, Le Hoang Van, Le Tan Thinh
//Page:    VLSI Technology
//--------------------------------------

interface RegConfig_Interface;
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
endinterface: RegConfig_Interface
