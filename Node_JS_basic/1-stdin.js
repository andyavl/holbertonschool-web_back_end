const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false
});

console.log('Welcome to Holberton School, what is your name?');

let name = null;

rl.on('line', (line) => {
  name = line.trim();
  console.log(`Your name is: ${name}`);
});

rl.on('close', () => {
  console.log('This important software is now closing');
});
