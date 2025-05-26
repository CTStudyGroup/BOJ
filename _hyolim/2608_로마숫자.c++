#include <iostream>
#include <string>
#include <map>

using namespace std;

string str1, str2;

map<char,int> m;

int toNum(string temp){
	int num=0;
	for(int i=0;i<temp.length();i++){
		if(i!=temp.length()-1){
			if(temp[i]=='I'&&temp[i+1]=='V'){
				num+=4;
				i++; continue;
			}
			if(temp[i]=='I'&&temp[i+1]=='X'){
				num+=9;
				i++; continue;
			}
			if(temp[i]=='X'&&temp[i+1]=='L'){
				num+=40;
				i++; continue;
			}
			if(temp[i]=='X'&&temp[i+1]=='C'){
				num+=90;
				i++; continue;
			}
			if(temp[i]=='C'&&temp[i+1]=='D'){
				num+=400;
				i++; continue;
			}
			if(temp[i]=='C'&&temp[i+1]=='M'){
				num+=900;
				i++; continue;
			}
		}
		num+=m[temp[i]];
	}
	return num;
}

string toString(int num){
	string temp;


	for(int i=0;i<num/1000;i++){
		temp+="M";
	}

	num%=1000;

	if(num/100==4){
		temp+="CD";
	}else if(num/100==9){
		temp+="CM";
	}else{
		if(num/100>=5) {
			temp+="D";
			num-=500;
		}
		for (int i = 0; i < num/100; ++i)
		{
			temp+="C";
		}
	}
	num%=100;

	if(num/10==4){
		temp+="XL";
	}else if(num/10==9){
		temp+="XC";
	}else{
		if(num/10>=5) {
			temp+="L";
			num-=50;
		}
		for (int i = 0; i < num/10; ++i)
		{
			temp+="X";
		}
	}
	num%=10;

	if(num==4){
		temp+="IV";
	}else if(num==9){
		temp+="IX";
	}else{
		if(num>=5) {
			temp+="V";
			num-=5;
		}
		for (int i = 0; i < num; ++i)
		{
			temp+="I";
		}
	}

	return temp;
}

void solve(){
	m['I']=1;
	m['V']=5;
	m['X']=10;
	m['L']=50;
	m['C']=100;
	m['D']=500;
	m['M']=1000;
	// 1. 보통 왼쪽에 큰 숫자를, 오른쪽에 작은 숫자

	// 2. V(5), L(50), D(500)는 한 번만 사용 가능
	// 3. I(1), X(10), C(100), M(1000)은 연속 세 번까지 가능
	// 4. IV(4), IX(9), XL(40), XC(90), CD(400), CM(900) 만 가능
	//    4-1. 이들 각각은 한 번씩만 사용 가능
	//    4-2. (IV,IX) , (XL,XC), (CD,CM) 같이 사용 불가
	// 5. 모든 수는 가장 적은 개수의 로마 숫자들로 표시해야함

	// 판별 순서
	// 1. 4번인지 확인한다.
	// 2. 그냥 더한다.
	int answer=toNum(str1)+toNum(str2);
	cout<<answer<<"\n";
	cout<<toString(answer);
	// cout<<"\n"<<toString(4);

}

int main(){
	cin>>str1>>str2;
	solve();
}