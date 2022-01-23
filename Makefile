# https://stackoverflow.com/a/63785469
# https://www.gnu.org/software/make/manual/html_node/Phony-Targets.html
.PHONY: test
test:
		PYTHONPATH=. pytest