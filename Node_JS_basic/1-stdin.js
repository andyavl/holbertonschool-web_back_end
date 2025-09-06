console.log('Welcome to Holberton School, what is your name?');

process.stdin.on('data', (buffer) => {
  const INPUT = buffer.toString().trim();
  console.log(`Your name is: ${INPUT}`);
});

process.stdin.on('end', () => {
  console.log('This important software is now closing');
});
