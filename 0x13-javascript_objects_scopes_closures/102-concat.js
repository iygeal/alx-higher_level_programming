#!/usr/bin/node

// Import the fs module for file operations
const fs = require('fs');

// Get the file paths of the source files and the destination file from the command line arguments
const sourceFilePath1 = process.argv[2];
const sourceFilePath2 = process.argv[3];
const destinationFilePath = process.argv[4];

// Read the content of the first source file synchronously
const sourceContent1 = fs.readFileSync(sourceFilePath1, 'utf8');

// Read the content of the second source file synchronously
const sourceContent2 = fs.readFileSync(sourceFilePath2, 'utf8');

// Concatenate the content of the two source files
const concatenatedContent = sourceContent1 + sourceContent2;

// Write the concatenated content to the destination file synchronously
fs.writeFileSync(destinationFilePath, concatenatedContent);
