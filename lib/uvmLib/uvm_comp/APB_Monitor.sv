//--------------------------------------
//Project: The UVM environemnt for UART (Universal Asynchronous Receiver Transmitter)
//Function: Monitor
//Author:  Truong Cong Hoang Viet, Pham Thanh Tram, Nguyen Sinh Ton, Doan Duc Hoang, Nguyen Hung Quan
//Page:    VLSI Technology
//--------------------------------------
class cApbMasterMonitor extends uvm_monitor;
  //Register to Factory
	`uvm_component_utils(cApbMasterMonitor)
  //Internal variables
  logic preset_n;
  cApbTransaction coApbTransaction;
  //Declare analysis ports
  uvm_analysis_port #(logic) preset_toScoreboard; 
  uvm_analysis_port #(cApbTransaction) ap_toScoreboard;
  //Declare the monitored interfaces
	virtual interface ifApbMaster vifApbMaster;
 // virtual interface ifInterrupt vifInterrupt;
	//Constructor
	function new (string name = "cApbMasterMonitor", uvm_component parent = null);
		super.new(name,parent);
	endfunction
  //
	function void build_phase(uvm_phase phase);
		super.build_phase(phase);
    //Check the APB connection
		if(!uvm_config_db#(virtual interface ifApbMaster)::get(this,"","vifApbMaster",vifApbMaster)) begin
			`uvm_error("cApbMasterDriver","Can NOT get vifApbMaster!!!")
		end
    //Check the interrupt connection
 //   if(!uvm_config_db#(virtual interface ifInterrupt)::get(this,"","vifInterrupt",vifInterrupt)) begin
 //			`uvm_error("cVSequencer","Can NOT get vifInterrupt!!!")
 //		end
    //Create objects and analysis ports
    ap_toScoreboard = new("ap_toScoreboard", this);	
	  preset_toScoreboard = new("preset_toScoreboard", this);
    coApbTransaction = cApbTransaction::type_id::create("coApbTransaction",this);
	endfunction
  //
	virtual task run_phase(uvm_phase phase);
		super.run_phase(phase);
		fork
      //Detect transaction on APB interface and send to Scoreboard
		  collect_data();
      //Setect reset status and send to Scoreboard
		  detect_reset();
//Remove interrupt      //Monitor interrupt enable
//Remove interrupt      monitor_ifEn ();
//Remove interrupt      //Detect interrupt
//Remove interrupt      detect_intf ();
		join
    
  endtask: run_phase	
	//On each clock, detect a valid transaction
  // -> get the valid transaction
  // -> send the transaction to analysis port ap_toScoreboard
  virtual task collect_data();
	  while(1) begin
      @(posedge vifApbMaster.pclk) begin
        #1ps
        if(vifApbMaster.psel && vifApbMaster.penable && vifApbMaster.pready) begin
          //Get APB transaction on APB interface
          coApbTransaction.paddr[31:0] =  vifApbMaster.paddr[31:0];
          coApbTransaction.pstrb[3:0] = vifApbMaster.pstrb[3:0];
          coApbTransaction.pwrite = vifApbMaster.pwrite;
          coApbTransaction.pwdata[31:0] =  vifApbMaster.pwdata[31:0];
          coApbTransaction.prdata[31:0] =  vifApbMaster.prdata[31:0];
		  coApbTransaction.pprot[2:0] =  vifApbMaster.pprot[2:0];
          //Send the transaction to analysis port which is connected to Scoreboard
          ap_toScoreboard.write(coApbTransaction);
        end
      end
	  end
  endtask
	//On each clock, send the reset status to Scoreboard
  //via analysis port preset_toScoreboard
	virtual task detect_reset();
	  while(1) begin
			@(posedge vifApbMaster.pclk);
      #1ps
			this.preset_n = vifApbMaster.preset_n;
			preset_toScoreboard.write(this.preset_n);
		end
	endtask
 //Remove interrupt //Detect interrupt toggle
 //Remove interrupt logic [4:0] ifEn = 5'd0;
 //Remove interrupt `ifdef INTERRUPT_COM
 //Remove interrupt   logic ifSta = 1'b0;
 //Remove interrupt `else
 //Remove interrupt   logic [4:0] ifSta = 5'd0;
 //Remove interrupt `endif
 //Remove interrupt virtual task monitor_ifEn ();
 //Remove interrupt   //-------------------------------------
 //Remove interrupt   // Update interrupt enable
 //Remove interrupt   //-------------------------------------
 //Remove interrupt   while (1) begin
 //Remove interrupt     @(posedge vifApbMaster.pclk);
 //Remove interrupt     #1ps
 //Remove interrupt     if (vifApbMaster.psel && vifApbMaster.penable 
 //Remove interrupt     && vifApbMaster.pready && vifApbMaster.pwrite 
 //Remove interrupt     && (vifApbMaster.paddr[15:0] == 16'h0010)) begin
 //Remove interrupt       //Use "<=" to make sure only check after enable
 //Remove interrupt	    ifEn[4:0] <= vifApbMaster.pwdata[4:0];
 //Remove interrupt	  end
 //Remove interrupt   end
 //Remove interrupt endtask
 //Remove interrupt //
 //Remove interrupt virtual task detect_intf ();
 //Remove interrupt   while(1) begin
 //Remove interrupt     @(posedge vifApbMaster.pclk);
 //Remove interrupt     #1ps
 //Remove interrupt     //-------------------------------------
 //Remove interrupt     // Check the interrupt signals
 //Remove interrupt     //-------------------------------------
 //Remove interrupt     `ifdef INTERRUPT_COM
 //Remove interrupt       if (vifInterrupt.ctrl_if) begin
 //Remove interrupt         if (~ifSta) begin
 //Remove interrupt           if (~|ifEn[4:0]) begin
 //Remove interrupt             `uvm_error("cApbMasterMonitor", "INTERRUPT is toggled but NOT have any interrupt enable")
 //Remove interrupt           end
 //Remove interrupt           else begin
 //Remove interrupt             `uvm_warning("cApbMasterMonitor", $sformatf("INTERRUPT is toggled when interrupt enable is %5b", ifEn[4:0]))
 //Remove interrupt           end
 //Remove interrupt         ifSta = 1'b1;
 //Remove interrupt         end
 //Remove interrupt       end
 //Remove interrupt       else begin
 //Remove interrupt         ifSta = 1'b0;
 //Remove interrupt       end
 //Remove interrupt     `else
 //Remove interrupt       if (vifInterrupt.ctrl_tif) begin
 //Remove interrupt         if (~ifSta[0]) begin
 //Remove interrupt           if (~ifEn[0]) begin
 //Remove interrupt             `uvm_error("cApbMasterMonitor", "Transmit interrupt is toggled but it is not enable")
 //Remove interrupt           end
 //Remove interrupt           else
 //Remove interrupt             `uvm_warning("cApbMasterMonitor", "Transmit interrupt is toggled because TXFIFO is empty")
 //Remove interrupt         end
 //Remove interrupt         ifSta[0] = 1'b1;
 //Remove interrupt       end
 //Remove interrupt       else begin
 //Remove interrupt         ifSta[0] = 1'b0;
 //Remove interrupt       end
 //Remove interrupt       //
 //Remove interrupt       if (vifInterrupt.ctrl_rif) begin
 //Remove interrupt         if (~ifSta[1]) begin
 //Remove interrupt           if (~ifEn[1])
 //Remove interrupt             `uvm_error("cApbMasterMonitor", "Receiver interrupt is toggled but it is not enable")
 //Remove interrupt           else
 //Remove interrupt             `uvm_warning("cApbMasterMonitor", "Receiver interrupt is toggled because RXFIFO is full")
 //Remove interrupt         end
 //Remove interrupt         ifSta[1] = 1'b1;
 //Remove interrupt       end
 //Remove interrupt       else begin
 //Remove interrupt         ifSta[1] = 1'b0;
 //Remove interrupt       end
 //Remove interrupt       //
 //Remove interrupt       if (vifInterrupt.ctrl_oif) begin
 //Remove interrupt         if (~ifSta[2]) begin
 //Remove interrupt           if (~ifEn[2])
 //Remove interrupt             `uvm_error("cApbMasterMonitor", "Overflow interrupt is toggled but it is not enable")
 //Remove interrupt           else
 //Remove interrupt             `uvm_warning("cApbMasterMonitor", "Overflow interrupt is toggled because RXFIFO is full but a new UART frame is received")
 //Remove interrupt         end
 //Remove interrupt         ifSta[2] = 1'b1;
 //Remove interrupt       end
 //Remove interrupt       else begin
 //Remove interrupt         ifSta[2] = 1'b0;
 //Remove interrupt       end
 //Remove interrupt       //
 //Remove interrupt       if (vifInterrupt.ctrl_pif) begin
 //Remove interrupt         if (~ifSta[3]) begin
 //Remove interrupt           if (~ifEn[3])
 //Remove interrupt             `uvm_error("cApbMasterMonitor", "Parity interrupt is toggled but it is not enable")
 //Remove interrupt           else
 //Remove interrupt             `uvm_warning("cApbMasterMonitor", "Parity interrupt is toggled because parity bit is wrong")
 //Remove interrupt         end
 //Remove interrupt         ifSta[3] = 1'b1;
 //Remove interrupt       end
 //Remove interrupt       else begin
 //Remove interrupt         ifSta[3] = 1'b0;
 //Remove interrupt       end
 //Remove interrupt       //
 //Remove interrupt       if (vifInterrupt.ctrl_fif) begin
 //Remove interrupt         if (~ifSta[4]) begin
 //Remove interrupt           if (~ifEn[4])
 //Remove interrupt             `uvm_error("cApbMasterMonitor", "Frame error interrupt is toggled but it is not enable")
 //Remove interrupt           else
 //Remove interrupt             `uvm_warning("cApbMasterMonitor", "Frame error interrupt is toggled because STOP bit is 0")
 //Remove interrupt         end
 //Remove interrupt         ifSta[4] = 1'b1;
 //Remove interrupt       end
 //Remove interrupt       else begin
 //Remove interrupt         ifSta[4] = 1'b0;
 //Remove interrupt       end
 //Remove interrupt     `endif
 //Remove interrupt   end
 //Remove interrupt
 endtask
endclass
