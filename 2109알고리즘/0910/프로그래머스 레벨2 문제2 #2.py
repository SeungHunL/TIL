def solution(files):
    n={}
    for file in files:
        for i in range(len(file)):
            if file[i].isdigit():
                keyf = file[:i].lower()
                if file[:i].lower() in n:
                    n[keyf] = [file] + n.get(keyf)
                else:
                    n[keyf] = [file]
                break
    for k in n:
        for j in n[k]:
            print(j[len(k):])

    answer=[]
    return answer
ind=["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
snd=["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
solution(ind)

