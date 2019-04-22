import jinja2
import random
import string


def setup_template(template_name):
    templateLoader = jinja2.FileSystemLoader(searchpath="templates")
    templateEnv = jinja2.Environment(loader=templateLoader)
    template = templateEnv.get_template(template_name)
    return template


def single_if_wkst(difficulty):
    symbols = [">", "<", "==", "!=", "<=", ">="]
    template_path = "if_worksheet_templates/if_diff_{0}_{1}.tmpl"
    template_full = setup_template(template_path.format(difficulty, "full"))
    template_partial = setup_template(template_path.format(difficulty,
                                                           "partial"))
    if difficulty == 1:
        vals = {
            "val1": str(random.randint(-15, 15)),
            "condition": symbols[random.randint(0, 5)],
            "val2": str(random.randint(-15, 15)),
            "word": "Hello"
        }
        return {
            "full_code": template_full.render(code=vals),
            "partial_code": template_partial.render(code=vals)
        }
    elif difficulty == 2:
        vals = {
            "val1": str(random.randint(-15, 15)),
            "condition": symbols[random.randint(0, 5)],
            "val2": str(random.randint(-15, 15)),
            "word_true": "Hello",
            "word_false": "World"
        }
        return {
            "full_code": template_full.render(code=vals),
            "partial_code": template_partial.render(code=vals)
        }
    elif difficulty == 3:
        variable_name = random.choice(list(string.ascii_lowercase))
        vals = {
            "variable_name": variable_name,
            "variable_value": str(random.randint(-15, 15)),
            "condition": symbols[random.randint(0, 5)],
            "comparative_value": str(random.randint(-15, 15)),
            "word_true": "Hello",
            "word_false": "World",
        }
        return {
            "full_code": template_full.render(code=vals),
            "partial_code": template_partial.render(code=vals)
        }
    elif difficulty == 4:
        letters = list(string.ascii_lowercase)
        random.shuffle(letters)
        variable_name_one = letters.pop()
        variable_name_two = letters.pop()

        vals = {
            "variable_one": variable_name_one,
            "variable_two": variable_name_two,
            "value_one": str(random.randint(-15, 15)),
            "value_two": str(random.randint(-15, 15)),
            "condition": symbols[random.randint(0, 5)],
            "word_true": "Hello",
            "word_false": "World",
        }
        return {
            "full_code": template_full.render(code=vals),
            "partial_code": template_partial.render(code=vals)
        }

    elif difficulty == 5:
        operators = ["+", "-", "*", "/", "%"]
        letters = list(string.ascii_lowercase)
        random.shuffle(letters)
        variable_name_one = letters.pop()
        variable_name_two = letters.pop()

        vals = {
            "variable_one": variable_name_one,
            "variable_two": variable_name_two,
            "value_one": str(random.randint(-15, 15)),
            "value_two": str(random.randint(-15, 15)),
            "operator_one": random.choice(operators),
            "operator_two": random.choice(operators),
            "random_val_one": str(random.randint(-15, 15)),
            "random_val_two": str(random.randint(-15, 15)),
            "condition": symbols[random.randint(0, 5)],
            "word_true": "Hello",
            "word_false": "World",
        }

        return {
            "full_code": template_full.render(code=vals),
            "partial_code": template_partial.render(code=vals)
        }


if __name__ == "__main__":
    one = single_if_wkst(1)
    print(one["full_code"])
    print(one["partial_code"])
    print("=" * 80)
    two = single_if_wkst(2)
    print(two["full_code"])
    print(two["partial_code"])
    print("=" * 80)
    three = single_if_wkst(3)
    print(three["full_code"])
    print(three["partial_code"])
    print("=" * 80)
    four = single_if_wkst(4)
    print(four["full_code"])
    print(four["partial_code"])
    print("=" * 80)
    five = single_if_wkst(5)
    print(five["full_code"])
    print(five["partial_code"])
