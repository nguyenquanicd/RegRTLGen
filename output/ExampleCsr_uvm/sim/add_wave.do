onerror {resume}
quietly WaveActivateNextPane {} 0
add wave -noupdate -divider -height 23 {APB SIGNAL}
add wave -noupdate /RegRTL_Top/ExampleCsr/pclk
add wave -noupdate /RegRTL_Top/ExampleCsr/preset_n
add wave -noupdate /RegRTL_Top/ExampleCsr/penable
add wave -noupdate /RegRTL_Top/ExampleCsr/psel
add wave -noupdate /RegRTL_Top/ExampleCsr/pready
add wave -noupdate /RegRTL_Top/ExampleCsr/paddr
add wave -noupdate /RegRTL_Top/ExampleCsr/pwrite
add wave -noupdate /RegRTL_Top/ExampleCsr/pwdata
add wave -noupdate /RegRTL_Top/ExampleCsr/pstrb
add wave -noupdate /RegRTL_Top/ExampleCsr/prdata
add wave -noupdate /RegRTL_Top/ExampleCsr/pslverr
add wave -noupdate /RegRTL_Top/ExampleCsr/pprot
add wave -noupdate /RegRTL_Top/ExampleCsr/write_protect_en
add wave -noupdate -divider -height 23 {USER SIGNAL}
add wave -noupdate /RegRTL_Top/ExampleCsr/ACTRL_reg 
add wave -noupdate /RegRTL_Top/ExampleCsr/ACTRL_byte_we 
add wave -noupdate /RegRTL_Top/ExampleCsr/ACTRL_ivalue 
add wave -noupdate /RegRTL_Top/ExampleCsr/ACTRL_RESERVED_iwe 
add wave -noupdate /RegRTL_Top/ExampleCsr/ACTRL_BAUND1_3_w1 
add wave -noupdate /RegRTL_Top/ExampleCsr/ACTRL_BAUND1_2_w1 
add wave -noupdate /RegRTL_Top/ExampleCsr/ACTRL_BAUND0_1_w0 
add wave -noupdate /RegRTL_Top/ExampleCsr/ACTRL_RWI_iwe 
add wave -noupdate /RegRTL_Top/ExampleCsr/BCTRL_reg 
add wave -noupdate /RegRTL_Top/ExampleCsr/BCTRL_read_en 
add wave -noupdate /RegRTL_Top/ExampleCsr/BCTRL_byte_we 
add wave -noupdate /RegRTL_Top/ExampleCsr/BCTRL_ivalue 
add wave -noupdate /RegRTL_Top/ExampleCsr/BCTRL_RESERVED_iwe 
add wave -noupdate /RegRTL_Top/ExampleCsr/BCTRL_ROS_iwe 
add wave -noupdate /RegRTL_Top/ExampleCsr/BCTRL_ROC_iwe 
add wave -noupdate /RegRTL_Top/ExampleCsr/BCTRL_RO_iwe 
TreeUpdate [SetDefaultTree]
#WaveRestoreCursors {{Cursor 1} {925 ns} 0}
#quietly wave cursor active 1
#configure wave -namecolwidth 218
#configure wave -valuecolwidth 145
#configure wave -justifyvalue left
#configure wave -signalnamewidth 1
#configure wave -snapdistance 10
#configure wave -datasetprefix 0
#configure wave -rowmargin 4
#configure wave -childrowmargin 2
#configure wave -gridoffset 0
#configure wave -gridperiod 1
#configure wave -griddelta 40
#configure wave -timeline 0
#configure wave -timelineunits ns
update
WaveRestoreZoom {0 ns} {1050 ns}
