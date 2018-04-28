#include <stdio.h>
#include "stack.cpp"

int main() {
	
	stack<char> s('h');
	s.push('e');
	s.push('l');
	s.push('l');
	s.push('o');
	s.push(' ');
	s.push('w');
	s.push('o');
	s.push('r');
	s.push('l');
	s.push('d');
	
	s.print();

	printf("size : %d\n",s.size());
	
	return 0 ;
}
