# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: 2025 igo95862
from __future__ import annotations

from asyncio import run as asyncio_run

from sdbus_async.notifications import FreedesktopNotifications

# FreedesktopNotifications is a class that automatically proxies to
# the notifications daemon's service name and path.
# NotificationsInterface is the raw interface that can be used to
# implement your own daemon or proxied to non-standard path.


async def main() -> None:
    # Default bus will be used if no bus is explicitly passed.
    # When running as user the default bus will be session bus where
    # Notifications daemon usually runs.
    notifications = FreedesktopNotifications()

    await notifications.notify(
        # summary is the only required argument.
        # For other arguments default values will be used.
        summary="FooBar",
    )


if __name__ == "__main__":
    asyncio_run(main())
