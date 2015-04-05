#!/bin/bash

ALL_FILES_TO_LINT="environment/environment.py synthesis/synthesis.py typing/bcontext.py typing/belement.py typing/bfunction.py typing/bset.py"
pylint -rn $ALL_FILES_TO_LINT
