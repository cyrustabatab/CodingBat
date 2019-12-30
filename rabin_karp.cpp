#include <iostream>
#include <string>
#include <cmath>


int rabin_karp(std::string s1,std::string s2) {
    
    if (s1.size() < s2.size())
        return -1;


    long current_hash{},target_hash{};
    int x{53};
    bool same{true};

    for(int i=0;i < s2.size();i++) {
        if(same && s1[i] != s2[i])
            same = false;

        current_hash = current_hash * x + static_cast<int>(s1[i]);
        target_hash = target_hash * x + static_cast<int>(s2[i]);

    }
    
    std::cout << current_hash << " " << target_hash << std::endl;
    if(same)
        return 0;


    long power{std::pow(x,s2.size() - 1)};
    

    for(int i = s2.size();i < s1.size();i++) {
        char letter_to_remove = s1[i - s2.size()];
        char letter_to_add = s1[i];
        current_hash = (current_hash - power * static_cast<int>(letter_to_remove)) * x + static_cast<int>(letter_to_add);
        if(current_hash == target_hash && s1.substr(i - s2.size() + 1,s2.size()) == s2)
                return i - s2.size() + 1;


    }

    return -1;




}


int main() {
    
    std::cout << rabin_karp("hello","lo") << std::endl;


}
