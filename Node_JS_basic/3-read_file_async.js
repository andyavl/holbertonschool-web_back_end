const fs = require('fs');

function countStudents (file) {
  return new Promise((resolve, reject) => {
    fs.readFile(file, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      try {
        const lines = data.trim().split('\n');
        const students = lines.slice(1).filter((line) => line.trim() !== '');

        console.log('Number of students: ' + students.length);

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

        resolve();
      } catch (error) {
        reject(new Error('Cannot load the database'));
      }
    });
  });
}

module.exports = countStudents;
