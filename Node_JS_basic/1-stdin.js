// We use the 'readline' module to interact with the user through the command line.
const readline = require('readline');

// Create an interface to read input and show output to the user.
const rl = readline.createInterface({
  input: process.stdin,  // Reading from the command line
  output: process.stdout  // Writing to the command line
});

// Ask the user for their name with a friendly prompt
rl.question('Welcome to Holberton School, what is your name?\n', (name) => {
  // Once the user answers, print out their name
  console.log(`Your name is: ${name}`);

  // When the user is done, let's say goodbye with a message
  rl.on('close', () => {
    console.log('This important software is now closing');
  });

  // Close the interface after the user enters their name.
  rl.close();
});
