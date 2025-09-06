process.stdout.write('Welcome to Holberton School, what is your name?\n');

process.stdin.on('readable', () => {
  const myName = process.stdin.read();
  if (myName !== null) {
    process.stdout.write(`Your name is: ${myName}`);
  }
});

process.stdin.on('close', () => {
  process.stdout.write('This important software is now closing\n');
});
