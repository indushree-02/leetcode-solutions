class Solution:
    def asteroidCollision(self, a: List[int]) -> List[int]:
        st=[]
        for i in a:
            if i>0:
                st.append(i)
            else:
                while st and st[-1]>0 and abs(i)>st[-1]:
                    st.pop()
                if st and abs(i)==st[-1]:
                    st.pop()
                    continue
                elif st and abs(i)<st[-1]:
                    continue
                else:
                    st.append(i)
        return st
