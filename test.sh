#! /bin/sh
# rebuild prog if necessary
make runtest
# shifts the positional arg to the left to remove the first arg (script name)
shift
# run prog with all args passed to the shell
make runtest "$@"
