package com.company;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.ParameterizedType;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.StringTokenizer;


class Planet {
    int planet_num;
    int x;
    int y;
    int z;

    public Planet(int planet_num, int x,  int y, int z) {
        this.planet_num = planet_num;
        this.x = x;
        this.y = y;
        this.z = z;
    }

    public String toString() {
        return String.format(" planet_num : %d, x: %d, y: %d, z: %d", this.planet_num, this.x, this.y, this.z);
    }
}

public class S2887 {



    public static void main(String[] args) throws IOException {
        ArrayList<Planet> planets = new ArrayList<>();

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            Planet p = new Planet(
                    i,
                    Integer.parseInt(st.nextToken()),
                    Integer.parseInt(st.nextToken()),
                    Integer.parseInt(st.nextToken())
            );

            planets.add(p);
        }

        planets.sort((o1, o2) -> {
            int x1 = o1.x;
            int x2 = o2.x;

            if (x1 == x2) return 0;
            else if (x1 > x2) return 1;
            else return -1;

        });


        for (Planet p: planets) {
            System.out.println(p);
        }


    }
}
