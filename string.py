def algo(s):
    print(s.count('i')) # how many 'i' are in the string
    print(s.find('i')) # first occurence of 'i'
    print(s.isalnum()) # does s only contain alpha numeric values
    print(s.lower()) # convert s to lower case
    print(s.islower()) # if s contains only lowercase letters
    

if __name__ == '__main__':
    test_string = 'This is a test string'
    algo(test_string)

    alpha_num_string = 'abc123'
    algo(alpha_num_string)
