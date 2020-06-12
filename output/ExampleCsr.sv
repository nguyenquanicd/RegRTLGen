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

//Version: 1.0
//Description: Register specification of VG
//
//
module ExampleCsr
  #(
    //Parameters are the fixed values and are created by tool. 
    //For this reason, they are localparams and NOT changed.
    //If you want to change the parameters, the RTL code shall be generated again.
    localparam int REGGEN_WPROT_MODE = 1,
    localparam int REGGEN_WPROT_ERR  = 1,
    localparam int REGGEN_SEC_MODE   = 1,
    localparam int REGGEN_SEC_ERR    = 1,
    localparam int REGGEN_ASYNC_MODE = 1,
    localparam int REGGEN_SYNC_STAGE = 2,
    localparam int REGGEN_ADDR_WIDTH = 16,
    localparam int REGGEN_DATA_WIDTH = 32,
    localparam int REGGEN_STRB_WIDTH = REGGEN_DATA_WIDTH/8
  )
  (
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
    output logic [REGGEN_DATA_WIDTH-1:0] prdata,
    //User interface is synchronized to reg_clk
     input  logic write_protect_en,
       output logic ACTRL_write_en,
       output logic [REGGEN_STRB_WIDTH-1:0] ACTRL_byte_we,
       input  logic [$GenFullBitRange] ACTRL_RESERVED_ivalue,
       input  logic ACTRL_RESERVED_iwe,
       output logic [REGGEN_DATA_WIDTH-1:0] ACTRL_BAUND_reg,
       input  logic [$GenFullBitRange] ACTRL_BUSY_ivalue,
       input  logic ACTRL_BUSY_iwe,
       output logic [REGGEN_DATA_WIDTH-1:0] ACTRL_EN_reg,
       output logic ACTRL_BAUND_3_w1,
       output logic ACTRL_BAUND_2_w1,
  );
  //pclk
  assign setup_phase = psel & ~penable;
  //Synchronizer
  generate
    if (REGGEN_ASYNC_MODE == 1) begin: AsyncMode
      //Access request
      assign req_inv = setup_phase;
       always_ff @ (posedge pclk, negedge preset_n) begin
        if (!preset_n)
          req_in <= '0;
        else if (req_inv)
          reg_in <= ~req_in;
      end
       always_ff @ (posedge reg_clk, negedge reg_rst_n) begin
        if (!reg_rst_n)
          req_sync <= '0;
        else
          req_sync <= {req_sync[REGGEN_SYNC_STAGE-1:1], req_in};
      end
      assign req_en = req_sync[REGGEN_SYNC_STAGE-1] ^ ack_in;
      //Access acknowledge
       always_ff @ (posedge reg_clk, negedge reg_rst_n) begin
        if (!reg_clk)
          ack_in <= '0;
        else if (req_inv)
          ack_in <= ~ack_in;
      end
       always_ff @ (posedge pclk, negedge preset_n) begin
        if (!preset_n)
          ack_sync <= '0;
        else
          ack_sync <= {ack_sync[REGGEN_SYNC_STAGE-1:1], ack_in};
      end
      assign ack_en = ack_sync[REGGEN_SYNC_STAGE-1] ~^ req_in;
      assign clr_pready = req_inv;
       always_ff @ (posedge pclk, negedge preset_n) begin
        if (!preset_n)
          pready <= '0;
        else if (clr_pready)
          pready <= '0;
        else
          pready <= ack_en;
      end
      //
      if (REGGEN_WPROT_MODE == 1) begin: AsyncWProt
         always_ff @ (posedge reg_clk, negedge reg_rst_n) begin
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
  //
     assign ACTRL_byte_we[0] = pstrb[0] & ACTRL_write_en;
     assign ACTRL_byte_we[2] = pstrb[2] & ACTRL_write_en;
     assign ACTRL_byte_we[3] = pstrb[3] & ACTRL_write_en;
  //Use the bit range, GenPartialBitRange, to select the strobe index, GenPStrbIndex
  //---------------------------------------
    //Reg  : ACTRL
    //Field: RESERVED
    //Bit  : 31:28
    //APB Write
    //Write to set
    //Write to clear
    //
     assign ACTRL_sc_value[31:28] = ACTRL_RESERVED_ivalue[31:28];
    //Write from internal operation
     assign ACTRL_RESERVED_ivalue[31:28] = ACTRL_RESERVED_iwe? ACTRL_RESERVED_ivalue[31:28]: ACTRL_reg[31:28];
    //Reg  : ACTRL
    //Field: RESERVED
    //Bit  : 14:8
    //APB Write
    //Write to set
    //Write to clear
    //
     assign ACTRL_sc_value[14:8] = ACTRL_RESERVED_ivalue[14:8];
    //Write from internal operation
     assign ACTRL_RESERVED_ivalue[14:8] = ACTRL_RESERVED_iwe? ACTRL_RESERVED_ivalue[14:8]: ACTRL_reg[14:8];
    //Reg  : ACTRL
    //Field: RESERVED
    //Bit  : 7:1
    //APB Write
    //Write to set
    //Write to clear
    //
     assign ACTRL_sc_value[7:1] = ACTRL_RESERVED_ivalue[7:1];
    //Write from internal operation
     assign ACTRL_RESERVED_ivalue[7:1] = ACTRL_RESERVED_iwe? ACTRL_RESERVED_ivalue[7:1]: ACTRL_reg[7:1];
    //Reg  : ACTRL
    //Field: BAUND
    //Bit  : 27:24
    //APB Write
     assign ACTRL_next[27:24] = ACTRL_byte_we[3]? pwdata[27:24]: ACTRL_sc_value[27:24];
    //Write to set
    //Write to clear
    //
     assign ACTRL_sc_value[27:24] = ACTRL_BAUND_ivalue[27:24];
    //Write from internal operation
     assign ACTRL_BAUND_ivalue[27:24] = ACTRL_reg[27:24];
    //Reg  : ACTRL
    //Field: BAUND
    //Bit  : 23:16
    //APB Write
     assign ACTRL_next[23:16] = ACTRL_byte_we[2]? pwdata[23:16]: ACTRL_sc_value[23:16];
    //Write to set
    //Write to clear
    //
     assign ACTRL_sc_value[23:16] = ACTRL_BAUND_ivalue[23:16];
    //Write from internal operation
     assign ACTRL_BAUND_ivalue[23:16] = ACTRL_reg[23:16];
    //Reg  : ACTRL
    //Field: BUSY
    //Bit  : 15
    //APB Write
    //Write to set
    //Write to clear
    //
     assign ACTRL_sc_value[15] = ACTRL_BUSY_ivalue[15];
    //Write from internal operation
     assign ACTRL_BUSY_ivalue[15] = ACTRL_BUSY_iwe? ACTRL_BUSY_ivalue[15]: ACTRL_reg[15];
    //Reg  : ACTRL
    //Field: EN
    //Bit  : 0
    //APB Write
     assign ACTRL_next[0] = ACTRL_byte_we[0]? pwdata[0]: ACTRL_sc_value[0];
    //Write to set
    //Write to clear
    //
     assign ACTRL_sc_value[0] = ACTRL_EN_ivalue[0];
    //Write from internal operation
     assign ACTRL_EN_ivalue[0] = ACTRL_reg[0];
  //
    assign ACTRL_next[31:28] = ACTRL_next[31:28];
      if (!reg_rst_n)
      else if (ACTRL_byte_we[3])
    end
    assign ACTRL_next[14:8] = ACTRL_next[14:8];
      if (!reg_rst_n)
      else if (ACTRL_byte_we[1])
    end
    assign ACTRL_next[7:1] = ACTRL_next[7:1];
      if (!reg_rst_n)
      else if (ACTRL_byte_we[0])
    end
    assign ACTRL_next[27:24] = ACTRL_next[27:24];
      if (!reg_rst_n)
      else if (ACTRL_byte_we[3])
    end
    assign ACTRL_next[23:16] = ACTRL_next[23:16];
      if (!reg_rst_n)
      else if (ACTRL_byte_we[2])
    end
    assign ACTRL_next[15] = ACTRL_next[15];
      if (!reg_rst_n)
      else if (ACTRL_byte_we[1])
    end
    assign ACTRL_next[0] = ACTRL_next[0];
      if (!reg_rst_n)
      else if (ACTRL_byte_we[0])
    end
  //Read data
  //
     assign ACTRL_RESERVED_rvalue[31:28] = ACTRL_read_en? ACTRL_reg[31:28]: '0;
  //
     assign ACTRL_RESERVED_rvalue[14:8] = ACTRL_read_en? ACTRL_reg[14:8]: '0;
  //
     assign ACTRL_RESERVED_rvalue[7:1] = ACTRL_read_en? ACTRL_reg[7:1]: '0;
  //
     assign ACTRL_BAUND_rvalue[27:24] = ACTRL_read_en? ACTRL_reg[27:24]: '0;
  //
     assign ACTRL_BAUND_rvalue[23:16] = ACTRL_read_en? ACTRL_reg[23:16]: '0;
  //
     assign ACTRL_BUSY_rvalue[15] = ACTRL_read_en? ACTRL_reg[15]: '0;
  //
     assign ACTRL_EN_rvalue[0] = ACTRL_read_en? ACTRL_reg[0]: '0;
  //Create a variable to store $GenRDataOR = OR($GenRegName_rvalue)
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
   always_ff @ (posedge reg_clk, negedge reg_rst_n) begin
    if (!reg_rst_n)
      pslverr <= '0;
    else if (req_en)
      pslverr <= pslverr_nxt;
  end
endmodule: ExampleCsr
