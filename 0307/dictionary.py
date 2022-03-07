vocab = {'sanitizer' : '살균제',
         'ambition' : '야망',
         'conscience' : '양심',
         'civilization' : '문명'}

# dict = {'key' : 'value'}

# print(vocab)
vocab['privilege'] = '특권'
vocab['principle'] = '원칙'
#
# print(vocab)
# print(len(vocab))
#
# print(list(vocab))

# print(vocab.values())
# print('야망' in vocab.values())

# for value in vocab.values():
#     print(value)
#
# for key in vocab.keys():
#     print(key)

# for key, value in vocab.items():
#     print(key, value)

# dictionary practice
# 사전 뒤집기

# print(vocab)

# def reversed_dict(some_dict):
#     new_dict = {}
#     for key, value in some_dict.items():
#         # print(key, value)
#         new_dict[value] = key
#     return new_dict
#
# print("영-한 단어장\n{}\n".format(vocab))
#
# reversed_vocab = reversed_dict(vocab)
# print("한-영 단어장\n{}\n".format(reversed_vocab))

# 투표 집계하기

votes = ['김영자', '강승기', '최만수', '김영자', '강승기', '강승기', '최만수', '김영자', \
'최만수', '김영자', '최만수', '김영자', '김영자', '최만수', '최만수', '최만수', '강승기', \
'강승기', '김영자', '김영자', '최만수', '김영자', '김영자', '강승기', '김영자']

vote_counter = {}

for name in votes:
    if name not in vote_counter:
        vote_counter[name] = 1
    else:
        vote_counter[name] += 1

print(vote_counter)
