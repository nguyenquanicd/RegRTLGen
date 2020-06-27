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
    localparam int REGGEN_SYNC_STAGE = 3,
    localparam int REGGEN_ADDR_WIDTH = 16,
    localparam int REGGEN_DATA_WIDTH = 32,
    localparam int REGGEN_STRB_WIDTH = REGGEN_DATA_WIDTH/8
  )
  (
    //User interface is synchronized to reg_clk
    input  logic write_protect_en,
    output logic ACTRL_write_en,
    output logic [REGGEN_STRB_WIDTH-1:0] ACTRL_byte_we,
    input  logic [REGGEN_STRB_WIDTH-1:0] ACTRL_ivalue,
    output logic BCTRL_write_en,
    output logic BCTRL_read_en,
    output logic [REGGEN_STRB_WIDTH-1:0] BCTRL_byte_we,
    input  logic [REGGEN_STRB_WIDTH-1:0] BCTRL_ivalue,
    output logic [REGGEN_DATA_WIDTH-1:0] ACTRL_BAUND1_reg,
    output logic [REGGEN_DATA_WIDTH-1:0] ACTRL_BAUND0_reg,
    output logic [REGGEN_DATA_WIDTH-1:0] ACTRL_RW_W0S_reg,
    output logic [REGGEN_DATA_WIDTH-1:0] ACTRL_RW_W1S_reg,
    output logic [REGGEN_DATA_WIDTH-1:0] ACTRL_RW_W1C_reg,
    output logic [REGGEN_DATA_WIDTH-1:0] ACTRL_RW_WS_reg,
    output logic [REGGEN_DATA_WIDTH-1:0] ACTRL_RW_WC_reg,
    output logic [REGGEN_DATA_WIDTH-1:0] ACTRL_RW_RS_reg,
    output logic [REGGEN_DATA_WIDTH-1:0] ACTRL_RW_RC_reg,
    input  logic ACTRL_RWI_iwe,
    output logic [REGGEN_DATA_WIDTH-1:0] ACTRL_RWI_reg,
    output logic [REGGEN_DATA_WIDTH-1:0] ACTRL_RW_reg,
    output logic [REGGEN_DATA_WIDTH-1:0] BCTRL_BAUND3_reg,
    output logic [REGGEN_DATA_WIDTH-1:0] BCTRL_BAUND2_reg,
    output logic [REGGEN_DATA_WIDTH-1:0] BCTRL_WO1_reg,
    output logic [REGGEN_DATA_WIDTH-1:0] BCTRL_WO0_reg,
    output logic [REGGEN_DATA_WIDTH-1:0] BCTRL_WOS_reg,
    output logic [REGGEN_DATA_WIDTH-1:0] BCTRL_WOC_reg,
    output logic [REGGEN_DATA_WIDTH-1:0] BCTRL_WO_reg,
    input  logic BCTRL_ROS_iwe,
    input  logic BCTRL_ROC_iwe,
    input  logic BCTRL_RO_iwe,
    output logic ACTRL_BAUND1_3_w1,
    output logic ACTRL_BAUND1_2_w1,
    output logic ACTRL_BAUND0_1_w0,
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
  //// Define Internal signals
  logic setup_phase;
  logic pwrite_en;
  logic pread_en;
  logic req_en;
  logic wprot_en_sync;
  logic [REGGEN_DATA_WIDTH-1:0] prdata_next;
  logic [REGGEN_DATA_WIDTH-1:0] prdata;
  logic prot_error;
  logic sec_error;
  logic pslverr_nxt;
  //Synchronizer
  generate
    if (REGGEN_ASYNC_MODE == 1) begin: AsyncMode
      logic req_inv;
      logic reg_in;
      logic req_sync;
      logic ack_in;
      logic ack_sync;
      logic ack_en;
      logic clr_pready;
      if (REGGEN_WPROT_MODE == 1) begin: AsyncWProt
          logic [REGGEN_SYNC_STAGE-1:0] wprot_sync;
      end
    end
  endgenerate
  logic ACTRL_sel;
  logic ACTRL_write_en;
  logic ACTRL_read_en;
  logic [REGGEN_STRB_WIDTH-1:0] ACTRL_byte_we;
  logic [REGGEN_DATA_WIDTH-1:0] ACTRL_next;
  logic [REGGEN_DATA_WIDTH-1:0] ACTRL_reg;
  logic [REGGEN_DATA_WIDTH-1:0] ACTRL_sc_value;
  logic [REGGEN_DATA_WIDTH-1:0] ACTRL_rvalue;
  logic BCTRL_sel;
  logic BCTRL_write_en;
  logic BCTRL_read_en;
  logic [REGGEN_STRB_WIDTH-1:0] BCTRL_byte_we;
  logic [REGGEN_DATA_WIDTH-1:0] BCTRL_next;
  logic [REGGEN_DATA_WIDTH-1:0] BCTRL_reg;
  logic [REGGEN_DATA_WIDTH-1:0] BCTRL_sc_value;
  logic [REGGEN_DATA_WIDTH-1:0] BCTRL_rvalue;
  //
  //
  //
  logic ACTRL_RW_W0S_1_set;
  //
  logic ACTRL_RW_W1S_1_w1;
  logic ACTRL_RW_W1S_1_set;
  //
  //
  logic ACTRL_RW_W0C_0_w0;
  logic ACTRL_RW_W0C_0_clr;
  //
  logic ACTRL_RW_W1C_0_clr;
  logic ACTRL_RW_WS_0_set;
  //
  //
  logic ACTRL_RW_WC_0_clr;
  //
  //
  //
  //
  //
  //
  //
  logic BCTRL_WO1_0_w1;
  logic BCTRL_WO1_0_set;
  //
  //
  logic BCTRL_WO0_0_w0;
  logic BCTRL_WO0_0_clr;
  //
  //
  //
  logic BCTRL_ROS_0_set;
  //
  //
  logic BCTRL_ROC_0_clr;
  //
  //
  logic [REGGEN_STRB_WIDTH-1:0] ACTRL_RESERVED_rvalue;
  logic [REGGEN_STRB_WIDTH-1:0] ACTRL_BAUND1_rvalue;
  logic [REGGEN_STRB_WIDTH-1:0] ACTRL_BAUND0_rvalue;
  logic [REGGEN_STRB_WIDTH-1:0] ACTRL_RW_W0S_rvalue;
  logic [REGGEN_STRB_WIDTH-1:0] ACTRL_RW_W1S_rvalue;
  logic [REGGEN_STRB_WIDTH-1:0] ACTRL_RW_W0C_rvalue;
  logic [REGGEN_STRB_WIDTH-1:0] ACTRL_RW_W1C_rvalue;
  logic [REGGEN_STRB_WIDTH-1:0] ACTRL_RW_WS_rvalue;
  logic [REGGEN_STRB_WIDTH-1:0] ACTRL_RW_WC_rvalue;
  logic [REGGEN_STRB_WIDTH-1:0] ACTRL_RW_RS_rvalue;
  logic [REGGEN_STRB_WIDTH-1:0] ACTRL_RW_RC_rvalue;
  logic [REGGEN_STRB_WIDTH-1:0] ACTRL_RWI_rvalue;
  logic [REGGEN_STRB_WIDTH-1:0] ACTRL_RW_rvalue;
  logic [REGGEN_STRB_WIDTH-1:0] BCTRL_RESERVED_rvalue;
  logic [REGGEN_STRB_WIDTH-1:0] BCTRL_BAUND3_rvalue;
  logic [REGGEN_STRB_WIDTH-1:0] BCTRL_BAUND2_rvalue;
  logic [REGGEN_STRB_WIDTH-1:0] BCTRL_WO1_rvalue;
  logic [REGGEN_STRB_WIDTH-1:0] BCTRL_WO0_rvalue;
  logic [REGGEN_STRB_WIDTH-1:0] BCTRL_WOS_rvalue;
  logic [REGGEN_STRB_WIDTH-1:0] BCTRL_WOC_rvalue;
  logic [REGGEN_STRB_WIDTH-1:0] BCTRL_WO_rvalue;
  logic [REGGEN_STRB_WIDTH-1:0] BCTRL_ROS_rvalue;
  logic [REGGEN_STRB_WIDTH-1:0] BCTRL_ROC_rvalue;
  logic [REGGEN_STRB_WIDTH-1:0] BCTRL_RO_rvalue;
  //// End-Define Internal signals
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
  assign ACTRL_sel = (paddr == REGGEN_OFFSET_ADDR_ACTRL);
  assign ACTRL_write_en = ACTRL_sel & pwrite_en 
                                & (REGGEN_WPROT_MODE? ~wprot_en_sync: 1'b1)
                                & (REGGEN_SEC_MODE?   ~pprot[1]: 1'b1);
  assign ACTRL_read_en  = ACTRL_sel & pread_en 
                                & (REGGEN_SEC_MODE?   ~pprot[1]: 1'b1);
  assign BCTRL_sel = (paddr == REGGEN_OFFSET_ADDR_BCTRL);
  assign BCTRL_write_en = BCTRL_sel & pwrite_en 
                                & (REGGEN_WPROT_MODE? ~wprot_en_sync: 1'b1)
                                & (REGGEN_SEC_MODE?   ~pprot[1]: 1'b1);
  assign BCTRL_read_en  = BCTRL_sel & pread_en 
                                & (REGGEN_SEC_MODE?   ~pprot[1]: 1'b1);
  //
  assign ACTRL_byte_we[0] = pstrb[0] & ACTRL_write_en;
  assign ACTRL_byte_we[1] = pstrb[1] & ACTRL_write_en;
  assign ACTRL_byte_we[2] = pstrb[2] & ACTRL_write_en;
  assign ACTRL_byte_we[3] = pstrb[3] & ACTRL_write_en;
  assign BCTRL_byte_we[0] = pstrb[0] & BCTRL_write_en;
  assign BCTRL_byte_we[1] = pstrb[1] & BCTRL_write_en;
  assign BCTRL_byte_we[2] = pstrb[2] & BCTRL_write_en;
  assign BCTRL_byte_we[3] = pstrb[3] & BCTRL_write_en;
  //Use the bit range, GenPartialBitRange, to select the strobe index, GenPStrbIndex
  //---------------------------------------
  //Reg  : ACTRL
  //Field: BAUND1
  //Bit  : 27:24
  //APB Write
  assign ACTRL_next[27:24] = ACTRL_byte_we[3]? pwdata[27:24]: ACTRL_sc_value[27:24];
  //Write to set
  //Write to clear
  //
  assign ACTRL_sc_value[27:24] = ACTRL_ivalue[27:24];
  //Write from internal operation
  assign ACTRL_ivalue[27:24] = ACTRL_reg[27:24];
  //Reg  : ACTRL
  //Field: BAUND1
  //Bit  : 23:16
  //APB Write
  assign ACTRL_next[23:16] = ACTRL_byte_we[2]? pwdata[23:16]: ACTRL_sc_value[23:16];
  //Write to set
  //Write to clear
  //
  assign ACTRL_sc_value[23:16] = ACTRL_ivalue[23:16];
  //Write from internal operation
  assign ACTRL_ivalue[23:16] = ACTRL_reg[23:16];
  //Reg  : ACTRL
  //Field: BAUND0
  //Bit  : 15:10
  //APB Write
  assign ACTRL_next[15:10] = ACTRL_byte_we[1]? pwdata[15:10]: ACTRL_sc_value[15:10];
  //Write to set
  //Write to clear
  //
  assign ACTRL_sc_value[15:10] = ACTRL_ivalue[15:10];
  //Write from internal operation
  assign ACTRL_ivalue[15:10] = ACTRL_reg[15:10];
  //Reg  : ACTRL
  //Field: RW_W0S
  //Bit  : 9
  //APB Write
  assign ACTRL_next[9] = ACTRL_byte_we[1]? pwdata[9]: ACTRL_sc_value[9];
  //Write to set
  assign ACTRL_sc_value[9] = ACTRL_RW_W0S_1_set? '1: ACTRL_ivalue[9];
  assign ACTRL_RW_W0S_1_set = ACTRL_byte_we[1] & (~|pwdata[9]);
  //Write to clear
  //
  //Write from internal operation
  assign ACTRL_ivalue[9] = ACTRL_reg[9];
  //Reg  : ACTRL
  //Field: RW_W1S
  //Bit  : 8
  //APB Write
  assign ACTRL_next[8] = ACTRL_byte_we[1]? pwdata[8]: ACTRL_sc_value[8];
  //Write to set
  assign ACTRL_sc_value[8] = ACTRL_RW_W1S_1_set? '1: ACTRL_ivalue[8];
  assign ACTRL_RW_W1S_1_w1 = ACTRL_byte_we[1] & (&pwdata[8]);
  assign ACTRL_RW_W1S_1_set = ACTRL_RW_W1S_1_w1;
  //Write to clear
  //
  //Write from internal operation
  assign ACTRL_ivalue[8] = ACTRL_reg[8];
  //Reg  : ACTRL
  //Field: RW_W0C
  //Bit  : 7
  //APB Write
  assign ACTRL_next[7] = ACTRL_byte_we[0]? pwdata[7]: ACTRL_sc_value[7];
  //Write to set
  //Write to clear
  assign ACTRL_sc_value[7] = ACTRL_RW_W0C_0_clr? '0: ACTRL_ivalue[7];
  assign ACTRL_RW_W0C_0_w0 = ACTRL_byte_we[0] & (~|pwdata[7]);
  assign ACTRL_RW_W0C_0_clr = ACTRL_RW_W0C_0_w0;
  //
  //Write from internal operation
  assign ACTRL_ivalue[7] = ACTRL_reg[7];
  //Reg  : ACTRL
  //Field: RW_W1C
  //Bit  : 6
  //APB Write
  assign ACTRL_next[6] = ACTRL_byte_we[0]? pwdata[6]: ACTRL_sc_value[6];
  //Write to set
  //Write to clear
  assign ACTRL_sc_value[6] = ACTRL_RW_W1C_0_clr? '0: ACTRL_ivalue[6];
  assign ACTRL_RW_W1C_0_clr = ACTRL_byte_we[0] & (&pwdata[6]);
  //
  //Write from internal operation
  assign ACTRL_ivalue[6] = ACTRL_reg[6];
  //Reg  : ACTRL
  //Field: RW_WS
  //Bit  : 5
  //APB Write
  assign ACTRL_next[5] = ACTRL_byte_we[0]? pwdata[5]: ACTRL_sc_value[5];
  //Write to set
  assign ACTRL_sc_value[5] = ACTRL_RW_WS_0_set? '1: ACTRL_ivalue[5];
  assign ACTRL_RW_WS_0_set = ACTRL_byte_we[0];
  //Write to clear
  //
  //Write from internal operation
  assign ACTRL_ivalue[5] = ACTRL_reg[5];
  //Reg  : ACTRL
  //Field: RW_WC
  //Bit  : 4
  //APB Write
  assign ACTRL_next[4] = ACTRL_byte_we[0]? pwdata[4]: ACTRL_sc_value[4];
  //Write to set
  //Write to clear
  assign ACTRL_sc_value[4] = ACTRL_RW_WC_0_clr? '0: ACTRL_ivalue[4];
  assign ACTRL_RW_WC_0_clr = ACTRL_byte_we[0];
  //
  //Write from internal operation
  assign ACTRL_ivalue[4] = ACTRL_reg[4];
  //Reg  : ACTRL
  //Field: RW_RS
  //Bit  : 3
  //APB Write
  assign ACTRL_next[3] = ACTRL_byte_we[0]? pwdata[3]: ACTRL_sc_value[3];
  //Write to set
  //Write to clear
  //
  assign ACTRL_sc_value[3] = ACTRL_ivalue[3];
  //Write from internal operation
  assign ACTRL_ivalue[3] = ACTRL_reg[3];
  //Reg  : ACTRL
  //Field: RW_RC
  //Bit  : 2
  //APB Write
  assign ACTRL_next[2] = ACTRL_byte_we[0]? pwdata[2]: ACTRL_sc_value[2];
  //Write to set
  //Write to clear
  //
  assign ACTRL_sc_value[2] = ACTRL_ivalue[2];
  //Write from internal operation
  assign ACTRL_ivalue[2] = ACTRL_reg[2];
  //Reg  : ACTRL
  //Field: RWI
  //Bit  : 1
  //APB Write
  assign ACTRL_next[1] = ACTRL_byte_we[0]? pwdata[1]: ACTRL_sc_value[1];
  //Write to set
  //Write to clear
  //
  assign ACTRL_sc_value[1] = ACTRL_ivalue[1];
  //Write from internal operation
  assign ACTRL_ivalue[1] = ACTRL_RWI_iwe? ACTRL_ivalue[1]: ACTRL_reg[1];
  //Reg  : ACTRL
  //Field: RW
  //Bit  : 0
  //APB Write
  assign ACTRL_next[0] = ACTRL_byte_we[0]? pwdata[0]: ACTRL_sc_value[0];
  //Write to set
  //Write to clear
  //
  assign ACTRL_sc_value[0] = ACTRL_ivalue[0];
  //Write from internal operation
  assign ACTRL_ivalue[0] = ACTRL_reg[0];
  //Reg  : BCTRL
  //Field: BAUND3
  //Bit  : 27:24
  //APB Write
  assign BCTRL_next[27:24] = BCTRL_byte_we[3]? pwdata[27:24]: BCTRL_sc_value[27:24];
  //Write to set
  //Write to clear
  //
  assign BCTRL_sc_value[27:24] = BCTRL_ivalue[27:24];
  //Write from internal operation
  assign BCTRL_ivalue[27:24] = BCTRL_reg[27:24];
  //Reg  : BCTRL
  //Field: BAUND3
  //Bit  : 23:16
  //APB Write
  assign BCTRL_next[23:16] = BCTRL_byte_we[2]? pwdata[23:16]: BCTRL_sc_value[23:16];
  //Write to set
  //Write to clear
  //
  assign BCTRL_sc_value[23:16] = BCTRL_ivalue[23:16];
  //Write from internal operation
  assign BCTRL_ivalue[23:16] = BCTRL_reg[23:16];
  //Reg  : BCTRL
  //Field: BAUND2
  //Bit  : 15:8
  //APB Write
  assign BCTRL_next[15:8] = BCTRL_byte_we[1]? pwdata[15:8]: BCTRL_sc_value[15:8];
  //Write to set
  //Write to clear
  //
  assign BCTRL_sc_value[15:8] = BCTRL_ivalue[15:8];
  //Write from internal operation
  assign BCTRL_ivalue[15:8] = BCTRL_reg[15:8];
  //Reg  : BCTRL
  //Field: WO1
  //Bit  : 7
  //APB Write
  assign BCTRL_next[7] = BCTRL_byte_we[0]? pwdata[7]: BCTRL_sc_value[7];
  //Write to set
  assign BCTRL_sc_value[7] = BCTRL_WO1_0_set? '1: BCTRL_ivalue[7];
  assign BCTRL_WO1_0_w1 = BCTRL_byte_we[0] & (&pwdata[7]);
  assign BCTRL_WO1_0_set = BCTRL_WO1_0_w1;
  //Write to clear
  //
  //Write from internal operation
  assign BCTRL_ivalue[7] = BCTRL_reg[7];
  //Reg  : BCTRL
  //Field: WO0
  //Bit  : 6
  //APB Write
  assign BCTRL_next[6] = BCTRL_byte_we[0]? pwdata[6]: BCTRL_sc_value[6];
  //Write to set
  //Write to clear
  assign BCTRL_sc_value[6] = BCTRL_WO0_0_clr? '0: BCTRL_ivalue[6];
  assign BCTRL_WO0_0_w0 = BCTRL_byte_we[0] & (~|pwdata[6]);
  assign BCTRL_WO0_0_clr = BCTRL_WO0_0_w0;
  //
  //Write from internal operation
  assign BCTRL_ivalue[6] = BCTRL_reg[6];
  //Reg  : BCTRL
  //Field: WOS
  //Bit  : 5
  //APB Write
  assign BCTRL_next[5] = BCTRL_byte_we[0]? pwdata[5]: BCTRL_sc_value[5];
  //Write to set
  //Write to clear
  //
  assign BCTRL_sc_value[5] = BCTRL_ivalue[5];
  //Write from internal operation
  assign BCTRL_ivalue[5] = BCTRL_reg[5];
  //Reg  : BCTRL
  //Field: WOC
  //Bit  : 4
  //APB Write
  assign BCTRL_next[4] = BCTRL_byte_we[0]? pwdata[4]: BCTRL_sc_value[4];
  //Write to set
  //Write to clear
  //
  assign BCTRL_sc_value[4] = BCTRL_ivalue[4];
  //Write from internal operation
  assign BCTRL_ivalue[4] = BCTRL_reg[4];
  //Reg  : BCTRL
  //Field: WO
  //Bit  : 3
  //APB Write
  assign BCTRL_next[3] = BCTRL_byte_we[0]? pwdata[3]: BCTRL_sc_value[3];
  //Write to set
  //Write to clear
  //
  assign BCTRL_sc_value[3] = BCTRL_ivalue[3];
  //Write from internal operation
  assign BCTRL_ivalue[3] = BCTRL_reg[3];
  //Reg  : BCTRL
  //Field: ROS
  //Bit  : 2
  //APB Write
  assign BCTRL_next[2] = BCTRL_byte_we[0]? pwdata[2]: BCTRL_sc_value[2];
  //Write to set
  assign BCTRL_sc_value[2] = BCTRL_ROS_0_set? '1: BCTRL_ivalue[2];
  assign BCTRL_ROS_0_set = BCTRL_read_en;
  //Write to clear
  //
  //Write from internal operation
  assign BCTRL_ivalue[2] = BCTRL_ROS_iwe? BCTRL_ivalue[2]: BCTRL_reg[2];
  //Reg  : BCTRL
  //Field: ROC
  //Bit  : 1
  //APB Write
  assign BCTRL_next[1] = BCTRL_byte_we[0]? pwdata[1]: BCTRL_sc_value[1];
  //Write to set
  //Write to clear
  assign BCTRL_sc_value[1] = BCTRL_ROC_0_clr? '0: BCTRL_ivalue[1];
  assign BCTRL_ROC_0_clr = BCTRL_read_en;
  //
  //Write from internal operation
  assign BCTRL_ivalue[1] = BCTRL_ROC_iwe? BCTRL_ivalue[1]: BCTRL_reg[1];
  //Reg  : BCTRL
  //Field: RO
  //Bit  : 0
  //APB Write
  assign BCTRL_next[0] = BCTRL_byte_we[0]? pwdata[0]: BCTRL_sc_value[0];
  //Write to set
  //Write to clear
  //
  assign BCTRL_sc_value[0] = BCTRL_ivalue[0];
  //Write from internal operation
  assign BCTRL_ivalue[0] = BCTRL_RO_iwe? BCTRL_ivalue[0]: BCTRL_reg[0];
  //
  //assign ACTRL_next[27:24] = ACTRL_next[27:24];
  always_ff @ (posedge reg_clk, negedge reg_rst_n) begin
    if (!reg_rst_n)
      ACTRL_reg[27:24] <= 4'b0000;
    else if (ACTRL_byte_we[3])
      ACTRL_reg[27:24] <= ACTRL_next[27:24];
  end
  //assign ACTRL_next[23:16] = ACTRL_next[23:16];
  always_ff @ (posedge reg_clk, negedge reg_rst_n) begin
    if (!reg_rst_n)
      ACTRL_reg[23:16] <= 8'hff;
    else if (ACTRL_byte_we[2])
      ACTRL_reg[23:16] <= ACTRL_next[23:16];
  end
  //assign ACTRL_next[15:10] = ACTRL_next[15:10];
  always_ff @ (posedge reg_clk, negedge reg_rst_n) begin
    if (!reg_rst_n)
      ACTRL_reg[15:10] <= 6'd0;
    else if (ACTRL_byte_we[1])
      ACTRL_reg[15:10] <= ACTRL_next[15:10];
  end
  //assign ACTRL_next[9] = ACTRL_next[9];
  always_ff @ (posedge reg_clk, negedge reg_rst_n) begin
    if (!reg_rst_n)
      ACTRL_reg[9] <= 1'b0;
    else if (ACTRL_byte_we[1])
      ACTRL_reg[9] <= ACTRL_next[9];
  end
  //assign ACTRL_next[8] = ACTRL_next[8];
  always_ff @ (posedge reg_clk, negedge reg_rst_n) begin
    if (!reg_rst_n)
      ACTRL_reg[8] <= 1'b0;
    else if (ACTRL_byte_we[1])
      ACTRL_reg[8] <= ACTRL_next[8];
  end
  //assign ACTRL_next[7] = ACTRL_next[7];
  always_ff @ (posedge reg_clk, negedge reg_rst_n) begin
    if (!reg_rst_n)
      ACTRL_reg[7] <= 1'b0;
    else if (ACTRL_byte_we[0])
      ACTRL_reg[7] <= ACTRL_next[7];
  end
  //assign ACTRL_next[6] = ACTRL_next[6];
  always_ff @ (posedge reg_clk, negedge reg_rst_n) begin
    if (!reg_rst_n)
      ACTRL_reg[6] <= 1'b0;
    else if (ACTRL_byte_we[0])
      ACTRL_reg[6] <= ACTRL_next[6];
  end
  //assign ACTRL_next[5] = ACTRL_next[5];
  always_ff @ (posedge reg_clk, negedge reg_rst_n) begin
    if (!reg_rst_n)
      ACTRL_reg[5] <= 1'b0;
    else if (ACTRL_byte_we[0])
      ACTRL_reg[5] <= ACTRL_next[5];
  end
  //assign ACTRL_next[4] = ACTRL_next[4];
  always_ff @ (posedge reg_clk, negedge reg_rst_n) begin
    if (!reg_rst_n)
      ACTRL_reg[4] <= 1'b0;
    else if (ACTRL_byte_we[0])
      ACTRL_reg[4] <= ACTRL_next[4];
  end
  //assign ACTRL_next[3] = ACTRL_next[3];
  always_ff @ (posedge reg_clk, negedge reg_rst_n) begin
    if (!reg_rst_n)
      ACTRL_reg[3] <= 1'b0;
    else if (ACTRL_byte_we[0])
      ACTRL_reg[3] <= ACTRL_next[3];
  end
  //assign ACTRL_next[2] = ACTRL_next[2];
  always_ff @ (posedge reg_clk, negedge reg_rst_n) begin
    if (!reg_rst_n)
      ACTRL_reg[2] <= 1'b0;
    else if (ACTRL_byte_we[0])
      ACTRL_reg[2] <= ACTRL_next[2];
  end
  //assign ACTRL_next[1] = ACTRL_next[1];
  always_ff @ (posedge reg_clk, negedge reg_rst_n) begin
    if (!reg_rst_n)
      ACTRL_reg[1] <= 1'b0;
    else if (ACTRL_byte_we[0])
      ACTRL_reg[1] <= ACTRL_next[1];
  end
  //assign ACTRL_next[0] = ACTRL_next[0];
  always_ff @ (posedge reg_clk, negedge reg_rst_n) begin
    if (!reg_rst_n)
      ACTRL_reg[0] <= 1'b0;
    else if (ACTRL_byte_we[0])
      ACTRL_reg[0] <= ACTRL_next[0];
  end
  //assign BCTRL_next[27:24] = BCTRL_next[27:24];
  always_ff @ (posedge reg_clk, negedge reg_rst_n) begin
    if (!reg_rst_n)
      BCTRL_reg[27:24] <= 4'b0000;
    else if (BCTRL_byte_we[3])
      BCTRL_reg[27:24] <= BCTRL_next[27:24];
  end
  //assign BCTRL_next[23:16] = BCTRL_next[23:16];
  always_ff @ (posedge reg_clk, negedge reg_rst_n) begin
    if (!reg_rst_n)
      BCTRL_reg[23:16] <= 8'hff;
    else if (BCTRL_byte_we[2])
      BCTRL_reg[23:16] <= BCTRL_next[23:16];
  end
  //assign BCTRL_next[15:8] = BCTRL_next[15:8];
  always_ff @ (posedge reg_clk, negedge reg_rst_n) begin
    if (!reg_rst_n)
      BCTRL_reg[15:8] <= 8'd0;
    else if (BCTRL_byte_we[1])
      BCTRL_reg[15:8] <= BCTRL_next[15:8];
  end
  //assign BCTRL_next[7] = BCTRL_next[7];
  always_ff @ (posedge reg_clk, negedge reg_rst_n) begin
    if (!reg_rst_n)
      BCTRL_reg[7] <= 1'b0;
    else if (BCTRL_byte_we[0])
      BCTRL_reg[7] <= BCTRL_next[7];
  end
  //assign BCTRL_next[6] = BCTRL_next[6];
  always_ff @ (posedge reg_clk, negedge reg_rst_n) begin
    if (!reg_rst_n)
      BCTRL_reg[6] <= 1'b0;
    else if (BCTRL_byte_we[0])
      BCTRL_reg[6] <= BCTRL_next[6];
  end
  //assign BCTRL_next[5] = BCTRL_next[5];
  always_ff @ (posedge reg_clk, negedge reg_rst_n) begin
    if (!reg_rst_n)
      BCTRL_reg[5] <= 1'b0;
    else if (BCTRL_byte_we[0])
      BCTRL_reg[5] <= BCTRL_next[5];
  end
  //assign BCTRL_next[4] = BCTRL_next[4];
  always_ff @ (posedge reg_clk, negedge reg_rst_n) begin
    if (!reg_rst_n)
      BCTRL_reg[4] <= 1'b0;
    else if (BCTRL_byte_we[0])
      BCTRL_reg[4] <= BCTRL_next[4];
  end
  //assign BCTRL_next[3] = BCTRL_next[3];
  always_ff @ (posedge reg_clk, negedge reg_rst_n) begin
    if (!reg_rst_n)
      BCTRL_reg[3] <= 1'b0;
    else if (BCTRL_byte_we[0])
      BCTRL_reg[3] <= BCTRL_next[3];
  end
  //assign BCTRL_next[2] = BCTRL_next[2];
  always_ff @ (posedge reg_clk, negedge reg_rst_n) begin
    if (!reg_rst_n)
      BCTRL_reg[2] <= 1'b0;
    else if (BCTRL_byte_we[0])
      BCTRL_reg[2] <= BCTRL_next[2];
  end
  //assign BCTRL_next[1] = BCTRL_next[1];
  always_ff @ (posedge reg_clk, negedge reg_rst_n) begin
    if (!reg_rst_n)
      BCTRL_reg[1] <= 1'b0;
    else if (BCTRL_byte_we[0])
      BCTRL_reg[1] <= BCTRL_next[1];
  end
  //assign BCTRL_next[0] = BCTRL_next[0];
  always_ff @ (posedge reg_clk, negedge reg_rst_n) begin
    if (!reg_rst_n)
      BCTRL_reg[0] <= 1'b0;
    else if (BCTRL_byte_we[0])
      BCTRL_reg[0] <= BCTRL_next[0];
  end
  //Read data
  assign ACTRL_RESERVED_rvalue[31:28] = '0;
  assign ACTRL_BAUND1_rvalue[27:24] = ACTRL_read_en? ACTRL_reg[27:24]: '0;
  assign ACTRL_BAUND1_rvalue[23:16] = ACTRL_read_en? ACTRL_reg[23:16]: '0;
  assign ACTRL_BAUND0_rvalue[15:10] = ACTRL_read_en? ACTRL_reg[15:10]: '0;
  assign ACTRL_RW_W0S_rvalue[9] = ACTRL_read_en? ACTRL_reg[9]: '0;
  assign ACTRL_RW_W1S_rvalue[8] = ACTRL_read_en? ACTRL_reg[8]: '0;
  assign ACTRL_RW_W0C_rvalue[7] = ACTRL_read_en? ACTRL_reg[7]: '0;
  assign ACTRL_RW_W1C_rvalue[6] = ACTRL_read_en? ACTRL_reg[6]: '0;
  assign ACTRL_RW_WS_rvalue[5] = ACTRL_read_en? ACTRL_reg[5]: '0;
  assign ACTRL_RW_WC_rvalue[4] = ACTRL_read_en? ACTRL_reg[4]: '0;
  assign ACTRL_RW_RS_rvalue[3] = ACTRL_read_en? ACTRL_reg[3]: '0;
  assign ACTRL_RW_RC_rvalue[2] = ACTRL_read_en? ACTRL_reg[2]: '0;
  assign ACTRL_RWI_rvalue[1] = ACTRL_read_en? ACTRL_reg[1]: '0;
  assign ACTRL_RW_rvalue[0] = ACTRL_read_en? ACTRL_reg[0]: '0;
  assign BCTRL_RESERVED_rvalue[31:28] = '0;
  assign BCTRL_BAUND3_rvalue[27:24] = BCTRL_read_en? BCTRL_reg[27:24]: '0;
  assign BCTRL_BAUND3_rvalue[23:16] = BCTRL_read_en? BCTRL_reg[23:16]: '0;
  assign BCTRL_BAUND2_rvalue[15:8] = BCTRL_read_en? BCTRL_reg[15:8]: '0;
  assign BCTRL_WO1_rvalue[7] = '0;
  assign BCTRL_WO0_rvalue[6] = '0;
  assign BCTRL_WOS_rvalue[5] = '0;
  assign BCTRL_WOC_rvalue[4] = '0;
  assign BCTRL_WO_rvalue[3] = '0;
  assign BCTRL_ROS_rvalue[2] = BCTRL_read_en? BCTRL_reg[2]: '0;
  assign BCTRL_ROC_rvalue[1] = BCTRL_read_en? BCTRL_reg[1]: '0;
  assign BCTRL_RO_rvalue[0] = BCTRL_read_en? BCTRL_reg[0]: '0;
  //
  assign ACTRL_rvalue = {REGGEN_DATA_WIDTH{ACTRL_read_en}} & ACTRL_reg;
  assign BCTRL_rvalue = {REGGEN_DATA_WIDTH{BCTRL_read_en}} & BCTRL_reg;
  assign prdata_next = ACTRL_rvalue | BCTRL_rvalue;
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
  //
endmodule: ExampleCsr
