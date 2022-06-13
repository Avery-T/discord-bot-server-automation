#!/bin/bash

OUTPUT=$(smbclient \\\\10.0.0.80\\SommersMedia -U='william' 'william' -c 'cd Raw\ ; ls' | wc -l); echo $OUTPUT > number_of_files_in_raw_folder.txt; echo $OUTPUT


