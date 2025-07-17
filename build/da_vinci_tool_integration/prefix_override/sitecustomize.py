import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/suphasitpp/my_msc_ws/install/da_vinci_tool_integration'
