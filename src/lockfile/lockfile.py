# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import fcntl


class LockFile:
    handle = None

    def __init__(self, filename, wait_for_acquire=False):
        self.filename = filename
        # This will create it if it does not exist already
        self.handle = open(filename, "w")
        self.wait_for_acquire = wait_for_acquire

    # flock() is a blocking call unless it is bitwise ORed with LOCK_NB to avoid blocking
    # on lock acquisition.  This blocking is what I use to provide atomicity across forked
    # Django processes since native python locks and semaphores only work at the thread level
    def acquire(self):
        if self.wait_for_acquire:
            fcntl.flock(self.handle, fcntl.LOCK_EX)
        else:
            fcntl.flock(self.handle, fcntl.LOCK_EX | fcntl.LOCK_NB)

    def release(self):
        fcntl.flock(self.handle, fcntl.LOCK_UN)

    def __del__(self):
        self.handle.close()
