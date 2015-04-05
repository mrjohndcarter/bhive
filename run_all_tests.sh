#!/bin/bash

# list of all bhive modules to test
# due to packaging structure, we need to specify module 'paths'
ALL_MODULES="bhive.environment.environment bhive.typing.bcontext bhive.typing.belement bhive.typing.bfunction bhive.typing.bset"

# need to run from directory above module for relative imports to work correctly
pushd .
cd ..
green -vv $ALL_MODULES
popd
