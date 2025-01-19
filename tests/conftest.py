# necessario per runnare test con pytest (altrimenti non importa modelpoint e hypotesis ecc..)
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))