class Solution {
    public int islandPerimeter(int[][] grid) {
        Queue<List<Integer>> q = new LinkedList<>();
        int[][] visit = new int[grid.length][grid[0].length];
        int[][] d = {{0, -1}, {1, 0}, {0, 1}, {-1, 0}};
        int answer = 0;
        for(int i=0; i<grid.length; i++){
            for(int j=0; j<grid[0].length; j++){
                if(grid[i][j]==1 && visit[i][j] == 0) {
                    visit[i][j]=1;
                    q.add(List.of(j, i));
                } 
                
                while(!q.isEmpty()){
                    List<Integer> cur = q.poll();
                    for(int k = 0; k < 4; k++){
                        int nx = cur.get(0) + d[k][0];
                        int ny = cur.get(1) + d[k][1];
                        if(nx>=0 && nx < grid[0].length && ny >=0 && ny < grid.length) {
                            if(grid[ny][nx]==0) {
                                answer++;
                            } else if(visit[ny][nx] ==0){
                                visit[ny][nx]=1;
                                q.add(List.of(nx, ny));
                            }
                        } else {
                            answer++;
                        }
                    }
                }
            }
        }
        
        return answer;
    }
}