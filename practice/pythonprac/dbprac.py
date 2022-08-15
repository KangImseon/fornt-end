from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

#pymongo(insert)
## run 후, *db를 refresh 를 해야한다.
# doc = {'name':'bobby','age':21}
# db.users.insert_one(doc)

### 'users'라는 collection에 {'name':'bobby','age':21}를 넣습니다.
# db.users.insert_one({'name':'kay','age':27})
# db.users.insert_one({'name':'john','age':30})
# db.users.insert_one({'name':'sean','age':27})

#pymongo(find)
# same_ages = list(db.users.find({'age':21},{'_id':False}))
# print(same_ages)

#pymongo(find_one)
user = db.users.find_one({'name':'bobby'})

# 저장 - 예시
doc = {'name':'bobby','age':21}
db.users.insert_one(doc)

# 한 개 찾기 - 예시
user = db.users.find_one({'name':'bobby'})

# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
same_ages = list(db.users.find({'age':21},{'_id':False}))

# 바꾸기 - 예시
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# 지우기 - 예시
db.users.delete_one({'name':'bobby'})


# 저장하기


