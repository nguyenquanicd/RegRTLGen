onerror {resume}
quietly WaveActivateNextPane {} 0
add wave -noupdate -divider -height 23 {APB SIGNAL}
add wave -noupdate /RegRTL_Top/module_name_here/pclk
add wave -noupdate /RegRTL_Top/module_name_here/preset_n
add wave -noupdate /RegRTL_Top/module_name_here/penable
add wave -noupdate /RegRTL_Top/module_name_here/psel
add wave -noupdate /RegRTL_Top/module_name_here/pready
add wave -noupdate /RegRTL_Top/module_name_here/paddr
add wave -noupdate /RegRTL_Top/module_name_here/pwrite
add wave -noupdate /RegRTL_Top/module_name_here/pwdata
add wave -noupdate /RegRTL_Top/module_name_here/pstrb
add wave -noupdate /RegRTL_Top/module_name_here/prdata
add wave -noupdate /RegRTL_Top/module_name_here/pslverr
add wave -noupdate /RegRTL_Top/module_name_here/pprot
add wave -noupdate /RegRTL_Top/module_name_here/write_protect_en
add wave -noupdate -divider -height 23 {USER SIGNAL}
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
