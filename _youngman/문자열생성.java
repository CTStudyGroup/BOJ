import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        List<Character> word = new ArrayList<>(), list = new ArrayList<>();
        for (int i=0;i<N;i++) {
            word.add(br.readLine().charAt(0));
        }
        int front = 0, end = N-1;
        while(front<=end) {
            if (word.get(front)<word.get(end)) list.add(word.get(front++)); // 앞쪽 글자가 더 작을 때
            else if (word.get(front)>word.get(end)) list.add(word.get(end--)); // 뒷쪽 글자가 더 작을 때
            else { // 앞, 뒤 문자가 같을 때
                int tempF = front+1, tempE = end-1, size = list.size();
                while(tempF<=tempE) {
                    if (word.get(tempF)<word.get(tempE)) { // 앞쪽과 가까운 문자가 더 작은 값이면
                        list.add(word.get(front++)); // 앞쪽 글자 list에 추가
                        break;
                    }
                    else if (word.get(tempF)>word.get(tempE)) { // 뒷쪽과 가까운 문자가 더 작은 값이면
                        list.add(word.get(end--)); // 뒷쪽 글자 list에 추가
                        break;
                    }
                    else tempF++; tempE--; // 계속 같을 시
                }
                // 만약 리스트에 값이 추가가 되지 않았다면 모든 값이 똑같으므로 앞쪽 글자 list에 추가
                if (size==list.size()) list.add(word.get(front++));
            }
        }
        for (int i=0;i<list.size();i++) {
            if (i!=0 && i%80==0) System.out.println(); // 80글자마다 새줄 문자 출력
            System.out.print(list.get(i));
        }
    }
}