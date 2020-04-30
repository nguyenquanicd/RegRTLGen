//---------------------------------------------------------------
//Copyright © 2020 by VLSI Technology blog in Vietnam
//Website    : http://nguyenquanicd.blogspot.com/
//Author     :
//  RTL design - Nguyen Hung Quan (nguyenquan.icd@gmail.com)
//  Tool design- Le Hoang Van     (lehoangvan.for.business@gmail.com)
//Description: Register file with APB interface
//Language   : System Verilog
//Model type : Synthesizable
//---------------------------------------------------------------
//Version    : 1.0
//Date       : Apr.30.2020
//---------------------------------------------------------------
module $GenModuleName
  #(
    parameter  int REGGEN_SYNC_STAGE = $GenSyncStageParam,
    parameter  int REGGEN_ADDR_WIDTH = $GenAddrParam,
    parameter  int REGGEN_DATA_WIDTH = $GenDataParam,
    localparam int REGGEN_STRB_WIDTH = REGGEN_DATA_WIDTH/8
  )
  (
    //Clock and reset
    input  logic reg_clk,   //User clock
    input  logic reg_rst_n, //User reset is synchronized to reg_clk
    input  logic pclk,      //APB clock
    input  logic presetn,   //APB reset is synchronized to pclk
    //APB interface is synchronized to pclk
    input  logic psel,
    input  logic penable,
    input  logic pwrite,
    input  logic [REGGEN_STRB_WIDTH-1:0] pstrb,
    input  logic [REGGEN_ADDR_WIDTH-1:0] paddr,
    input  logic [REGGEN_DATA_WIDTH-1:0] pwdata,
    input  logic [2:0] pprot,
    output logic pready,
    output logic pslverr,
    output logic [REGGEN_DATA_WIDTH-1:0] prdata,
    //User interface is synchronized to reg_clk
    $GenWProt input  logic write_protect_en,
    $GenStartLoop
    $RWI$RO$ROC$ROS input  logic $GenRegName_$GenRegField_ivalue,
    $RWI$RO$ROC$ROS input  logic $GenRegName_$GenRegField_iwe,
    $POW  output logic [REGGEN_STRB_WIDTH-1:0] $GenRegName_byte_we,
    $POW1 output logic $GenRegName_$GenRegField_set,
    $POW0 output logic $GenRegName_$GenRegField_clr,
    $RW$RWI$RW_RC$RW_RS$RW_WC$RW_WS$RW_W1C$RW_W0S$RW_W1S$RW_W0S$WO$WOC$WOS$WO0$WO1 output logic [REGGEN_DATA_WIDTH-1:0] $GenRegName_$GenRegField_reg
    $GenEndLoop
  );
  //pclk
  assign setup_phase = psel & ~penable;
  //Synchronizer
  $GenStartBlock$GenAsync
    //Access request
    assign req_inv = setup_phase;
    $GenAsyncReset always_ff @ (posedge pclk, negedge presetn) begin
    $GenSyncReset always_ff @ (posedge pclk) begin
      if (!presetn)
        req_in <= '0;
      else if (req_inv)
        reg_in <= ~req_in;
    end
    $GenAsyncReset always_ff @ (posedge reg_clk, negedge reg_rst_n) begin
    $GenSyncReset always_ff @ (posedge reg_clk) begin
      if (!reg_rst_n)
        req_sync <= '0;
      else
        req_sync <= {req_sync[REGGEN_SYNC_STAGE-1:1], req_in};
    end
    assign req_en = req_sync[1]
    //Access acknowledge
    
  $GenEndBlock$GenAsync
  //
endmodule: $GenModuleName