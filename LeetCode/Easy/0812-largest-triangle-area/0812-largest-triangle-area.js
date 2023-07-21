/**
 * @param {number[][]} points
 * @return {number}
 */
var largestTriangleArea = function(points) {
  let result = 0;
  for(let i=0; i<points.length-2; i++){
      const startX = points[i][0];
      const startY = points[i][1];
      for(let j=i+1; j<points.length-1; j++){
          for(let k=j+1; k<points.length; k++){
              const v1 = [points[j][0] - startX, points[j][1] - startY];
              const v2 = [points[k][0] - startX, points[k][1] - startY];
              const area = (Math.abs(v1[0]*v2[1]-v1[1]*v2[0])/2).toFixed(5);
              result = Math.max(area, result);
          }
      }
  }
    
    return result;
};