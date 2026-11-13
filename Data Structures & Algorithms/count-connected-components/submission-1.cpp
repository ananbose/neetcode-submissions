class Solution {
private:
        unordered_set<int> visited;
        int count = 0;
        unordered_map<int,vector<int>> graph;
public:
    int countComponents(int n, vector<vector<int>>& edges) {
        for (const auto& edge : edges) {
            int a = edge[0];
            int b = edge[1];
            graph[a].push_back(b);
            graph[b].push_back(a);
        }
        for ( int i = 0; i<n; i++) {
            if (visited.find(i) == visited.end())
            {
                count++;
                dfs(i,graph);
            }
        }
        return count; 
    }
    void dfs(int node, unordered_map<int,vector<int>> graph ) {
        visited.insert(node);
        for( auto nigh: graph[node]) {
            if (visited.find(nigh)==visited.end()){
                dfs(nigh,graph);
            }
        }


    }
};
