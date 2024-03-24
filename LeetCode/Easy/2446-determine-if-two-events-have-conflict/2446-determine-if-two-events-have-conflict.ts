function haveConflict(event1: string[], event2: string[]): boolean {
  const convertTime = (timeString: string) => {
    const [hour, minute] = timeString.split(":");
    return parseInt(hour) * 60 + parseInt(minute);
  };

  const converted1 = event1.map(convertTime);
  const converted2 = event2.map(convertTime);
  const prev = converted1[0] < converted2[0] ? converted1 : converted2;
  const next = converted1[0] < converted2[0] ? converted2 : converted1;
  return prev[1] >= next[0];
}
