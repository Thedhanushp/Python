#import from the main fun modules

import modules

print(modules.__name__)#to detect the which module is taken
modules.checkNegOrPos(-10)

#if we dont want the full content in the module that case use
from modules import checkNegOrPos
checkNegOrPos(10)

#"as" is used for shot n
import modules as mod 
from modules import checkNegOrPos