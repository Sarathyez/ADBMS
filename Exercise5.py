import pymongo
DEFAULT_CONNECTION_URL="mongodb://localhost:27017/"
client=pymongo.MongoClient(DEFAULT_CONNECTION_URL)
#print(client.database_names())
db=client["college"]
coll=db["studlist"]

#print("\nQ1:\n")
#for x in coll.find({"gender":"female","course":"MCA"},{"_id":0,"name.fname":1,"name.lname":1,"mark":1}):
#	print(x["name"]["fname"]+ " "+x["name"]["lname"]+ " ",x["mark"])

#print("\nQ2:\n")
#for x in coll.find({"course":"MCA"}).sort("mark",-1).limit(1):
#	print(x["name"]["fname"]+ " "+x["name"]["lname"]+ " "+x["address"]["house_name"]+" "+x["address"]["city"]+" "+x["gender"]+" "+x["course"]+" ",x["mark"]," "+x["grade"]+" ",x["phone"]["no"])

#print("\nQ3:\n")
#for x in coll.find({"gender":"male","grade":"A+"},{"_id":0,"name.fname":1,"name.lname":1,"grade":1,"gender":1}):
#	print(x["name"]["fname"]+ " "+x["name"]["lname"])

#print("\nQ4:\n")
#for x in coll.find({"course":"Mechanical"}).sort("mark",-1).limit(3):
#	print(x["name"]["fname"]+ " "+x["name"]["lname"]+ " "+x["address"]["house_name"]+" "+x["address"]["city"]+" "+x["gender"]+" "+x["course"]+" ",x["mark"]," "+x["grade"]+" ",x["phone"]["no"])

#print("\nQ5:\n")
#for x in coll.find({"gender":"female","mark":{'$gt':90}},{"_id":0,"name.fname":1,"name.lname":1,"mark":1,"grade":1}):
#	print(x["name"]["fname"]+ " "+x["name"]["lname"]+ " ",x["mark"]," ",x["grade"])

#print("\n\nQ6:\n")
#for x in coll.find({"mark":{'$gt':80,'$lt':90}},{"_id":0,"name.fname":1,"name.lname":1,"course":1,"mark":1}):
	#print(x)
#print("\n\nQ7:\n")
#for x in coll.find({"name.fname":{'$regex':'V'}},{"_id":0,"name.fname":1,"name.lname":1}):
#	print(x["name"]["fname"]+" "+x["name"]["lname"])
#print("\nQ8:\n")
#for x in coll.find({"address.city":"Kollam"},{"_id":0,"name.fname":1,"name.lname":1,"address.city":1}):
#	print(x["name"]["fname"]+ " "+x["name"]["lname"]+ " ",x["address"]["city"])
#print("\nQ9:\n")
#for x in coll.find({"address.city":{'$nin':['Kollam','Thiruvananthapuram']}},{"_id":0,"name.fname":1,"name.lname":1,"address.city":1}):
#	print(x["name"]["fname"]+ " "+x["name"]["lname"]+ " ",x["address"]["city"])
for x in coll.find({"gender":"female","address.city":{'$nin':['Kollam','Thiruvananthapuram']}},{"_id":0,"name.fname":1,"name.lname":1,"address.city":1}):
	print(x["name"]["fname"]+ " "+x["name"]["lname"]+ " ",x["address"]["city"])




