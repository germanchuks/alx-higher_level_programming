#!/usr/bin/node
/* Concats 2 files.
The first argument is the file path of the first source file
The second argument is the file path of the second source file
The third argument is the file path of the destination
*/

const fs = require('fs');

const contentA = fs.readFileSync(process.argv[2]);
const contentB = fs.readFileSync(process.argv[3]);

const concatenatedContent = contentA + contentB;

fs.writeFileSync(process.argv[4], concatenatedContent);
