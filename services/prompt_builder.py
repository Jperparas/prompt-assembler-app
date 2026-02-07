def generate_meta_prompt(inputs):
    persona, aim, recipients, theme, structure = inputs
    
    prompt_template = """You are a prompt engineering expert. Your task is to CREATE A PROMPT (not answer it yourself) based on the PARTS framework below.

PARTS Framework Input:
- Persona: {persona}
- Aim: {aim}
- Recipients: {recipients}
- Theme: {theme}
- Structure: {structure}

Generate a single, complete prompt that another LLM could use. The prompt should incorporate all the PARTS elements above.

IMPORTANT: Output ONLY the prompt itself - do not execute it, do not provide an answer, just write the prompt that would be given to another AI.

Example format:
"You are a [persona]. Your task is to [aim] for [recipients]. Focus on [theme] and use [structure]..."

Now create the prompt:"""
    
    return prompt_template.format(
        persona=persona if persona else "Not specified",
        aim=aim if aim else "Not specified",
        recipients=recipients if recipients else "Not specified",
        theme=theme if theme else "Not specified",
        structure=structure if structure else "Not specified"
    )  
