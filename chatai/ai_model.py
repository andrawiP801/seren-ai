import openai, os
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

from chatai.models import SiteConfig


def get_chat(qry, session, history):
    siteconfig = SiteConfig.objects.first()
    os.environ["OPENAI_API_KEY"] = siteconfig.open_ai_key  # api key here
    openai.api_key = os.getenv("OPENAI_API_KEY")
    llm = ChatOpenAI(model=siteconfig.open_ai_model if siteconfig.open_ai_model else "gpt-3.5-turbo-1106", temperature=0.9)
    chat_history_for_chain = ChatMessageHistory()

    """Provide me with the data for the project.

    A conversational Al to which I can tell my problems, a situation that happened to me, 
    or my feelings so that it can advise, recommend, or encourage me in some way, 
    either by giving me breathing exercises, phrases to lift my spirits, 
    activities to cope with the situation, etc."""
    system_prompt = siteconfig.prompt if siteconfig.prompt else """You are a helpful assistant, below are instruction you should keep in mind.
                    - To whom I can confide my problems, situations that have occurred to me, or my feelings.
                    - In return, you should offer advice, recommendations, or encourage me in some way.
                    - You can suggest any therapy, breathing exercises, running routines, or motivational phrases to help me overcome the situation.
                    """
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"""{system_prompt}
                """,
            ),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}"),
        ]
    )

    chain = prompt | llm

    chain_with_message_history = RunnableWithMessageHistory(
        chain,
        lambda session_id: chat_history_for_chain,
        input_messages_key="input",
        history_messages_key="chat_history",
    )
    msg = chain_with_message_history.invoke(
    {"input": qry, "chat_history": history},
    {"configurable": {"session_id": f"{session}"}},
    )
    return msg