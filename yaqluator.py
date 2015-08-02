import json
import os
import types

import yaql
import yaml


def list_examples():
    files = os.listdir("static/examples")
    return [filename.replace('.json', '') for filename in files]

def get_example(example_name):
    with open("static/examples/"+example_name+".json", "r") as file:
        return json.load(file)


def evaluate(yaql_expression, yaml_string):

    # Parse YAML
    try:
        loaded_yaml = yaml.load(yaml_string)
    except yaml.parser.ParserError as pe:
        raise YamlException("Invalid YAML: " + str(pe))
    except Exception as e:
        raise YamlException("Exception loading YAML: " + str(e))

    # Parse YAQL expression
    try:
        parse = yaql.parse(yaql_expression)
    except yaql.exceptions.YaqlGrammarException as ge:
        raise YaqlException("Invalid YAQL expression: " + str(ge))
    except Exception as e:
        raise YaqlException("Exception parsing YAQL expression: " + str(e))


    # Evaluate YAQL expression against the YAML
    try:
        res = parse.evaluate(loaded_yaml)
        if isinstance(res, types.GeneratorType):
            res = list(res)
        return res
    except Exception as e:
        raise YaqlException("Exception evaluating YAQL expression: " + str(e))


def _get_matched_values(partial_value, sub_value):
    return [key for key in partial_value.keys() if key.startswith(sub_value)]


def auto_complete(yaql_expression, yaml_string):

    yaql_exp_valid = True
    res = []
    try:
        if yaql_expression[-1] != "]":
            if yaql_expression.count("[") > yaql_expression.count("]"):
                # we are in a middle of $....[ ...
                first_dlr_index = yaql_expression.rfind("$")
                expression_prefix = yaql_expression[:first_dlr_index - 1]
                sub_value = yaql_expression[first_dlr_index + 2:]
            else:
                # only dots
                last_dot_index = yaql_expression.rindex(".")
                sub_value = yaql_expression[last_dot_index + 1:]
                expression_prefix = yaql_expression[:last_dot_index]

            partial_value = evaluate(expression_prefix, yaml_string)

            res = []
            if partial_value:
                if isinstance(partial_value, list) or isinstance(partial_value, types.GeneratorType):
                    for index, item in enumerate(list(partial_value)):
                        if isinstance(item, list):
                            res.extend(range(len(item)))
                        elif isinstance(item, dict):
                            res.extend(_get_matched_values(item, sub_value))
                elif isinstance(partial_value, dict):
                    res = _get_matched_values(partial_value, sub_value)
    except (YamlException, YaqlException):
        pass

    try:
        evaluate(yaql_expression, yaml_string)
    except YaqlException:
        yaql_exp_valid = False

    return {
        "yaql_valid": yaql_exp_valid,
        "suggestions": list(set(res))
    }

#data = get_example("nova_v2_show")
#print auto_complete("$.server.links[$.href.port=90]", json.dumps(data))
#print auto_complete("$.server.net1dfd740c6Index0", json.dumps(data))

#$.server.links[$.href[$.url.length()>10]]
#print evaluate("$.server.links[$.hr", json.dumps(data))

class YamlException(Exception):
    def __init__(self, message):

        # Call the base class constructor with the parameters it needs
        super(YamlException, self).__init__(message)

class YaqlException(Exception):
    def __init__(self, message):

        # Call the base class constructor with the parameters it needs
        super(YaqlException, self).__init__(message)
