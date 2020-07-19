  //// Define Internal signals
  logic setup_phase;
  logic pwrite_en;
  logic pread_en;
  logic req_en;
  logic wprot_en_sync;
  logic [REGGEN_DATA_WIDTH-1:0] prdata_next;
  logic prot_error;
  logic sec_error;
  logic pslverr_nxt;
  $GenStartLoop$GenRegName
    logic $GenRegName_sel;
    $RW$RW_RC$RW_RS$RW_WC$RW_WS$RW_W1C$RW_W0S$RW_W1S$RW_W0S$WO$WOC$WOS$WO0$WO1 logic $GenRegName_write_en;
    $GenNOT$POR logic $GenRegName_read_en;
    $GenNOT$POW$POW0$POW1 logic [REGGEN_STRB_WIDTH-1:0] $GenRegName_byte_we;
    logic [REGGEN_DATA_WIDTH-1:0] $GenRegName_next;
    $GenNOT$RW$RWI$RW_RC$RW_RS$RW_WC$RW_WS$RW_W1C$RW_W0S$RW_W1S$RW_W0S$WO$WOC$WOS$WO0$WO1 logic [REGGEN_DATA_WIDTH-1:0] $GenRegName_reg;
    logic [REGGEN_DATA_WIDTH-1:0] $GenRegName_ivalue_next;
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
  //// End-Define Internal signals
