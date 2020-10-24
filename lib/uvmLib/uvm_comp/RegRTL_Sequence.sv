//--------------------------------------
//Project: The UVM environemnt for UART (Universal Asynchronous Receiver Transmitter)
//Function: User UVM Sequence - This is the TEST PATTERN created by user
//  - User modifty this class to create the expected transactions for the test purpose
//Author:  Pham Thanh Tram, Nguyen Sinh Ton, Doan Duc Hoang, Truong Cong Hoang Viet, Nguyen Hung Quan
//Page:    VLSI Technology
//--------------------------------------

class cVSequence extends uvm_sequence#(cApbTransaction);
  //Register to Factory
	`uvm_object_utils(cVSequence)
  `uvm_declare_p_sequencer(cVSequencer)
  
  cApbMasterWriteSeq WriteSeq;
  cApbMasterReadSeq ReadSeq;
  // Object must not have veriable "parent" (refer to class cVSequencer)
	function new (string name = "cVSequence");
		super.new(name);
	endfunction
  //TEST PATTERN is written at here
  task body();
    #50ns
    //--------------------------------------------
    //Setting UART-TX (uart_0)
    //--------------------------------------------
    //Set baud rate
    `ApbWriteTX(32'h00000008,32'h00000006) //200000
    `ApbReadTX(32'h00000008,32'h00000006,32'hffffffff)
    //Enable
    `ApbWriteTX(32'h00000004,32'h00000001)
    `ApbReadTX(32'h00000004,32'h00000001,32'h00000001)
    //--------------------------------------------
    //Setting UART-RX (uart_1)
    //--------------------------------------------
    //Set baud rate
    `ApbWriteRX(32'h00000008,32'h0000003) //200000
    `ApbReadRX(32'h00000008,32'h00000003,32'hffffffff)
    //Enable
    `ApbWriteRX(32'h00000004,32'h00000001)
    `ApbReadRX(32'h00000004,32'h00000001,32'h00000001)
    //
    //Write to DATA register of UART-TX to send data
    //Note: DATA only is 8-bit LSB
    for (int i = 0; i < 18; i++) begin
      `ApbWriteTX(32'h0000000C,i)
      `ApbWriteRX(32'h0000000C,~i)
    end
    //Check DATA on UART RX
    while (1) begin
      #100
      `ApbReadRX(32'h00000004,32'h00000040,32'h00000000)
      if (ReadSeq.coApbTransaction.prdata[6]) begin
        `ApbReadRX(32'h0000000C,32'h00000055,32'h00000000)
      end
      //
      `ApbReadTX(32'h00000004,32'h00000040,32'h00000000)
      if (ReadSeq.coApbTransaction.prdata[6]) begin
        `ApbReadTX(32'h0000000C,32'h00000055,32'h00000000)
      end
    end
  endtask
endclass