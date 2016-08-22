#!/usr/bin/env python
import time
if time.daylight:
    print time.altzone*-1
else:
    print time.timezone*-1

