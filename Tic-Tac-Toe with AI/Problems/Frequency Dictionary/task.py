# put your python code here
st = dict()
for word in input().split():
    st[word.lower()] = st.get(word.lower(), 0) + 1
for k, v in st.items():
    print(f"{k} {v}")
