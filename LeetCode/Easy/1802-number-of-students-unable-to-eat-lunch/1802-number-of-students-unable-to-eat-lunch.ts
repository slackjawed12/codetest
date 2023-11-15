function countStudents(students: number[], sandwiches: number[]): number {
    let count = 0;
    while(count < students.length) {
        if(students[0] === sandwiches[0]) {
            count = 0;
            students.shift();
            sandwiches.shift();
        } else {
            students.push(students.shift());
            count++;
        }
    }
    return students.length;
};