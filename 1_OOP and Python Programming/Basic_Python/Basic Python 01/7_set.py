# Set => (No Duplicates), (Unordered => তাই এতে ইনডেক্সিং (set[0]) কাজ করে না), (Mutable)

my_set = {1, 5, 3, 7, 1}
print(my_set)

""" 
আপনি যদি একদম ফাঁকা সেট বানাতে চান empty_set = {}, তবে পাইথন এটিকে সেট না ভেবে Dictionary ধরে নেবে। ফাঁকা সেট বানাতে হলে অবশ্যই set() ফাংশন ব্যবহার করতে হয়:
"""

empty_dict = {}     # এটি ডিকশনারি
empty_set = set()   # এটি সঠিক ফাঁকা সেট


fruits = {"apple", "banana", "cherry"}
print(fruits)

fruits.add("mango")
print(fruits)

if "apple" in fruits:
    fruits.remove("apple")
    print(f"apple remove kora hoycha")
else:
    print("pawa jaynai")

""" 
সেট থেকে উপাদান রিমুভ করার সময় যদি আপনি চান যে উপাদান না থাকলেও পাইথন কোনো এরর (KeyError) না দিয়ে চুপচাপ কোড চালিয়ে যাক, তবে সরাসরি discard() মেথড ব্যবহার করতে পারেন। এর জন্য আলাদা করে if চেক করার প্রয়োজন হয় না। 
"""

fruits.discard("mango")
print(fruits)

print(fruits)


A = {1, 2, 3}
B = {3, 4, 5}
print(A | B)
print(A & B)

# ডিফারেন্স বা ব্যবধান (difference -): প্রথম সেটে আছে কিন্তু দ্বিতীয় সেটে নেই এমন উপাদানগুলো।
print(A - B)

# সিমেট্রিক ডিফারেন্স (symmetric_difference বা ^): উভয় সেটের কমন উপাদান বাদ দিয়ে বাকি সব উপাদান।
print(A ^ B)

num = [1, 5, 3, 1, 4, 2, 4, 1, 7]
print(num)

# সেটের একটি দারুণ ব্যবহার: ডুপ্লিকেট দূর করা (Duplicate Removal)
unique_num = list(set(num))
print(unique_num)