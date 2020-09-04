///
  // clock & reset
  input  logic reg_clk,   //User clock
  input  logic reg_rst_n, //User reset is synchronized to reg_clk
///
  
///
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
///
    
///
  // Write protection = YES
  input  logic write_protect_en,
  
  //RWI RO ROC ROS
  input  logic [REGGEN_DATA_WIDTH-1:0] $GenRegName_ivalue,
  input  logic $GenRegName_$GenRegField_iwe,
/// 


=> write_protect_en

                REG A:
          => $GenRegName_$GenRegField_iwe|        
       => $GenRegName_$GenRegField_iwe|  |    
    => $GenRegName_$GenRegField_iwe|  |  |    
 => $GenRegName_$GenRegField_iwe|  |  |  |  ...
                                
=> [31:0] $GenRegName_ivalue [31-24] [23-16] [15-8] [7-0] => [31:0] $GenRegName_reg
                                                          => $GenRegName_read_en (pulse)
                                |       |       |     |  => [3:0] $GenRegName_byte_we (pulse)       
                                |       |       |     |      
                                |       |       |     |0 => $GenRegName_$GenRegField_0_w1 (pulse)
                                |       |       |        => $GenRegName_$GenRegField_0_w0 (pulse)
                                |       |       |        => ...
                                |       |       |1 => $GenRegName_$GenRegField_1_w1 (pulse)  
                                |       |          => $GenRegName_$GenRegField_1_w0 (pulse)
                                |       |          => ...
                                |       |2 => $GenRegName_$GenRegField_2_w1 (pulse)
                                |          => $GenRegName_$GenRegField_2_w0 (pulse)
                                |          => ...
                                |3 => $GenRegName_$GenRegField_3_w1 (pulse)
                                   => $GenRegName_$GenRegField_3_w0 (pulse)   
                                   => ...
                                                              
                REG B:
          => $GenRegName_$GenRegField_iwe|        
       => $GenRegName_$GenRegField_iwe|  |    
    => $GenRegName_$GenRegField_iwe|  |  |    
 => $GenRegName_$GenRegField_iwe|  |  |  |  ...
                                
=> [31:0] $GenRegName_ivalue [31-24] [23-16] [15-8] [7-0] => [31:0] $GenRegName_reg
                                                          => $GenRegName_read_en (pulse)
                                |       |       |     |  => [3:0] $GenRegName_byte_we (pulse)       
                                |       |       |     |      
                                |       |       |     |0 => $GenRegName_$GenRegField_0_w1 (pulse)
                                |       |       |        => $GenRegName_$GenRegField_0_w0 (pulse)
                                |       |       |        => ...
                                |       |       |1 => $GenRegName_$GenRegField_1_w1 (pulse)  
                                |       |          => $GenRegName_$GenRegField_1_w0 (pulse)
                                |       |          => ...
                                |       |2 => $GenRegName_$GenRegField_2_w1 (pulse)
                                |          => $GenRegName_$GenRegField_2_w0 (pulse)
                                |          => ...
                                |3 => $GenRegName_$GenRegField_3_w1 (pulse)
                                   => $GenRegName_$GenRegField_3_w0 (pulse)   
                                   => ...
                                        
                                        
                                        
          
          
          
          