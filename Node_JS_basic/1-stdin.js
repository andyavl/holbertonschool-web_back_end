console.log('Welcome to Holberton School, what is your name?');

process.stdin.on('data', (buffer) => {
  const myName = buffer.toString().trim();
  if (myName !== null) {
  console.log(`Your name is: ${myName}`);
  }
});

process.stdin.on('end', () => {
  console.log('This important software is now closing');
});
