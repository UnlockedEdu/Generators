from flask import Blueprint, jsonify
import jinja2
import random
import string
import os

ifs_bp = Blueprint('ifs_bp', __name__)


def setup_template(template_name):
    templates_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                  "templates")
    templateLoader = jinja2.FileSystemLoader(searchpath=templates_path)
    templateEnv = jinja2.Environment(loader=templateLoader)
    template = templateEnv.get_template(template_name)
    return template


@ifs_bp.route('/ifs/<language>/<int:num_questions>/<int:difficulty>')
def single_if_wkst(language, difficulty, num_questions):
    supported_langs = ["java"]
    error_responses = {'errors': []}
    if num_questions < 1 or num_questions > 100:
        error_responses['errors'].append("invalid number of questsions."
                                         "range is 0<x<100")
    if difficulty not in range(1, 6):
        error_responses['errors'].append("invalid difficulty. Options are 1-5")

    if language not in supported_langs:
        error_responses['errors'].append("invalid language. Supported languages"
                                         "are {0!r}".format(supported_langs))

    if error_responses['errors']:
        return jsonify(error_responses), 400

    symbols = [">", "<", "==", "!=", "<=", ">="]
    template_path = "if_worksheet_templates/{0}/if_diff_{1}_{2}.tmpl"
    template_full = setup_template(template_path.format(language, difficulty,
                                                        "full"))
    template_partial = setup_template(template_path.format(language,
                                                           difficulty,
                                                           "partial"))
    results = {'questions': []}
    if difficulty == 1:
        for r in range(0, num_questions):
            vals = {
                "val1": str(random.randint(-15, 15)),
                "condition": symbols[random.randint(0, 5)],
                "val2": str(random.randint(-15, 15)),
                "word": "Hello"
            }
            results['questions'].append({
                "full_code": template_full.render(code=vals),
                "partial_code": template_partial.render(code=vals)
            })
    elif difficulty == 2:
        for r in range(0, num_questions):
            vals = {
                "val1": str(random.randint(-15, 15)),
                "condition": symbols[random.randint(0, 5)],
                "val2": str(random.randint(-15, 15)),
                "word_true": "Hello",
                "word_false": "World"
            }
            results['questions'].append({
                "full_code": template_full.render(code=vals),
                "partial_code": template_partial.render(code=vals)
            })
    elif difficulty == 3:
        for r in range(0, num_questions):
            variable_name = random.choice(list(string.ascii_lowercase))
            vals = {
                "variable_name": variable_name,
                "variable_value": str(random.randint(-15, 15)),
                "condition": symbols[random.randint(0, 5)],
                "comparative_value": str(random.randint(-15, 15)),
                "word_true": "Hello",
                "word_false": "World",
            }
            results['questions'].append({
                "full_code": template_full.render(code=vals),
                "partial_code": template_partial.render(code=vals)
            })
    elif difficulty == 4:
        for r in range(0, num_questions):
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
            results['questions'].append({
                "full_code": template_full.render(code=vals),
                "partial_code": template_partial.render(code=vals)
            })
    elif difficulty == 5:
        for r in range(0, num_questions):
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

            results['questions'].append({
                "full_code": template_full.render(code=vals),
                "partial_code": template_partial.render(code=vals)
            })
    return jsonify(results), 200
