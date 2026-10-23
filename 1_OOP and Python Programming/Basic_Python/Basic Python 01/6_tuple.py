# tuple => Immutable (কোনো আইটেমের মান পরিবর্তন করা যায় না)

my_tuple = ("apple", "banana", "mango", "cherry")
print(my_tuple)

t = (5) # এটি int ডেটা টাইপ
tt = (5,) # এটি tuple ডেটা টাইপ

# print(type(t))
# print(type(tt))

print(my_tuple[1])
print(my_tuple[::-1])
print(my_tuple[0::])

numbers = (2, 4, 5, 7, 2, 2, 5, 4, 8)

# count(): টুপলের ভেতরে কোনো নির্দিষ্ট মান কতবার আছে তা গুনে বলে।
print(numbers.count(2))
# index(): কোনো নির্দিষ্ট মান প্রথম কত নম্বর ইনডেক্সে পাওয়া গেছে তা রিটার্ন করে।
print(numbers.index(5))

student = ("khadiza", 22, "CSE")
name, age, dept = student
print(name, age, dept)

""" 
৬. লিস্ট থাকা সত্ত্বেও কেন আমরা Tuple ব্যবহার করব? (Interview FAQ)
১. নিরাপত্তা (Data Safety): আপনার ডেটা যদি এমন হয় যা প্রোগ্রাম চলাকালীন কোনোভাবেই পরিবর্তন হওয়ার কথা নয় (যেমন কনফিগারেশন বা ফিক্সড ডাটা), তবে টুপল ব্যবহার করলে ভুলবশত ডেটা পরিবর্তন হয়ে যাওয়ার ঝুঁকি থাকে না।
২. মেমোরি ও স্পিড (Performance): পাইথনের মেমোরি ম্যানেজমেন্টের কারণে লিস্টের চেয়ে টুপল আকারে ছোট হয় এবং এটি প্রসেস হতে তুলনামূলক কম সময় নেয়।
৩. ডিকশনারির কি (Dictionary Key): পাইথনে ডিকশনারির key হিসেবে লিস্ট ব্যবহার করা যায় না (કારણ list mutable), কিন্তু Tuple ব্যবহার করা যায়।
"""