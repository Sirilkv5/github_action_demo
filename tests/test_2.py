import os,sys
sys.path.insert(0,os.getcwd())

from script import add
def test_add():
    subj = add(2,3)
    assert isinstance(subj,int)