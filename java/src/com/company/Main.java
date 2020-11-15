package com.company;


import java.io.*;
import java.util.*;

public class Main {

    private static int n, m, v;
    private static boolean[] visited;
    private static int [][] graph;
    private static ArrayList<String> answer;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        v = Integer.parseInt(st.nextToken());

        graph = new int[n+1][n+1];
        visited = new boolean[n+1];
        answer = new ArrayList<String>();
        for (int i=0; i < m; i++) {
            StringTokenizer nodes = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(nodes.nextToken());
            int y = Integer.parseInt(nodes.nextToken());
            graph[x][y] = 1;
            graph[y][x] = 1;
        }

        dfs(1);
        writeAnswer();
        bfs();
        writeAnswer();







    }

    public static void init() {
        answer = new ArrayList<String>();
        visited = new boolean[n+1];
    }

    public static void writeAnswer() throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        for (int i=0; i < answer.size(); i++) {
            bw.write(answer.get(i));
            if (i < answer.size()-1) bw.write(" ");
        }
        bw.newLine();
        bw.flush();


    }

    public static void dfs(int node) {
        visited[node] = true;
        answer.add(Integer.toString(node));
        for (int i=1; i<n+1; i++) {
            if (graph[node][i] == 1 && !visited[i]) {
                dfs(i);
            }

        }
    }

    public static void bfs() {
        Queue<Integer> q = new LinkedList<>();
        q.offer(1);
        visited[1] = true;
        while (!q.isEmpty()) {
            int node = q.poll();
            answer.add(Integer.toString(node));
            for (int i=1; i<n+1; i++) {
                if (graph[node][i] == 1 && !visited[i]) {
                    visited[i] = true;
                    q.offer(i);
                }
            }
        }
    }


}
