#include <iostream>
#include <fstream>
#include <unordered_map>
#include <unordered_set>
#include <string>
#include <vector>
#include <sstream>
#include <stdlib.h>
#include <string.h>

bool ghostsAtEnd(std::vector<std::string> nodes, std::unordered_set<std::string> endNodes) {
    for (std::string node : nodes) {
        if (endNodes.find(node) == endNodes.end()) return false;
    }
    return true;
}

int main () {
    std::ifstream file("input.txt");
    std::string line;
    std::vector<std::string> data;

    while (std::getline(file, line)) {
        if (line == "\n" || line.empty()) continue;
        data.push_back(line);
    }

    std::vector<int> steps;
    for (char c : data[0]) {
        steps.push_back(c == 'L' ? 0 : 1);
    }

    std::unordered_map<std::string, std::array<std::string, 2>> paths;
    std::unordered_set<std::string> endNodes;
    std::vector<std::string> nodes;
    for (int i = 1; i < data.size(); i++) {
        std::string key = data[i].substr(0,3);
        std::string left = data[i].substr(7,3);
        std::string right = data[i].substr(12,3);

        std::array<std::string, 2> value = {left, right};
        paths.insert(std::make_pair(key, value));

        std::string lastLetter = key.substr(2,1);
        if (lastLetter == "A") {
            nodes.push_back(key);
        } else if (lastLetter == "Z") {
            endNodes.insert(key);
        }
    }


    std::cout << endNodes.size() << "\n";
    std::cout << "Computing\n";
    ulong counter = 0;
    int i = 0;
    bool done = ghostsAtEnd(nodes, endNodes);
    while (!done) {
        if (counter % 10000000 == 0) std::cout << counter << '\n';
        for (int g = 0; g < nodes.size(); g++) {
            nodes[g] = paths[nodes[g]][steps[i]];
        }
        i = (i + 1) % steps.size();
        counter++;
        done = ghostsAtEnd(nodes, endNodes);
    }
    
    std::cout << counter << '\n';
    return 0;
}