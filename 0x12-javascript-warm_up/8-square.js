#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  let msg = '';
  for (let i = 0; i < size; i++) {
    msg += 'X';
  }
  for (let j = 0; j < size; j++) {
    console.log(msg);
  }
}
