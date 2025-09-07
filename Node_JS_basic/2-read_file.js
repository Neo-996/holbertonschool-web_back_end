const fs = require('fs'); // We're using the fs module to read the file

function countStudents(path) {
  try {
    // Let's read the CSV file synchronously, as we want to process it immediately
    const data = fs.readFileSync(path, 'utf8');

    // Split the data into lines, so we can work with each student entry individually
    const lines = data.trim().split('\n');
    
    // Initialize an object to store the field counts
    const fields = {};
    let studentCount = 0; // Total number of students

    // Go through each line, except the first (header) line
    lines.slice(1).forEach((line) => {
      const [firstName, field] = line.split(',');
      
      if (field) {  // Only process valid student records (skip empty lines)
        if (!fields[field]) {
          fields[field] = [];  // If we haven't seen this field before, create a new array
        }
        fields[field].push(firstName);  // Add the student's name to the field's list
        studentCount++;  // Increment the total student count
      }
    });

    // Print the total number of students
    console.log(`Number of students: ${studentCount}`);

    // For each field, print out the number of students and their names
    Object.keys(fields).forEach((field) => {
      console.log(`Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`);
    });

  } catch (error) {
    // If there's an error reading the file, let's let the user know
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
