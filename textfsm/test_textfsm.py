from netmiko import ConnectHandler
import pytest
from textfsmlab2 import oneforall

def test_r1_int():
    output = []
    for one in oneforall(1):
        print(f"{one['neighbor_name']} is connected to your {one['local_interface']}")
        output.append(f"{one['neighbor_name']} is connected to your {one['local_interface']}")
    assert output[0] == "R2.ipa.com is connected to your Gig 0/2"
    assert output[1] == "S0.ipa.com is connected to your Gig 0/0"
def test_r2_int():
    output = []
    for one in oneforall(2):
        print(f"{one['neighbor_name']} is connected to your {one['local_interface']}")
        output.append(f"{one['neighbor_name']} is connected to your {one['local_interface']}")
    assert output[0] == "S0.ipa.com is connected to your Gig 0/0"
    assert output[1] == "R1.ipa.com is connected to your Gig 0/1"
    assert output[2] == "S1.ipa.com is connected to your Gig 0/2"

def test_s1_int():
    output = []
    for one in oneforall(3):
        print(f"{one['neighbor_name']} is connected to your {one['local_interface']}")
        output.append(f"{one['neighbor_name']} is connected to your {one['local_interface']}")
    assert output[0] == "R2.ipa.com is connected to your Gig 0/1"
    assert output[1] == "S0.ipa.com is connected to your Gig 0/0"

test_r1_int()
test_r2_int()
test_s1_int()

