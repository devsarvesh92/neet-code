from benedict import benedict

d = {"a": 1, "b": 1, "c": 1}
bd = benedict(d, keyattr_dynamic=True)
print(bd.a)

# read from csv
data = benedict(keyattr_dynamic=True).from_csv(
    "/Users/sarvesh/Personal/prep/dsa/lib_fun/test.csv"
)
vals = data["values"]
print([val for val in vals if val and int(val.Column3) > 30])


bd.to_json()
