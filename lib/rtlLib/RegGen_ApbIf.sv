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
$GenUserHeader
module $GenModuleName
  #(
    //Parameters are the fixed values and are created by tool. 
    //For this reason, they are localparams and NOT changed.
    //If you want to change the parameters, the RTL code shall be generated again.
    localparam int REGGEN_WPROT_MODE = $GenWProtParam,
    localparam int REGGEN_WPROT_ERR  = $GenWProtErrParam,
    localparam int REGGEN_SEC_MODE   = $GenSecParam,
    localparam int REGGEN_SEC_ERR    = $GenSecErrParam,
    localparam int REGGEN_ASYNC_MODE = $GenAsyncParam,
    localparam int REGGEN_SYNC_STAGE = $GenSyncStageParam,
    localparam int REGGEN_ADDR_WIDTH = $GenAddrParam,
    localparam int REGGEN_DATA_WIDTH = $GenDataParam,
    localparam int REGGEN_STRB_WIDTH = REGGEN_DATA_WIDTH/8
  )
  (
    //User interface is synchronized to reg_clk
    $GenWProtParam input  logic write_protect_en,
    $GenStartLoop$GenRegName
      $POW$POW0$POW1 output logic $GenRegName_write_en,
      $POR output logic $GenRegName_read_en,
      $POW$POW0$POW1 output logic [REGGEN_STRB_WIDTH-1:0] $GenRegName_byte_we,
      $RWI$RO$ROC$ROS input  logic [REGGEN_STRB_WIDTH-1:0] $GenRegName_ivalue,
    $GenEndLoop
    $GenStartLoop$GenRegName$GenRegField
      $RWI$RO$ROC$ROS input  logic $GenRegName_$GenRegField_iwe,
      $RW$RWI$RW_RC$RW_RS$RW_WC$RW_WS$RW_W1C$RW_W0S$RW_W1S$RW_W0S$WO$WOC$WOS$WO0$WO1 output logic [REGGEN_DATA_WIDTH-1:0] $GenRegName_$GenRegField_reg,
    $GenEndLoop
    $GenStartLoop$GenRegName$GenRegField$GenPartialBitRange
      $POW1 output logic $GenRegName_$GenRegField_$GenPStrbIndex_w1,
      $POW0 output logic $GenRegName_$GenRegField_$GenPStrbIndex_w0,
    $GenEndLoop
    //Clock and reset
    input  logic reg_clk,   //User clock
    input  logic reg_rst_n, //User reset is synchronized to reg_clk
    input  logic pclk,      //APB clock
    input  logic preset_n,   //APB reset is synchronized to pclk
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
    output logic [REGGEN_DATA_WIDTH-1:0] prdata
  );
  logic setup_phase;
  //pclk
  assign setup_phase = psel & ~penable;
  //Synchronizer
  generate
    if (REGGEN_ASYNC_MODE == 1) begin: AsyncMode
      //Access request
      assign req_inv = setup_phase;
      $GenAsyncReset always_ff @ (posedge pclk, negedge preset_n) begin
      $GenSyncReset always_ff @ (posedge pclk) begin
        if (!preset_n)
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
      assign req_en = req_sync[REGGEN_SYNC_STAGE-1] ^ ack_in;
      //Access acknowledge
      $GenAsyncReset always_ff @ (posedge reg_clk, negedge reg_rst_n) begin
      $GenSyncReset always_ff @ (posedge reg_clk) begin
        if (!reg_clk)
          ack_in <= '0;
        else if (req_inv)
          ack_in <= ~ack_in;
      end
      $GenAsyncReset always_ff @ (posedge pclk, negedge preset_n) begin
      $GenSyncReset always_ff @ (posedge pclk) begin
        if (!preset_n)
          ack_sync <= '0;
        else
          ack_sync <= {ack_sync[REGGEN_SYNC_STAGE-1:1], ack_in};
      end
      assign ack_en = ack_sync[REGGEN_SYNC_STAGE-1] ~^ req_in;
      assign clr_pready = req_inv;
      $GenAsyncReset always_ff @ (posedge pclk, negedge preset_n) begin
      $GenSyncReset always_ff @ (posedge pclk) begin
        if (!preset_n)
          pready <= '0;
        else if (clr_pready)
          pready <= '0;
        else
          pready <= ack_en;
      end
      //
      if (REGGEN_WPROT_MODE == 1) begin: AsyncWProt
        $GenAsyncReset always_ff @ (posedge reg_clk, negedge reg_rst_n) begin
        $GenSyncReset always_ff @ (posedge reg_clk) begin
          if (!reg_rst_n)
            wprot_sync <= '0;
          else
            wprot_sync <= {wprot_sync[REGGEN_SYNC_STAGE-1:1], write_protect_en};
        end
        assign wprot_en_sync = wprot_sync[REGGEN_SYNC_STAGE-1];
      end
      else begin: AsyncNoWProt
        assign wprot_en_sync = 1'b0;
      end
    end
    else begin: SyncMode
      assign req_en = setup_phase;
      assign pready = 1'b1;
      if (REGGEN_WPROT_MODE == 1) begin: SyncWProt
        assign wprot_en_sync = write_protect_en;
      end
      else begin: SyncNoWProt
        assign wprot_en_sync = 1'b0;
      end
    end
  endgenerate
  //
  assign pwrite_en = req_en & pwrite;
  assign pread_en  = req_en & ~pwrite;
  $GenStartLoop$GenRegName
    assign $GenRegName_sel = (paddr == REGGEN_OFFSET_ADDR_$GenRegName);
    assign $GenRegName_write_en = $GenRegName_sel & pwrite_en 
                                  & (REGGEN_WPROT_MODE? ~wprot_en_sync: 1'b1)
                                  & (REGGEN_SEC_MODE?   ~pprot[1]: 1'b1);
    assign $GenRegName_read_en  = $GenRegName_sel & pread_en 
                                  & (REGGEN_SEC_MODE?   ~pprot[1]: 1'b1);
  $GenEndLoop
  //
  $GenStartLoop$GenRegName
    $RW$RWI$RW_RC$RW_RS$WO assign $GenRegName_byte_we[$GenPStrbIndex] = pstrb[$GenPStrbIndex] & $GenRegName_write_en;
  $GenEndLoop
  //Use the bit range, GenPartialBitRange, to select the strobe index, GenPStrbIndex
  //---------------------------------------
  $GenStartLoop$GenRegName$GenRegField$GenPartialBitRange
    //Reg  : $GenRegName
    //Field: $GenRegField
    //Bit  : $GenPartialBitRange
    //APB Write
    $RW$RWI$RW_RC$RW_RS$WO assign $GenRegName_next[$GenPartialBitRange] = $GenRegName_byte_we[$GenPStrbIndex]? pwdata[$GenPartialBitRange]: $GenRegName_sc_value[$GenPartialBitRange];
    //Write to set
    $RW_WS$RW_W1S$RW_W0S$WO1$ROS assign $GenRegName_sc_value[$GenPartialBitRange] = $GenRegName_$GenRegField_$GenPStrbIndex_set? '1: $GenRegName_ivalue[$GenPartialBitRange];
    $RW_WS assign $GenRegName_$GenRegField_$GenPStrbIndex_set = $GenRegName_byte_we[$GenPStrbIndex];
    $RW_W1S$WO1 assign $GenRegName_$GenRegField_$GenPStrbIndex_w1 = $GenRegName_byte_we[$GenPStrbIndex] & (&pwdata[$GenPartialBitRange]);
    $RW_W1S$WO1 assign $GenRegName_$GenRegField_$GenPStrbIndex_set = $GenRegName_$GenRegField_$GenPStrbIndex_w1;
    $RW_W0S assign $GenRegName_$GenRegField_$GenPStrbIndex_set = $GenRegName_byte_we[$GenPStrbIndex] & (~|pwdata[$GenPartialBitRange]);
    $ROS assign $GenRegName_$GenRegField_$GenPStrbIndex_set = $GenRegName_read_en;
    //Write to clear
    $RW_WC$RW_W1C$RW_W0C$WO0$ROC assign $GenRegName_sc_value[$GenPartialBitRange] = $GenRegName_$GenRegField_$GenPStrbIndex_clr? '0: $GenRegName_ivalue[$GenPartialBitRange];
    $RW_WC assign $GenRegName_$GenRegField_$GenPStrbIndex_clr = $GenRegName_byte_we[$GenPStrbIndex];
    $RW_W1C assign $GenRegName_$GenRegField_$GenPStrbIndex_clr = $GenRegName_byte_we[$GenPStrbIndex] & (&pwdata[$GenPartialBitRange]);
    $RW_W0C$WO0 assign $GenRegName_$GenRegField_$GenPStrbIndex_w0 = $GenRegName_byte_we[$GenPStrbIndex] & (~|pwdata[$GenPartialBitRange]);
    $RW_W0C$WO0 $GenRegName_$GenRegField_$GenPStrbIndex_clr = $GenRegName_$GenRegField_$GenPStrbIndex_w0;
    $ROC assign $GenRegName_$GenRegField_$GenPStrbIndex_clr = $GenRegName_read_en;
    //
    $GenNOT$RW_WS$RW_W1S$RW_W0S$WO1$ROS$RW_WC$RW_W1C$RW_W0C$WO0$ROC assign $GenRegName_sc_value[$GenPartialBitRange] = $GenRegName_ivalue[$GenPartialBitRange];
    //Write from internal operation
    $RWI$RO$ROC$ROS assign $GenRegName_ivalue[$GenPartialBitRange] = $GenRegName_$GenRegField_iwe? $GenRegName_ivalue[$GenPartialBitRange]: $GenRegName_reg[$GenPartialBitRange];
    $GenNOT$RWI$RO$ROC$ROS assign $GenRegName_ivalue[$GenPartialBitRange] = $GenRegName_reg[$GenPartialBitRange];
  $GenEndLoop
  //
  $GenStartLoop$GenRegName$GenRegField$GenPartialBitRange
    assign $GenRegName_next[$GenPartialBitRange] = $GenRegName_next[$GenPartialBitRange];
    $GenAsyncReset always_ff @ (posedge reg_clk, negedge reg_rst_n) begin
    $GenSyncReset always_ff @ (posedge reg_clk) begin
      if (!reg_rst_n)
        $GenRegName_reg[$GenPartialBitRange] <= $GenFieldReset;
      else if ($GenRegName_byte_we[$GenPStrbIndex])
        $GenRegName_reg[$GenPartialBitRange] <= $GenRegName_next[$GenPartialBitRange];
    end
  $GenEndLoop
  //Read data
  $GenStartLoop$GenRegName$GenRegField$GenPartialBitRange
    $GenNOT$WO$WO1$WO0$WOC$WOS assign $GenRegName_$GenRegField_rvalue[$GenPartialBitRange] = $GenRegName_read_en? $GenRegName_reg[$GenPartialBitRange]: '0;
    $RESERVED$WO$WO1$WO0$WOC$WOS assign $GenRegName_$GenRegField_rvalue[$GenPartialBitRange] = '0;
  $GenEndLoop
  //
  $GenStartLoop$GenRegName
    assign $GenRegName_rvalue = {REGGEN_DATA_WIDTH{$GenRegName_read_en}} & $GenRegName_reg;
  $GenEndLoop
  assign prdata_next = $GenRDataOR;
  //
  always_ff @ (posedge reg_clk) begin
    if (pread_en)
      prdata <= prdata_next;
  end
  //
  assign prot_error = (REGGEN_WPROT_MODE & REGGEN_WPROT_ERR)? (pwrite_en & wprot_en_sync): '0;
  assign sec_error  = (REGGEN_SEC_MODE & REGGEN_SEC_ERR)? pprot[1]: '0;
  assign pslverr_nxt = prot_error | sec_error;
  $GenAsyncReset always_ff @ (posedge reg_clk, negedge reg_rst_n) begin
  $GenSyncReset always_ff @ (posedge reg_clk) begin
    if (!reg_rst_n)
      pslverr <= '0;
    else if (req_en)
      pslverr <= pslverr_nxt;
  end
  //
endmodule: $GenModuleName
