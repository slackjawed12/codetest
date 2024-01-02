function lemonadeChange(bills: number[]): boolean {
  let store = {
    "5": 0,
    "10": 0,
    "20": 0,
  };

  for (const bill of bills) {
    if (bill === 5) {
      store["5"] += 1;
    } else if (bill === 10) {
      if (store["5"] >= 1) {
        store["5"] -= 1;
        store["10"] += 1;
      } else {
        return false;
      }
    } else {
      if (store["10"] >= 1 && store["5"] >= 1) {
        store["5"] -= 1;
        store["10"] -= 1;
        store["20"] += 1;
      } else if (store["5"] >= 3) {
        store["5"] -= 3;
        store["20"] += 1;
      } else {
        return false;
      }
    }
  }

  return true;
}
