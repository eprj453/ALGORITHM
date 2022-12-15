package com.company;

import java.io.*;
import java.util.StringTokenizer;

public class Sudoku2580 {

    static int [][] sudokuBoard = new int[9][9];
    public static void main(String[] args) throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int i = 0; i < 9; i++) {
            StringTokenizer line = new StringTokenizer(br.readLine());
            for (int j = 0; j < 9; j++) {
                sudokuBoard[i][j] = Integer.parseInt(line.nextToken());

            }
        }

    }
}
