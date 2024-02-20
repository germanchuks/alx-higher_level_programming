#!/usr/bin/node
// Script that reads and prints the content of a file
const fs = require('fs');

const file_path = process.argv[2];

fs.readFile(file_path, 'utf-8', (err, data) => {
    if (err) {
        console.error(err);
    } else {
        console.log(data);
    }
});
