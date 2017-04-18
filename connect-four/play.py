#!/usr/bin/env python -u
from random import randrange
import time
import json
import sys


def test_queue():
	for _ in range(10):
		i = randrange(0,7)
		print type(i)
		sys.stdout.flush()
		print json.dumps({"move": i})
		time.sleep(1)

if __name__ == '__main__':
	test_queue()
