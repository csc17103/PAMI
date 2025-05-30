__copyright__ = """
#  Copyright (C)  2021 Rage Uday Kiran
#
#      This program is free software: you can redistribute it and/or modify
#      it under the terms of the GNU General Public License as published by
#      the Free Software Foundation, either version 3 of the License, or
#      (at your option) any later version.
#
#      This program is distributed in the hope that it will be useful,
#      but WITHOUT ANY WARRANTY; without even the implied warranty of
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#      GNU General Public License for more details.
#
#      You should have received a copy of the GNU General Public License
#      along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from abc import ABC as _ABC, abstractmethod as _abstractmethod
import time as _time
import validators as _validators
from urllib.request import urlopen as _urlopen
import csv as _csv
import pandas as _pd
from collections import defaultdict as _defaultdict
from itertools import combinations as _c
import os as _os
import os.path as _ospath
import psutil as _psutil
from array import *
import functools as _functools
import sys as _sys

class _highUtilityPatternStreamMining(_ABC):
    """
    :Description:   This abstract base class defines the variables and methods that every high utility pattern stream mining algorithm must
                    employ in PAMI

    :Attributes:

        iFile : str
            Input file name or path of the input file
        minUtil: integer 
            The user can specify minUtil either in count
        sep : str
            This variable is used to distinguish items from one another in a transaction. The default seperator is tab space or \t.
            However, the users can override their default separator
        startTime:float
            To record the start time of the algorithm
        endTime:float
            To record the completion time of the algorithm
        finalPatterns: dict
            Storing the complete set of patterns in a dictionary variable
        oFile : str
            Name of the output file to store complete set of frequent patterns
        memoryUSS : float
            To store the total amount of USS memory consumed by the program
        memoryRSS : float
            To store the total amount of RSS memory consumed by the program

    :Methods:

        mine()
            Calling this function will start the actual mining process
        getPatterns()
            This function will output all interesting patterns discovered by an algorithm
        save(oFile)
            This function will store the discovered patterns in an output file specified by the user
        getPatternsAsDataFrame()
            The function outputs the patterns generated by an algorithm as a data frame
        getMemoryUSS()
            This function outputs the total amount of USS memory consumed by a mining algorithm
        getMemoryRSS()
            This function outputs the total amount of RSS memory consumed by a mining algorithm
        getRuntime()
            This function outputs the total runtime of a mining algorithm

    """

    def __init__(self, iFile, minUtil, windowSize, paneSize, sep = "\t"):
        """
        :param iFile: Input file name or path of the input file
        :type iFile: str
        :param minUtil: The user can specify minUtil in count 
        :type minUtil: int 
        :param sep: separator used to distinguish items from each other. The default separator is tab space. However, users can override the default separator
        :type sep: str

        """

        self._iFile = iFile
        self._sep = sep
        self._oFile = " "
        self._minUtil = minUtil
        self._windowSize = windowSize
        self._paneSize = paneSize
        self._startTime = float()
        self._endTime = float()
        self._memoryUSS = float()
        self._memoryRSS = float()
        self._finalPatterns = {}

    @_abstractmethod
    def startMine(self):
        """Code for the mining process will start from this function"""

        pass

    @_abstractmethod
    def getPatterns(self):
        """Complete set of frequent patterns generated will be retrieved from this function"""

        pass

    @_abstractmethod
    def save(self):
        """Complete set of frequent patterns will be saved in to an output file from this function
        """

        pass

    @_abstractmethod
    def getPatternsAsDataFrame(self):
        """Complete set of frequent patterns will be loaded in to data frame from this function"""

        pass

    @_abstractmethod
    def getMemoryUSS(self):
        """Total amount of USS memory consumed by the program will be retrieved from this function"""

        pass

    @_abstractmethod
    def getMemoryRSS(self):
        """Total amount of RSS memory consumed by the program will be retrieved from this function"""

        pass


    @_abstractmethod
    def getRuntime(self):
        """Total amount of runtime taken by the program will be retrieved from this function"""

        pass