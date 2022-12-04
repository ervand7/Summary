#include <iostream>

// Node отдельный объект односвязного списка
class Node {
// определим 2 публичные переменные
public:
    double data; // храним как вещественное значение
    Node* next; // ссылка на следующий объект

// объявим конструктор:
public:
    Node(double data) {
        this->data = data;
        this->next = NULL;
    }
};

// пропишем основной класс
class OneLinkedList {
public:
    // публичные переменные: ссылка на первый и последний объект
    Node* head, * tail;

// пропишем конструктор этого класса
public:
    OneLinkedList() {
        this->head = this->tail = NULL;
    }

    // прописываем деструктор
    ~OneLinkedList() {
        while(head != NULL) pop_front();
    }

    // прописываем метод, позволяющий удалять первый объект в односвязном списке
    void pop_front(){
        if(head == NULL) return;
        if(head == tail) {
            delete tail;
            head = tail = NULL;
            return;

        }
        // создадим временный указатель Node
        Node* node = head;
        head = node->next;
        delete node;
    }

    // пропишем метод, который будет добавлять объект в конец односвязного списка
    void push_back(double data) {
        // создаем новый объект используя конструктор класса Node
        Node* node = new Node(data);
        if(head == NULL) head = node;
        if (tail != NULL) tail->next = node;
        tail = node;
    }

    // пропишем метод, который будет добавлять объект в начало односвязного списка
    void push_front(double data) {
        Node* node = new Node(data);
        node->next = head;
        head = node;
        if (tail == NULL) tail = node;
    }

    // пропишем метод, который будет удалять объект с конца списка
    void pop_back() {
        if (tail == NULL) return;
        if (head == tail) {
            delete tail;
            head = tail = NULL;
            return;
        }

        // создадим временный указатель Node
        Node* node = head;
        for(;node->next != tail; node = node->next);
        node->next = NULL;
        delete tail;
        tail = node;
    }

    // пропишем метод, возвращающий объект по индексу k
    Node* getAt(int k) {
        if (k < 0) return NULL;
        // создадим временный указатель Node
        Node* node = head;
        // создадим счетчик индексов
        int n = 0;
        while(node && n != k && node->next) {
            node = node->next;
            n++;
            
        }

        return (n==k) ? node : NULL;
    }

    // пропишем метод вставки элемента по указанному индексу
    void insert(int k, double data) {
        Node* left = getAt(k);
        if (left == NULL) return;

        Node* right = left->next;
        // создаем новый объект используя конструктор класса Node
        Node* node = new Node(data);

        left->next = node;
        node->next = right;
        if (right == NULL) tail = node;
    }

    // пропишем метод удаления промежуточного элемента
    void erase (int k) {
        if (k < 0) return;
        if (k == 0) {
            pop_front();
            return;
        }

        Node* left = getAt(k - 1);
        Node* node = left->next;
        if (node == NULL) return;
        Node* right = node->next;
        left->next = right;
        if (node == tail) tail = left;
        delete node;
    }


};

int main()
{
    OneLinkedList lst;
    lst.push_front(1);
    lst.push_back(2);

    Node* n = lst.getAt(0);
    double d = (n != NULL) ? n->data : 0;
    std::cout << d << std::endl;

    lst.erase(1);
    lst.insert(0, 5);
    lst.insert(0, 2);
    for(Node* node = lst.head; node != NULL; node = node->next)
        std::cout << node->data << " ";

    std::cout << std::endl;
    return 0;
}