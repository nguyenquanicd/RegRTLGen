//--------------------------------------
//Project:  The UVM environemnt for UART (Universal Asynchronous Receiver Transmitter)
//Function: All interfaces
//Author:   Nguyen Hung Quan, Pham Thanh Tram, Nguyen Sinh Ton, Doan Duc Hoang, Truong Cong Hoang Viet
//Page:     VLSI Technology
//--------------------------------------
//APB interface
//interface ifApbMaster (input logic pclk, input logic preset_n);
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
endinterface: ifApbMaster
//Interrupt interface 
// Remove interrupt interface ifInterrupt;
// Remove interrupt   `ifdef INTERRUPT_COM
// Remove interrupt     logic ctrl_if;
// Remove interrupt   `else
// Remove interrupt     logic ctrl_tif;
// Remove interrupt     logic ctrl_rif;
// Remove interrupt     logic ctrl_pif;
// Remove interrupt     logic ctrl_oif;  
// Remove interrupt     logic ctrl_fif;
// Remove interrupt    `endif
// Remove interrupt endinterface: ifInterrupt
// Remove interrupt //UART interface
// Remove interrupt interface ifUart (input logic pclk, input logic preset_n);
// Remove interrupt   logic uart_tx;
// Remove interrupt   logic uart_rx;
// Remove interrupt endinterface: ifUart