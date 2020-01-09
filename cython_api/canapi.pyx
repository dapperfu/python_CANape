# distutils: language = "c++"

import cython
import numpy as np
cimport numpy as np

from libc.string cimport memcpy
from libc.stdlib cimport malloc

