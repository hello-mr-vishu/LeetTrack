class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        int[][] result = new int[intervals.length+1][2];
        int i = 0;
        int j = 0;

        while (i<intervals.length && intervals[i][1]<newInterval[0]){
          result[j++] = intervals[i++];
        }

        while(i<intervals.length && intervals[i][0] <= newInterval[1]){
          newInterval[0] = Math.min(newInterval[0] , intervals[i][0]);
          newInterval[1] = Math.max(newInterval[1], intervals[i++][1]);
        }

        result[j++] = newInterval;
        while (i<intervals.length){
          result[j++] = intervals[i++];
        }


        return java.util.Arrays.copyOf(result,j);


    }
}