package com.company;

import java.io.*;
import java.util.StringTokenizer;

class Factorial {

    static int getFactorial(int number, int answer) {
        if (number == 0) {
            return answer;
        };
        return getFactorial(number-1, answer * number);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n  = Integer.parseInt(br.readLine());
        if (n == 0) bw.write("0");
        else bw.write(String.valueOf(getFactorial(n, 1)));
        bw.flush();
        bw.close();
    }
}
