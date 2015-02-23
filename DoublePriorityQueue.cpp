#include <iostream>
#include <algorithm>
#include <cassert>
#include <vector>

template <typename T>
class DPQ {
strut Elem {
T val;
double a;
double b;
Elem(T val,double a,double b):
val{val},
a{a},
b{b}
}
};
std::vector<Elem> elems{};
public:
void enqueue(T val,double a,double b){
elems.emplace_back(val,a,b);  //emplace_back adds those values at the end of the container
}
T dequeue_a(){
 auto it = std::max_element(elems.begin(), elems.end(),
        [](const Elem& x, const Elem& y){ return x.a < y.a; }); //auto will automatically assign the type
    T val = it->val;  //asigns it to val
    elems.erase(it);
    return val;
}
T dequeue_b{
 auto it = std::max_element(elems.begin(), elems.end(),
        [](const Elem& x, const Elem& y){ return x.b < y.b; });
    T val = it->val;
    elems.erase(it);
    return val;
}
void clear(){
elems.clear();
}
std::size_t size() const {
    return elems.size();
  }
};

int main()
{
  DPQ<std::string> people;

  people.enqueue("Vincent", 12.0, 4.2);
  people.enqueue("Shawn", 5.0, 5.1);
  people.enqueue("Steve", 5.0, 5.1);
  people.enqueue("Fred", 9.0, 0.1);

  assert(people.size() == 4);

  assert(people.dequeue_a() == "Vincent");
  assert(people.dequeue_a() == "Fred");
  assert(people.dequeue_b() == "Shawn");

  assert(people.size() == 1);

  people.clear();

  assert(people.size() == 0);

  return 0;
}
