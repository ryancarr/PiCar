#!/bin/sh
#############################################################################
# This script installs the sixad driver for the Sixaxis PS3 Controller on a
# fresh install of the official Raspbian image (2014-01-07) for the Raspberry 
# Pi. 
#
# Setup:
# Attach a compatible Bluetooth adapter to the Pi. You can find a list of 
# compatible adapters at <http://elinux.org/RPi_USB_Bluetooth_adapters>. I
# use the Sabrent BT-USBT and it works fine.
#
# Copy this script to the Pi (replace IP_ADDRESS with the IP address of the 
# pi):
#
#  scp install-sixaxis.sh pi@IP_ADDRESS:.
#
# Execute the script on the Pi:
#
#  ssh pi@IP_ADDRESS "./install-sixaxis.sh"
#
# Pair your PS3 controller with the Pi's bluetooth adapter by plugging it 
# into the Pi's USB and then executing the following:
#
#  ssh pi@IP_ADDRESS "sudo ./qtsixa/utils/bins/sixpair"
# 
# Unplug the PS3 controller from the USB and reboot:
#
#  ssh pi@IP_ADDRESS "sudo reboot"
#
# When the Raspberry Pi finishes restarting, hit the "Playstation" button on
# the center of the controller. If it vibrates, then you've successfully 
# gotten everything set up.
#############################################################################
set -e
sudo apt-get update
sudo apt-get -y install bluez bluez-utils bluez-compat bluez-hcidump checkinstall libbluetooth-dev libusb-dev joystick git libjack-jackd2-dev
git clone -b sdp-error-workaround git://github.com/johntrimble/qtsixa.git
cd qtsixa/sixad
sudo mkdir -p /var/lib/sixad/profiles
make
sudo make install
sudo update-rc.d sixad defaults
cd ../utils
make
sudo make install
