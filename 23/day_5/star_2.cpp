#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <climits>

struct SeedRange
{
    unsigned long start;
    unsigned long length;
};

struct Converter
{
    unsigned long source;
    unsigned long destination;
    unsigned long length;
};

std::vector<Converter> extractValues(const std::vector<std::string>& data, int& i) {
    std::vector<Converter> converter;
    int n = data.size();
    while (i < n && data[i].rfind(':') > data[i].size()) {
        std::stringstream ss;
        std::string src, dest, len;
        ss << data[i];
        ss >> dest;
        ss >> src;
        ss >> len;
        converter.push_back({stoul(src), stoul(dest), stoul(len)});
        i++;
    }
    i++;
    return converter;
}

unsigned long convertValue(const std::vector<Converter>& converter, unsigned long value) {
    for (Converter con : converter) {
        if (value >= con.source && value < con.source + con.length) {
            return value - con.source + con.destination;
        }
    }
    return value;
}

int main () {
    std::ifstream file("day_5/input.txt");
    std::string line;
    std::vector<std::string> data;

    while (std::getline(file, line)) {
        if (line == "\n" || line.empty()) continue;
        data.push_back(line);
    }

    std::vector<SeedRange> seeds;
    std::string start;
    std::string length;
    std::stringstream ss;
    ss << data[0];
    ss >> start;
    while (!ss.eof()) {
        ss >> start;
        ss >> length;
        SeedRange range = {stoul(start),stoul(length)};
        
        seeds.push_back(range);
    }

    int i = 2;
    std::vector<Converter> seedToSoil = extractValues(data, i);
    std::vector<Converter> soilToFertilizer = extractValues(data, i);
    std::vector<Converter> fertilizerToWater = extractValues(data, i);
    std::vector<Converter> waterToLight = extractValues(data, i);
    std::vector<Converter> lightToTemperature = extractValues(data, i);
    std::vector<Converter> temperatureToHumidity = extractValues(data, i);
    std::vector<Converter> humidityToLocation = extractValues(data, i);

    unsigned long minLocation = ULONG_MAX;
    for (SeedRange range : seeds) {
        std::cout << "Range from " << range.start << " to " << range.length << '\n';
        unsigned long value;
        for (unsigned long seed = range.start; seed < range.start + range.length; seed++) {
            value = convertValue(seedToSoil, seed);
            value = convertValue(soilToFertilizer, value);
            value = convertValue(fertilizerToWater, value);
            value = convertValue(waterToLight, value);
            value = convertValue(lightToTemperature, value);
            value = convertValue(temperatureToHumidity, value);
            value = convertValue(humidityToLocation, value);
            if (value < minLocation) minLocation = value;
        }
    }
    std::cout << minLocation << '\n';
    return 0;
}