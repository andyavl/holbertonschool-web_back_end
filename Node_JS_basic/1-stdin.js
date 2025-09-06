process.stdout.write('Welcome to Holberton School, what is your name?\n');

process.stdin.on('data', (buffer) => {
  const myName = buffer.toString().trim();
  process.stdout.write(`Your name is: ${myName}\n`);
});

process.stdin.on('end', () => {
  process.stdout.write('This important software is now closing\n');
});
