from langchain_core.prompts import PromptTemplate,ChatPromptTemplate

def prompt_template_example():
    prompt = PromptTemplate(
        input_variables=["topic"],
        template="You are a teacher Explain about the following topic: {topic} ?"
    )
    result = prompt.invoke({"topic": "Artificial Intelligence"})

    return {"prompt_template_result": result}
