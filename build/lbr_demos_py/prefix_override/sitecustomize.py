import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/suphasitpp/my_msc_ws/install/lbr_demos_py'
