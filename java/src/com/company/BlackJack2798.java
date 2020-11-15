package com.company;

import java.io.*;
import java.util.StringTokenizer;

public class BlackJack2798 {
    static int n, m;
    static int [] cardArray;
    static int answer = 0;

    static int getMinValue(int a, int b) {
        int absA = Math.abs(m - a);
        int absB = Math.abs(m - b);
        if (absA < absB) return a;
        else return b;
    }

    static void countSumOfCards(int r, int cur, int start, int sum) {

        if (sum > m) return;

        if (r == cur) {
            answer = Math.max(sum, answer);
            return;
        } else {
            for (int i = start; i < n; i++) {
                countSumOfCards(r, cur+1, i+1, sum + cardArray[i]);
            }
        }

    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer nm = new StringTokenizer(br.readLine());

        n = Integer.parseInt(nm.nextToken());
        m = Integer.parseInt(nm.nextToken());

        cardArray = new int[n];

        StringTokenizer cards = new StringTokenizer(br.readLine());
        for (int i=0; i < n; i++) {
            cardArray[i] = Integer.parseInt(cards.nextToken());
        }

        countSumOfCards(3, 0, 0,0);
        System.out.println(answer);
        bw.write(answer);
    }
}
