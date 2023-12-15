function finalValueAfterOperations(operations: string[]): number {
  return operations.reduce((prev, cur) => {
    if (cur[1] == "-") {
      return prev - 1;
    }
    return prev + 1;
  }, 0);
}
