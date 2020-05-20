#!/bin/bash

SOURCE="./female-first-names.txt"

sort --random-sort "${SOURCE}" |
    less
