#include <iostream>
#include <cstring>
using namespace std;

class Queue
{
private:
	typedef struct _node
	{
		int data;
		_node* next;
	}Node;
	Node* front;
	Node* rear;
	int size;

public:
	void QueueInit()
	{
		front = NULL;
		rear = NULL;
		size = 0;
	}
	void Enq(int data)
	{
		Node* nNode = new Node();
		nNode->data = data;
		nNode->next = NULL;
		if (front== NULL)
		{
			front = nNode;
			rear = nNode;
		}
		else
		{
			rear->next = nNode;
			rear = nNode;
		}
		size++;
	}
	int Deq()
	{
		Node* rnode = front;
		int rd = rnode->data;
		front = front->next;
		size--;
		delete rnode;
		return rd;
	}
	int GetFront()
	{
		return front->data;
	}
	int GetRear()
	{
		return rear->data;
	}
	int Getsize()
	{
		return size;
	}
	int empty()
	{
		if (size == 0) return 1;
		else return 0;
	}
};

void Josephus(Queue *pq, int vol, int order)
{
	int i, j;
	j = 0;
	int* temp = new int[vol+1];
	while (!pq->empty())
	{
		for (i = 0; i < order-1; i++)
		{
			pq->Enq(pq->Deq());
		}
		temp[j++] = pq->Deq();
	}

	cout << "<";
	for (int i = 0; i < vol; i++)
	{
		if (i == vol - 1) cout << temp[i];
		else cout << temp[i] << ", ";
	}
	cout << ">";
	delete[] temp;
}

int main(void)
{
	int N, K;
	cin >> N >> K;
	Queue *q=new Queue();
	q->QueueInit();
	for (int i = 1; i <= N; i++)
	{
		q->Enq(i);
	}
	
	Josephus(q, N, K);
	
	delete q;
	return 0;
}