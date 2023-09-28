def read_fasta(file):
    new_lst = []
    lst = file.read().split('>')[1:]        
    for i in range(len(lst)):
        new = lst[i].split('\n', 1)
        seq = new[1].replace('\n', '')
        new_lst.append(seq)        
    return (new_lst)

def CONS():
    with open ('rosalind_cons.txt', 'r') as f:
        lst = read_fasta(f)  
        matrix = []
        A = []
        C = []
        G = []
        T = []
        l = len(lst[0])
        for i in range(l):
            A_count = C_count = G_count = T_count = 0
            for j in lst:
                if j[i] == 'A':
                    A_count += 1
                elif j[i] == 'C':
                    C_count += 1
                elif j[i] == 'G':
                    G_count += 1
                elif j[i] == 'T':
                    T_count += 1             
            A.append(A_count)
            C.append(C_count)
            G.append(G_count)
            T.append(T_count)
        
    matrix.extend([A, C, G, T])
    cons = []      
    for i in range(l):
        profile = []
        for L in matrix:
            profile.append(L[i])
        M = max(profile)
        if profile.index(M) == 0:
            cons.append('A')
        elif profile.index(M) == 1:
            cons.append('C')
        elif profile.index(M) == 2:
            cons.append('G')
        elif profile.index(M) == 3:
            cons.append('T')

    print (''.join(cons))
    print ('A:', *A)
    print ('C:', *C)
    print ('G:', *G)
    print ('T:', *T)
CONS()