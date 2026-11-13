class LRUCache {
private :
        int capacity;
      using entry = pair<int,int>;
      list <entry> entries;
      unordered_map<int,list<entry>::iterator> lookup;

public:
    LRUCache(int capacity): capacity(capacity) {

    }
    
    int get(int key) {
        const auto it = lookup.find(key);
        if(it!=lookup.end()) {
            auto node = it->second;
            entries.splice(entries.begin(), entries , node);
            return node->second;
        }
        return -1;
    }
    
    void put(int key, int value) {
        const auto it = lookup.find(key);
        if(it!=lookup.end()) {
            auto node = it->second;
            entries.splice(entries.begin(), entries , node);
            node->second = value;
            return;
        }
        entries.push_front({key, value});
        lookup[key] = entries.begin();
        if (lookup.size()>capacity) {
            int oldest = entries.back().first;
            lookup.erase(oldest);
            entries.pop_back();

        }
        
    }
};
