function countTestedDevices(batteryPercentages: number[]): number {
  let counter = 0;
  for (let i = 0; i < batteryPercentages.length; i++) {
    if (batteryPercentages[i] > 0) {
      counter += 1;
      for (let j = i + 1; j < batteryPercentages.length; j++) {
        batteryPercentages[j] -= batteryPercentages[j] > 0 ? 1 : 0;
      }
    }
  }

  return counter;
}
