st = set()
for i in input().split():
    if i not in st:
        st.add(i)
        print('NO')
    else:
        print('YES')