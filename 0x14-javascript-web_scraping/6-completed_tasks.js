#!/usr/bin/node
/* Script  that computes the number of tasks completed by user id. */
const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const tasks = JSON.parse(body);
    const tasksCompleted = tasks.filter(task => task.completed);
    const tasksCompletedByUser = tasksCompleted.reduce((count, task) => {
      count[task.userId] = (count[task.userId] || 0) + 1;
      return count;
    }, {});
    console.log(tasksCompletedByUser);
  }
});
