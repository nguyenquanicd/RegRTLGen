//---------------------------------------------------------------
//Copyright © 2020 by VLSI Technology blog in Vietnam
//Website    : http://nguyenquanicd.blogspot.com/
//Author     : Nguyen Hung Quan (nguyenquan.icd@gmail.com)
//Description: Register file library with APB interface
//Language   : System Verilog
//---------------------------------------------------------------
//Version    : 1.0
//Date       : Apr.30.2020
//---------------------------------------------------------------
module $GenModuleName
  #(
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
    input  logic write_protect_en,
    input  logic $GenInternalWriteReg,
    input  logic $GEnInternalWriteRegWe,
    output logic [REGGEN_STRB_WIDTH-1:0] $GenRegName_byte_we,
    output logic $GenRegName_$GenRegField_set,
    output logic $GenRegName_$GenRegField_clr,
    output logic [REGGEN_DATA_WIDTH-1:0] $GenRegName_$GenRegField_reg
  );
  //pclk
  
  //
endmodule: $GenModuleName