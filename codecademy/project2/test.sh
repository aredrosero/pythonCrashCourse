#!/bin/bash

# Define your name and the directory where the files will be created
yourName="yourName"
directory="./files_directory"

# Create the directory if it doesn't exist
mkdir -p "$directory"

# Find the maximum existing number in the directory
max_number=$(find "$directory" -type f -name "${yourName}*" | grep -oE '[0-9]+' | sort -n | tail -n 1)

# Initialize a counter to create the next batch of 25 files
counter=1

# Number of files to create in this batch
batch_size=25

# Create 25 empty files with increasing numbers
for ((i = max_number + 1; i <= max_number + batch_size; i++)); do
  filename="${yourName}${i}"
  touch "${directory}/${filename}"
done

# Display a long list of the directory and its contents
ls -l "$directory"