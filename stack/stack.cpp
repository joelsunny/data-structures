#include <stdio.h>
#include <stdexcept>

#include "stack.h"

template <class T>

bool stack<T>::push(T data) {

    head = new node<T> (data, head) ;

    return true ;

}

template <class T>

T  stack<T>::pop() {

    if(head == nullptr) {

        throw std::runtime_error("stack underflow");

    }

    T ret_data = head->data ;
    head = head->next ;
    return ret_data ;

}

template <class T>

T  stack<T>::top() {

    if(head == nullptr) {

        throw std::runtime_error("empty stack");

    }

    return head->data ;
}

template <class T>

bool stack<T>::empty() {

    if( head == nullptr ) {

        return true ;

    }

    return false ;

}

template <class T>

int stack<T>::size() {

    int _size = 0;

    for(node<T>* loop=head; loop != nullptr; loop=loop->next) {

       ++ _size ;

    }

    return _size ;
}

template <class T>

stack<T>::stack(T data) {

    this->push(data);

}

template <class T>

node<T>::node(T data, node<T>* next) {

    this->data = data ;
    this->next = next ;

}

template <class T>

void stack<T>::print() {


    for(node<T>* loop=head; loop != nullptr; loop=loop->next) {

        printf("Element: %c\n",loop->data);

    }

}
