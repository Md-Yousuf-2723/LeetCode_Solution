# Problem Link 
https://leetcode.com/problems/integer-to-roman/

## SS of submission
![[leetcode12.png]]

```C++
string intToRoman(int num){
const string tho[] = {"","M","MM","MMM"};
const string hun[] = {"","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"};
const string ten[] = {"","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"};
const string ones[] = {"","I","II","III","IV","V","VI","VII","VIII","IX"};
return tho[num/1000]
		+ hun[(num%1000)/100]
		+ ten[(num%100)/10]
		+ ones[num%10];
}
```


