class ParkingSystem {
    carSlot:{cur:number; max:number;}[];
    constructor(big: number, medium: number, small: number) {
        this.carSlot = [{cur:0, max:big},{cur:0, max:medium},{cur:0, max:small}];
    }

    addCar(carType: number): boolean {
        if(this.carSlot[carType-1].cur === this.carSlot[carType-1].max) {
            return false;
        }
        
        this.carSlot[carType-1].cur += 1;
        return true;
    }
}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * var obj = new ParkingSystem(big, medium, small)
 * var param_1 = obj.addCar(carType)
 */