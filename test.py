def main():
	s=input()
	st=set()
	for i in s:
		st.add(i)
	n=len(st)
	mini=len(s)
	for i in range(len(s)):
		cnt=0
		slen=0
		vis=[0]*26
		for j in range(i,len(s)):
			if vis[ord(s[j])-97]==0:
				cnt+=1
				vis[ord(s[j])-97]=1
			slen+=1
			if cnt==n:
				mini=min(slen,mini)
				break
	print(mini)
main()