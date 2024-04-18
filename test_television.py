import pytest
from television import Television

@pytest.fixture
def tv():
    return Television()

def test_init(tv):
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_power(tv):
    # Test when the TV is turned on
    tv.power()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    
    # Test when the TV is turned off
    tv.power()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"



def test_mute(tv):
    # Test when the TV is on, volume increased once, and then TV muted
    tv.power()
    tv.volume_up()
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    
    # Test when the TV is on and unmuted
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"
    
    # Test when the TV is off and muted
    tv.power()
    tv.mute()
    assert str(tv) == "Power = False, Channel = 0, Volume = 1"
    
    # Test when the TV is off and unmuted
    tv.mute()
    assert str(tv) == "Power = False, Channel = 0, Volume = 1"



def test_channel_up(tv):
    # Test when the TV is off and the channel has been increased
    tv.channel_up()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0" #####
    
    # Test when the TV is on and the channel has been increased
    tv.power()
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 1, Volume = 0"
    
    # Test when the TV is on and one has increased the channel past the maximum value
    for _ in range(3):
        tv.channel_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"



def test_channel_down(tv):
    # Test when the TV is off and the channel has been decreased
    tv.channel_down()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"
    
    # Test when the TV is on and one has decreased the channel past the minimum value
    tv.power()
    tv.channel_down()
    assert str(tv) == "Power = True, Channel = 3, Volume = 0"
    
    

def test_volume_up(tv):
    # Test when the TV is off and the volume has been increased
    tv.volume_up()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"
    
    # Test when the TV is on and the volume has been increased
    tv.power()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"
    
    # Test when the TV is on, muted, and the volume has been increased
    tv.mute()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"
    
    # Test when the TV is on and one has increased the volume past the maximum value
    for _ in range(2):
        tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"
    
    

def test_volume_down(tv):
    # Test when the TV is off and the volume has been decreased
    tv.volume_down()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"
    
    # Test when the TV is on and the volume has been decreased
    tv.power()
    tv.volume_up()  # Increase volume to maximum
    tv.volume_up()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"
    
    # Test when the TV is on, muted, and the volume has been decreased
    tv.volume_up()
    tv.mute()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"
    
    # Test when the TV is on and one has decreased the volume past the minimum value
    tv.volume_down()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    
    

if __name__ == "__main__":
    pytest.main()