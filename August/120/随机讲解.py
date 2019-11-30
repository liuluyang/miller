import random
import json

explain = ["蔡子涵", "王昱斌", "白凤杰", "李贺", "郭冀邯", "李康", "杨兴鹏", "李建波", "孙业滕"]

print(random.choice(explain))


def random_explain(explain):
    if explain:
        show_name = explain.pop(random.randint(0, len(explain) - 1))
        return show_name


def random_name(file_name):
    with open(file_name, "r", encoding="utf-8") as f_read:
        res = json.loads(f_read.read())
        if res["explain"]:
            show_name = random_explain(res["explain"])
            print(show_name)
            res['unexplain'].append(show_name)
            if not res["explain"]:
                print(res["explain"])
                res["explain"] = (random.shuffle(res['unexplain']))
                res['unexplain'].clear()
        return res


def write_name(filename,data):
    with open(filename, "w", encoding="utf-8") as f_write:
        f_write.write(json.dumps(data, ensure_ascii=False))


# res = random_name("./show")
# write_name("./show", res)








