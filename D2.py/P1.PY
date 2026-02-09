#CONCATINATION
name="DEEPTI"
roll_no=180
percentage=90.5
student=True
print(name , roll_no , percentage , student)
# want to change anything then usually write that phase 
# python will automatically take the updated value
percentage= 85.6
print(name , roll_no , percentage , student) 
# concatenation
print("MY NAME IS" +name)
print("MY NAME IS "+name + " AND MY ROLL NUMBER",roll_no)
#concatenate same datatype use (+), diff. datatype use (,)
print("I SCORE", percentage,"% IN MY FINAL EXAMS. I AM A STUDENT IS", student)
# print expressions 
print("my percentage has changed to", percentage-2.0)
# print with seperator then use sep=""
print(name,roll_no ,percentage ,student ,sep=" * ")