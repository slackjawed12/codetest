function countTime(time: string): number {
  const hour = time.slice(0, 2);
  const minute = time.slice(3);
  let hourCount = 1;
  if (hour[0] === "?" && hour[1] === "?") {
    hourCount = 24;
  } else if (hour[0] === "?") {
    hourCount = parseInt(hour[1]) < 4 ? 3 : 2;
  } else if (hour[1] === "?") {
    hourCount = parseInt(hour[0]) === 2 ? 4 : 10;
  }

  let minuteCount = 1;
  if (minute[0] === "?" && minute[1] === "?") {
    minuteCount = 60;
  } else if (minute[0] === "?") {
    minuteCount = 6;
  } else if (minute[1] === "?") {
    minuteCount = 10;
  }

  return hourCount * minuteCount;
}
