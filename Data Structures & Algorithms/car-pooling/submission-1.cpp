class Solution {
public:
    bool carPooling(vector<vector<int>>& trips, int capacity) {
        priority_queue<
            pair<int, int>,
            vector<pair<int, int>>,
            greater<pair<int, int>>
        > pq;

        for (auto& trip : trips) {
            int passengers = trip[0];
            int from = trip[1];
            int to = trip[2];

            pq.push({from, passengers});   // pickup
            pq.push({to, -passengers});    // dropoff
        }

        int current = 0;

        while (!pq.empty()) {
            auto top = pq.top();
            pq.pop();

            current += top.second;

            if (current > capacity) {
                return false;
            }
        }

        return true;
    }
};

/*
drives ast cannot turn and drive west; 



itn cap acity

int trips

trips[i] = [numPassengers[i], from[i], to[i]
    ith trip has numPassengers[i]

pick the mup from[i] drop to[i]



if we have pq

pq.push({}) from[i] to[i]

1,2 



if numPassengers[i] <= capacity and  from[i] < to[i]:

get difference? 

to[i] - from[i]

if difference is less than from+ difference;

then we return false? 






*/