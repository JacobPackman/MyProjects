#!/bin/bash
mullvad disconnect
mullvad always-require-vpn set off
openvpn --config /home/jacob/client.ovpn --daemon
pid=$(pgrep openvpn)
mullvad split-tunnel pid add $pid 
mullvad always-require-vpn set on 
mullvad connect

