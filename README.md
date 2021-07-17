[![Documentation Status](https://readthedocs.org/projects/python-sdbus-notifications/badge/?version=latest)](https://python-sdbus-notifications.readthedocs.io/en/latest/?badge=latest)
# Freedesktop notifications binds for python-sdbus

Supports both asyncio (under `sdbus_async.notifications` module) and blocking (under `sdbus_block.notifications` module) 

Implemented:

* NotificationsInterface - notifications interface to implement your own notifications daemon.
* FreedesktopNotifications - notifications interface proxy connected to `org.freedesktop.Notifications` service and `/org/freedesktop/Notifications` path

## Requirements

* `python-sdbus` version higher than 0.8rc2

See [python-sdbus requirements](https://github.com/igo95862/python-sdbus#requirements).

## Installation

`pip install --only-binary ':all:' sdbus-notifications`

# [Documentation](https://python-sdbus-notifications.readthedocs.io/en/latest/)

This is the sub-project of [python-sdbus](https://github.com/igo95862/python-sdbus).

See the [python-sdbus documentation](https://python-sdbus.readthedocs.io/en/latest/).
