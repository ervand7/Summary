#include <iostream>

// Node отдельный объект двусвязного списка
class Node {
// определим публичные данные
public:
    double data; // храним как вещественное значение
    Node* prev, * next; // указатели (тип Node) на предыдущий и след элементы двусвязного списка

// объявим конструктор:
public:
    Node(double data) {
        this->data = data;
        this->prev = this->next = NULL;
    }
};

// пропишем основной класс
class TwoLinkedList {
public:
    // публичные указатели на первый и последний объект двусвязного списка
    Node* head, * tail;

// пропишем конструктор этого класса
public:
    TwoLinkedList() {
        head = tail = NULL;
    }

// пропишем деструктор этого класса
public:
    ~TwoLinkedList() {
        while(head != NULL);
        pop_front();
    }

    // пропишем метод, который будет добавлять объект в начало двусвязного списка
    Node* push_front(double data) {
        // создадим временный указатель ptr
        Node* ptr = new Node(data);
        ptr->next = head;
        if (head != NULL)
            head->prev = ptr;
        if (tail == NULL)
            tail = ptr;
        head = ptr;
        return ptr;
    }

    // пропишем метод, который будет добавлять объект в конец двусвязного списка
    Node* push_back(double data) {
        // создадим временный указатель ptr
        Node* ptr = new Node(data);
        ptr->prev = tail;
        if (tail != NULL)
            tail->next = ptr;
        if (head == NULL)
            head = ptr;
        tail = ptr;
        return ptr;
    }

    // прописываем метод, позволяющий удалять первый объект двусвязного списка
    void pop_front(){
        if(head == NULL) return;
        // создадим временный указатель ptr
        Node* ptr = head->next;
        if (ptr != NULL)
            ptr->prev = NULL;
        else
            tail = NULL;
        delete head;
        head = ptr;
    }

    // прописываем метод, позволяющий удалять последний объект двусвязного списка
    void pop_back() {
        if(tail == NULL) return;
        // создадим временный указатель ptr
        Node* ptr = tail->prev;
        if (ptr != NULL)
            ptr->next = NULL;
        else
            head = NULL;
        delete tail;
        tail = ptr;
    }

    // пропишем метод, возвращающий объект по индексу
    Node* getAt(int index) {
        // создадим временный указатель ptr
        Node* ptr = head;
        // создадим счетчик индексов
        int n = 0;
        while(n != index) {
            if (ptr == NULL)
                return ptr;
            ptr = ptr->next;
            n++;
            
        }

        return ptr;
    }

    // создаем оператор [], чтобы получать элемент по индексу не только через getAt
    Node* operator [] (int index) {
        return getAt(index);
    }

    // пропишем метод для вставки элемента в произвольное место двусвязного списка 
    Node* insert(int index, double data){
        Node* right = getAt(index);
        if (right == NULL)
            return push_back(data);

        Node* left = right->prev;
        if (left == NULL)
            return push_front(data);

        Node* ptr = new Node(data);
        ptr->prev = left;
        ptr->next = right;
        left->next = ptr;
        right->prev = ptr;

        return ptr;
    }

    // пропишем метод удаления промежуточного элемента двусвязного списка
    void erase (int index) {
        Node* ptr = getAt(index);
        if (ptr == NULL) {
            return;
        }

        if (ptr->prev == NULL) {
            pop_front();
            return;
        }

        if (ptr->next == NULL) {
            pop_back();
            return;
        }

        Node* left = ptr->prev;
        Node* right = ptr->next;
        left->next = right;
        right->prev = left;

        delete ptr;
    }


};

int main()
{
    TwoLinkedList lst;
    lst.push_back(1.0);
    lst.push_back(3.0);
    lst.push_back(4.0);
    lst.push_back(5.0);

    std::cout << lst[1]->data <<std::endl;

    lst.insert(2, -5.0);
    lst.insert(20, -10.0);
    lst.erase(3);
    lst.erase(30);

    // перебор с начала до конца
    for(Node* ptr = lst.head; ptr != NULL; ptr = ptr->next)
        std::cout << ptr->data << " ";
        std::cout << std::endl;

    // перебор с конца до начала
    for(Node* ptr = lst.tail; ptr != NULL; ptr = ptr->prev)
        std::cout << ptr->data << " ";
        std::cout << std::endl;
    return 0;
}