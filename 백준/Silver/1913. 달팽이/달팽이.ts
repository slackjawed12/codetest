import fs = require("fs");

const [N, target] = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map(Number);

interface MoverState {
  handle(mover: Mover, matrix: number[][]): MoverState;
}
class LeftState implements MoverState {
  handle(mover: Mover, matrix: number[][]): MoverState {
    const [x, y] = [mover.x, mover.y];
    matrix[y][x] = mover.num--;
    if (x === 0 || matrix[y][x - 1] !== 0) {
      mover.y++;
      return new DownState();
    }
    mover.x--;
    return this;
  }
}
class RightState implements MoverState {
  handle(mover: Mover, matrix: number[][]): MoverState {
    const [x, y] = [mover.x, mover.y];
    matrix[y][x] = mover.num--;
    if (x === matrix.length - 1 || matrix[y][x + 1] !== 0) {
      mover.y--;
      return new UpState();
    }
    mover.x++;
    return this;
  }
}
class UpState implements MoverState {
  handle(mover: Mover, matrix: number[][]): MoverState {
    const [x, y] = [mover.x, mover.y];
    matrix[y][x] = mover.num--;
    if (y === 0 || matrix[y - 1][x] !== 0) {
      mover.x--;
      return new LeftState();
    }
    mover.y--;
    return this;
  }
}

class DownState implements MoverState {
  handle(mover: Mover, matrix: number[][]): MoverState {
    const [x, y] = [mover.x, mover.y];
    matrix[y][x] = mover.num--;
    if (y === matrix.length - 1 || matrix[y + 1][x] !== 0) {
      mover.x++;
      return new RightState();
    }
    mover.y++;
    return this;
  }
}
class Mover {
  x: number;
  y: number;
  num: number;
  state: MoverState;
  constructor(x: number, y: number, num: number, state: MoverState) {
    this.x = x;
    this.y = y;
    this.num = num;
    this.state = state;
  }
  move(matrix: number[][]): [number, number] {
    this.state = this.state.handle(this, matrix);
    return [this.x, this.y];
  }
}

const mover = new Mover(0, 0, N * N, new DownState());
const matrix = Array.from(Array(N), (_) => Array.from(Array(N), (_) => 0));
matrix[mover.y][mover.x] = mover.num;
let [ax, ay] = [0, 0];

while (mover.num > 0) {
  if (mover.num === target) {
    [ax, ay] = [mover.x + 1, mover.y + 1];
  }
  mover.move(matrix);
}

console.log(matrix.map((row) => row.join(" ")).join("\n"));
console.log([ay, ax].join(" "));
