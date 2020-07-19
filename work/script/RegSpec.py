RegSpec = {}
RegSpec['GenUserHeader'] = """
//Version: 1.0
//Description: Register specification of VG
//
//"""
RegSpec['RegSpec_Test'] = {}
RegSpec['RegSpec_Test']['Common_Config'] = {}
RegSpec['RegSpec_Test']['Common_Config']['GenRDataOR'] = []
RegSpec['RegSpec_Test']['Common_Config']['GenModuleName'] = "ExampleCsr"
RegSpec['RegSpec_Test']['Common_Config']['Interface'] = "APB4"
RegSpec['RegSpec_Test']['Common_Config']['GenDataParam'] = "32"
RegSpec['RegSpec_Test']['Common_Config']['GenAddrParam'] = "16"
RegSpec['RegSpec_Test']['Common_Config']['GenAsyncReset'] = "1"
RegSpec['RegSpec_Test']['Common_Config']['GenSyncReset'] = "0"
RegSpec['RegSpec_Test']['Common_Config']['GenAsyncParam'] = "1"
RegSpec['RegSpec_Test']['Common_Config']['GenSyncStageParam'] = "3"
RegSpec['RegSpec_Test']['Common_Config']['GenWProtParam'] = "1"
RegSpec['RegSpec_Test']['Common_Config']['GenSecParam'] = "1"
RegSpec['RegSpec_Test']['Common_Config']['GenWProtErrParam'] = "1"
RegSpec['RegSpec_Test']['Common_Config']['GenSecErrParam'] = "1"
RegSpec['RegSpec_Test']['Register_No_1'] = {}
RegSpec['RegSpec_Test']['Register_No_1']['Common_Config'] = {}
RegSpec['RegSpec_Test']['Register_No_1']['Common_Config']['GenRegName'] = "ACTRL"
RegSpec['RegSpec_Test']['Register_No_1']['Common_Config']['Register_Description'] = "A control register"
RegSpec['RegSpec_Test']['Register_No_1']['Common_Config']['GenRegOffsetParam'] = "16'h0000"
RegSpec['RegSpec_Test']['Common_Config']['GenRDataOR'].append("ACTRL_rvalue")
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
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_1']['Common_Config']['Ful_BitRange'] = []
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_1']['Register_Field_Split_No_1'] = {}
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_1']['Register_Field_Split_No_1']['GenPartialBitRange'] = "31:28"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_1']['Register_Field_Split_No_1']['GenFieldReset'] = "4'd0"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_1']['Register_Field_Split_No_1']['GenPStrbIndex'] = "3"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_1']['Common_Config']['Ful_BitRange'].append(31)
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_1']['Common_Config']['Ful_BitRange'].append(28)
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_1']['Register_Field_Split_No_1']['RW_Property'] = []
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_1']['Register_Field_Split_No_1']['RW_Property'].append("RO")
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_1']['Common_Config']['RW_Property'].append("RO")
RegSpec['RegSpec_Test']['Register_No_1']['Common_Config']['RW_Property']['Strobe_3'].append("RO")
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_2'] = {}
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_2']['Common_Config'] = {}
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_2']['Common_Config']['GenRegField'] = "BAUND1"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_2']['Common_Config']['Field_Desciption'] = """Baud rate 1"""
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_2']['Common_Config']['RW_Property'] = []
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_2']['Common_Config']['Ful_BitRange'] = []
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_2']['Register_Field_Split_No_1'] = {}
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_2']['Register_Field_Split_No_1']['GenPartialBitRange'] = "27:24"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_2']['Register_Field_Split_No_1']['GenFieldReset'] = "4'b0000"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_2']['Register_Field_Split_No_1']['GenPStrbIndex'] = "3"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_2']['Common_Config']['Ful_BitRange'].append(27)
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_2']['Common_Config']['Ful_BitRange'].append(24)
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
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_2']['Common_Config']['Ful_BitRange'].append(23)
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_2']['Common_Config']['Ful_BitRange'].append(16)
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_2']['Register_Field_Split_No_2']['RW_Property'] = []
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_2']['Register_Field_Split_No_2']['RW_Property'].append("RW")
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_2']['Common_Config']['RW_Property'].append("RW")
RegSpec['RegSpec_Test']['Register_No_1']['Common_Config']['RW_Property']['Strobe_2'].append("RW")
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_2']['Register_Field_Split_No_2']['RW_Property'].append("POW1")
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_2']['Common_Config']['RW_Property'].append("POW1")
RegSpec['RegSpec_Test']['Register_No_1']['Common_Config']['RW_Property']['Strobe_2'].append("POW1")
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_3'] = {}
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_3']['Common_Config'] = {}
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_3']['Common_Config']['GenRegField'] = "BAUND0"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_3']['Common_Config']['Field_Desciption'] = """Baud rate 0"""
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_3']['Common_Config']['RW_Property'] = []
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_3']['Common_Config']['Ful_BitRange'] = []
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_3']['Register_Field_Split_No_1'] = {}
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_3']['Register_Field_Split_No_1']['GenPartialBitRange'] = "15:10"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_3']['Register_Field_Split_No_1']['GenFieldReset'] = "6'd0"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_3']['Register_Field_Split_No_1']['GenPStrbIndex'] = "1"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_3']['Common_Config']['Ful_BitRange'].append(15)
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_3']['Common_Config']['Ful_BitRange'].append(10)
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_3']['Register_Field_Split_No_1']['RW_Property'] = []
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_3']['Register_Field_Split_No_1']['RW_Property'].append("RW")
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_3']['Common_Config']['RW_Property'].append("RW")
RegSpec['RegSpec_Test']['Register_No_1']['Common_Config']['RW_Property']['Strobe_1'].append("RW")
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_3']['Register_Field_Split_No_1']['RW_Property'].append("POW0")
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_3']['Common_Config']['RW_Property'].append("POW0")
RegSpec['RegSpec_Test']['Register_No_1']['Common_Config']['RW_Property']['Strobe_1'].append("POW0")
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_4'] = {}
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_4']['Common_Config'] = {}
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_4']['Common_Config']['GenRegField'] = "RW_W0S"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_4']['Common_Config']['Field_Desciption'] = """Test RW_W0S"""
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_4']['Common_Config']['RW_Property'] = []
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_4']['Common_Config']['Ful_BitRange'] = []
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_4']['Register_Field_Split_No_1'] = {}
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_4']['Register_Field_Split_No_1']['GenPartialBitRange'] = "9"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_4']['Register_Field_Split_No_1']['GenFieldReset'] = "1'b0"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_4']['Register_Field_Split_No_1']['GenPStrbIndex'] = "1"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_4']['Common_Config']['Ful_BitRange'].append(9)
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_4']['Common_Config']['Ful_BitRange'].append(9)
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_4']['Register_Field_Split_No_1']['RW_Property'] = []
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_4']['Register_Field_Split_No_1']['RW_Property'].append("RW_W0S")
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_4']['Common_Config']['RW_Property'].append("RW_W0S")
RegSpec['RegSpec_Test']['Register_No_1']['Common_Config']['RW_Property']['Strobe_1'].append("RW_W0S")
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_5'] = {}
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_5']['Common_Config'] = {}
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_5']['Common_Config']['GenRegField'] = "RW_W1S"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_5']['Common_Config']['Field_Desciption'] = """Test RW_W1S"""
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_5']['Common_Config']['RW_Property'] = []
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_5']['Common_Config']['Ful_BitRange'] = []
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_5']['Register_Field_Split_No_1'] = {}
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_5']['Register_Field_Split_No_1']['GenPartialBitRange'] = "8"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_5']['Register_Field_Split_No_1']['GenFieldReset'] = "1'b0"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_5']['Register_Field_Split_No_1']['GenPStrbIndex'] = "1"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_5']['Common_Config']['Ful_BitRange'].append(8)
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_5']['Common_Config']['Ful_BitRange'].append(8)
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_5']['Register_Field_Split_No_1']['RW_Property'] = []
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_5']['Register_Field_Split_No_1']['RW_Property'].append("RW_W1S")
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_5']['Common_Config']['RW_Property'].append("RW_W1S")
RegSpec['RegSpec_Test']['Register_No_1']['Common_Config']['RW_Property']['Strobe_1'].append("RW_W1S")
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_6'] = {}
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_6']['Common_Config'] = {}
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_6']['Common_Config']['GenRegField'] = "RW_W0C"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_6']['Common_Config']['Field_Desciption'] = """Test RW_W0C"""
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_6']['Common_Config']['RW_Property'] = []
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_6']['Common_Config']['Ful_BitRange'] = []
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_6']['Register_Field_Split_No_1'] = {}
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_6']['Register_Field_Split_No_1']['GenPartialBitRange'] = "7"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_6']['Register_Field_Split_No_1']['GenFieldReset'] = "1'b0"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_6']['Register_Field_Split_No_1']['GenPStrbIndex'] = "0"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_6']['Common_Config']['Ful_BitRange'].append(7)
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_6']['Common_Config']['Ful_BitRange'].append(7)
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_6']['Register_Field_Split_No_1']['RW_Property'] = []
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_6']['Register_Field_Split_No_1']['RW_Property'].append("RW_W0C")
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_6']['Common_Config']['RW_Property'].append("RW_W0C")
RegSpec['RegSpec_Test']['Register_No_1']['Common_Config']['RW_Property']['Strobe_0'].append("RW_W0C")
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_7'] = {}
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_7']['Common_Config'] = {}
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_7']['Common_Config']['GenRegField'] = "RW_W1C"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_7']['Common_Config']['Field_Desciption'] = """Test RW_W1C"""
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_7']['Common_Config']['RW_Property'] = []
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_7']['Common_Config']['Ful_BitRange'] = []
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_7']['Register_Field_Split_No_1'] = {}
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_7']['Register_Field_Split_No_1']['GenPartialBitRange'] = "6"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_7']['Register_Field_Split_No_1']['GenFieldReset'] = "1'b0"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_7']['Register_Field_Split_No_1']['GenPStrbIndex'] = "0"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_7']['Common_Config']['Ful_BitRange'].append(6)
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_7']['Common_Config']['Ful_BitRange'].append(6)
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_7']['Register_Field_Split_No_1']['RW_Property'] = []
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_7']['Register_Field_Split_No_1']['RW_Property'].append("RW_W1C")
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_7']['Common_Config']['RW_Property'].append("RW_W1C")
RegSpec['RegSpec_Test']['Register_No_1']['Common_Config']['RW_Property']['Strobe_0'].append("RW_W1C")
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_8'] = {}
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_8']['Common_Config'] = {}
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_8']['Common_Config']['GenRegField'] = "RW_WS"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_8']['Common_Config']['Field_Desciption'] = """Test RW_WS"""
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_8']['Common_Config']['RW_Property'] = []
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_8']['Common_Config']['Ful_BitRange'] = []
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_8']['Register_Field_Split_No_1'] = {}
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_8']['Register_Field_Split_No_1']['GenPartialBitRange'] = "5"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_8']['Register_Field_Split_No_1']['GenFieldReset'] = "1'b0"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_8']['Register_Field_Split_No_1']['GenPStrbIndex'] = "0"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_8']['Common_Config']['Ful_BitRange'].append(5)
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_8']['Common_Config']['Ful_BitRange'].append(5)
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_8']['Register_Field_Split_No_1']['RW_Property'] = []
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_8']['Register_Field_Split_No_1']['RW_Property'].append("RW_WS")
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_8']['Common_Config']['RW_Property'].append("RW_WS")
RegSpec['RegSpec_Test']['Register_No_1']['Common_Config']['RW_Property']['Strobe_0'].append("RW_WS")
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_9'] = {}
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_9']['Common_Config'] = {}
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_9']['Common_Config']['GenRegField'] = "RW_WC"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_9']['Common_Config']['Field_Desciption'] = """Test RW_WC"""
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_9']['Common_Config']['RW_Property'] = []
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_9']['Common_Config']['Ful_BitRange'] = []
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_9']['Register_Field_Split_No_1'] = {}
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_9']['Register_Field_Split_No_1']['GenPartialBitRange'] = "4"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_9']['Register_Field_Split_No_1']['GenFieldReset'] = "1'b0"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_9']['Register_Field_Split_No_1']['GenPStrbIndex'] = "0"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_9']['Common_Config']['Ful_BitRange'].append(4)
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_9']['Common_Config']['Ful_BitRange'].append(4)
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_9']['Register_Field_Split_No_1']['RW_Property'] = []
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_9']['Register_Field_Split_No_1']['RW_Property'].append("RW_WC")
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_9']['Common_Config']['RW_Property'].append("RW_WC")
RegSpec['RegSpec_Test']['Register_No_1']['Common_Config']['RW_Property']['Strobe_0'].append("RW_WC")
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_10'] = {}
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_10']['Common_Config'] = {}
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_10']['Common_Config']['GenRegField'] = "RW_RS"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_10']['Common_Config']['Field_Desciption'] = """Test RW_RS"""
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_10']['Common_Config']['RW_Property'] = []
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_10']['Common_Config']['Ful_BitRange'] = []
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_10']['Register_Field_Split_No_1'] = {}
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_10']['Register_Field_Split_No_1']['GenPartialBitRange'] = "3"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_10']['Register_Field_Split_No_1']['GenFieldReset'] = "1'b0"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_10']['Register_Field_Split_No_1']['GenPStrbIndex'] = "0"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_10']['Common_Config']['Ful_BitRange'].append(3)
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_10']['Common_Config']['Ful_BitRange'].append(3)
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_10']['Register_Field_Split_No_1']['RW_Property'] = []
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_10']['Register_Field_Split_No_1']['RW_Property'].append("RW_RS")
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_10']['Common_Config']['RW_Property'].append("RW_RS")
RegSpec['RegSpec_Test']['Register_No_1']['Common_Config']['RW_Property']['Strobe_0'].append("RW_RS")
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_11'] = {}
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_11']['Common_Config'] = {}
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_11']['Common_Config']['GenRegField'] = "RW_RC"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_11']['Common_Config']['Field_Desciption'] = """Test RW_RC"""
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_11']['Common_Config']['RW_Property'] = []
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_11']['Common_Config']['Ful_BitRange'] = []
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_11']['Register_Field_Split_No_1'] = {}
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_11']['Register_Field_Split_No_1']['GenPartialBitRange'] = "2"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_11']['Register_Field_Split_No_1']['GenFieldReset'] = "1'b0"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_11']['Register_Field_Split_No_1']['GenPStrbIndex'] = "0"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_11']['Common_Config']['Ful_BitRange'].append(2)
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_11']['Common_Config']['Ful_BitRange'].append(2)
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_11']['Register_Field_Split_No_1']['RW_Property'] = []
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_11']['Register_Field_Split_No_1']['RW_Property'].append("RW_RC")
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_11']['Common_Config']['RW_Property'].append("RW_RC")
RegSpec['RegSpec_Test']['Register_No_1']['Common_Config']['RW_Property']['Strobe_0'].append("RW_RC")
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_12'] = {}
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_12']['Common_Config'] = {}
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_12']['Common_Config']['GenRegField'] = "RWI"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_12']['Common_Config']['Field_Desciption'] = """Test RWI"""
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_12']['Common_Config']['RW_Property'] = []
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_12']['Common_Config']['Ful_BitRange'] = []
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_12']['Register_Field_Split_No_1'] = {}
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_12']['Register_Field_Split_No_1']['GenPartialBitRange'] = "1"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_12']['Register_Field_Split_No_1']['GenFieldReset'] = "1'b0"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_12']['Register_Field_Split_No_1']['GenPStrbIndex'] = "0"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_12']['Common_Config']['Ful_BitRange'].append(1)
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_12']['Common_Config']['Ful_BitRange'].append(1)
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_12']['Register_Field_Split_No_1']['RW_Property'] = []
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_12']['Register_Field_Split_No_1']['RW_Property'].append("RWI")
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_12']['Common_Config']['RW_Property'].append("RWI")
RegSpec['RegSpec_Test']['Register_No_1']['Common_Config']['RW_Property']['Strobe_0'].append("RWI")
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_13'] = {}
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_13']['Common_Config'] = {}
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_13']['Common_Config']['GenRegField'] = "RW"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_13']['Common_Config']['Field_Desciption'] = """Test RW"""
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_13']['Common_Config']['RW_Property'] = []
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_13']['Common_Config']['Ful_BitRange'] = []
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_13']['Register_Field_Split_No_1'] = {}
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_13']['Register_Field_Split_No_1']['GenPartialBitRange'] = "0"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_13']['Register_Field_Split_No_1']['GenFieldReset'] = "1'b0"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_13']['Register_Field_Split_No_1']['GenPStrbIndex'] = "0"
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_13']['Common_Config']['Ful_BitRange'].append(0)
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_13']['Common_Config']['Ful_BitRange'].append(0)
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_13']['Register_Field_Split_No_1']['RW_Property'] = []
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_13']['Register_Field_Split_No_1']['RW_Property'].append("RW")
RegSpec['RegSpec_Test']['Register_No_1']['Register_Field_No_13']['Common_Config']['RW_Property'].append("RW")
RegSpec['RegSpec_Test']['Register_No_1']['Common_Config']['RW_Property']['Strobe_0'].append("RW")
RegSpec['RegSpec_Test']['Register_No_2'] = {}
RegSpec['RegSpec_Test']['Register_No_2']['Common_Config'] = {}
RegSpec['RegSpec_Test']['Register_No_2']['Common_Config']['GenRegName'] = "BCTRL"
RegSpec['RegSpec_Test']['Register_No_2']['Common_Config']['Register_Description'] = "B control register"
RegSpec['RegSpec_Test']['Register_No_2']['Common_Config']['GenRegOffsetParam'] = "16'h0004"
RegSpec['RegSpec_Test']['Common_Config']['GenRDataOR'].append("BCTRL_rvalue")
RegSpec['RegSpec_Test']['Register_No_2']['Common_Config']['RW_Property'] = {}
RegSpec['RegSpec_Test']['Register_No_2']['Common_Config']['RW_Property']['Strobe_0'] = []
RegSpec['RegSpec_Test']['Register_No_2']['Common_Config']['RW_Property']['Strobe_1'] = []
RegSpec['RegSpec_Test']['Register_No_2']['Common_Config']['RW_Property']['Strobe_2'] = []
RegSpec['RegSpec_Test']['Register_No_2']['Common_Config']['RW_Property']['Strobe_3'] = []
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_1'] = {}
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_1']['Common_Config'] = {}
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_1']['Common_Config']['GenRegField'] = "RESERVED"
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_1']['Common_Config']['Field_Desciption'] = """Reserved
Read as zeros"""
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_1']['Common_Config']['RW_Property'] = []
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_1']['Common_Config']['Ful_BitRange'] = []
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_1']['Register_Field_Split_No_1'] = {}
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_1']['Register_Field_Split_No_1']['GenPartialBitRange'] = "31:28"
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_1']['Register_Field_Split_No_1']['GenFieldReset'] = "4'd0"
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_1']['Register_Field_Split_No_1']['GenPStrbIndex'] = "3"
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_1']['Common_Config']['Ful_BitRange'].append(31)
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_1']['Common_Config']['Ful_BitRange'].append(28)
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_1']['Register_Field_Split_No_1']['RW_Property'] = []
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_1']['Register_Field_Split_No_1']['RW_Property'].append("RO")
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_1']['Common_Config']['RW_Property'].append("RO")
RegSpec['RegSpec_Test']['Register_No_2']['Common_Config']['RW_Property']['Strobe_3'].append("RO")
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_2'] = {}
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_2']['Common_Config'] = {}
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_2']['Common_Config']['GenRegField'] = "BAUND3"
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_2']['Common_Config']['Field_Desciption'] = """Baud rate 3"""
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_2']['Common_Config']['RW_Property'] = []
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_2']['Common_Config']['Ful_BitRange'] = []
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_2']['Register_Field_Split_No_1'] = {}
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_2']['Register_Field_Split_No_1']['GenPartialBitRange'] = "27:24"
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_2']['Register_Field_Split_No_1']['GenFieldReset'] = "4'b0000"
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_2']['Register_Field_Split_No_1']['GenPStrbIndex'] = "3"
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_2']['Common_Config']['Ful_BitRange'].append(27)
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_2']['Common_Config']['Ful_BitRange'].append(24)
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_2']['Register_Field_Split_No_1']['RW_Property'] = []
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_2']['Register_Field_Split_No_1']['RW_Property'].append("RW")
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_2']['Common_Config']['RW_Property'].append("RW")
RegSpec['RegSpec_Test']['Register_No_2']['Common_Config']['RW_Property']['Strobe_3'].append("RW")
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_2']['Register_Field_Split_No_1']['RW_Property'].append("POR")
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_2']['Common_Config']['RW_Property'].append("POR")
RegSpec['RegSpec_Test']['Register_No_2']['Common_Config']['RW_Property']['Strobe_3'].append("POR")
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_2']['Register_Field_Split_No_2'] = {}
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_2']['Register_Field_Split_No_2']['GenPartialBitRange'] = "23:16"
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_2']['Register_Field_Split_No_2']['GenFieldReset'] = "8'hff"
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_2']['Register_Field_Split_No_2']['GenPStrbIndex'] = "2"
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_2']['Common_Config']['Ful_BitRange'].append(23)
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_2']['Common_Config']['Ful_BitRange'].append(16)
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_2']['Register_Field_Split_No_2']['RW_Property'] = []
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_2']['Register_Field_Split_No_2']['RW_Property'].append("RW")
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_2']['Common_Config']['RW_Property'].append("RW")
RegSpec['RegSpec_Test']['Register_No_2']['Common_Config']['RW_Property']['Strobe_2'].append("RW")
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_2']['Register_Field_Split_No_2']['RW_Property'].append("POR")
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_2']['Common_Config']['RW_Property'].append("POR")
RegSpec['RegSpec_Test']['Register_No_2']['Common_Config']['RW_Property']['Strobe_2'].append("POR")
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_3'] = {}
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_3']['Common_Config'] = {}
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_3']['Common_Config']['GenRegField'] = "BAUND2"
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_3']['Common_Config']['Field_Desciption'] = """Baud rate 2"""
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_3']['Common_Config']['RW_Property'] = []
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_3']['Common_Config']['Ful_BitRange'] = []
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_3']['Register_Field_Split_No_1'] = {}
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_3']['Register_Field_Split_No_1']['GenPartialBitRange'] = "15:8"
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_3']['Register_Field_Split_No_1']['GenFieldReset'] = "8'd0"
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_3']['Register_Field_Split_No_1']['GenPStrbIndex'] = "1"
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_3']['Common_Config']['Ful_BitRange'].append(8)
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_3']['Common_Config']['Ful_BitRange'].append(15)
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_3']['Register_Field_Split_No_1']['RW_Property'] = []
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_3']['Register_Field_Split_No_1']['RW_Property'].append("RW")
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_3']['Common_Config']['RW_Property'].append("RW")
RegSpec['RegSpec_Test']['Register_No_2']['Common_Config']['RW_Property']['Strobe_1'].append("RW")
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_3']['Register_Field_Split_No_1']['RW_Property'].append("POW")
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_3']['Common_Config']['RW_Property'].append("POW")
RegSpec['RegSpec_Test']['Register_No_2']['Common_Config']['RW_Property']['Strobe_1'].append("POW")
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_4'] = {}
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_4']['Common_Config'] = {}
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_4']['Common_Config']['GenRegField'] = "WO1"
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_4']['Common_Config']['Field_Desciption'] = """Test WO1"""
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_4']['Common_Config']['RW_Property'] = []
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_4']['Common_Config']['Ful_BitRange'] = []
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_4']['Register_Field_Split_No_1'] = {}
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_4']['Register_Field_Split_No_1']['GenPartialBitRange'] = "7"
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_4']['Register_Field_Split_No_1']['GenFieldReset'] = "1'b0"
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_4']['Register_Field_Split_No_1']['GenPStrbIndex'] = "0"
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_4']['Common_Config']['Ful_BitRange'].append(7)
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_4']['Common_Config']['Ful_BitRange'].append(7)
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_4']['Register_Field_Split_No_1']['RW_Property'] = []
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_4']['Register_Field_Split_No_1']['RW_Property'].append("WO1")
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_4']['Common_Config']['RW_Property'].append("WO1")
RegSpec['RegSpec_Test']['Register_No_2']['Common_Config']['RW_Property']['Strobe_0'].append("WO1")
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_5'] = {}
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_5']['Common_Config'] = {}
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_5']['Common_Config']['GenRegField'] = "WO0"
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_5']['Common_Config']['Field_Desciption'] = """Test WO0"""
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_5']['Common_Config']['RW_Property'] = []
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_5']['Common_Config']['Ful_BitRange'] = []
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_5']['Register_Field_Split_No_1'] = {}
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_5']['Register_Field_Split_No_1']['GenPartialBitRange'] = "6"
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_5']['Register_Field_Split_No_1']['GenFieldReset'] = "1'b0"
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_5']['Register_Field_Split_No_1']['GenPStrbIndex'] = "0"
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_5']['Common_Config']['Ful_BitRange'].append(6)
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_5']['Common_Config']['Ful_BitRange'].append(6)
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_5']['Register_Field_Split_No_1']['RW_Property'] = []
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_5']['Register_Field_Split_No_1']['RW_Property'].append("WO0")
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_5']['Common_Config']['RW_Property'].append("WO0")
RegSpec['RegSpec_Test']['Register_No_2']['Common_Config']['RW_Property']['Strobe_0'].append("WO0")
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_6'] = {}
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_6']['Common_Config'] = {}
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_6']['Common_Config']['GenRegField'] = "WOS"
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_6']['Common_Config']['Field_Desciption'] = """Test WOS"""
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_6']['Common_Config']['RW_Property'] = []
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_6']['Common_Config']['Ful_BitRange'] = []
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_6']['Register_Field_Split_No_1'] = {}
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_6']['Register_Field_Split_No_1']['GenPartialBitRange'] = "5"
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_6']['Register_Field_Split_No_1']['GenFieldReset'] = "1'b0"
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_6']['Register_Field_Split_No_1']['GenPStrbIndex'] = "0"
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_6']['Common_Config']['Ful_BitRange'].append(5)
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_6']['Common_Config']['Ful_BitRange'].append(5)
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_6']['Register_Field_Split_No_1']['RW_Property'] = []
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_6']['Register_Field_Split_No_1']['RW_Property'].append("WOS")
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_6']['Common_Config']['RW_Property'].append("WOS")
RegSpec['RegSpec_Test']['Register_No_2']['Common_Config']['RW_Property']['Strobe_0'].append("WOS")
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_7'] = {}
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_7']['Common_Config'] = {}
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_7']['Common_Config']['GenRegField'] = "WOC"
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_7']['Common_Config']['Field_Desciption'] = """Test WOC"""
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_7']['Common_Config']['RW_Property'] = []
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_7']['Common_Config']['Ful_BitRange'] = []
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_7']['Register_Field_Split_No_1'] = {}
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_7']['Register_Field_Split_No_1']['GenPartialBitRange'] = "4"
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_7']['Register_Field_Split_No_1']['GenFieldReset'] = "1'b0"
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_7']['Register_Field_Split_No_1']['GenPStrbIndex'] = "0"
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_7']['Common_Config']['Ful_BitRange'].append(4)
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_7']['Common_Config']['Ful_BitRange'].append(4)
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_7']['Register_Field_Split_No_1']['RW_Property'] = []
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_7']['Register_Field_Split_No_1']['RW_Property'].append("WOC")
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_7']['Common_Config']['RW_Property'].append("WOC")
RegSpec['RegSpec_Test']['Register_No_2']['Common_Config']['RW_Property']['Strobe_0'].append("WOC")
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_8'] = {}
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_8']['Common_Config'] = {}
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_8']['Common_Config']['GenRegField'] = "WO"
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_8']['Common_Config']['Field_Desciption'] = """Test WO"""
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_8']['Common_Config']['RW_Property'] = []
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_8']['Common_Config']['Ful_BitRange'] = []
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_8']['Register_Field_Split_No_1'] = {}
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_8']['Register_Field_Split_No_1']['GenPartialBitRange'] = "3"
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_8']['Register_Field_Split_No_1']['GenFieldReset'] = "1'b0"
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_8']['Register_Field_Split_No_1']['GenPStrbIndex'] = "0"
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_8']['Common_Config']['Ful_BitRange'].append(3)
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_8']['Common_Config']['Ful_BitRange'].append(3)
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_8']['Register_Field_Split_No_1']['RW_Property'] = []
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_8']['Register_Field_Split_No_1']['RW_Property'].append("WO")
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_8']['Common_Config']['RW_Property'].append("WO")
RegSpec['RegSpec_Test']['Register_No_2']['Common_Config']['RW_Property']['Strobe_0'].append("WO")
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_9'] = {}
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_9']['Common_Config'] = {}
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_9']['Common_Config']['GenRegField'] = "ROS"
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_9']['Common_Config']['Field_Desciption'] = """Test ROS"""
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_9']['Common_Config']['RW_Property'] = []
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_9']['Common_Config']['Ful_BitRange'] = []
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_9']['Register_Field_Split_No_1'] = {}
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_9']['Register_Field_Split_No_1']['GenPartialBitRange'] = "2"
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_9']['Register_Field_Split_No_1']['GenFieldReset'] = "1'b0"
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_9']['Register_Field_Split_No_1']['GenPStrbIndex'] = "0"
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_9']['Common_Config']['Ful_BitRange'].append(2)
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_9']['Common_Config']['Ful_BitRange'].append(2)
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_9']['Register_Field_Split_No_1']['RW_Property'] = []
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_9']['Register_Field_Split_No_1']['RW_Property'].append("ROS")
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_9']['Common_Config']['RW_Property'].append("ROS")
RegSpec['RegSpec_Test']['Register_No_2']['Common_Config']['RW_Property']['Strobe_0'].append("ROS")
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_10'] = {}
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_10']['Common_Config'] = {}
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_10']['Common_Config']['GenRegField'] = "ROC"
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_10']['Common_Config']['Field_Desciption'] = """Test ROC"""
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_10']['Common_Config']['RW_Property'] = []
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_10']['Common_Config']['Ful_BitRange'] = []
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_10']['Register_Field_Split_No_1'] = {}
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_10']['Register_Field_Split_No_1']['GenPartialBitRange'] = "1"
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_10']['Register_Field_Split_No_1']['GenFieldReset'] = "1'b0"
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_10']['Register_Field_Split_No_1']['GenPStrbIndex'] = "0"
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_10']['Common_Config']['Ful_BitRange'].append(1)
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_10']['Common_Config']['Ful_BitRange'].append(1)
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_10']['Register_Field_Split_No_1']['RW_Property'] = []
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_10']['Register_Field_Split_No_1']['RW_Property'].append("ROC")
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_10']['Common_Config']['RW_Property'].append("ROC")
RegSpec['RegSpec_Test']['Register_No_2']['Common_Config']['RW_Property']['Strobe_0'].append("ROC")
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_11'] = {}
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_11']['Common_Config'] = {}
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_11']['Common_Config']['GenRegField'] = "RO"
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_11']['Common_Config']['Field_Desciption'] = """Test RO"""
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_11']['Common_Config']['RW_Property'] = []
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_11']['Common_Config']['Ful_BitRange'] = []
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_11']['Register_Field_Split_No_1'] = {}
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_11']['Register_Field_Split_No_1']['GenPartialBitRange'] = "0"
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_11']['Register_Field_Split_No_1']['GenFieldReset'] = "1'b0"
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_11']['Register_Field_Split_No_1']['GenPStrbIndex'] = "0"
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_11']['Common_Config']['Ful_BitRange'].append(0)
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_11']['Common_Config']['Ful_BitRange'].append(0)
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_11']['Register_Field_Split_No_1']['RW_Property'] = []
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_11']['Register_Field_Split_No_1']['RW_Property'].append("RO")
RegSpec['RegSpec_Test']['Register_No_2']['Register_Field_No_11']['Common_Config']['RW_Property'].append("RO")
RegSpec['RegSpec_Test']['Register_No_2']['Common_Config']['RW_Property']['Strobe_0'].append("RO")
