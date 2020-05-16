import java.util.*;
import java.lang.*;
import java.io.*;

class Solution {
    public int maxSubarraySumCircular(int[] A) {
        int sum = A[0];
        int max = A[0];
        int K = 0, cs = 0;
        // initial Kadane
        for(int i=1;i<A.length;i++){
            sum = Math.max(A[i], sum + A[i]);
            max = Math.max(max, sum);
        }
        K = max;
        // Circular Sum or sum of all elements
        for(int i = 0; i < A.length; i++){
            cs  += A[i];
        }
        // multiplying all element with -1
        for(int  i = 0 ; i < A.length; i++){
            A[i] = A[i] * -1;
        }
        // Second Kadane Sum
        sum = A[0];
        max = A[0];
        for(int i=1;i<A.length; i++){
            sum = Math.max(A[i], sum + A[i]);
            max = Math.max(max , sum);
        }
        cs += max;
        if (cs > K && cs != 0)
            return cs;
        else
            return K;
        
    }
}