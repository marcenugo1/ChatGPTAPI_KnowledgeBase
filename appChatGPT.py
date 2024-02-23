import tkinter as tk
from tkinter import  Entry, Button
import openai

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())
client = openai.OpenAI()

knowledgeBase = [ {'role':'system', 'content':"""You are an assistant, and your primary objective is to answer questions from users on how to wash clothes on a washing machine. Only answer the question based on the Knowledge base below; if the question can't be answered based on the Knowledge base, respond with  \ "I don't know\ "\n
Knowledge base: How to wash your clothes correctly. 
Step one is first to make sure to look into the clothes tags to see if they need to be washed manually or if they can be washed on a washing machine. After making sure you can use your washing machine, separate your clothes based on the color. Do not wash clothes of brighter colors with clothes of darker colors. For example, separate the clothes into three different piles. White color clothes, Darker color clothes, and Color clothes and wash them separately. 

Step two is to choose the proper washing cycle depending on the fabric of your clothes. Your options range from normal to delicate and quick cycles.
 
Step three is to set the water temperature. Using the correct water setting in your washing machine can make a difference in your laundry. Hot water, for example, sanitizes and kills germs better, but in some cases, it can shrink your clothes, fade your fabrics, and require a lot more energy. So, use hot water only for bath and kitchen towels, bedding, sturdy fabrics, and any highly dirtied items. Use warm water for somewhat dirty loads, dark colors, and the permanent press cycle. Last, use cold water in the delicate cycle for delicate things, fabrics with dyes that might bleed, or clothes that aren't extremely dirty. Coldwater is the gentlest way of washing your clothes, and it also requires less energy, so you can save energy and protect the environment.

Step four is to add detergent and softener. The amount of detergent needed varies by load size and washing machine type, so check the back of the detergent box and look for any labels on your washing machine to find out how much you should use.
 
Step five is to load the washing machine. Ensure to keep your clothes manageable, as overloading the washing machine may result in the clothes not being cleaned as they should be.

The last step is to turn on the washing machine. Close the door and click the start button. 
"""} ] 

def getResponse(messages): 
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content

def sendPrompt_btnClick():
    btnAsk.config(state=tk.DISABLED)
    lblLoading.pack()
    lblLoading.update_idletasks()
    btnAsk.update_idletasks()
    
    userPrompt = entry.get()
    entry.delete(0, tk.END) 
    #add an example response  
    knowledgeBase.append({'role': 'user', 'content': f"What is the last step for washing your clothes?"})
    knowledgeBase.append({'role': 'assistant', 'content': f"Turn on the washing machine. Close the door and click the start button."})
    knowledgeBase.append({'role': 'user', 'content': f"{userPrompt}"})
    response = getResponse(knowledgeBase)
    knowledgeBase.append({'role': 'assistant', 'content': f"{response}"})
    
    lblUser.config(text='User:')
    lblUsr.config(text=userPrompt)
    
    lblAssistant.config(text='Assistant:')
    lblMessage.config(text=response)
    print(response)

    lblLoading.pack_forget()
    btnAsk.config(state=tk.NORMAL)
  

start = tk.Tk()
start.title("NLP CLASS")
start.geometry("800x400")

lblLoading = tk.Label(start, text="Loading...", font=("Helvetica", 16,"bold"))
lblLoading.pack_forget()

entry = Entry(start,width=50)
entry.pack(pady=10)

btnAsk = Button(start, text="Ask ChatGPT", command=sendPrompt_btnClick,bd=5)
btnAsk.pack()

lblUser = tk.Label(start, text='User:')
lblUser.pack()
lblUsr = tk.Label(start, text='')
lblUsr.pack()

lblAssistant = tk.Label(start, text='Assistant:')
lblAssistant.pack()
lblMessage = tk.Label(start, text='', wraplength=700)
lblMessage.pack()

start.mainloop()
