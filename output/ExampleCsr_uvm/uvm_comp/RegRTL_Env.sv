//--------------------------------------
//Project: The UVM environemnt for RegisterRTL
//Function: UVM environment only contains the UVM components (Agents, Scoreboard, Sequencer)
//Author:  Nguyen Hung Quan, Le Hoang Van, Tran Huu Duy
//Page:    VLSI Technology
//--------------------------------------

class RegRTL_Env extends uvm_env;
  cApbMasterAgent coApbMasterAgent;
  RegConfig_Agent co_RegConfig_Agent;
  RegRTL_Scoreboard co_RegRTL_Scoreboard;
  RegRTL_Sequencer co_RegRTL_Sequencer;

  `uvm_component_utils(RegRTL_Env)

  function new(string name = "RegRTL_Env", uvm_component parent = null);
  super.new(name,parent);
  endfunction: new
  
  function void build_phase(uvm_phase phase);
    super.build_phase(phase);
    coApbMasterAgent     = cApbMasterAgent::type_id::create("coApbMasterAgent",this);
    co_RegConfig_Agent   = RegConfig_Agent::type_id::create("co_RegConfig_Agent",this);
    co_RegRTL_Scoreboard = RegRTL_Scoreboard::type_id::create("co_RegRTL_Scoreboard",this);
    co_RegRTL_Sequencer  = RegRTL_Sequencer::type_id::create("co_RegRTL_Sequencer",this);
  endfunction: build_phase

  function void connect_phase(uvm_phase phase);
    super.connect_phase(phase);
  
    $cast(co_RegRTL_Sequencer.coApbMasterAgent, this.coApbMasterAgent);
    $cast(co_RegRTL_Sequencer.co_RegConfig_Agent, this.co_RegConfig_Agent);
    $cast(co_RegRTL_Sequencer.co_RegRTL_Scoreboard, this.co_RegRTL_Scoreboard);
  
    coApbMasterAgent.coApbMasterMonitor.ap_toScoreboard.connect(co_RegRTL_Scoreboard.aimp_transAPB);
    coApbMasterAgent.coApbMasterMonitor.preset_toScoreboard.connect(co_RegRTL_Scoreboard.aimp_resetAPB);
    co_RegConfig_Agent.co_RegConfig_Monitor.ap_ACTRL_monitor.connect(co_RegRTL_Scoreboard.aimp_frmMonitor_ACTRL); 
    co_RegConfig_Agent.co_RegConfig_Monitor.ap_BCTRL_monitor.connect(co_RegRTL_Scoreboard.aimp_frmMonitor_BCTRL); 
    
  endfunction: connect_phase
endclass: RegRTL_Env
