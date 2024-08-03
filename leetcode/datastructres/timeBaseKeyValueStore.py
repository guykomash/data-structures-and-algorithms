'''
981. Time Based Key-Value Store
https://leetcode.com/problems/time-based-key-value-store/description/


Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.

void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.

String get(String key, int timestamp) Returns a value such that set was called previously, with 
timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
 

Example 1:

Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output
[null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
timeMap.get("foo", 1);         // return "bar"
timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
timeMap.get("foo", 4);         // return "bar2"
timeMap.get("foo", 5);         // return "bar2"

'''

class TimeMap:

    def __init__(self):
        self.store = {} # key -> array of (timestamp,value)


    def set(self, key: str, value: str, timestamp: int) -> None:
        vals = self.store.get(key, [])
        vals.append([timestamp, value])
        self.store[key] = vals

    def get(self, key: str, timestamp: int) -> str:
        vals = self.store.get(key, [])
        if not vals: return ""

        l = 0
        r = len(vals) - 1
        ret_val = ""
        while l <= r:
            m_idx = l + (r - l) // 2
            m_ts, m_val = vals[m_idx][0], vals[m_idx][1]
            if m_ts == timestamp:
                return m_val
            elif m_ts < timestamp:
                ret_val = m_val
                l = m_idx + 1
            else:
                r = m_idx - 1
        return ret_val



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)


if __name__ == "__main__":
    timeMap = TimeMap()
    res = []
    timeMap.set("foo", "bar", 1)   # store the key "foo" and value "bar" along with timestamp = 1.
    res.append(timeMap.get("foo", 1))         # return "bar"
    res.append(timeMap.get("foo", 3))         # return "bar", since there is no value corresponding to foo at        timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
    timeMap.set("foo", "bar2", 4) # store the key "foo" and value "bar2" along with timestamp = 4.
    res.append(timeMap.get("foo", 4))         # return "bar2"
    res.append(timeMap.get("foo", 5))         # return "bar2"

    print(res, sep="\n")
    # foo -> [(bar, 1), (bar2,4)]

    # [bar, ,bar , bar2, bar2]