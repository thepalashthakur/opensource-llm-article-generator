import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
from datetime import datetime

model_path = "models/llama-2-7b-chat.ggmlv3.q2_K.bin"
def getLLamaresponse(input_text):
    llm=CTransformers(model=model_path,
                      model_type='llama')
    template="""write an article for {input_text}"""

    prompt=PromptTemplate(input_variables=["input_text"],
                          template=template)
    before_time = datetime.now()
    response=llm(prompt.format(input_text=input_text))
    after_time = datetime.now()

    return response + "\n - Process Started : " + str(before_time)  + " - Process Ended : " + str(after_time)


st.set_page_config(page_title="Article GPT",
                    page_icon='⭐️',
                    layout='centered',
                    initial_sidebar_state='collapsed')

st.header("Article GPT ⭐️")
input_text=st.text_input("Enter the Blog Topic")

submit=st.button("Generate")

if submit:
    st.write(getLLamaresponse(input_text))