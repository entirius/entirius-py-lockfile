# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import unittest

from lockfile import LockFile


class TestEvents(unittest.TestCase):
    def test_simple(self):
        lock = LockFile("/tmp/_lock_test.tmp")
        lock.acquire()
        try:
            pass
        finally:
            lock.release()

    def test_raise_ioerror(self):
        lock1 = LockFile("/tmp/_lock_test.tmp")
        lock2 = LockFile("/tmp/_lock_test.tmp")
        lock1.acquire()
        try:
            is_error_cached = False
            try:
                lock2.acquire()
            except OSError:
                # Exception becouse another instance is running ...
                is_error_cached = True
            finally:
                lock2.release()
            self.assertTrue(is_error_cached)
        finally:
            lock1.release()


if __name__ == "__main__":
    unittest.main()
