def mix_string(s1, s2):
    first_char = s1[:1] + s2[:1]
    middle_char = s1[int(len(s1)/2):int(len(s1)/2)+1] + s2[int(len(s2)/2):int(len(s2)/2)+1]
    last_char = s1[len(s1)-1] + s2[len(s2)-1]
    res = first_char+middle_char+last_char
    print(res)


mix_string("abdur", "rahman")
