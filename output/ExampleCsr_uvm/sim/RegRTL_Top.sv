//--------------------------------------
//Project: The UVM environemnt for RegisterRTL
//Function: APB Monitor
//Author:  Nguyen Hung Quan, Le Hoang Van, Tran Huu Duy
//Page:    VLSI Technology
//--------------------------------------

`define CLOCK_CYCLE 50
//Include the UVM library
`include "uvm_pkg.sv"
`include "uvm_macros.svh"
`include "RegRTL_Macro.svh"
//
//Most TOP module
//
module RegRTL_Top;
  //Import UVM package
  import uvm_pkg::*;
  //Include all used classes
  `include "APB_Interface.sv"
  `include "APB_Transaction.sv"
  `include "APB_Sequencer.sv"
  `include "APB_Sequence.sv"
  `include "APB_Driver.sv"
  `include "APB_Monitor.sv"
  `include "APB_Agent.sv"
  
  `include "RegConfig_Interface.sv"
  `include "RegConfig_Transaction.sv"
  `include "RegConfig_Sequencer.sv"
  `include "RegConfig_Sequence.sv"
  `include "RegConfig_Driver.sv"
  `include "RegConfig_Monitor.sv"
  `include "RegConfig_Agent.sv"

  `include "RegRTL_Scoreboard.sv"
  `include "RegRTL_Sequencer.sv"
  `include "RegRTL_Sequence.sv"
  `include "RegRTL_Env.sv"
  `include "RegRTL_Test.sv"
  
  //Interface declaration
  ifApbMaster vifApbMaster_Top();
  RegConfig_Interface vRegConfig_Interface_Top();

  //Clock generator
  //Create 2 asynchronous clock to test
  reg apb_clk = 1'b0;
  always #(`CLOCK_CYCLE/2) apb_clk = ~apb_clk;
  assign vifApbMaster_Top.pclk = apb_clk;

  //Reset generator
  //Only reset one time when starting the simulation
  reg reset_n;
  initial begin
    reset_n = 1'b0;
    #(`CLOCK_CYCLE)
    reset_n = 1'b1;
  end
  assign vifApbMaster_Top.preset_n = reset_n;

  //TOP DUT instance
  ExampleCsr ExampleCsr( 
     //RegConfig Interface
    .ACTRL_reg(vRegConfig_Interface_Top.ACTRL_reg), 
    .ACTRL_byte_we(vRegConfig_Interface_Top.ACTRL_byte_we), 
    .ACTRL_ivalue(vRegConfig_Interface_Top.ACTRL_ivalue), 
    .ACTRL_RESERVED_iwe(vRegConfig_Interface_Top.ACTRL_RESERVED_iwe), 
    .ACTRL_BAUND1_3_w1(vRegConfig_Interface_Top.ACTRL_BAUND1_3_w1), 
    .ACTRL_BAUND1_2_w1(vRegConfig_Interface_Top.ACTRL_BAUND1_2_w1), 
    .ACTRL_BAUND0_1_w0(vRegConfig_Interface_Top.ACTRL_BAUND0_1_w0), 
    .ACTRL_RWI_iwe(vRegConfig_Interface_Top.ACTRL_RWI_iwe), 
    .BCTRL_reg(vRegConfig_Interface_Top.BCTRL_reg), 
    .BCTRL_read_en(vRegConfig_Interface_Top.BCTRL_read_en), 
    .BCTRL_byte_we(vRegConfig_Interface_Top.BCTRL_byte_we), 
    .BCTRL_ivalue(vRegConfig_Interface_Top.BCTRL_ivalue), 
    .BCTRL_RESERVED_iwe(vRegConfig_Interface_Top.BCTRL_RESERVED_iwe), 
    .BCTRL_ROS_iwe(vRegConfig_Interface_Top.BCTRL_ROS_iwe), 
    .BCTRL_ROC_iwe(vRegConfig_Interface_Top.BCTRL_ROC_iwe), 
    .BCTRL_RO_iwe(vRegConfig_Interface_Top.BCTRL_RO_iwe), 
     //APB Interface
    .pclk(vifApbMaster_Top.pclk),
    .preset_n(vifApbMaster_Top.preset_n),
    .pwrite(vifApbMaster_Top.pwrite),
    .psel(vifApbMaster_Top.psel), 
    .penable(vifApbMaster_Top.penable),
    .paddr(vifApbMaster_Top.paddr),
    .pwdata(vifApbMaster_Top.pwdata),
    .pstrb(vifApbMaster_Top.pstrb), 
    .prdata(vifApbMaster_Top.prdata),
    .pready(vifApbMaster_Top.pready),
    .pslverr(vifApbMaster_Top.pslverr),
    .pprot(vifApbMaster_Top.pprot),
    .write_protect_en(vifApbMaster_Top.wprot_en)
  );
  //Interface connection
  //Connect TOP DUT to UVM components
  initial begin
    //Connect APB interface
    uvm_config_db#(virtual interface ifApbMaster)::set(null,"uvm_test_top.co_RegRTL_Env.coApbMasterAgent*","vifApbMaster",vifApbMaster_Top);
    //Connect RegConfig interface
    uvm_config_db#(virtual interface RegConfig_Interface)::set(null,"uvm_test_top.co_RegRTL_Env.co_RegConfig_Agent*","vif_RegConfig_IF",vRegConfig_Interface_Top);
  end
  //Run the test pattern
  initial begin
    //This method will get the test name from UVM_TESTNAME
    //which is assigned in the RUN command
    run_test();
  end
  
endmodule
