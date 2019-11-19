#!/bin/bash

if [ "$EUID" -ne 0 ]; then
	echo "This script must be run as root.";
	exit
fi

if [ ! -x "$(command -v dpkg)" ]; then
	echo "You must have dpkg installed (are you on sure you are on Debian or Ubuntu?)"
	exit
fi

STABLE_DPKG_URL='https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb'
DEBIAN_CHROME_BINARY='/usr/bin/google-chrome'

if [ -x "$(command -v wget)" ]; then
	wget "$STABLE_DPKG_URL" -O chrome.deb
else
	if [ -x "$(command -v curl)" ]; then
		curl -s "$STABLE_DPKG_URL" > chrome.deb
	else
		echo "You must have curl or wget to obtain the Chrome installer"
	fi
fi

yes | dpkg -i chrome.deb

rm chrome.deb
