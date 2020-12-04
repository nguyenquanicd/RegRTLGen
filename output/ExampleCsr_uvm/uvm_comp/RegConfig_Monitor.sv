//--------------------------------------
//Project: The UVM environemnt for RegisterRTL
//Function: Register Config Monitor
//Author:  Nguyen Hung Quan, Le Hoang Van, Le Tan Thinh
//Page:    VLSI Technology
//--------------------------------------

class RegConfig_Monitor extends uvm_monitor;
  virtual interface RegConfig_Interface vif_RegConfig_IF;
  
  ACTRL_monitor co_ACTRL_monitor; 
  uvm_analysis_port #(ACTRL_monitor) ap_ACTRL_monitor; 
  BCTRL_monitor co_BCTRL_monitor; 
  uvm_analysis_port #(BCTRL_monitor) ap_BCTRL_monitor; 

  `uvm_component_utils(RegConfig_Monitor)
  
  function new (string name = "RegConfig_Monitor", uvm_component parent = null);
    super.new(name,parent);
  endfunction: new

  function void build_phase(uvm_phase phase);
    super.build_phase(phase);
    if(!uvm_config_db#(virtual interface ifApbMaster)::get(this,"","vif_RegConfig_IF",vif_RegConfig_IF)) begin
      `uvm_error("cApbMasterDriver","Can NOT get vif_RegConfig_IF!!!")
    end
    
    co_ACTRL_monitor = ACTRL_monitor::type_id::create("co_ACTRL_monitor",this); 
    ap_ACTRL_monitor = new("ap_ACTRL_monitor", this);	
    co_BCTRL_monitor = BCTRL_monitor::type_id::create("co_BCTRL_monitor",this); 
    ap_BCTRL_monitor = new("ap_BCTRL_monitor", this);	
  endfunction: build_phase

  virtual task run_phase(uvm_phase phase);
    super.run_phase(phase);
    fork
      ACTRL_collect_data(); 
      BCTRL_collect_data(); 
    join
  endtask: run_phase
  

  virtual task ACTRL_collect_data();
    while(1) begin
      @(vif_RegConfig_IF.ACTRL_reg 
        or vif_RegConfig_IF.ACTRL_byte_we 
        or vif_RegConfig_IF.ACTRL_ivalue 
        or vif_RegConfig_IF.ACTRL_RESERVED_iwe 
        or vif_RegConfig_IF.ACTRL_BAUND1_3_w1 
        or vif_RegConfig_IF.ACTRL_BAUND1_2_w1 
        or vif_RegConfig_IF.ACTRL_BAUND0_1_w0 
        or vif_RegConfig_IF.ACTRL_RWI_iwe 

      ) begin
        #1ps
        co_ACTRL_monitor.ACTRL_reg = vif_RegConfig_IF.ACTRL_reg; 
        co_ACTRL_monitor.ACTRL_byte_we = vif_RegConfig_IF.ACTRL_byte_we; 
        co_ACTRL_monitor.ACTRL_ivalue = vif_RegConfig_IF.ACTRL_ivalue; 
        co_ACTRL_monitor.ACTRL_RESERVED_iwe = vif_RegConfig_IF.ACTRL_RESERVED_iwe; 
        co_ACTRL_monitor.ACTRL_BAUND1_3_w1 = vif_RegConfig_IF.ACTRL_BAUND1_3_w1; 
        co_ACTRL_monitor.ACTRL_BAUND1_2_w1 = vif_RegConfig_IF.ACTRL_BAUND1_2_w1; 
        co_ACTRL_monitor.ACTRL_BAUND0_1_w0 = vif_RegConfig_IF.ACTRL_BAUND0_1_w0; 
        co_ACTRL_monitor.ACTRL_RWI_iwe = vif_RegConfig_IF.ACTRL_RWI_iwe; 

        ap_ACTRL_monitor.write(co_ACTRL_monitor);
      end
    end
  endtask: ACTRL_collect_data

  virtual task BCTRL_collect_data();
    while(1) begin
      @(vif_RegConfig_IF.BCTRL_reg 
        or vif_RegConfig_IF.BCTRL_read_en 
        or vif_RegConfig_IF.BCTRL_byte_we 
        or vif_RegConfig_IF.BCTRL_ivalue 
        or vif_RegConfig_IF.BCTRL_RESERVED_iwe 
        or vif_RegConfig_IF.BCTRL_ROS_iwe 
        or vif_RegConfig_IF.BCTRL_ROC_iwe 
        or vif_RegConfig_IF.BCTRL_RO_iwe 

      ) begin
        #1ps
        co_BCTRL_monitor.BCTRL_reg = vif_RegConfig_IF.BCTRL_reg; 
        co_BCTRL_monitor.BCTRL_read_en = vif_RegConfig_IF.BCTRL_read_en; 
        co_BCTRL_monitor.BCTRL_byte_we = vif_RegConfig_IF.BCTRL_byte_we; 
        co_BCTRL_monitor.BCTRL_ivalue = vif_RegConfig_IF.BCTRL_ivalue; 
        co_BCTRL_monitor.BCTRL_RESERVED_iwe = vif_RegConfig_IF.BCTRL_RESERVED_iwe; 
        co_BCTRL_monitor.BCTRL_ROS_iwe = vif_RegConfig_IF.BCTRL_ROS_iwe; 
        co_BCTRL_monitor.BCTRL_ROC_iwe = vif_RegConfig_IF.BCTRL_ROC_iwe; 
        co_BCTRL_monitor.BCTRL_RO_iwe = vif_RegConfig_IF.BCTRL_RO_iwe; 

        ap_BCTRL_monitor.write(co_BCTRL_monitor);
      end
    end
  endtask: BCTRL_collect_data
  
endclass: RegConfig_Monitor
