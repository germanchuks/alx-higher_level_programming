#!/usr/bin/node
/* Concats 2 files.
The first argument is the file path of the first source file
The second argument is the file path of the second source file
The third argument is the file path of the destination
*/

const fs = require('fs');

if (process.argv.length !== 5) {
  console.log('Usage: ./102-concat.js fileA fileB fileC');
  process.exit(1);
}

const fileAPath = process.argv[2];
const fileBPath = process.argv[3];
const destPath = process.argv[4];

try {
  const contentA = fs.readFileSync(fileAPath);
  const contentB = fs.readFileSync(fileBPath);

  const concatenatedContent = contentA + '\n' + contentB;

  fs.writeFileSync(destPath, concatenatedContent);
} catch (err) {
  console.log(err.message);
  process.exit(1);
}
