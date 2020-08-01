  // clock & reset
  input  logic reg_clk,   //User clock
  input  logic reg_rst_n, //User reset is synchronized to reg_clk
  
  // APB interface 
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
  input  logic pclk,      //APB clock
  input  logic preset_n,   //APB reset is synchronized to pclk    
  
  // Write protection = YES
  input  logic write_protect_en,
  
  //RWI RO ROC ROS
  input  logic [REGGEN_DATA_WIDTH-1:0] $GenRegName_ivalue,
  input  logic $GenRegName_$GenRegField_iwe,
  

  
  
  // all Write property
  output logic [REGGEN_DATA_WIDTH-1:0] $GenRegName_reg,
  
  // POR
  output logic $GenRegName_read_en,
  
  // POW POW0 POW1
  output logic [REGGEN_STRB_WIDTH-1:0] $GenRegName_byte_we,
    // POW1 
    output logic $GenRegName_$GenRegField_$GenPStrbIndex_w1,
    // POW0 
    output logic $GenRegName_$GenRegField_$GenPStrbIndex_w0,
