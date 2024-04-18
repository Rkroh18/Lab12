import pytest
from television import Television

@pytest.fixture
def tv():
    return Television()

def test_init(tv):
    assert tv.stat == False
    assert tv.muted == False
    assert tv.vol == 0
    assert tv.channel == 0

def test_power(tv):
    tv.power()
    assert tv.stat == True
    tv.power()
    assert tv.stat == False

def test_mute(tv):
    tv.power()
    tv.mute()
    assert tv.muted == True
    tv.mute()
    assert tv.muted == False

def test_channel_up(tv):
    tv.power()
    tv.channel_up()
    assert tv.channel == 1
    for _ in range(4):
        tv.channel_up()
    assert tv.channel == 1

def test_channel_down(tv):
    tv.power()
    tv.channel_down()
    assert tv.channel == 3
    for _ in range(4):
        tv.channel_down()
    assert tv.channel == 3

def test_volume_up(tv):
    tv.power()
    tv.volume_up()
    assert tv.vol == 1
    for _ in range(3):
        tv.volume_up()
    assert tv.vol == 2
    tv.mute()
    tv.volume_up()
    assert tv.muted == False

def test_volume_down(tv):
    tv.power()
    tv.volume_down()
    assert tv.vol == 0
    tv.volume_down()
    assert tv.vol == 0
    tv.mute()
    tv.volume_down()
    assert tv.muted == False
    
if __name__ == "__main__":
    pytest.main()