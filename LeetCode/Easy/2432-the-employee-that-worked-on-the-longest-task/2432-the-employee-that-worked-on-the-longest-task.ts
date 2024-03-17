function hardestWorker(n: number, logs: number[][]): number {
  let maxHour = 0;
  let answer = 999999;
  for (let i = 0; i < logs.length; i++) {
    const worker = logs[i][0];
    const hour = i === 0 ? logs[i][1] : logs[i][1] - logs[i - 1][1];
    if (hour > maxHour) {
      answer = worker;
      maxHour = hour;
    } else if (hour === maxHour) {
      answer = Math.min(worker, answer);
    }
  }

  return answer;
}
