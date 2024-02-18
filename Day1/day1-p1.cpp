#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    // Keys and values to ben found from in strings
    int keys_length_small = 10;
    string keys_small[10] = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"};
    int values_small[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};

    int keys_lenghts_full = 20;
    string keys_full[20] = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"};
    int values_full[20] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9};


    string example_input[7] = {"two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"};
    // string ex = "two1nine34";

    vector<int> numbers;

    for(int i = 0; i < 7; i++){
        string ex = example_input[i];
        vector<int> out;

        for(int c = 0; c < ex.length(); c++){
            for(int k = 0; k < keys_length_small; k++){
                string key = keys_small[k];
                int l = key.length();

                if(ex.substr(c, l) == key){
                    out.push_back(values_small[k]);
                }
            }
        }

        if (out.empty()){
            numbers.push_back(0);
        } else {
            int first = out[0];
            int last = out.back();
            numbers.push_back((first + last));
        }
    }


    // cout << "[";
    for(auto &c: numbers)
        cout << c << ", ";
    // cout << "]";

    return 0;
}