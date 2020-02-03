'''
From: Facebook
Difficulty: Medium

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
'''

def count_n_ways(message):
    if message.startswith('0'):
        return 0
        
    if len(message) == 0 or len(message) == 1:
        return 1
    
    if len(message) == 2:
        if message[0] == '1' or (message[0] == '2' and int(message[1]) <= 6):
            return 1
        else:
            return 0

    total = count_n_ways(message[1:]) + count_n_ways(message[2:]) + 1
    return total
    

print(count_n_ways('1132'))
