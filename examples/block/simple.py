# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: 2025 igo95862
from __future__ import annotations

from sdbus_block.notifications import FreedesktopNotifications


def main() -> None:
    # Default bus will be used if no bus is explicitly passed.
    # When running as user the default bus will be session bus where
    # Notifications daemon usually runs.
    notifications = FreedesktopNotifications()

    notifications.notify(
        # summary is the only required argument.
        # For other arguments default values will be used.
        summary="FooBar",
    )


if __name__ == "__main__":
    main()
