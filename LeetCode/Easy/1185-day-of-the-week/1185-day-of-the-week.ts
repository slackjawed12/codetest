function dayOfTheWeek(day: number, month: number, year: number): string {
    const date = new Date(`${year}-${month<10?'0'+month : month}-${day<10?'0'+day:day}`);
    switch(date.getDay()){
        case 0:
            return "Sunday";
        case 1:
            return "Monday";
        case 2:
            return "Tuesday";
        case 3:
            return "Wednesday";
        case 4:
            return "Thursday";
        case 5:
            return "Friday";
        case 6:
            return "Saturday";
    }
};