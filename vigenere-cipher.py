import re


text = "lrqhm  sgcta mfmni lklya xksdm bzrwt dkaix oxsda zemnt ljxod brwtt hxvem wvwtp hdsne wietu rejod iiiep rdmnf kvlie wfvya ifyrz dkmoz izzee ffvek hrvsm jfegd hrxay himcm qzrwt rjisk psslu fjlap rnaee wrrdf rueye lxrep wyiey degib dkmoz siscx ddetu rexhu vdsmq qksue gvgrq htemq djegd hrxbq dtsnx lxlta iyspq wfqix ozsne rwres ufwlm yvwwt ryedn hvrsq diidu qkler orqee rwaif kvviz jzrjg vkmcq lkgay hrwav rpsue grcbd hrota hehtt hcsns qzkhf rwxhq ligab wzzif boboa"
text = re.sub(r'\W+', '', text)

fragments = []

for i in range(len(text)-2):
    fragments.append(text[i:i+3])

fragments = list(dict.fromkeys(fragments)) # Remove duplicates

indices_list = []

for fragment in fragments:
    indices = [match.start() for match in re.finditer(fragment, text)]
    if len(indices) > 1:
        indices_list.append(indices)

distances = []

for indices in indices_list:
    if len(indices) < 3:
        distances.append(indices[1] - indices[0])

    else:
        distances.append(indices[1] - indices[0])
        distances.append(indices[2] - indices[1])
        # distances.append(indices[3] - indices[1])

distances = list(dict.fromkeys(distances)) # Remove duplicates
#print(distances)









########
# Deel twee
########

text = list(text)

#print(text)

# Basically create columns from characters
a = collections.Counter(text[::5])
b = collections.Counter(text[1::5])
c = collections.Counter(text[2::5])
d = collections.Counter(text[3::5])
e = collections.Counter(text[4::5])

print(a, b, c, d, e)