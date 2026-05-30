from rules import RULES

def process_scenario(user_input):

    if "wet floor" in user_input.lower():
        rule = RULES["danger"]
        tool = "Safety_Alert_Tool"
        response = "Do not walk on the wet floor because you may slip and fall."

    elif "stressed" in user_input.lower():
        rule = RULES["stress"]
        tool = "Emotional_Support_Tool"
        response = "It is okay. Let us go through one step at a time."

    print("Rule:", rule)
    print("Tool:", tool)
    print("Response:", response)

scenario = input("Enter ASD scenario: ")
process_scenario(scenario)
