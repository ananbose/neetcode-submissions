class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        // #first get the graph of what needs to be done and chidren are the ones that can be done , and then the indegree as well , for indegree of 0 you add to q and then for each member of queue you see if theyhave neighbors and if their indegree is 0 then add them
        map <int, vector<int>> seen;
        std::vector<int> indegree(numCourses, 0);
        queue<int> q;
        for (auto pre: prerequisites) {
            int i = pre[0];
            int j = pre[1];
            seen[j].push_back(i);
            indegree[i]++;
        }
    int completed = 0;
    for (int c=0; c<numCourses; c++) {
        if (indegree[c] == 0) {
            q.push(c);
            
        }
    }
    while(q.size()>0) {
        int node = q.front();
        q.pop();
        completed ++;
        if (completed == numCourses) {
            return true;
        }
        vector<int> neighbors = seen[node];
        if (neighbors.size()>0) {
            for ( auto n: neighbors) {
                indegree[n]--;
                if (indegree[n] == 0) {
                    q.push(n);
                }
            }
        } 
    }
    return completed == numCourses;
};
};
