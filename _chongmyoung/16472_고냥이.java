import java.util.*;
class Main {
  public static int solution(char[] arr, int n){
    int answer = 0;
    int left = 0, right = 0;
    int[] count = new int[26];// 알파벳 갯수
    int kind = 0; // 현재 다른 알파벳 종류 수
    
    while(right < arr.length){
      int r = arr[right] - 'a';
      if(count[r] == 0) kind++;
      count[r]++;
      right++;

      while(n < kind){
        int l = arr[left] - 'a';
        count[l]--;
        if(count[l] == 0) kind--;
        left++;
      }
      answer = Math.max(answer, right - left);
    }
    return answer;
  }

  public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    String s = sc.next();
    char[] arr = s.toCharArray();
    System.out.println(solution(arr, n));
  }
}
