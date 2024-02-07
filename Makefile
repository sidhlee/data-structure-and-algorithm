# Declares that test is a command, not the filename that might exist in the current folder.
.PHONY: test
test:
# MAKECMDGOALS has the list of targets after "make" command.
# eg. "test path" from `make test path`
# `word` function returns n-th string from a space-separated list of strings
# ignored tests that takes too long. Individual test watch doesn't get triggered on dependency change
		PYTHONPATH=. ptw --ignore recursion/test_recursion.py $(word 2, $(MAKECMDGOALS))