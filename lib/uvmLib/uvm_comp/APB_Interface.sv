//--------------------------------------
//Project: The UVM environemnt for RegisterRTL
//Function: APB Interface
//Author:  Nguyen Hung Quan, Le Hoang Van, Tran Huu Duy
//Page:    VLSI Technology
//--------------------------------------

interface ifApbMaster;
  logic pclk;
  logic preset_n;
  logic psel;
  logic penable;
  logic pwrite;
  logic [31:0] paddr;
  logic [31:0] pwdata;
  logic [31:0] prdata;
  logic [3:0]  pstrb;
  logic [2:0]  pprot;
  logic        pready;
  logic        pslverr;
  logic wprot_en;
endinterface: ifApbMaster
