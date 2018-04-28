#ifndef _Stack_
#define _Stack_

template <class T>

struct node {
            
    T     data ;
    node *next ;

    node(T data, node* next);

};

template <class T>

class stack {
    
    public : 
        
        // methods
        stack(T data) ;
        bool   push(T data) ;
        T      pop() ;
        T      top() ;
        bool   empty() ; 
        int    size() ;
        void   print() ;

    private : 

        node<T>* head  = nullptr ;

};

#endif
