class Solution { 
    boolean LieOnLine(int a[], int b[], int c[])
    {
        int x = a[0], y = a[1];
        int x1 = b[0], y1 = b[1];
        int x2 = c[0], y2 = c[1];
        if ((x-x1)*(y1-y2) == (x1-x2)*(y-y1))
            return true;
        else
            return false;
    }
    public boolean checkStraightLine(int[][] coordinates) {
        for(int i=2;i<coordinates.length; i++){
            if(!LieOnLine(coordinates[0], coordinates[1], coordinates[i]))
                return false;
        }
        return true;
    }
  
}