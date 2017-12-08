import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class SolutionFib {
    public static void main(String args[] ) throws Exception {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT */
        int n;
        BigInteger t1,t2,R;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        String[] strs = line.trim().split("\\s+");
        t1 = new BigInteger(strs[0]);
        t2 = new BigInteger(strs[1]);
        R = BigInteger.ZERO;
        n = Integer.parseInt(strs[2]);
        int  count = 2;
        while(count<n) {
        	//System.out.println("Hello");
        	R = t1.add(t2.multiply(t2));
        	t1 = t2;
        	t2 = R;
        	count++;
        }
        System.out.println(R);
    }
}
