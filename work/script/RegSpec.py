RegSpec = {}
RegSpec['Common_Info'] = """Version: 1.0
Description: Register specification of VG

"""
RegSpec['RegSpec_Example'] = {}
RegSpec['RegSpec_Example']['Common_Config'] = {}
RegSpec['RegSpec_Example']['Common_Config']['Gen'] = "Yes/No"
RegSpec['RegSpec_Example']['Common_Config']['Module_Name'] = "ExampleCsr"
RegSpec['RegSpec_Example']['Common_Config']['Interface'] = "APB4"
RegSpec['RegSpec_Example']['Common_Config']['DataWidth'] = "32"
RegSpec['RegSpec_Example']['Common_Config']['AddrWidth'] = "16"
RegSpec['RegSpec_Example']['Common_Config']['Reset'] = "Async/Sync"
RegSpec['RegSpec_Example']['Common_Config']['Synchronization'] = "Async/Sync"
RegSpec['RegSpec_Example']['Common_Config']['SynchronousStage'] = "2/3"
RegSpec['RegSpec_Example']['Common_Config']['Write_Protection'] = "No/Yes"
RegSpec['RegSpec_Example']['Common_Config']['Secure'] = "No/Yes"
RegSpec['RegSpec_Example']['Common_Config']['SlaveError'] = "WProt/Sec"
RegSpec['RegSpec_Example']['Register_No_1'] = {}
RegSpec['RegSpec_Example']['Register_No_1']['Common_Config'] = {}
RegSpec['RegSpec_Example']['Register_No_1']['Common_Config']['Generate_Flag'] = "Gen/-"
RegSpec['RegSpec_Example']['Register_No_1']['Common_Config']['Register_Name'] = "ACTRL"
RegSpec['RegSpec_Example']['Register_No_1']['Common_Config']['Register_Description'] = "A control register"
RegSpec['RegSpec_Example']['Register_No_1']['Common_Config']['Initial_Value'] = "16'h0000"
RegSpec['RegSpec_Example']['Register_No_1']['Common_Config']['RW_Property'] = {}
RegSpec['RegSpec_Example']['Register_No_1']['Common_Config']['RW_Property']['Strobe_0'] = []
RegSpec['RegSpec_Example']['Register_No_1']['Common_Config']['RW_Property']['Strobe_1'] = []
RegSpec['RegSpec_Example']['Register_No_1']['Common_Config']['RW_Property']['Strobe_2'] = []
RegSpec['RegSpec_Example']['Register_No_1']['Common_Config']['RW_Property']['Strobe_3'] = []
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_1'] = {}
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_1']['Common_Config'] = {}
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_1']['Common_Config']['Field_Name'] = "RESERVED"
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_1']['Common_Config']['Field_Desciption'] = """Reserved
Read as zeros"""
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_1']['Register_Field_Split_No_1'] = {}
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_1']['Register_Field_Split_No_1']['Bit_Range'] = "31:28"
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_1']['Register_Field_Split_No_1']['Reset_Value'] = "4'd0"
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_1']['Register_Field_Split_No_1']['Strobe_Index'] = "3"
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_1']['Register_Field_Split_No_1']['RW_Property'] = []
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_1']['Register_Field_Split_No_1']['RW_Property'].append("RO")
RegSpec['RegSpec_Example']['Register_No_1']['Common_Config']['RW_Property']['Strobe_3'].append("RO")
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_2'] = {}
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_2']['Common_Config'] = {}
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_2']['Common_Config']['Field_Name'] = "BAUND"
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_2']['Common_Config']['Field_Desciption'] = """Baud rate."""
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_2']['Register_Field_Split_No_1'] = {}
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_2']['Register_Field_Split_No_1']['Bit_Range'] = "27:24"
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_2']['Register_Field_Split_No_1']['Reset_Value'] = "4'b0000"
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_2']['Register_Field_Split_No_1']['Strobe_Index'] = "3"
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_2']['Register_Field_Split_No_1']['RW_Property'] = []
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_2']['Register_Field_Split_No_1']['RW_Property'].append("RW")
RegSpec['RegSpec_Example']['Register_No_1']['Common_Config']['RW_Property']['Strobe_3'].append("RW")
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_2']['Register_Field_Split_No_1']['RW_Property'].append("POW1")
RegSpec['RegSpec_Example']['Register_No_1']['Common_Config']['RW_Property']['Strobe_3'].append("POW1")
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_2']['Register_Field_Split_No_2'] = {}
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_2']['Register_Field_Split_No_2']['Bit_Range'] = "23:16"
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_2']['Register_Field_Split_No_2']['Reset_Value'] = "8'hff"
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_2']['Register_Field_Split_No_2']['Strobe_Index'] = "2"
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_2']['Register_Field_Split_No_2']['RW_Property'] = []
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_2']['Register_Field_Split_No_2']['RW_Property'].append("RW")
RegSpec['RegSpec_Example']['Register_No_1']['Common_Config']['RW_Property']['Strobe_2'].append("RW")
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_2']['Register_Field_Split_No_2']['RW_Property'].append("POW1")
RegSpec['RegSpec_Example']['Register_No_1']['Common_Config']['RW_Property']['Strobe_2'].append("POW1")
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_3'] = {}
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_3']['Common_Config'] = {}
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_3']['Common_Config']['Field_Name'] = "BUSY"
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_3']['Common_Config']['Field_Desciption'] = """UART busy.
0 : UART is idle
1 : UART is busy"""
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_3']['Register_Field_Split_No_1'] = {}
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_3']['Register_Field_Split_No_1']['Bit_Range'] = "15"
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_3']['Register_Field_Split_No_1']['Reset_Value'] = "1'b0"
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_3']['Register_Field_Split_No_1']['Strobe_Index'] = "1"
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_3']['Register_Field_Split_No_1']['RW_Property'] = []
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_3']['Register_Field_Split_No_1']['RW_Property'].append("RO")
RegSpec['RegSpec_Example']['Register_No_1']['Common_Config']['RW_Property']['Strobe_1'].append("RO")
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_4'] = {}
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_4']['Common_Config'] = {}
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_4']['Common_Config']['Field_Name'] = "RESERVED"
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_4']['Common_Config']['Field_Desciption'] = """Reserved
Read as zeros"""
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_4']['Register_Field_Split_No_1'] = {}
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_4']['Register_Field_Split_No_1']['Bit_Range'] = "14:8"
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_4']['Register_Field_Split_No_1']['Reset_Value'] = "7'd0"
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_4']['Register_Field_Split_No_1']['Strobe_Index'] = "1"
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_4']['Register_Field_Split_No_1']['RW_Property'] = []
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_4']['Register_Field_Split_No_1']['RW_Property'].append("RO")
RegSpec['RegSpec_Example']['Register_No_1']['Common_Config']['RW_Property']['Strobe_1'].append("RO")
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_4']['Register_Field_Split_No_2'] = {}
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_4']['Register_Field_Split_No_2']['Bit_Range'] = "7:1"
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_4']['Register_Field_Split_No_2']['Reset_Value'] = "7'd0"
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_4']['Register_Field_Split_No_2']['Strobe_Index'] = "0"
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_4']['Register_Field_Split_No_2']['RW_Property'] = []
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_4']['Register_Field_Split_No_2']['RW_Property'].append("RO")
RegSpec['RegSpec_Example']['Register_No_1']['Common_Config']['RW_Property']['Strobe_0'].append("RO")
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_5'] = {}
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_5']['Common_Config'] = {}
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_5']['Common_Config']['Field_Name'] = "EN"
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_5']['Common_Config']['Field_Desciption'] = """UART enable.
0 : Disable
1  :Enable"""
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_5']['Register_Field_Split_No_1'] = {}
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_5']['Register_Field_Split_No_1']['Bit_Range'] = "0"
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_5']['Register_Field_Split_No_1']['Reset_Value'] = "1'b0"
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_5']['Register_Field_Split_No_1']['Strobe_Index'] = "0"
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_5']['Register_Field_Split_No_1']['RW_Property'] = []
RegSpec['RegSpec_Example']['Register_No_1']['Register_Field_No_5']['Register_Field_Split_No_1']['RW_Property'].append("RW")
RegSpec['RegSpec_Example']['Register_No_1']['Common_Config']['RW_Property']['Strobe_0'].append("RW")
RegSpec['RegSpec_Example']['Register_No_2'] = {}
RegSpec['RegSpec_Example']['Register_No_2']['Common_Config'] = {}
RegSpec['RegSpec_Example']['Register_No_2']['Common_Config']['Generate_Flag'] = "Gen/-"
RegSpec['RegSpec_Example']['Register_No_2']['Common_Config']['Register_Name'] = "BCTRL"
RegSpec['RegSpec_Example']['Register_No_2']['Common_Config']['Register_Description'] = "B control register"
RegSpec['RegSpec_Example']['Register_No_2']['Common_Config']['Initial_Value'] = "16'h0004"
RegSpec['RegSpec_Example']['Register_No_2']['Common_Config']['RW_Property'] = {}
RegSpec['RegSpec_Example']['Register_No_2']['Common_Config']['RW_Property']['Strobe_0'] = []
RegSpec['RegSpec_Example']['Register_No_2']['Common_Config']['RW_Property']['Strobe_1'] = []
RegSpec['RegSpec_Example']['Register_No_2']['Common_Config']['RW_Property']['Strobe_2'] = []
RegSpec['RegSpec_Example']['Register_No_2']['Common_Config']['RW_Property']['Strobe_3'] = []
RegSpec['RegSpec_Example']['Register_No_2']['Register_Field_No_1'] = {}
RegSpec['RegSpec_Example']['Register_No_2']['Register_Field_No_1']['Common_Config'] = {}
RegSpec['RegSpec_Example']['Register_No_2']['Register_Field_No_1']['Common_Config']['Field_Name'] = "RESERVED"
RegSpec['RegSpec_Example']['Register_No_2']['Register_Field_No_1']['Common_Config']['Field_Desciption'] = """None"""
RegSpec['RegSpec_Example']['Register_No_2']['Register_Field_No_1']['Register_Field_Split_No_1'] = {}
RegSpec['RegSpec_Example']['Register_No_2']['Register_Field_No_1']['Register_Field_Split_No_1']['Bit_Range'] = "31:28"
RegSpec['RegSpec_Example']['Register_No_2']['Register_Field_No_1']['Register_Field_Split_No_1']['Reset_Value'] = "4'd0"
RegSpec['RegSpec_Example']['Register_No_2']['Register_Field_No_1']['Register_Field_Split_No_1']['Strobe_Index'] = "3"
RegSpec['RegSpec_Example']['Register_No_2']['Register_Field_No_1']['Register_Field_Split_No_1']['RW_Property'] = []
RegSpec['RegSpec_Example']['Register_No_2']['Register_Field_No_1']['Register_Field_Split_No_1']['RW_Property'].append("RO")
RegSpec['RegSpec_Example']['Register_No_2']['Common_Config']['RW_Property']['Strobe_3'].append("RO")
RegSpec['RegSpec_Example']['Register_No_2']['Register_Field_No_2'] = {}
RegSpec['RegSpec_Example']['Register_No_2']['Register_Field_No_2']['Common_Config'] = {}
RegSpec['RegSpec_Example']['Register_No_2']['Register_Field_No_2']['Common_Config']['Field_Name'] = "BAUND"
RegSpec['RegSpec_Example']['Register_No_2']['Register_Field_No_2']['Common_Config']['Field_Desciption'] = """None"""
RegSpec['RegSpec_Example']['Register_No_2']['Register_Field_No_2']['Register_Field_Split_No_1'] = {}
RegSpec['RegSpec_Example']['Register_No_2']['Register_Field_No_2']['Register_Field_Split_No_1']['Bit_Range'] = "27:24"
RegSpec['RegSpec_Example']['Register_No_2']['Register_Field_No_2']['Register_Field_Split_No_1']['Reset_Value'] = "4'b0000"
RegSpec['RegSpec_Example']['Register_No_2']['Register_Field_No_2']['Register_Field_Split_No_1']['Strobe_Index'] = "3"
RegSpec['RegSpec_Example']['Register_No_2']['Register_Field_No_2']['Register_Field_Split_No_1']['RW_Property'] = []
RegSpec['RegSpec_Example']['Register_No_2']['Register_Field_No_2']['Register_Field_Split_No_1']['RW_Property'].append("RW")
RegSpec['RegSpec_Example']['Register_No_2']['Common_Config']['RW_Property']['Strobe_3'].append("RW")
RegSpec['RegSpec_Example']['Register_No_2']['Register_Field_No_2']['Register_Field_Split_No_2'] = {}
RegSpec['RegSpec_Example']['Register_No_2']['Register_Field_No_2']['Register_Field_Split_No_2']['Bit_Range'] = "23:16"
RegSpec['RegSpec_Example']['Register_No_2']['Register_Field_No_2']['Register_Field_Split_No_2']['Reset_Value'] = "8'hff"
RegSpec['RegSpec_Example']['Register_No_2']['Register_Field_No_2']['Register_Field_Split_No_2']['Strobe_Index'] = "2"
RegSpec['RegSpec_Example']['Register_No_2']['Register_Field_No_2']['Register_Field_Split_No_2']['RW_Property'] = []
RegSpec['RegSpec_Example']['Register_No_2']['Register_Field_No_2']['Register_Field_Split_No_2']['RW_Property'].append("RW")
RegSpec['RegSpec_Example']['Register_No_2']['Common_Config']['RW_Property']['Strobe_2'].append("RW")
RegSpec['RegSpec_Example']['Register_No_2']['Register_Field_No_3'] = {}
RegSpec['RegSpec_Example']['Register_No_2']['Register_Field_No_3']['Common_Config'] = {}
RegSpec['RegSpec_Example']['Register_No_2']['Register_Field_No_3']['Common_Config']['Field_Name'] = "ABC2"
RegSpec['RegSpec_Example']['Register_No_2']['Register_Field_No_3']['Common_Config']['Field_Desciption'] = """None"""
RegSpec['RegSpec_Example']['Register_No_2']['Register_Field_No_3']['Register_Field_Split_No_1'] = {}
RegSpec['RegSpec_Example']['Register_No_2']['Register_Field_No_3']['Register_Field_Split_No_1']['Bit_Range'] = "7:3"
RegSpec['RegSpec_Example']['Register_No_2']['Register_Field_No_3']['Register_Field_Split_No_1']['Reset_Value'] = "3'b010"
RegSpec['RegSpec_Example']['Register_No_2']['Register_Field_No_3']['Register_Field_Split_No_1']['Strobe_Index'] = "0"
RegSpec['RegSpec_Example']['Register_No_2']['Register_Field_No_3']['Register_Field_Split_No_1']['RW_Property'] = []
RegSpec['RegSpec_Example']['Register_No_2']['Register_Field_No_3']['Register_Field_Split_No_1']['RW_Property'].append("RW_RS")
RegSpec['RegSpec_Example']['Register_No_2']['Common_Config']['RW_Property']['Strobe_0'].append("RW_RS")
RegSpec['RegSpec_Example']['Register_No_2']['Register_Field_No_4'] = {}
RegSpec['RegSpec_Example']['Register_No_2']['Register_Field_No_4']['Common_Config'] = {}
RegSpec['RegSpec_Example']['Register_No_2']['Register_Field_No_4']['Common_Config']['Field_Name'] = "ABC1"
RegSpec['RegSpec_Example']['Register_No_2']['Register_Field_No_4']['Common_Config']['Field_Desciption'] = """None"""
RegSpec['RegSpec_Example']['Register_No_2']['Register_Field_No_4']['Register_Field_Split_No_1'] = {}
RegSpec['RegSpec_Example']['Register_No_2']['Register_Field_No_4']['Register_Field_Split_No_1']['Bit_Range'] = "4:1"
RegSpec['RegSpec_Example']['Register_No_2']['Register_Field_No_4']['Register_Field_Split_No_1']['Reset_Value'] = "4'd0"
RegSpec['RegSpec_Example']['Register_No_2']['Register_Field_No_4']['Register_Field_Split_No_1']['Strobe_Index'] = "0"
RegSpec['RegSpec_Example']['Register_No_2']['Register_Field_No_4']['Register_Field_Split_No_1']['RW_Property'] = []
RegSpec['RegSpec_Example']['Register_No_2']['Register_Field_No_4']['Register_Field_Split_No_1']['RW_Property'].append("RW_RC")
RegSpec['RegSpec_Example']['Register_No_2']['Common_Config']['RW_Property']['Strobe_0'].append("RW_RC")
RegSpec['RegSpec_Example']['Register_No_2']['Register_Field_No_5'] = {}
RegSpec['RegSpec_Example']['Register_No_2']['Register_Field_No_5']['Common_Config'] = {}
RegSpec['RegSpec_Example']['Register_No_2']['Register_Field_No_5']['Common_Config']['Field_Name'] = "ABC"
RegSpec['RegSpec_Example']['Register_No_2']['Register_Field_No_5']['Common_Config']['Field_Desciption'] = """None"""
RegSpec['RegSpec_Example']['Register_No_2']['Register_Field_No_5']['Register_Field_Split_No_1'] = {}
RegSpec['RegSpec_Example']['Register_No_2']['Register_Field_No_5']['Register_Field_Split_No_1']['Bit_Range'] = "0"
RegSpec['RegSpec_Example']['Register_No_2']['Register_Field_No_5']['Register_Field_Split_No_1']['Reset_Value'] = "1'b0"
RegSpec['RegSpec_Example']['Register_No_2']['Register_Field_No_5']['Register_Field_Split_No_1']['Strobe_Index'] = "0"
RegSpec['RegSpec_Example']['Register_No_2']['Register_Field_No_5']['Register_Field_Split_No_1']['RW_Property'] = []
RegSpec['RegSpec_Example']['Register_No_2']['Register_Field_No_5']['Register_Field_Split_No_1']['RW_Property'].append("RWI")
RegSpec['RegSpec_Example']['Register_No_2']['Common_Config']['RW_Property']['Strobe_0'].append("RWI")
