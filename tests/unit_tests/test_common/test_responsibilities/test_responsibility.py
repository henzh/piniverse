# The MIT License (MIT)
#
# Copyright (c) 2019 Henry Zhao
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import pytest

from piniverse.common.responsibilities.responsibility import Responsibility, ResponsibilityUtils


def test_responsibility():
    a = Responsibility(key='a', value='1')
    assert a.key == 'a'
    assert a.value == '1'
    assert a.successor == None

    c = Responsibility(key='c', value='3')
    b = Responsibility(key='b', value='2', successor=c)
    assert b.key == 'b'
    assert b.value == '2'
    assert b.successor == c
    assert c.key == 'c'
    assert c.value == '3'
    assert c.successor == None

    
def test_responsibility_utils(capsys):
    a = Responsibility(key='a', value='1')
    assert a.key == 'a'
    assert a.value == '1'
    assert a.successor == None

    b = Responsibility(key='b', value='2')
    assert b.key == 'b'
    assert b.value == '2'
    assert b.successor == None

    responsibilities = ResponsibilityUtils.build(a, b)
    assert a.successor == b
    assert b.successor == None

    # ResponsibilityUtils.pretty_print(responsibilities)
    # captured = capsys.readouterr()
    # assert captured.out == '\n----- Responsibilities -----\n[key: a, value: 1] -> \n[key: b, value: 2] -> \nnull\n----------------------------\n'
    # assert captured.err == ''
