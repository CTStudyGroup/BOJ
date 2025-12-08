/** BOJ1493_박스채우기
 * # 문제
 * - length × width × height 크기의 박스를 한 변의 길이는 2의 제곱꼴인 정육면체 큐브로 재워야함
 * - 목표: 큐브의 최소 개수 || -1
 *
 *
 * # 제한
 * - 2초
 * - 128MB
 * - 1 ≤ length, width, height ≤ 10^6
 * - 1 ≤ n ≤ 20
 * - 0 ≤ Ai < 20
 * - 0 ≤ Bi ≤ 10^6
 *
 * - int 써도 될듯?
 *
 * - 시간이 2촌대 지금 이대로 하면
 * - 10^6 * 10^6 * 10^6 짜리 공간을 1로만 채워야할때,,, 재귀적으로 이걸 다 탐색하게되는구나...!
 * - 그러면 1만 남았을 때, 간단히 처리하는 로직을 추가할까?
 *
 *
 * # 풀이
 * - 그냥 분할 정복으로 반씩 나눠서 풀면 될 것 같은데 -> 아니다..
 * - 큐브의 종류와 개수가 정해져 있음...
 * - L W H 중에 가장 작은 걸 기준으로 큐브 한개를 쓰고, 나머지를 나눔?
 * - 아니면 큐브 개수가 정해져 있으니까, 큰 큐브부터 하나 넣고 나머지 부분 탐색? 근데,, 3차원인데 괜찮을까?
 *
 */

import java.io.*;
import java.util.*;
public class BOJ1493_박스채우기 {
    static int length, width, height, N;
    static long oneCube = 0;
    static Map<Integer, Integer> cubes = new TreeMap<>(Collections.reverseOrder());   // key 기준 정렬

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] temp = br.readLine().split(" ");
        length = Integer.parseInt(temp[0]);
        width = Integer.parseInt(temp[1]);
        height = Integer.parseInt(temp[2]);

        N = Integer.parseInt(br.readLine());
        int cube, cnt;
        for (int n=0; n<N; n++) {
            temp = br.readLine().split(" ");
            cube = Integer.parseInt(temp[0]);
            cnt = Integer.parseInt(temp[1]);
            if (cube == 0) oneCube = cnt;
            else cubes.put(cube, cnt);

        }

        System.out.println(fillCube(0,0,0,length,width,height));
    }

    static int fillCube(int x, int y, int z, int l, int w, int h) {
//        System.out.println();
//        System.out.println(x + " " + y + " " + z);
//        System.out.println(l + " " + w + " " + h);
        if (l <= 0 || w <= 0 || h <= 0) return 0;

        // 남아있는 가장 큰 큐브로 채우기
        int result = 0;
        int min = l > w ? (w > h ? h : w) : (l > h ? h : l);
        int c = 0;

        for (int cube : cubes.keySet()) {
            c = (int) Math.pow(2,cube);
            if (c <= min && cubes.get(cube) != 0) {
                result ++;
                int cubeCnt = cubes.get(cube) - 1;
                if (cubeCnt == 0) {
                    cubes.remove(cube);
                } else {
                    cubes.put(cube, cubeCnt);
                }
                break;
            }
        }
//        System.out.println(cubes.toString());
//        System.out.println(result);
        if (result == 0) {
//            System.out.println(oneCube);
//            System.out.println(l*w*h);
            oneCube -= (long) l*w*h;
            result += (long) l*w*h;
            if (oneCube < 0) return -1;
            else return result;
        }

        // 나머지 부분 정육면체 형태로 분할해서 fillCube 호출
        // 만일 중간에 호출한 결과가 -1이면 -1 return
        // 오른쪽
        int cnt;
        cnt = fillCube(x+c, y, z, l-c, w, h); // x
        if (cnt == -1) return -1;
        else result += cnt;

        // 오른쪽 제외 뒤쪽
        cnt = fillCube(x, y+c, z, c, w-c, h); // x
        if (cnt == -1) return -1;
        else result += cnt;

        // 똑같은 xy의 위쪽
        cnt = fillCube(x, y, z+c, c, c, h-c); // x
        if (cnt == -1) return -1;
        else result += cnt;

        // 아니면 호출한 결과끼리 더하고 + 1해서 return
        return result;
    }
}
