from typing import Any


def calc_pts(ops: list[Any]) -> int:
    res: list[int] = []

    for ip in ops:
        try:
            num = int(ip)
            res.append(num)
        except ValueError:
            match ip:
                case "+":
                    res.append(res[-1] + res[-2])
                case "C":
                    del res[-1]
                case "D":
                    res.append(res[-1] * 2)
    return sum(res)


print(calc_pts(["5", "-2", "4", "C", "D", "9", "+", "+"]))
print(calc_pts(["1", "C"]))
