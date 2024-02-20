#!/usr/bin/node
// Script that writes a string to a file.
const fs = require('fs');

const file_path = process.argv[2];
const string_to_write = process.argv[3];

fs.writeFile(file_path, string_to_write, 'utf-8', (err, data) => {
    if (err) {
        console.error(err);
    }
});
