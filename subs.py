inp = 'TGAACGCCATTAACGCCAAAGCTCGCCAAACGCCATAACGCCATGCCTAACGCCACAACGCCAGAACGCCAAACGCCAAAAACGCCATTTTGTGAACGCCAAACGCCAAAAACGCCAAAACGCCAGAAACGCCAAACGCCAGGTCTAACGGAAACGCCAGGCAACGCCAAACGCCAAACGCCATTGAACGCCAACGAACGCCAACCAACGCCATGTGAACGCCAGTAACGCCATAACGCCAAACGCCATGTTGGGAGTGTTTTCAACGCCAACAACGCCACAACGCCAGCAAACGCCAAACGCCACGACAACGCCAGGAATCAACGCCACAACGCCACTGTAACGCCATAACGCCAAACGCCATTAAACGCCACATCGTAACGCCAGGAACGCCAGTTTAACGCCAAACGCCAGGAACAACGCCAAAACGCCAAAACGCCAGAACGCCAAACGCCAAACGCCACGAAAACGCCAAACGCCAAACGCCACAACGCCAAACGCCAGTGTAACGCCAAAACGCCAAACGCCAGGTTAACGCCAGCGGTGAACGCCAGAACGCCAAACGCCACAATAAACGCCAAACGCCAGTTAACGCCAAACGCCAAACGCCAAAACGCCAAACGCCAGATTAACGCCACAACGCCAACAAGCCAACGCCAAACGCCACCAAAAACGCCACAACGCCATGCGCAATAACGCCAGAACGCCAGCGCAACGCCAAACGCCAAACGCCATAAAAACGCCAAACGCCAGTCTCAACGCCAAAATAACTGAACGCCAGAGCAAACGCCAAACGCCAAACGCCATACTCGAAAACGCCAAACGCCAAACGCCATCTAACGCCAAACGCCACTAAACGCCACCACTTCTAACGCCAATGGGCCTCACAACGCCATCTGGTGAACGCCAGAATAAACGCCACAGAACGCCACGAGCAACGCCAAACGCCATAACGCCATACGGAACGCCACAACGCCAACAACGCCA'
 

for x in range(len(inp)):

    if inp[x:].startswith("AACGCCAAA"):
        
        print(x + 1, end = ' ')