onerror {resume}
quietly WaveActivateNextPane {} 0
add wave -noupdate -divider -height 23 {REG RTL}
add wave -noupdate /testTop/dut_top/pclk
add wave -noupdate /testTop/dut_top/preset_n
add wave -noupdate /testTop/dut_top/pwrite
add wave -noupdate /testTop/dut_top/psel
add wave -noupdate /testTop/dut_top/penable
add wave -noupdate /testTop/dut_top/paddr
add wave -noupdate /testTop/dut_top/pwdata
add wave -noupdate /testTop/dut_top/pstrb
add wave -noupdate /testTop/dut_top/prdata
add wave -noupdate /testTop/dut_top/pready
add wave -noupdate /testTop/dut_top/pslverr
add wave -noupdate /testTop/dut_top/pprot
add wave -noupdate /testTop/dut_top/write_protect_en
TreeUpdate [SetDefaultTree]
WaveRestoreCursors {{Cursor 1} {925 ns} 0}
quietly wave cursor active 1
configure wave -namecolwidth 218
configure wave -valuecolwidth 145
configure wave -justifyvalue left
configure wave -signalnamewidth 1
configure wave -snapdistance 10
configure wave -datasetprefix 0
configure wave -rowmargin 4
configure wave -childrowmargin 2
configure wave -gridoffset 0
configure wave -gridperiod 1
configure wave -griddelta 40
configure wave -timeline 0
configure wave -timelineunits ns
update
WaveRestoreZoom {0 ns} {1050 ns}
