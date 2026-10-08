class Solution:
    def compress(self, chars: List[str]) -> int:
        #everytime you encounter a new char , keep it in char , old char , keep deleting and adding to count ??
        read=0
        write = 0
        start = read
        while read < len(chars):
            if read+1<len(chars) and chars[read+1]==chars[read]:
                read+=1
            else:
                number = str(read-start+1)
                chars[write]=chars[read]
                l=len(number)
                if read-start+1 ==1:
                    write+=1
                    read+=1
                    start=read
                else:
                    write+=1
                    chars[write:write+l]=number
                    print("CHARS",chars)
                    write+=l
                    read+=1
                    start = read
        return len(chars[0:write])
