//--------------------------------------
//Project: The UVM environemnt for RegisterRTL
//Function: Macros
//Author:  Nguyen Hung Quan, Le Hoang Van, Tran Huu Duy
//Page:    VLSI Technology
//--------------------------------------

//--------------------------------------
// Setting for "RWI RO ROC ROS" Register
// address - 32-bit write address
// value - 32-bit write value 
// enable - logic 0/1
//--------------------------------------
`define RegConfig(address,value,upper,lower,enable) \
`uvm_do_on_with(RegConfigSeq, p_sequencer.co_RegConfig_Agent.co_RegConfig_Sequencer, { \
               RegConfigSeq.Reg_Addr[31:0] == address; \
               RegConfigSeq.Reg_Data[31:0] == value; \
               RegConfigSeq.Reg_Upper_bit  == upper; \
               RegConfigSeq.Reg_Lower_bit  == lower; \
               RegConfigSeq.Reg_IWE_value  == enable; \
               })
               
//--------------------------------------
//Write "value" to "address" of a register
// address - 32-bit write address
// value - 32-bit write value 
//--------------------------------------
`define ApbWrite(address,value) \
`uvm_do_on_with(WriteSeq, p_sequencer.coApbMasterAgent.coApbMasterSequencer, { \
               WriteSeq.conEn      == 1'b0; \
               WriteSeq.addr[31:0] == address; \
               WriteSeq.data[31:0] == value; \
               WriteSeq.be[3:0]    == 4'b1111; \
               })

//--------------------------------------
//Read "value" from "address" of a register
// address - 32-bit read address
// expectedReadData - 32-bit expected read value
// mask - 32-bit mask, 1=compared, 0=masked/ignored
//--------------------------------------
`define ApbRead(address,expectedData,uMask) \
`uvm_do_on_with(ReadSeq, p_sequencer.coApbMasterAgent.coApbMasterSequencer, { \
               ReadSeq.conEn      == 1'b0; \
               ReadSeq.addr[31:0] == address; \
               ReadSeq.expectedReadData[31:0] == expectedData; \
               ReadSeq.mask[31:0] == uMask; \
               })


//--------------------------------------
//Write random "value" to "address" of a register
// address - 32-bit read address
//--------------------------------------

`define ApbWriteRand(address) \
`uvm_do_on_with(WriteSeq, p_sequencer.coApbMasterAgent.coApbMasterSequencer, { \
               WriteSeq.conEn      == 1'b0; \
               WriteSeq.addr[31:0] == address; \
               WriteSeq.be[3:0]    == 4'b1111; \
               WriteSeq.data<=32'hFF; \
               WriteSeq.data>= 32'h00; \
               })
               
//--------------------------------------
//Read "value" from "address" of a register
// address - 32-bit read address
//--------------------------------------
               
`define ApbReadWoCmpr(address) \
`uvm_do_on_with(ReadSeqWoCmpr, p_sequencer.coApbMasterAgent.coApbMasterSequencer, { \
               ReadSeqWoCmpr.conEn      == 1'b0; \
               ReadSeqWoCmpr.addr[31:0] == address; \
               })

