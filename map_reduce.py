# """mapper"""
# import sys
# for line in sys.stdin:
#     line=line.strip()
#     words=line.split()
#     for word in words:
#         print("{}\t{}".format(word,1))
#
# """reducer"""
# import sys
# current_word=None
# current_count=0
# word=None
#
# for line in sys.stdin:
#     word,count=line.split("\t",1)
#     try:
#         count=int(count)
#     except ValueError:
#         continue
#     if current_word==word:
#         current_count+=1
#     else:
#         if current_count:
#             print("{}\t{}".format(current_word,current_count))
#         current_word=word
#         current_count=count
#
# if current_word==word:
#     print("{}\t{}".format(current_word,current_count))
"""
mapper
"""
import sys
for line in sys.stdin:
    line=line.strip()
    words=words.split()
    for word in words:
        print("{}/t{}".format(word,1))
"""
reducer
"""
import sys
cur_word=None
cur_count=0
for kv in sys.stdin:
    kv=kv.strip()
    k,v=kv.split("/t",1)
    if k==cur_word:
        cur_count+=1
    else:
        if cur_count:
            print("{}/t{}".format(cur_word,cur_count))
            cur_word=v
            cur_count=k
if cur_word==v:
    print("{}/t{}".format(cur_word, cur_count))





