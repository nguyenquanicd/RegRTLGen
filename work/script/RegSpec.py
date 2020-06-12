RegSpec = {}
RegSpec['GenUserHeader'] = """
//Version: 1.0
//Description: Register specification of VG
//
//"""
RegSpec['RegSpec_Test'] = {}
RegSpec['RegSpec_Test']['Common_Config'] = {}
RegSpec['RegSpec_Test']['Common_Config']['GenModuleName'] = "ExampleCsr"
RegSpec['RegSpec_Test']['Common_Config']['Interface'] = "APB4"
RegSpec['RegSpec_Test']['Common_Config']['GenDataParam'] = "32"
RegSpec['RegSpec_Test']['Common_Config']['GenAddrParam'] = "16"
RegSpec['RegSpec_Test']['Common_Config']['GenAsyncReset'] = "1"
RegSpec['RegSpec_Test']['Common_Config']['GenSyncReset'] = "0"
RegSpec['RegSpec_Test']['Common_Config']['GenAsyncParam'] = "1"
RegSpec['RegSpec_Test']['Common_Config']['GenSyncStageParam'] = "2"
RegSpec['RegSpec_Test']['Common_Config']['GenWProtParam'] = "1"
RegSpec['RegSpec_Test']['Common_Config']['GenSecParam'] = "1"
RegSpec['RegSpec_Test']['Common_Config']['GenWProtErrParam'] = "1"
RegSpec['RegSpec_Test']['Common_Config']['GenSecErrParam'] = "1"
RegSpec['RegSpec_Test']['Register_No_1'] = {}
RegSpec['RegSpec_Test']['Register_No_1']['Common_Config'] = {}
RegSpec['RegSpec_Test']['Register_No_1']['Common_Config']['GenRegName'] = "ACTRL"
RegSpec['RegSpec_Test']['Register_No_1']['Common_Config']['Register_Description'] = "A control register"
RegSpec['RegSpec_Test']['Register_No_1']['Common_Config']['Initial_Value'] = "16'h0000"
RegSpec['RegSpec_Test']['Register_No_1']['Common_Config']['RW_Property'] = {}
RegSpec['RegSpec_Test']['Register_No_1']['Common_Config']['RW_Property']['Strobe_0'] = []
RegSpec['RegSpec_Test']['Register_No_1']['Common_Config']['RW_Property']['Strobe_1'] = []
RegSpec['RegSpec_Test']['Register_No_1']['Common_Config']['RW_Property']['Strobe_2'] = []
RegSpec['RegSpec_Test']['Register_No_1']['Common_Config']['RW_Property']['Strobe_3'] = []
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_1'] = {}
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_1']['Common_Config'] = {}
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_1']['Common_Config']['GenRegField'] = "RESERVED"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_1']['Common_Config']['Field_Desciption'] = """Reserved
Read as zeros"""
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_1']['Common_Config']['RW_Property'] = []
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_1']['Register_Field_Split_No_1'] = {}
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_1']['Register_Field_Split_No_1']['GenPartialBitRange'] = "31:28"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_1']['Register_Field_Split_No_1']['GenFieldReset'] = "4'd0"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_1']['Register_Field_Split_No_1']['GenPStrbIndex'] = "3"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_1']['Register_Field_Split_No_1']['RW_Property'] = []
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_1']['Register_Field_Split_No_1']['RW_Property'].append("RO")
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_1']['Common_Config']['RW_Property'].append("RO")
RegSpec['RegSpec_Test']['Register_No_1']['Common_Config']['RW_Property']['Strobe_3'].append("RO")
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_2'] = {}
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_2']['Common_Config'] = {}
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_2']['Common_Config']['GenRegField'] = "BAUND"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_2']['Common_Config']['Field_Desciption'] = """Baud rate."""
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_2']['Common_Config']['RW_Property'] = []
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_2']['Register_Field_Split_No_1'] = {}
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_2']['Register_Field_Split_No_1']['GenPartialBitRange'] = "27:24"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_2']['Register_Field_Split_No_1']['GenFieldReset'] = "4'b0000"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_2']['Register_Field_Split_No_1']['GenPStrbIndex'] = "3"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_2']['Register_Field_Split_No_1']['RW_Property'] = []
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_2']['Register_Field_Split_No_1']['RW_Property'].append("RW")
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_2']['Common_Config']['RW_Property'].append("RW")
RegSpec['RegSpec_Test']['Register_No_1']['Common_Config']['RW_Property']['Strobe_3'].append("RW")
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_2']['Register_Field_Split_No_1']['RW_Property'].append("POW1")
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_2']['Common_Config']['RW_Property'].append("POW1")
RegSpec['RegSpec_Test']['Register_No_1']['Common_Config']['RW_Property']['Strobe_3'].append("POW1")
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_2']['Register_Field_Split_No_2'] = {}
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_2']['Register_Field_Split_No_2']['GenPartialBitRange'] = "23:16"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_2']['Register_Field_Split_No_2']['GenFieldReset'] = "8'hff"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_2']['Register_Field_Split_No_2']['GenPStrbIndex'] = "2"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_2']['Register_Field_Split_No_2']['RW_Property'] = []
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_2']['Register_Field_Split_No_2']['RW_Property'].append("RW")
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_2']['Common_Config']['RW_Property'].append("RW")
RegSpec['RegSpec_Test']['Register_No_1']['Common_Config']['RW_Property']['Strobe_2'].append("RW")
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_2']['Register_Field_Split_No_2']['RW_Property'].append("POW1")
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_2']['Common_Config']['RW_Property'].append("POW1")
RegSpec['RegSpec_Test']['Register_No_1']['Common_Config']['RW_Property']['Strobe_2'].append("POW1")
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_3'] = {}
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_3']['Common_Config'] = {}
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_3']['Common_Config']['GenRegField'] = "BUSY"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_3']['Common_Config']['Field_Desciption'] = """UART busy.
0 : UART is idle
1 : UART is busy"""
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_3']['Common_Config']['RW_Property'] = []
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_3']['Register_Field_Split_No_1'] = {}
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_3']['Register_Field_Split_No_1']['GenPartialBitRange'] = "15"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_3']['Register_Field_Split_No_1']['GenFieldReset'] = "1'b0"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_3']['Register_Field_Split_No_1']['GenPStrbIndex'] = "1"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_3']['Register_Field_Split_No_1']['RW_Property'] = []
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_3']['Register_Field_Split_No_1']['RW_Property'].append("RO")
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_3']['Common_Config']['RW_Property'].append("RO")
RegSpec['RegSpec_Test']['Register_No_1']['Common_Config']['RW_Property']['Strobe_1'].append("RO")
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_1']['Register_Field_Split_No_2'] = {}
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_1']['Register_Field_Split_No_2']['GenPartialBitRange'] = "14:8"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_1']['Register_Field_Split_No_2']['GenFieldReset'] = "7'd0"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_1']['Register_Field_Split_No_2']['GenPStrbIndex'] = "1"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_1']['Register_Field_Split_No_2']['RW_Property'] = []
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_1']['Register_Field_Split_No_2']['RW_Property'].append("RO")
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_1']['Common_Config']['RW_Property'].append("RO")
RegSpec['RegSpec_Test']['Register_No_1']['Common_Config']['RW_Property']['Strobe_1'].append("RO")
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_1']['Register_Field_Split_No_3'] = {}
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_1']['Register_Field_Split_No_3']['GenPartialBitRange'] = "7:1"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_1']['Register_Field_Split_No_3']['GenFieldReset'] = "7'd0"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_1']['Register_Field_Split_No_3']['GenPStrbIndex'] = "0"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_1']['Register_Field_Split_No_3']['RW_Property'] = []
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_1']['Register_Field_Split_No_3']['RW_Property'].append("RO")
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_1']['Common_Config']['RW_Property'].append("RO")
RegSpec['RegSpec_Test']['Register_No_1']['Common_Config']['RW_Property']['Strobe_0'].append("RO")
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_4'] = {}
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_4']['Common_Config'] = {}
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_4']['Common_Config']['GenRegField'] = "EN"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_4']['Common_Config']['Field_Desciption'] = """UART enable.
0 : Disable
1  :Enable"""
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_4']['Common_Config']['RW_Property'] = []
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_4']['Register_Field_Split_No_1'] = {}
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_4']['Register_Field_Split_No_1']['GenPartialBitRange'] = "0"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_4']['Register_Field_Split_No_1']['GenFieldReset'] = "1'b0"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_4']['Register_Field_Split_No_1']['GenPStrbIndex'] = "0"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_4']['Register_Field_Split_No_1']['RW_Property'] = []
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_4']['Register_Field_Split_No_1']['RW_Property'].append("RW")
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_4']['Common_Config']['RW_Property'].append("RW")
RegSpec['RegSpec_Test']['Register_No_1']['Common_Config']['RW_Property']['Strobe_0'].append("RW")
