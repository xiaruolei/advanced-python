d = {
    "Bob": {"company": "Google"},
    "Jim": {"company": "Facebook"},
}

# # clear
# d.clear()
# print(d)


# # shallow copy
# d1 = d.copy()
# d1["Jim"]["company"] = "Amazon"
# print(d)
# print(d1)


# # deep copy
# import copy
#
# d2 = copy.deepcopy(d)
# d2["Jim"]["company"] = "Amazon"
# print(d)
# print(d2)


# # fromkeys
# keys = ["Bob", "Jim"]
# d3 = dict.fromkeys(keys, {"company": "USC"})
# print(d3)


# # get
# value = d.get("Tom", {"company": "LinkedIn"})

# # items
# for key, value in d.items():
#     print(key, value)


# # setdefault
# d.setdefault("Jason", {"company": "Oracle"})
# print(d)

# update
d.update(Jim={"company": "Amazon"}, Tom={"company": "LinkedIn"})
d.update({"Jason": {"company": "Microsoft"}})
d.update([("A", {"company": "A"}), ("B", {"company": "B"})])  # [(), ()]
d.update((("C", {"company": "C"}), ("D", {"company": "D"})))  # ((), ())
print(d)