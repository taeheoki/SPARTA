from pymongo import MongoClient
client = MongoClient('mongodb+srv://taeheoki:2365@cluster0.nham61w.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

db.movies.update_one({'title':'가버나움'},{'$set':{'score':'0'}})

movie = db.movies.find_one({'title':'가버나움'})
print(movie['score'])

# # 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
# moviesEqualGB = list(db.movies.find({'score':movie['score']}))
# for target_movie in moviesEqualGB :
#     print(target_movie['title'])
