//--------------------------------------
//Project: The UVM environemnt for RegisterRTL
//Function: Register Config Transaction
//Author:  Le Hoang Van, XXX
//Page:    VLSI Technology
//--------------------------------------

//--------------------------------------
// Setting for "RWI RO ROC ROS" Register
// address - 32-bit write address
// value - 32-bit write value 
// enable - logic 0/1
//--------------------------------------
`define RegConfig(address,value,upper,lower,enable) \
`uvm_do_on_with(RegConfigSeq, p_sequencer.coApbMasterAgentTx.coApbMasterSequencer, { \
               RegConfigSeq.Reg_Addr[31:0] == address; \
               RegConfigSeq.Reg_Data[31:0] == value; \
               RegConfigSeq.Reg_Upper_bit  == upper; \
               RegConfigSeq.Reg_Lower_bit  == lower; \
               RegConfigSeq.Reg_IWE_value  == enable; \
               })
               
//--------------------------------------
//Write "value" to "address" of a register of UART-TX
// address - 32-bit write address
// value - 32-bit write value 
//--------------------------------------
`define ApbWriteTX(address,value) \
`uvm_do_on_with(WriteSeq, p_sequencer.coApbMasterAgentTx.coApbMasterSequencer, { \
               WriteSeq.conEn      == 1'b0; \
               WriteSeq.addr[31:0] == address; \
               WriteSeq.data[31:0] == value; \
               WriteSeq.be[3:0]    == 4'b1111; \
               })

//--------------------------------------
//Read "value" from "address" of a register of UART-TX
// address - 32-bit read address
// expectedReadData - 32-bit expected read value
// mask - 32-bit mask, 1=compared, 0=masked/ignored
//--------------------------------------
`define ApbReadTX(address,expectedData,uMask) \
`uvm_do_on_with(ReadSeq, p_sequencer.coApbMasterAgentTx.coApbMasterSequencer, { \
               ReadSeq.conEn      == 1'b0; \
               ReadSeq.addr[31:0] == address; \
               ReadSeq.expectedReadData[31:0] == expectedData; \
               ReadSeq.mask[31:0] == uMask; \
               })

//--------------------------------------
//Write "value" to "address" of a register of UART-RX
// address - 32-bit write address
// value - 32-bit write value
//--------------------------------------
`define ApbWriteRX(address,value) \
`uvm_do_on_with(WriteSeq, p_sequencer.coApbMasterAgentRx.coApbMasterSequencer, { \
               WriteSeq.conEn      == 1'b0; \
               WriteSeq.addr[31:0] == address; \
               WriteSeq.data[31:0] == value; \
               WriteSeq.be[3:0]    == 4'b1111; \
               })

//--------------------------------------
//Read "value" from "address" of a register of UART-RX
// address - 32-bit read address
// expectedReadData - 32-bit expected read value
// mask - 32-bit mask, 1=compared, 0=masked/ignored
//--------------------------------------
`define ApbReadRX(address,expectedData,uMask) \
`uvm_do_on_with(ReadSeq, p_sequencer.coApbMasterAgentRx.coApbMasterSequencer, { \
               ReadSeq.conEn      == 1'b0; \
               ReadSeq.addr[31:0] == address; \
               ReadSeq.expectedReadData[31:0] == expectedData; \
               ReadSeq.mask[31:0] == uMask; \
               })
               
//--------------------------------------
//Write random "value" to "address" of a register of UART-RX
// address - 32-bit read address
// VietHTs
//--------------------------------------

`define ApbWriteRandTX(address) \
`uvm_do_on_with(WriteSeq, p_sequencer.coApbMasterAgentTx.coApbMasterSequencer, { \
               WriteSeq.conEn      == 1'b0; \
               WriteSeq.addr[31:0] == address; \
               WriteSeq.be[3:0]    == 4'b1111; \
               WriteSeq.data<=32'hFF; \
               WriteSeq.data>= 32'h00; \
               })
               
//--------------------------------------
//Read "value" from "address" of a register of UART-RX
// address - 32-bit read address
// VietHTs
//--------------------------------------
               
`define ApbReadWoCmprRX(address) \
`uvm_do_on_with(ReadSeqWoCmpr, p_sequencer.coApbMasterAgentRx.coApbMasterSequencer, { \
               ReadSeqWoCmpr.conEn      == 1'b0; \
               ReadSeqWoCmpr.addr[31:0] == address; \
               })

