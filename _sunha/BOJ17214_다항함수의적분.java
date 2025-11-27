/**
 * BOJ17214_다항함수의적분
 * # 문제
 * - 적분해서 출력
 * - 출력 형식
 * - 적분 상수: w
 * - 문자의 거듭제곱: x^2 == xx
 * <p>
 * # 제한
 * - 입력값 -> int 가능
 * - 2 <= abs(계수) < 10,000
 * - 0 <= abs(상수) < 10,000
 * <p>
 * # 풀이
 * - 그냥 풀면될것같은데
 */

import java.io.*;

public class BOJ17214_다항함수의적분 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String temp = br.readLine();
        String first = "0", second = "0";

        // 각각의 경우에 1을 생략해야함.
        // 상수항만 있는 경우
        if (!temp.contains("x")) {
            if (temp.equals("1")) {
                second = "";
            } else if (temp.equals("-1")) {
                second = "-";
            } else {
                second = temp;
            }
        }

        // 일차항만 있는 경우
        else if (temp.endsWith("x")) {
            temp = Integer.parseInt(temp.substring(0, temp.length() - 1)) / 2 + "";
            if (temp.equals("1")) {
                first = "";
            } else if (temp.equals("-1")) {
                first = "-";
            } else {
                first = temp;
            }
        }

        // 둘 다 있는 경우
        else {
            String[] nums = temp.split("x");
            nums[0] = Integer.parseInt(nums[0]) / 2 + "";
            if (nums[0].equals("1")) {
                first = "";
            } else if (nums[0].equals("-1")) {
                first = "-";
            } else {
                first = nums[0];
            }

            if (nums[1].equals("+1")) {
                second = "+";
            } else if (nums[1].equals("-1")) {
                second = "-";
            } else {
                second = nums[1];
            }
        }

        if (first.equals("0") && second.equals("0")) {
            System.out.println("W");
        } else if (first.equals("0")) {
            System.out.println(second + "x+W");
        } else if (second.equals("0")) {
            System.out.println(first + "xx+W");
        } else {
            System.out.println(first + "xx" + second + "x+W");
        }
    }
}
