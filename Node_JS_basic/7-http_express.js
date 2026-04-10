const express = require('express');
const countStudents = require('./3-read_file_async');

const args = process.argv.slice(2);
const DATABASE = args[0];

const app = express();
const port = 1245;

app.get("/", (req, res) => {
  res.send("Hello Holberton School!");
  });

app.get('/students', (req, res) => {
  res.send('This is the list of our students\n');
  countStudents(DATABASE)
    .then((data) => {
        res.write(data);
        res.end();
    })
  .catch((err) => {
    res.write(err.message);
    res.end();
    });
});



app.listen(port);

module.exports = app;
