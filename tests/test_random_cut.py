# Copyright 2022 D-Wave Systems Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

import numpy as np
import unittest


from components.random_cut import random_cut_generator
from components.packing3d import Cases

class TestRandomCut(unittest.TestCase):
    def test_random_cut_generator(self):
        bin_length, bin_width, bin_height = 10, 10, 10
        data = random_cut_generator(
            num_bins=1,
            bin_length=bin_length,
            bin_width=bin_width,
            bin_height=bin_height,
            num_cases=20
        )
        cases = Cases(data=data)
        self.assertEqual(
            np.sum(cases.length * cases.width * cases.height),
            bin_length * bin_width * bin_height/2
        )