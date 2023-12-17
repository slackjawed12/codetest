function minMovesToSeat(seats: number[], students: number[]): number {
  seats.sort((o1, o2) => o1 - o2);
  students.sort((o1, o2) => o1 - o2);
  let result = 0;
  for (let i = 0; i < seats.length; i++) {
    result += Math.abs(students[i] - seats[i]);
  }
  return result;
}
