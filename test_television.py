import pytest
from television import Television

def test_init():
    tv = Television()
    assert not tv._Television__status, "Television should be initially powered off."
    assert tv._Television__volume == 0, "Initial volume should be 0."
    assert tv._Television__channel == 0, "Initial channel should be 0."
    assert not tv._Television__muted, "Television should not be muted initially."

def test_power_toggle():
    tv = Television()
    tv.power()
    assert tv._Television__status, "Television should be powered on after toggle."
    tv.power()
    assert not tv._Television__status, "Television should be powered off after toggle."

def test_mute_toggle():
    tv = Television()
    tv.power()  # Turn on the TV
    tv.mute()
    assert tv._Television__muted, "Television should be muted."
    assert tv._Television__volume == 0, "Volume should be 0 when muted."
    tv.mute()
    assert not tv._Television__muted, "Television should be unmuted."
    assert tv._Television__volume == tv._Television__prev_volume, "Volume should revert to previous volume when unmuted."

def test_channel_up():
    tv = Television()
    tv.power()
    tv.channel_up()
    assert tv._Television__channel == 1, "Channel should increment by 1."
    for _ in range(3):  # Increment to test wrap-around
        tv.channel_up()
    assert tv._Television__channel == 0, "Channel should wrap around to 0."

def test_channel_down():
    tv = Television()
    tv.power()
    tv.channel_down()
    assert tv._Television__channel == 3, "Channel should wrap to MAX_CHANNEL on channel down from 0."
    tv.channel_down()
    assert tv._Television__channel == 2, "Channel should decrement by 1."

def test_volume_up():
    tv = Television()
    tv.power()
    tv.volume_up()
    assert tv._Television__volume == 1, "Volume should increment by 1."
    tv.volume_up()
    tv.volume_up()  # Should not exceed MAX_VOLUME
    assert tv._Television__volume == 2, "Volume should not exceed MAX_VOLUME."

def test_volume_down():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.volume_down()
    assert tv._Television__volume == 1, "Volume should decrement by 1."
    tv.volume_down()
    tv.volume_down()  # Should not go below MIN_VOLUME
    assert tv._Television__volume == 0, "Volume should not go below MIN_VOLUME."

