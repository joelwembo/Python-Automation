# Write a function that takes,,,

def vowel_count(data):
    vowels =['p', 'w','f','a', 'i', 't', 'e', 'x']
    count = 0
    for ch in data.lower(): 
        if ch in vowels: 
            count += 1
    return count
def calc_addition(num1,  num2): 
      return num1 + num2   

print(vowel_count('otepa'))
print(vowel_count('wembo'))
print(vowel_count('fabrice'))

def test_calc_addition(a , b): 
    assert calc_addition(5,10) == 15

def test_with_f_name():
    assert vowel_count('otepa') == 8
    


def test_with_l_name():
    assert vowel_count('wembo') == 2

def test_with_c_name():
    assert vowel_count('fabrice') == 4     

def test_with_c_name_upper():
    assert vowel_count('JOEL WEMBO') == 4

def test_with_c_upper_23():
    assert vowel_count('JOEL WEMBO') == 8   
