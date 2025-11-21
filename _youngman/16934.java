import java.io.*;
import java.util.*;

// 1. 트라이 노드 클래스 정의
class TrieNode {
    // 다음 문자를 위한 자식 노드 맵
    Map<Character, TrieNode> children;
    // 이 접두사를 포함하는 닉네임의 개수 (충돌 검사에 사용)
    int count;

    public TrieNode() {
        children = new HashMap<>();
        count = 0;
    }
}

public class 게임닉네임 {
    // 닉네임 전체가 중복될 경우의 횟수 관리 (e.g. baekjoon이 몇 번 등장했는지)
    static HashMap<String, Integer> fullNicknameCount = new HashMap<>();
    static TrieNode root = new TrieNode(); // 트라이의 루트 노드

    public static void main(String[] args) throws IOException {
        // 입력 속도 향상을 위해 BufferedReader 사용
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 첫 줄에서 N 값(유저 수)을 읽음
        int N = Integer.parseInt(br.readLine());

        StringBuilder result = new StringBuilder(); // 최종 출력을 모으기 위한 StringBuilder

        for (int i = 0; i < N; i++) {
            String nickname = br.readLine();

            // 1. 닉네임이 완전 중복되는 경우 처리 (e.g., baekjoon -> baekjoon2)
            if (fullNicknameCount.containsKey(nickname)) {
                // 기존 등장 횟수를 가져와 +1 하고 별칭을 '닉네임 + 숫자'로 만듦
                int count = fullNicknameCount.get(nickname) + 1;
                fullNicknameCount.put(nickname, count);
                result.append(nickname).append(count).append('\n');
            }
            // 2. 닉네임이 처음 등장하는 경우 (가장 짧은 유일 접두사 찾기)
            else {
                // 트라이를 통해 별칭을 찾고 삽입하는 함수 호출
                String alias = findAndInsertAlias(nickname);
                result.append(alias).append('\n');
                fullNicknameCount.put(nickname, 1); // 새로운 닉네임 등록
            }
        }

        System.out.print(result);
    }

    /**
     * 닉네임을 트라이에 삽입하고, 가장 짧은 유일 접두사(별칭)를 찾아 반환합니다.
     */
    private static String findAndInsertAlias(String nickname) {
        TrieNode current = root;
        StringBuilder currentPrefix = new StringBuilder();
        String alias = "";
        boolean aliasFound = false;

        // 1. 별칭을 찾으면서 동시에 트라이 구조를 탐색
        for (int i = 0; i < nickname.length(); i++) {
            char ch = nickname.charAt(i);

            // 현재 문자를 접두사에 추가
            currentPrefix.append(ch);

            TrieNode next = current.children.get(ch);

            // 다음 노드가 없으면 새로 만듭니다. (새로운 경로 시작)
            if (next == null) {
                next = new TrieNode();
                current.children.put(ch, next);
            }

            // 별칭이 아직 결정되지 않았을 때만 검사
            if (!aliasFound) {
                // 이 경로(접두사)가 이전에 다른 닉네임의 접두사로 사용된 적이 없다면 (count == 0)
                // 또는 이 경로가 처음 만들어진 경우 -> 가장 짧은 유일 접두사입니다.
                if (next.count == 0) {
                    alias = currentPrefix.toString();
                    aliasFound = true;
                }
            }

            // 다음 노드로 이동
            current = next;
        }

        // 2. 별칭이 발견되지 않은 경우 (모든 접두사가 다른 닉네임에 의해 사용된 경우)
        // 이 경우, 닉네임 전체(길이 L)가 별칭이 됩니다. (예: baekjoon)
        if (!aliasFound) {
            alias = nickname;
        }

        // 3. 트라이에 닉네임 전체 경로를 다시 삽입(접근)하면서 count를 1 증가시켜 다른 닉네임과의 충돌 정보를 갱신
        current = root;
        for (char ch : nickname.toCharArray()) {
            // 이미 위에서 노드를 생성했으므로 get으로 접근 가능
            current = current.children.get(ch);
            current.count++;
        }

        return alias;
    }
}