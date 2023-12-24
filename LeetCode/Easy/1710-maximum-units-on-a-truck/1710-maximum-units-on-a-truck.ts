function maximumUnits(boxTypes: number[][], truckSize: number): number {
  boxTypes.sort((o1, o2) => o2[1] - o1[1]);
  return boxTypes.reduce(
    (prev, cur) => {
      const extraSpace = truckSize - prev.boxes;
      const putBoxCount = Math.min(extraSpace, cur[0]);

      return {
        units: prev.units + cur[1] * putBoxCount,
        boxes: prev.boxes + putBoxCount,
      };
    },
    { units: 0, boxes: 0 }
  ).units;
}
