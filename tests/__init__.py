import sys
from os.path import abspath, dirname

# Adicione o caminho do diretório "src" ao sys.path
sys.path.insert(0, abspath(dirname(dirname(__file__))))