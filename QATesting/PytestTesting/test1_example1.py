# Write a function that takes,,,

def vowel_count(data):
    vowels =['p', 'w','f','a', 'i', 't', 'e']
    count = 0
    for ch in data: 
        if ch in vowels: 
            count += 1
    return count

#print(vowel_count('otepa'))
#print(vowel_count('wembo'))
#print(vowel_count('fabrice'))

def test_with_f_name():
    assert vowel_count('otepa') == 4

def test_with_l_name():
    assert vowel_count('wembo') == 2

def test_with_c_name():
    assert vowel_count('fabrice') == 4     

def test_with_c_name():
    assert vowel_count('JOEL WEMBO') == 3   
