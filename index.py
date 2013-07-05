import miniong
import os
import sys

WORKING_DIR = os.path.dirname( os.path.realpath(__file__) )

miniong.application = 'application'
miniong.modules = 'modules'
miniong.system = 'system'

sys.path.insert(0, os.path.join(WORKING_DIR, miniong.system))
sys.path.insert(0, os.path.join(WORKING_DIR, miniong.modules, 'minion'))
sys.path.insert(0, os.path.join(WORKING_DIR, miniong.application))

import minion

minion.factory().execute()
