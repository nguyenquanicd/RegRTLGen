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
  $GenStartLoop$GenRegName
    logic $GenRegName_sel;
    logic $GenRegName_write_en;
    logic $GenRegName_read_en;
    logic [REGGEN_STRB_WIDTH-1:0] $GenRegName_byte_we;
    logic [REGGEN_DATA_WIDTH-1:0] $GenRegName_next;
    logic [REGGEN_DATA_WIDTH-1:0] $GenRegName_reg;
    $RW_WS$RW_W1S$RW_W0S$WO1$ROS logic [REGGEN_DATA_WIDTH-1:0] $GenRegName_sc_value;
    logic [REGGEN_DATA_WIDTH-1:0] $GenRegName_rvalue;
  $GenEndLoop
  $GenStartLoop$GenRegName$GenRegField$GenPartialBitRange
    $RW_WS logic $GenRegName_$GenRegField_$GenPStrbIndex_set;
    $RW_W1S$WO1 logic $GenRegName_$GenRegField_$GenPStrbIndex_w1;
    $RW_W1S$WO1 logic $GenRegName_$GenRegField_$GenPStrbIndex_set;
    $RW_W0S logic $GenRegName_$GenRegField_$GenPStrbIndex_set;
    $ROS logic $GenRegName_$GenRegField_$GenPStrbIndex_set;
    //
    $RW_WC logic $GenRegName_$GenRegField_$GenPStrbIndex_clr;
    $RW_W1C logic $GenRegName_$GenRegField_$GenPStrbIndex_clr;
    $RW_W0C$WO0 logic $GenRegName_$GenRegField_$GenPStrbIndex_w0;
    $RW_W0C$WO0 logic $GenRegName_$GenRegField_$GenPStrbIndex_clr;
    $ROC logic $GenRegName_$GenRegField_$GenPStrbIndex_clr;
  $GenEndLoop
  //
  $GenStartLoop$GenRegName$GenRegField
    logic [REGGEN_STRB_WIDTH-1:0] $GenRegName_$GenRegField_rvalue;
    $RESERVED logic [REGGEN_STRB_WIDTH-1:0] $GenRegName_$GenRegField_rvalue;
  $GenEndLoop
  //// End-Define Internal signals
