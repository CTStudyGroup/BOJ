import java.io.*;
import java.util.*;

public class Main {
    static class Node {
        int prevLen; // 괄호 열리기 전까지 길이
        int mul;     // 반복 횟수 K

        Node(int prevLen, int mul) {
            this.prevLen = prevLen;
            this.mul = mul;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();

        Stack<Node> stack = new Stack<>();
        int length = 0; // 현재 구간 길이

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (c == '(') {
                int k = s.charAt(i - 1) - '0';

                // 바로 앞 숫자는 곱하기용이므로 길이에서 빼줌
                length--;

                // 스택에 (이전 길이, 반복 횟수) 저장
                stack.push(new Node(length, k));

                // 새로운 괄호 내부 시작 → 길이 초기화
                length = 0;
            } 
            else if (c == ')') {
                Node node = stack.pop();
                // 새로운 길이 = 이전까지의 길이 + K * (괄호 내부 길이)
                length = node.prevLen + node.mul * length;
            } 
            else {
                // 일반 문자일 경우 길이 +1
                length++;
            }
        }

        System.out.println(length);
    }
}
