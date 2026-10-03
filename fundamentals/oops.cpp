#include <iostream>

class Node {
public:
	int data;
	Node* next;

	Node(int value) : data(value), next(nullptr) {}
};

int main() {
	Node first(10);
	Node second(20);

	first.next = &second;

	std::cout << first.data << " -> " << first.next->data << " -> nullptr\n";
	return 0;
}


