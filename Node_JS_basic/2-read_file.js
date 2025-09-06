const fs = require('fs');

function countStudents (file) {
  try {
    const data = fs.readFileSync(file, 'utf-8');
    const lines = data.trim().split('\n');
    const students = lines.slice(1).filter((line) => line.trim() !== '');

    console.log(`Number of students: ${students.length}`);

    const studentFields = {};

    students.forEach((line) => {
      const parts = line.split(',');
      const firstname = parts[0];
      const field = parts[3];

      if (!studentFields[field]) {
        studentFields[field] = [];
      }
      studentFields[field].push(firstname);
    });

    for (const field in studentFields) {
      const names = studentFields[field];
      console.log(
        'Number of students in ' + field + ': ' + names.length + '. List: ' + names.join(', ')
      );
    }
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
