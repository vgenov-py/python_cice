course_1 = [{
		"name": "Patricia",
		"id" :  "1",
        "gender": "F"
	},
	{
		"name": "Nicole",
		"id" :  "2",
        "gender": "F"
	},
	{
		"name": "Javier",
		"id" :  "3",
        "gender": "M"
	},
	{
		"name": "Verónica",
		"id" :  "4",
        "gender": "F"
	},
	{
		"name": "Guillermo",
		"id" :  "5",
        "gender": "M"
	},
	{
		"name": "Pablo",
		"id" :  "6",
        "gender": "M"
	},
	{
		"name": "Patricia",
		"id" :  "7",
        "gender": "F"
	},
	{
		"name": "Patricia",
		"id" :  "8",
        "gender": "F"
	},
	
	]
course_2 =[
	{
		"name": "Germán",
		"id" :  "1",
        "gender": "M"
	},
	{
		"name": "Sara",
		"id" :  "2",
        "gender": "F"
	},
	{
		"name": "Jorge",
		"id" :  "3",
        "gender": "M"
	},
	{
		"name": "María",
		"id" :  "4",
        "gender": "F"
	},
	{
		"name": "Alicia",
		"id" :  "5",
        "gender": "F"
	},
	{
		"name": "Hernesto",
		"id" :  "6",
        "gender": "M"
	},]

new_students = ["Miguel", "Pedro", "Sandra"]

def add_new_students(where_to_add, to_add):
    for student in to_add:
        id = len(where_to_add) + 1
        new_student = {
            "name": student,
            "id": str(id)
        }
        where_to_add.append(new_student)
# add_new_students(course_1, new_students)
# print(course_1)

def id_verifier(givenList):
    all_ids = []
    for student in givenList:
        all_ids.append(student["id"])
    for id in all_ids:
        if all_ids.count(id) == 2:
            print(givenList[int(id)])

id_verifier(course_1)

def add_letter(givenList, letter):
    for student in givenList:
        student["id"] = student["id"] + letter
add_letter(course_1, "M")
add_letter(course_2, "T")
# print(course_1[0])

all_courses = []
all_courses.extend(course_1)
all_courses.extend(course_2)
# print(all_courses)

def separate(givenList):
    male = []
    female = []
    for student in givenList:
        if student["gender"] == "M":
            male.append(student)
        else:
            female.append(student)
    print(f"male:{male}")

separate(all_courses)

def add_course(givenList, course):
    for student in givenList:
        student["courses"] = [course]
add_courses(all_courses, "Python")
print(all_courses)
