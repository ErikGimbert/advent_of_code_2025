#!/bin/bash

# Script to add a new day for Advent of Code 2025
RED="\033[0;31m"
YELLOW='\033[0;33m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

# Find last existing day file
last_day_file=$(ls src/days/d*.py 2>/dev/null | sort -V | tail -n 1)
if [[ -z "$last_day_file" ]]; then
    last_day=0
else
    last_day=$(echo "$last_day_file" | sed -E 's/.*\/d([0-9]+)\.py/\1/')
fi
echo "Last existing day: $last_day"
if [[ -f "tests/test_day_$(printf "%02d" $last_day).py" ]]; then
    new_day=$((last_day + 1))
else
    echo -e "${YELLOW}Warning: Some files was missing for day $last_day. Try to fix them before adding a new day.${NC}"
    new_day=$last_day
fi
new_day_padded=$(printf "%02d" "$new_day")
echo "Creating files for day: $new_day"

# Create source file
new_day_src_file="src/days/d${new_day_padded}.py"
echo -n "    Creating source file: $new_day_src_file ..."
if [[ -f "$new_day_src_file" ]]; then
    echo -e " ${YELLOW}already exists.${NC}"
else
    cat src/days/_template.py | sed "s/DAY: int = 0/DAY: int = $new_day/" > "$new_day_src_file"
    if [[ $? -ne 0 ]]; then
        echo -e " ${RED}Error creating source file.${NC}"
        exit 1
    else
        echo -e " ${GREEN}done.${NC}"
    fi
fi

# Create test file
new_day_test_file="tests/test_day_${new_day_padded}.py"
echo -n "    Creating test file: $new_day_test_file ..."
if [[ -f "$new_day_test_file" ]]; then
    echo -e " ${YELLOW}already exists.${NC}"
else
    cat tests/_template_test.py | sed "s/from days._template import/from days.d${new_day_padded} import/g" > "$new_day_test_file"
    if [[ $? -ne 0 ]]; then
        echo -e " ${RED}Error creating test file.${NC}"
        exit 1
    else
        echo -e " ${GREEN}done.${NC}"
    fi
fi

# Final message
echo -e "${GREEN}All done! Happy coding for day $new_day!${NC}"
